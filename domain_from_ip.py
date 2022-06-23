'''
Find the domain name using an IP address

For this Python challenge, you'll want to import the Python socket library.
That’s the only hint. Write a function that accepts an IP address, makes a DNS
request, and returns the domain name that maps to that IP address using PTR DNS
records.

Original Challenge found here: 
https://www.codecademy.com/resources/blog/advanced-python-code-challenges/
'''

import socket


def ip_to_name(ip:str):
    '''Converts an IPv4 or IPv6 address to the fully qualified domain name\n
    Required parameters:
    ip (str): the Internet Protocol address to look up
    '''
    return socket.getfqdn(ip)


if __name__ == '__main__':

    ip = '8.8.8.8'

    print(ip, '=', ip_to_name(ip))

    ip = '208.67.222.222'

    print(ip, '=', ip_to_name(ip))
