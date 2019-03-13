import sys
import socket
import ipaddress
from model.IpValidator import IpValidator
from model.Converters import get_bin
from model.Converters import getNetAdress

# podpunkt numer 2. Jak pobrac lokalna maske ?

ip_address=""
if len(sys.argv) <= 1:
    # TODO: get local ip addres with mask if format "a.b.c.d/24"
    ip_address = socket.gethostbyname(socket.gethostname())
    print("nie podano adresu ip wiec pobieram loalnyy: " + ip_address)
elif len(sys.argv) >= 3:
    print("Error: za duzo argumentow, zamykam program")
    sys.exit(-2)
else:
    ip_address = sys.argv[1]

ip= IpValidator()
ip.setIpAndMask(ip_address)

getNetAdress(ip.ipAddress,ip.maskAddress)

#adres sieci za pomoca biblioteki
net = ipaddress.ip_network(ip_address ,False)
print(net.network_address)











