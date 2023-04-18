#!/usr/bin/python3

from netaddr import IPNetwork, iter_iprange, glob_to_iprange 
import re
import sys
import os.path
import ipaddress

'''
The program now has support for the following.  Allows for , and ; as a means to break the rows.
Note:  When CIDR notation is used, the program removes the network and broadcast address.
192.168.1.1
192.168.1.1-192.168.1.3
192.168.1.1/24
192.168.1.1-50
192.168.1.*
'''

def is_valid_ip_address(ip):
	try:
		ipaddress.ip_address(ip)
		return True
	except ValueError:
		return False

def process(ip_value):
	if re.search('-', ip_value):
		dash2(ip_value)
		withdash(ip_value)
	elif re.search('/',ip_value):
		for ip in IPNetwork(ip_value).iter_hosts():
			print(ip)
	elif re.search('^/s*$', ip_value):
		pass
	elif re.search('\*+', ip_value):
		for ip in glob_to_iprange(ip_value):
			print(ip)
	elif len(ip_value) == 0:
		pass
	else:
		if is_valid_ip_address(ip_value) == True:
			print(ip_value.lstrip().rstrip())
		else:
			pass

def withdash(ip_value):
    try:
        split_ip = ip_value.split('-')
        firstip, secondip  = split_ip[0].lstrip().rstrip(), split_ip[1].lstrip().rstrip()
        listfirstip, listsecondip = list(firstip.split('.')), list(secondip.split('.'))
        start, end = int(listfirstip[3]), int(listsecondip[3])
        first_3_octects = listfirstip[0:3]
        first_3 = (".".join(str(dot) for dot in first_3_octects))

        while start <= end:
            print(first_3 + "." + str(start))
            start = start + 1
    except IndexError:
        pass

def dash2(ip):
    try:
        pull_ip = ip.split('-')
        if len(pull_ip[1]) <= 3:
            firstip, secondip  = pull_ip[0].lstrip().rstrip(), pull_ip[1].lstrip().rstrip()
            listfirstip, listsecondip = list(firstip.split('.')), list(secondip.split('.'))
            start, end = int(listfirstip[3]), int(listsecondip[0])
            first_3_octects = listfirstip[0:3]
            first_3 = (".".join(str(dot) for dot in first_3_octects))
        
            while start <= end:
                print(first_3 + "." + str(start))
                start = start + 1

    except IndexError:
        pass
        
def usage():
	print("\n" + "Example Usage is:  ./ipparser.py \"nameoffile.txt\"" + "\n")

def main():
	try:
		filename = sys.argv[1]
		if not os.path.isfile(filename):
			print("File not Found")

		with open(filename, 'r') as ip_option:
			newlist = [line.strip() for line in ip_option]
		
		for ip in newlist:
			if re.search(',', ip):
				split_ip = ip.split(',')
				for octet in split_ip:
					process(octet)
			elif re.search(';', ip):
				split_ip = ip.split(';')
				for octet in split_ip:
					process(octet)
			else:
                		process(ip)
                		        
	except:
	        print("You must supply a file to parse")
	        usage()

	sys.exit(2)

if __name__ == "__main__":
    main()
