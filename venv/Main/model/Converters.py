import subprocess
import model.Converters


# konwertuje maske w postaci liczby nalezacej od 0 do 32 np 24
# na postac umozliwajaca obliczenie min adres sieci to jest np
# 11111111111111111111111110000000
def convert_mask_to_binary_without_dots(mask):
    convertedMask = ""
    for x in range(0, int(mask)):  # for (i=0; i <mask; i++)
        convertedMask = convertedMask + "1"
    for x in range(int(mask), 32):  # for (i=0; i <mask; i++)
        convertedMask = convertedMask + "0"

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
def getNetAdress(ip, mask): #mask format octets with dots
    ip = ip.replace('.', '')  # removs dots from ip to get 1111000... format
    mask = convert_mask_to_binary_without_dots(mask)  # converts mask to 1111000... format

    ip_int = int(ip, 2)  # otrzymanie wartosci ip
    mask_int = int(mask, 2)

    result = ip_int & mask_int  # wykonianie and na wartosciach ip i maski

    result = bin(result)  # wartosci operacji and daja wynik  i konwersja do bin
    result = result.replace('0b', "")

    result = '.'.join(result[i:i + 8] for i in range(0, len(result), 8))  # wstawianie kropki co 8 znakow

    print("adres sieci: "+ result)
    writeToFile("adres sieci: {}",result)
    return result


def getNetClass(ipAddress):
    firstOctet = ipAddress[:8]  # wytnij pierwsze 8 znakow
    firstOctet = int(firstOctet, 2)  # rzutuj na decimal

    res=""
    if (firstOctet <= 127):
        res= "A"
    elif (firstOctet >= 128 and firstOctet <= 191):
        res= "B"
    elif (firstOctet >= 192 and firstOctet <= 223):
        res= "C"
    elif (firstOctet >= 224 and firstOctet <= 239):
        res= "D"
    elif (firstOctet >= 240 and firstOctet <= 255):
        res= "E"

    print("klasa sieci: "+ res)
    writeToFile("klasa sieci: {}", res)
    return res


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
    return inverted_mask


def getBroadCast(netAddress, invertedMask):
    netAddress = netAddress.replace('.', "")  # remove dots from net address

    netAdr_int = int(netAddress, 2)  # otrzymanie wartosci ip w int
    invertedMask_int = int(invertedMask, 2)

    result = netAdr_int | invertedMask_int  # wykonianie and na wartosciach ip i maski

    result = bin(result)  # wartosci operacji and daja wynik  i konwersja do bin
    result = result.replace('0b', "")

    #wstaw kropki co 8 indexow
    bin_res = '.'.join(result[i:i + 8] for i in range(0, len(result), 8))
    print("boardcast adress binarnie: " + bin_res)
    writeToFile("boardcast adress binarnie: {}" , bin_res)

    #konwersja na dziesietne
    dec_res = bin_res.split('.')
    for idx, val in enumerate(dec_res):
        dec_res[idx] = str(int(val, 2))

    dec_res = ".".join(dec_res)
    print("boardcast adress dziesietnie: " + dec_res)
    writeToFile("boardcast adress dziesietnie: {}" , dec_res)

    return result; #res format to binarny bez kropek:)


def getMaxHostCount(mask):  # mask format example "24"
    result = 2 ** (32 - int(mask)) - 2

    print("max host count: " + str(result))
    writeToFile("max host count: {}" , str(result))
    return result


def getFirstHostAddress(netAddress):


    #convert to binary
    octets = netAddress.split('.')
    for idx, val in enumerate(octets):
        octets[idx] = str(int(val, 2))

    lastOctet=octets[3]
    lastOctet=int(lastOctet)+1
    octets[3]=str(lastOctet) # here we have dec first host address
    firstHostAddres_dec=".".join(octets)

    print("adres pierwszego hosta decymalnie : "+ str(firstHostAddres_dec))
    writeToFile("adres pierwszego hosta decymalnie : {}", str(firstHostAddres_dec))

    #konwerja na binarne pierwszego adresu hosta dziesietnego
    for idx, val in enumerate(octets):
        octets[idx] = str(get_bin(int(val), 2))

    firstHostAddres_bin = ".".join(octets)

    writeToFile("adres pierwszego hosta binarnie : {}", str(firstHostAddres_bin))
    print("adres pierwszego hosta binarnie : " + str(firstHostAddres_bin))


    return ""


def getLastHostAddres(broadCast):
    lastOctet = broadCast[-8:]  # get last 8 chars of str
    result = int(lastOctet, 2) - 1  # convert to decimal then subs 1

    print("adres ostatniego hosta: " + str(result))
    writeToFile("adres ostatniego hosta: {}" , str(result))
    return result


def getMaskFromConsole(ip):  # ip format example  '192.168.1.10'
    proc = subprocess.Popen('ipconfig', stdout=subprocess.PIPE)
    while True:
        line = proc.stdout.readline()
        if ip.encode() in line:
            break
    mask = proc.stdout.readline().rstrip().split(b':')[-1].replace(b' ', b'').decode()
    return mask

def writeToFile(msg,val):
    with open("D:\Studia\sem_4\sieci\output.txt", "a") as text_file:
        print(msg.format(val), file=text_file)
