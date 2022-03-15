import sys
import socket
from datetime import datetime


def scanports(ip,startport,endport):
    print('Scanning the ports under {} from {} to {}'.format(ip,startport,endport))
    openports = []
    try:
    	for port in range(startport,endport):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            
            result = s.connect_ex((ip,port))
            if result ==0:
                openports.append(port)
                print("Port {} is open".format(port))
            s.close()
		
    except KeyboardInterrupt:
        print("\n Quitting the scan !!!!")
        sys.exit()
    except socket.gaierror:
        print("\n Hostname Could Not Be Resolved !!!!")
        sys.exit()
    except socket.error:
        print("\ Server not responding !!!!")
        sys.exit()


scanports('ipaddress',1,65536)
