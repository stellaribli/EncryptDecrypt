def bikinListKata (input):
    list = []
    for kata in input:
        if ord(kata) >= 65 and ord(kata) <= 90:
            list.append(kata)
        else:
            if ord(kata) >= 97 and ord(kata) <= 122:
                temp = chr(ord(kata)-32)
                list.append(temp)
    return list

def lengkapiListKey (list,listKey):
    sisa = len(list) - len(listKey)
    if sisa > 0:
        for i in range (sisa):
            listKey.append(listKey[i])
    return listKey

def enkripsi (list,listKey):
    kataEnkripsi = ''
    for i in range (len(list)):
        temp = chr(((ord(list[i])-65 + ord(listKey[i])-65)%26)+65)
        kataEnkripsi += temp
    return kataEnkripsi

def listEnkripsi (kataEnkripsi):
    listFix = []
    for kata in kataEnkripsi:
        listFix.append(kata)
    return listFix

def dekripsi (listFix,listKey):
    kataDekripsi = ''
    for i in range (len(listFix)):
        temp = chr(((ord(listFix[i])-65 - ord(listKey[i])-65)%26)+65)
        kataDekripsi += temp
    return kataDekripsi

# MAIN PROGRAM #

inputKata = str(input("Masukan text: "))
inputKey = str(input("Masukan text: "))

list = bikinListKata(inputKata)
listKey = bikinListKata(inputKey)
listKey = lengkapiListKey(list,listKey)

kataEnkripsi = enkripsi(list,listKey)
listFix =  listEnkripsi(kataEnkripsi)
kataDekripsi = dekripsi(list,listKey)

print("Hasil Enkripsi: "+str(kataEnkripsi))
print("Hasil Dekripsi: "+str(kataDekripsi))