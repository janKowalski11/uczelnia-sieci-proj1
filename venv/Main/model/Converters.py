import subprocess


# konwertuje maske w postaci liczby nalezacej od 0 do 32 np 24
# na postac umozliwajaca obliczenie min adres sieci to jest np
# 11111111111111111111111110000000
def convert_mask_to_binary_without_dots(mask):
    convertedMask = ""
    for x in range(0, int(mask)):  # for (i=0; i <mask; i++)
        convertedMask = convertedMask + "1"
    for x in range(int(mask), 32):  # for (i=0; i <mask; i++)
        convertedMask = convertedMask + "0"

    print("przekonvertowana maska: " + str(mask) + " na postac: " + convertedMask + " dlugosc jej: " + str(
        len(convertedMask)))
    return convertedMask


# zeby zadzialalo to podaj maske w formacie otrzymanym z funkcji convert_mask_to_binary_without_dots
def convert_binary_mask_wihout_dots_to_have_dots(mask):
    mask = '.'.join(mask[i:i + 8] for i in range(0, len(mask), 8))
    return mask


# podaj maske w formacie z funkcji convert_binary_mask_wihout_dots_to_have_dots
def convert_binary_mask_with_dots_to_decimal(mask):
    octets = mask.split('.')
    for idx, val in enumerate(octets):
        octets[idx] = str(int(val, 2))

    octets = ".".join(octets)

    return octets


# x konwertowane na wartosc binarna, n liczba zer z przodu
def get_bin(x, n=8):
    return format(x, 'b').zfill(n)


# ręczna droga obliczania adresu sieci
def getNetAdress(ip, mask):
    ip = ip.replace('.', '')  # removs dots from ip to get 1111000... format
    mask = convert_mask_to_binary_without_dots(mask)  # converts mask to 1111000... format

    ip_int = int(ip, 2)  # otrzymanie wartosci ip
    mask_int = int(mask, 2)

    result = ip_int & mask_int  # wykonianie and na wartosciach ip i maski

    result = bin(result)  # wartosci operacji and daja wynik  i konwersja do bin
    result = result.replace('0b', "")

    result = '.'.join(result[i:i + 8] for i in range(0, len(result), 8))  # wstawianie kropki co 8 znakow

    return result


def getNetClass(ipAddress):
    firstOctet = ipAddress[:8]  # wytnij pierwsze 8 znakow
    firstOctet = int(firstOctet, 2)  # rzutuj na decimal

    if (firstOctet <= 127):
        return "A"
    elif (firstOctet >= 128 and firstOctet <= 191):
        return "B"
    elif (firstOctet >= 192 and firstOctet <= 223):
        return "C"
    elif (firstOctet >= 224 and firstOctet <= 239):
        return "D"
    elif (firstOctet >= 240 and firstOctet <= 255):
        return "E"


def isPrivate(ipAddress):
    firstOctet = ipAddress[:8]  # wytnij pierwsze 8 znakow
    firstOctet = int(firstOctet, 2)  # rzutuj na decimal

    secondOctet = ipAddress.split('.')
    secondOctet = secondOctet[1]
    secondOctet = int(secondOctet, 2)

    # https://forum.dobreprogramy.pl/t/ip-publiczne-czy-prywatne-tu-sie-dowiesz-jak-sprawdzic/361460
    if (firstOctet == 10):
        return True
    elif (firstOctet == 172):
        if (secondOctet >= 16 and secondOctet <= 31):
            return True
    elif (firstOctet == 192 and secondOctet == 168):
        return True

    return False


def invertMask(mask):
    mask_chars = list(mask)

    list_len = len(mask_chars)
    for i in range(0, list_len):
        if (mask_chars[i] == '1'):
            mask_chars[i] = '0'
        else:
            mask_chars[i] = '1'

    inverted_mask = "".join(mask_chars)
    print("inverted mask: " + inverted_mask)
    return inverted_mask


def getBroadCast(netAddress, invertedMask):
    netAddress = netAddress.replace('.', "")  # remove dots from net address

    netAdr_int = int(netAddress, 2)  # otrzymanie wartosci ip w int
    invertedMask_int = int(invertedMask, 2)

    result = netAdr_int | invertedMask_int  # wykonianie and na wartosciach ip i maski

    result = bin(result)  # wartosci operacji and daja wynik  i konwersja do bin
    result = result.replace('0b', "")

    print("board cast adress: " + result)

    return result;


def getMaxHostCount(fullIpadress):  # ip adress in format a.b.c.d/24
    splited = fullIpadress.split("/")
    mask = splited[1]

    result = 2 ** (32 - int(mask)) - 2

    print("max host count: " + str(result))
    return result


def getFirstHostAddress(netAddress):
    splited = netAddress.split('.')
    lastOctet = splited[3]
    result = int(lastOctet, 2) + 1  # convert to decimal then add 1

    print("adres pierwszego hosta: " + str(result))
    return result


def getLastHostAddres(broadCast):
    lastOctet = broadCast[-8:]  # get last 8 chars of str
    result = int(lastOctet, 2) - 1  # convert to decimal then subs 1
    print("adres ostatniego hosta: " + str(result))

    return result


def getMaskFromConsole(ip):  # ip format example  '192.168.1.10'
    proc = subprocess.Popen('ipconfig', stdout=subprocess.PIPE)
    while True:
        line = proc.stdout.readline()
        if ip.encode() in line:
            break
    mask = proc.stdout.readline().rstrip().split(b':')[-1].replace(b' ', b'').decode()

    return mask


def validateIp(ip): #ip format example '192.168.1.10'
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


def validateMask( mask): #mask format example "24"
    mask_int_value = int(mask)
    if mask_int_value >= 0 and mask_int_value <= 32:
        return True
    else:
        return False



    def validateIpAndMask( argument): #argument format example "192.168.1.10/24"
        splited = argument.split("/")

        ip = splited[0].split(".")
        mask = splited[1]

        if (self.validateIp(ip)):
            print("adres ip jest poprawny")
        else:
            print("adres ip jest NIE poprawny, zamykam program")
            sys.exit(-1)

        if (self.validateMask(mask)):
            print("maska jest poprawna")
        else:
            print("maska jest NIE poprawna, zamykam program")
            sys.exit(-1)

        return
