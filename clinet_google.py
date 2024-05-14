import socket
import sys
try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("socket successfully")
except socket.error as err:
    print("socket creation failed with error %s"%(err))

port=80
try:
    host_ip=socket.gethostbyname('www.google.com')
except socket.gaierror:
    print("there was an error resolving the host")
    sys.exit()
s.connect((host_ip,port))
print("the socket has successfully conneted to google")
print(host_ip)