
# Domain name from IP address
# accepts str representation of IP address
# returns str representation of Domain name

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
