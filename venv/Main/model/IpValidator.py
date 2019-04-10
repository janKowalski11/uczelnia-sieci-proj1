import sys
from model.Converters import get_bin


class IpValidator:
    consoleInput = ""

    ipAddress = ""  # format example "124.32.4.1"
    maskAddress = ""  # format example "24"

    def __init__(self):
        print("------------------")

    # converts ipAdress to binary octets divided with dots
    def convertIpToBinaryAndSave(self, ip):
        result = ""
        for x in ip:
            result = result + get_bin(int(x), 8) + "."
        result = result[:-1]  # removes last letter from result
        self.ipAddress = result

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

    def setIpAndMaskFromOneArg(self, argument):
        if('/' in argument):
            splited = argument.split("/")
        else:
            print("podany argument' "+ argument+ " 'jest bledny zamykam program" )
            sys.exit(-1)

        if('.' in argument):
            ip = splited[0].split(".")
            mask = splited[1]
        else:
            print("podany argument' " + argument + " 'jest bledny zamykam program")
            sys.exit(-1)

        if (self.validateIp(ip)):
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

    # TODO convert mask to number format!!! i bedzie wtedy kompatybilnosc kiedy uzytkownik podaje dane a kiedy nie
    def setIpAndMask(self, ip, mask):  # ip format "192.168.102.1" , mask format= "255.255.255.0"
        ip=ip.split('.')
        if (self.validateIp(ip)):
            print("adres ip jest poprawny")
            self.convertIpToBinaryAndSave(ip)
        else:
            print("adres ip jest NIE poprawny, zamykam program")
            sys.exit(-1)

        # nie ma potrzeby validacji maski pobranej z konsoli bo musi byc poprawna:)
        mask=mask.split(".")

        #konwersja maski z post typu "255.255.255.0" na binarna
        for idx, val in enumerate(mask):
            mask[idx] = get_bin(int(val))

        mask = "".join(mask)
        self.maskAddress = mask=mask.count('1')






