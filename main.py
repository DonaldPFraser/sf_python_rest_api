from simple_salesforce import Salesforce
import argparse
import json
import csv

parser = argparse.ArgumentParser(description='Salesforce Query Tool for Lockbox and FluentControl Integration.')
parser.add_argument('--q', '--f')
args = parser.parse_args()

username = json.load(open("C:\ProgramData\Tecan\VisionX\Integrations\SF\secrets\config.json"))['username']
password = json.load(open("C:\ProgramData\Tecan\VisionX\Integrations\SF\secrets\config.json"))['password']
security_token = json.load(open("C:\ProgramData\Tecan\VisionX\Integrations\SF\secrets\config.json"))['security_token']
domain = json.load(open("C:\ProgramData\Tecan\VisionX\Integrations\SF\secrets\config.json"))['domain']   


sf = Salesforce(username=username, 
                password=password, 
                security_token=security_token,
                domain=domain,)

response = sf.query_all("" + args.q + "")

records = response['records']
number_of_records = [len(records)]
with open('C:\ProgramData\Tecan\VisionX\Integrations\SF\query_output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(number_of_records)