################################################
# Title: DWH (Python Wifi Scanner)             #
# Created By : Don Randeep                     #
# Github : https://github.com/donrandeep       #
################################################

#Scan
import scapy.all as scapy
import re

#Loading Bar
import time
import sys

# User Interface Header
print('''\033[93m
                           ..:::.._
                        .:::::/|::::.
                       ::::::/ V|:::::
                      ::::::/'  |::::::
                      ::::<_,   (::::::
                       :::::|    \::::
                        '::/      \:'

 \033[92m                ██████╗  ██████╗ ███╗   ██╗
                 ██╔══██╗██╔═══██╗████╗  ██║
                 ██║  ██║██║   ██║██╔██╗ ██║
                 ██║  ██║██║   ██║██║╚██╗██║
                 ██████╔╝╚██████╔╝██║ ╚████║
                 ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝           ''')
print("\033[94m[---]\033[96m             The DON WIFI HUNTER (DWH)         \033[94m[---]")
print("\033[94m[---]\033[95m             \033[91mCreated by: \033[95mDon Randeep           \033[94m[---]")
print("\033[94m[---]\033[95m                 \033[91mVersion: \033[95m0.0.1                \033[94m[---]")
print("\033[94m[---]\033[95m                \033[91mLanguage: \033[95mPython               \033[94m[---]")
print("\033[94m[---]\033[95m         Follow me on Git Hub: @donrandeep     \033[94m[---]")


print("\033[93m            Welcome to The DON WIFI HUNTER - (DWH)  ")
print("\033[91m             Visit: https://github.com/donrandeep   ")


z = """ \033[92m     


             I'm Discover All Hosts In Your Network
        
    [+]█████████████████████████████████████████████████[+]

"""

# Loading Bar
for c in z:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.02)

# recognise IPv4 addresses.
ip_add_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")

# Get the address range to ARP
while True:
    ip_add_range_entered = input("\n\033[96mEnter Your IP Address & Range \033[93m(ex: 192.168.1.0/24):\033[92m ")
    if ip_add_range_pattern.search(ip_add_range_entered):
        print(f"{ip_add_range_entered} is a valid ip address range")
        break
arp_result = scapy.arping(ip_add_range_entered)