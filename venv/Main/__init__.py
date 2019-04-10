#todo refactor class ipValidator to functions
#add parsing mask from console if no arg given
##add saving to file
#punkt 7

#default config ip adress 192.168.1.145/25


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
from model.Converters import getLastHostAddres
from model.Converters import getMaskFromConsole
from model.Converters import validateIp
from model.Converters import validateMask
import model.Converters


ip_address = ""
if len(sys.argv) <= 1:
    ip_address = socket.gethostbyname(socket.gethostname())
    mask=getMaskFromConsole(ip_address)
    print("nie podano adresu ip i maski wiec pobieram loalnyy.\n Ip: " + ip_address +"\n Maska: "+ mask)
elif len(sys.argv) >= 3:
    print("Error: za duzo argumentow, zamykam program")
    sys.exit(-2)
else:
    ipAddressAndMask = sys.argv[1]
    validateIpAndMask(ipAddressAndMask)

# ip = IpValidator()
# ip.setIpAndMask(ip_address)

netAddress=getNetAdress(ip.ipAddress, ip.maskAddress)

getNetClass(ip.ipAddress)
isPrivate(ip.ipAddress)

mask_bin_noDots = convert_mask_to_binary_without_dots(ip.maskAddress)
mask_bin_dots= convert_binary_mask_wihout_dots_to_have_dots(mask_bin_noDots)
mask_dec_dots=convert_binary_mask_with_dots_to_decimal(mask_bin_dots)

inverted_mask=invertMask(mask_bin_noDots)


broadCast=getBroadCast(netAddress,inverted_mask)


maxHost=getMaxHostCount(ip_address)

getFirstHostAddress(netAddress)
getLastHostAddres(broadCast)