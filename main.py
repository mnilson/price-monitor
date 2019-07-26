import argparse
import json
import requests
import smtplib

from canadian_tire_adapter import CanadianTireAdapter
from home_depot_adapater import HomeDepotAdapter

parser = argparse.ArgumentParser()
parser.add_argument('--ses_user', required=True)
parser.add_argument('--ses_pw', required=True)
parser.add_argument('--from_email', required=True)
parser.add_argument('--to_email', required=True)
parser.add_argument('--to_short_email')
args = parser.parse_args()

results = []
adapters = [HomeDepotAdapter(), CanadianTireAdapter()]

for adapter in adapters:
    skus = adapter.get_skus()
    headers = adapter.get_headers()
    for sku in skus:
        response = requests.get(adapter.get_url(sku), headers=headers)
        if response.status_code == 200:
            data = json.loads(response.text)
            pi = adapter.to_price_info(data, sku, skus[sku])
            results.append(pi)
        else:
            print(f'{adapter.get_store()} sku {sku} response code {response.status_code}')

content = ''
max_savings = 0
for pi in results:
    content = content + pi.__repr__()
    if float(pi.savings) > max_savings:
        max_savings = float(pi.savings)

if max_savings == 0.0:
    short_content = 'No savings today'
else:
    short_content = f'Best Savings: {max_savings}'
print(content)

# send the email
ses_user = args.ses_user
ses_pw = args.ses_pw
from_addr = args.from_email
to_addr = args.to_email
to_short_addr = args.to_short_email
if max_savings == 0:
    subject = f'No sales today'
else:
    subject = f'Sales! Max: {max_savings}'
msg = f'From: {from_addr}\nTo: {to_addr}\nSubject: {subject}\n\n{content}'
short_msg = f'From: {from_addr}\nTo: {to_short_addr}\nSubject: {subject}\n\n{subject}'

hostname = 'email-smtp.us-west-2.amazonaws.com'
port = 587
with smtplib.SMTP(hostname, port=port) as s:
    s.connect(hostname, port=port)
    s.starttls()
    s.login(ses_user, ses_pw)
    if max_savings > 0.0:
        s.sendmail(from_addr, to_addr, msg)
    if to_short_addr is not None:
        s.sendmail(from_addr, to_short_addr, short_msg)
