#!/usr/bin/python3

from netaddr import IPNetwork, iter_iprange, glob_to_iprange
import re
import sys
import os.path
import ipaddress

class IPParser:
    def __init__(self, filename):
        self.filename = filename

    def is_valid_ip_address(self, ip):
        try:
            ipaddress.ip_address(ip)
            return True
        except ValueError:
            return print("Not a valid IP address")

    def process(self, ip_value):
        if re.search('-', ip_value):
            self.dash2(ip_value)
            self.withdash(ip_value)
        elif re.search('/', ip_value):
            for ip in IPNetwork(ip_value).iter_hosts():
                print(ip)
        elif re.search(r'^\s*$', ip_value):
            pass
        elif re.search('\*+', ip_value):
            for ip in glob_to_iprange(ip_value):
                print(ip)
        elif len(ip_value) == 0:
            pass
        else:
            if self.is_valid_ip_address(ip_value):
                print(ip_value.lstrip().rstrip())

    def withdash(self, ip_value):
        try:
            split_ip = ip_value.split('-')
            firstip, secondip = split_ip[0].lstrip().rstrip(), split_ip[1].lstrip().rstrip()
            listfirstip, listsecondip = list(firstip.split('.')), list(secondip.split('.'))
            start, end = int(listfirstip[3]), int(listsecondip[3])
            first_3_octets = listfirstip[0:3]
            first_3 = ".".join(str(dot) for dot in first_3_octets)

            while start <= end:
                print(first_3 + "." + str(start))
                start = start + 1
        except IndexError:
            pass

    def dash2(self, ip):
        try:
            pull_ip = ip.split('-')
            if len(pull_ip[1]) <= 3:
                firstip, secondip = pull_ip[0].lstrip().rstrip(), pull_ip[1].lstrip().rstrip()
                listfirstip, listsecondip = list(firstip.split('.')), list(secondip.split('.'))
                start, end = int(listfirstip[3]), int(listsecondip[0])
                first_3_octets = listfirstip[0:3]
                first_3 = ".".join(str(dot) for dot in first_3_octets)

                while start <= end:
                    print(first_3 + "." + str(start))
                    start = start + 1

        except IndexError:
            pass

    def usage(self):
        print("\n" + "Example Usage is:  ./ipparser.py \"nameoffile.txt\"" + "\n")

    def main(self):
        try:
            if not os.path.isfile(self.filename):
                print("File not Found")

            with open(self.filename, 'r') as ip_option:
                newlist = [line.strip() for line in ip_option]

            for ip in newlist:
                if re.search(',', ip):
                    split_ip = ip.split(',')
                    for octet in split_ip:
                        self.process(octet)
                elif re.search(';', ip):
                    split_ip = ip.split(';')
                    for octet in split_ip:
                        self.process(octet)
                else:
                    self.process(ip)

        except:
            print("You must supply a file to parse")
            self.usage()

        sys.exit(2)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./ipparser.py <filename>")
    else:
        ip_parser = IPParser(sys.argv[1])
        ip_parser.main()
