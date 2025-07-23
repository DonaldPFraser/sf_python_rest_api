from simple_salesforce import Salesforce
import sys
import json
import csv


query = sys.argv[1]

username = json.load(open("C:\ProgramData\Tecan\VisionX\Integrations\SF\secrets\config.json"))['username']
password = json.load(open("C:\ProgramData\Tecan\VisionX\Integrations\SF\secrets\config.json"))['password']
security_token = json.load(open("C:\ProgramData\Tecan\VisionX\Integrations\SF\secrets\config.json"))['security_token']
domain = json.load(open("C:\ProgramData\Tecan\VisionX\Integrations\SF\secrets\config.json"))['domain']   

query = query.replace("-", " ")

sf = Salesforce(username=username, 
                password=password, 
                security_token=security_token,
                domain=domain,)

response = sf.query_all("" + query + "")

records = response['records']
number_of_records = [len(records)]
with open('C:\ProgramData\Tecan\VisionX\Integrations\SF\query_output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(number_of_records)