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
from model.Converters import writeToFile
from model.Converters import ping
from model.Converters import ipBinaryToDecimal
import model.Converters

ip = IpValidator()
hostadrr = socket.gethostbyname(socket.gethostname()) # host address
if len(sys.argv) <= 1:
    ip_address = socket.gethostbyname(socket.gethostname())
    mask=getMaskFromConsole(ip_address)
    ip.setIpAndMask(ip_address,mask)
    print("nie podano adresu ip i maski wiec pobieram loalnyy.\n Ip: " + ip_address +"\n Maska: "+ mask)
elif len(sys.argv) >= 3:
    print("Error: za duzo argumentow, zamykam program")
    sys.exit(-2)
else:
    ipAddressAndMask = sys.argv[1]
    ip.setIpAndMaskFromOneArg(ipAddressAndMask)



netAddress=getNetAdress(ip.ipAddress, ip.maskAddress)
getNetClass(ip.ipAddress)

private=isPrivate(ip.ipAddress)
print ("czy jest prywatny czy nie: " +str(private))
writeToFile("czy jest prywatny czy nie: {}",str(private))

mask_bin_noDots = convert_mask_to_binary_without_dots(ip.maskAddress)

mask_bin_dots= convert_binary_mask_wihout_dots_to_have_dots(mask_bin_noDots)
print("maska binanie: "+ mask_bin_dots)
writeToFile("maska binanie:  {}",str(mask_bin_dots))

mask_dec_dots=convert_binary_mask_with_dots_to_decimal(mask_bin_dots)
print("maska dziesietnie: "+ mask_dec_dots)
writeToFile("maska dziesietnie:  {}",str(mask_dec_dots))

inverted_mask=invertMask(mask_bin_noDots)

broadCast=getBroadCast(netAddress,inverted_mask)

maxHost=getMaxHostCount(ip.maskAddress)

getFirstHostAddress(netAddress)
getLastHostAddres(broadCast)

ipDec=ipBinaryToDecimal(ip.ipAddress)
if(hostadrr==ipDec):
    ping(ip_address)


