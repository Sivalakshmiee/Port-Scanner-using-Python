# Importing all the required modules

import subprocess
import sys
import os

try:
    import scapy.all as scapy1
    import pyfiglet
    import sys
    import socket
    from datetime import datetime
except ImportError:
    print("Some modules are missing\n")
    print("Installing missing modules !!!!")
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'scapy', 'pyfiglet'])
finally:
    import scapy.all as scapy
    import pyfiglet
    import sys
    import socket
    from datetime import datetime
    print("\nAll modules are installed and excecuting the program!!!\n\n\n")
    
    
# Banner
print('-' * 50)
ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)
print("\t made  by  sivalakshmi ")
print('-' * 50)

# asking the choice from the user
print("1.External IP\n2.Local IP")
choice= input("enter the number:\n")

# Getting the Local IP of the system
def local_ip_getter():
    IPADDres = socket.gethostbyname(socket.gethostname())
    print("\nYour Local IP is- " + IPADDres)
    
# Scanning all the ip in the network
def scan(ip):
    arp_req_frame = scapy.ARP(pdst = ip)

    broadcast_ether_frame = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    
    broadcast_ether_arp_req_frame = broadcast_ether_frame / arp_req_frame

    answered_list = scapy.srp(broadcast_ether_arp_req_frame, timeout = 1, verbose = False)[0]
    result = []
    for i in range(0,len(answered_list)):
        client_dict = {"ip" : answered_list[i][1].psrc, "mac" : answered_list[i][1].hwsrc}
        result.append(client_dict)

    return result
  

# displaying the result of the scan
def display_result(result):
    print("-----------------------------------\nIP Address\tMAC Address\n-----------------------------------")
    for i in result:
        print("{}\t{}".format(i["ip"], i["mac"]))

# getting ip from user and sending it to the function
def get_ip(ip):
    scanned_output = scan(ip) 
    display_result(scanned_output)
    
# Port Scanner
def port_scanner(IP):
    target = IP
    print("-" * 50)
    print("Scanning Target: " + target)
    print("Scanning started at: " + str(datetime.now()))
    print("-" * 50)
    
    try:
        for port in range(1,65535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
    
		    # returns an error indicator
            result = s.connect_ex((target,port))
            if result ==0:
                print("Port {} is open".format(port))
            s.close()
    except KeyboardInterrupt:
            print("\nExiting Program !!!!")
            sys.exit()
    except socket.gaierror:
            print("\n Hostname Could Not Be Resolved !!!!")
            sys.exit()
            
# Domain to IP
def domain_to_ip():
    domain=input("Enter the domain name: ")
    domain_ip = socket.gethostbyname(domain)
    return domain_ip


if choice == "1":
    # print("External IP")
    os.system("cls")
    port_scanner(domain_to_ip())
    
elif choice == "2":
    # print("Local IP")
    os.system("cls")
    local_ip_getter()
    print("\n")
    print("-" * 50)
    get_ip(input("Enter the IP Address or Addresses to scan: \n"))
    print("\n")
    print("-" * 50)
    port_scanner(input("Enter the Above Shown Local IP Address to scan: \n"))
    
else:
    print("Invalid Input")
    

