def bikinListKata (input):
    list = []
    for kata in input:
        list.append(kata)
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
        temp = chr((ord(list[i]) + ord(listKey[i]))%256)
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
        temp = chr((ord(listFix[i])-ord(listKey[i]))%256)
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
kataDekripsi = dekripsi(listFix,listKey)

print("Hasil Enkripsi: "+str(kataEnkripsi))
print("Hasil Dekripsi: "+str(kataDekripsi))