#konwertuje maske w postaci liczby nalezacej od 0 do 32 np 24
#na postac umozliwajaca obliczenie min adres sieci to jest np
#11111111111111111111111110000000
def convert_mask_to_binary(mask):
    convertedMask=""
    for x in range(0,int(mask)):                  #for (i=0; i <mask; i++)
        convertedMask=convertedMask+ "1"
    for x in range(int(mask),32):                  #for (i=0; i <mask; i++)
        convertedMask=convertedMask+ "0"

    print("przekonvertowana maska: "+ str(mask)+ " na postac: "+ convertedMask + " dlugosc jej: "+str(len(convertedMask)))
    return convertedMask

#x konwertowane na wartosc binarna, n liczba zer z przodu
def get_bin(x, n=8):
    return format(x, 'b').zfill(n)

#ręczna droga obliczania adresu sieci
def getNetAdress(ip,mask):
    ip=ip.replace('.','') #removs dots from ip to get 1111000... format
    mask=convert_mask_to_binary_with_one_at_end(mask) # converts mask to 1111000... format

    ip_int=int(ip,2) # otrzymanie wartosci ip
    mask_int=int(mask,2)

    result= ip_int & mask_int #wykonianie and na wartosciach ip i maski

    result=bin(result) # wartosci operacji and daja wynik  i konwersja do bin
    result=result.replace('0b',"")

    result='.'.join(result[i:i+8] for i in range(0, len(result), 8)) # wstawianie kropki co 8 znakow

    print(result)

    return result

