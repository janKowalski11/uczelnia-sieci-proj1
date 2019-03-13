import sys
from model.Converters import get_bin



class IpValidator:
    consoleInput=""

    ipAddress = ""
    maskAddress = ""

    def __init__(self):
        print("tworze IpValidator")

    #converts ipAdress to binary octets divided with dots
    def convertIpToBinaryAndSave(self,ip):
        result = ""
        for x in ip:
            result = result + get_bin(int(x), 8) + "."
        result = result[:-1] #removes last letter from result
        print(result)
        self.ipAddress=result

    def validateIp(self, ip):
        if len(ip) != 4:
            return False
        else:
            for x in ip:
                if not x.isdigit():
                    return False
                i = int(x)
                if i < 0 or i > 255:
                    return False
        return True

    def validateMask(self, mask):
        mask_int_value = int(mask)
        if mask_int_value >= 0 and mask_int_value <= 32:
            return True
        else:
            return False

    def setIpAndMask(self, argument):
        splited = argument.split("/")

        ip = splited[0].split(".")
        mask = splited[1]

        if (self.validateIp(ip)):
            print("adres ip jest poprawny")
            self.convertIpToBinaryAndSave(ip)
        else:
            print("adres ip jest NIE poprawny, zamykam program")
            sys.exit(-1)

        if (self.validateMask(mask)):
            print("maska jest poprawna")
            self.maskAddress = mask
        else:
            print("maska jest NIE poprawna, zamykam program")
            sys.exit(-1)
        self.consoleInput = argument
