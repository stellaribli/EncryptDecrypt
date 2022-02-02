def bikinListKataExt (input):
    list = []
    for kata in input:
        list.append(kata)
    return list

def lengkapiListKeyExt (list,listKey):
    sisa = len(list) - len(listKey)
    if sisa > 0:
        for i in range (sisa):
            listKey.append(listKey[i]) 
    return listKey

def enkripsiExt (list,listKey):
    kataEnkripsi = ''
    for i in range (len(list)):
        temp = chr((ord(list[i]) + ord(listKey[i]))%256)
        kataEnkripsi += temp
    return kataEnkripsi

def listEnkripsiExt (kataEnkripsi):
    listFix = []
    for kata in kataEnkripsi:
        listFix.append(kata)
    return listFix

def dekripsiExt (listFix,listKey):
    kataDekripsi = ''
    for i in range (len(listFix)):
        temp = chr((ord(listFix[i])-ord(listKey[i]))%256)
        kataDekripsi += temp
    return kataDekripsi

# MAIN PROGRAM #

inputKata = str(input("Masukan text: "))
inputKey = str(input("Masukan text: "))

list = bikinListKataExt(inputKata)
listKey = bikinListKataExt(inputKey)
listKey = lengkapiListKeyExt(list,listKey)

kataEnkripsi = enkripsiExt(list,listKey)
listFix =  listEnkripsiExt(kataEnkripsi)
kataDekripsi = dekripsiExt(listFix,listKey)

print("Hasil Enkripsi: "+str(kataEnkripsi))
print("Hasil Dekripsi: "+str(kataDekripsi))