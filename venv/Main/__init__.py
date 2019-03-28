import sys
import socket
import ipaddress
from model.IpValidator import IpValidator
from model.Converters import get_bin
from model.Converters import getNetAdress
from model.Converters import getNetClass
from model.Converters import isPrivate
from model.Converters import convert_mask_to_binary_without_dots
from model.Converters import convert_binary_mask_wihout_dots_to_have_dots
from model.Converters import convert_binary_mask_with_dots_to_decimal
from model.Converters import invertMask
from model.Converters import getBroadCast
from model.Converters import getMaxHostCount
from model.Converters import getFirstHostAddress

# podpunkt numer 2. Jak pobrac lokalna maske ?

ip_address = ""
if len(sys.argv) <= 1:
    # TODO: get local ip addres with mask if format "a.b.c.d/24"
    ip_address = socket.gethostbyname(socket.gethostname())
    print("nie podano adresu ip wiec pobieram loalnyy: " + ip_address)
elif len(sys.argv) >= 3:
    print("Error: za duzo argumentow, zamykam program")
    sys.exit(-2)
else:
    ip_address = sys.argv[1]

ip = IpValidator()
ip.setIpAndMask(ip_address)

netAddress=getNetAdress(ip.ipAddress, ip.maskAddress)

# adres sieci za pomoca biblioteki
getNetClass(ip.ipAddress)
isPrivate(ip.ipAddress)

mask_bin_noDots = convert_mask_to_binary_without_dots(ip.maskAddress)
mask_bin_dots= convert_binary_mask_wihout_dots_to_have_dots(mask_bin_noDots)
mask_dec_dots=convert_binary_mask_with_dots_to_decimal(mask_bin_dots)

inverted_mask=invertMask(mask_bin_noDots)


broadCast=getBroadCast(netAddress,inverted_mask)


maxHost=getMaxHostCount(ip_address)

getFirstHostAddress(netAddress)
