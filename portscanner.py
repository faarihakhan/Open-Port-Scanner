import socket # establish a connection
from IPy import IP

# banner retrieve port information
def get_banner(so):
    return so.recv(1024) # size of bytes

# for single port one by one
def scan(target):   #def scan(target, port_num)
    converted_ip = check_IP(target)
    print('\n' + '[ *_* // scanning Target ]' + str(target))
    for port in range(1, 100):  #port_num
        port_scan(converted_ip, port)

#specify domain name as well as IP address
def check_IP(ipadress):
    try:
        IP(ipadress)
        return(ipadress)
    except ValueError:
        return socket.gethostbyname(ipadress) # convert domain name into ip address

#scanning
def port_scan(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5) # for scan faster set timeout
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            print('[+] Open Port ' + str(port) + ' : ' + str(banner.decode().strip('\n')))
        except:
            print('[+] Open Port ' + str(port))
    except:
        pass

if __name__ == '__main__':

    # specify one or multiple target
    target = input('[+] Enter Target To Scan(split multiple targets with, ): ')
    # port_num = input('Enter Number Of Ports You Want to scan : ')
    if ',' in target:
        for ip_add in target.split(','):
            scan(ip_add.strip(' ')) # strip it for uncessary empty spaces
    else:
        scan(target) # target one ip add and domain name

