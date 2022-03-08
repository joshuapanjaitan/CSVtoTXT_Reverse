import csv
from csv import reader
from traceback import print_tb
import pandas as pd 


data = pd.read_csv("KOTO DHCP reserve.csv")
duplicate_host = data["host"].duplicated()
duplicate_mac = data["mac"].duplicated()
duplicate_ip = data["ipaddress"].duplicated()
i = 0
a = 0
j = 0
print("="*20, "Duplicate Host ", "="*20)
for line in duplicate_host:
    if line == True:
        print(data["host"][i])
    i += 1

print("="*20, "Duplicate MAC Address ", "="*13)
for line2 in duplicate_mac:
    if line2 == True:
        print(data["mac"][a])
        a += 1

print("="*20, "Duplicate IpAddress ", "="*15)
for line in duplicate_ip:
    if line == True:
        print(data["ipaddress"][j])
    j += 1
print("="*57)
