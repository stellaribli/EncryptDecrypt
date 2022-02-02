def bikinListKataAuto (input):
    list = []
    for kata in input:
        if ord(kata) >= 65 and ord(kata) <= 90:
            list.append(kata)
        else:
            if ord(kata) >= 97 and ord(kata) <= 122:
                temp = chr(ord(kata)-32)
                list.append(temp)
    return list

def lengkapiListKeyAuto (list,listKey):
    sisa = len(list) - len(listKey)
    if sisa > 0:
        for i in range (sisa):
            listKey.append(list[i])
    return listKey

def enkripsiAuto (list,listKey):
    kataEnkripsi = ''
    for i in range (len(list)):
        temp = chr(((ord(list[i])-65 + ord(listKey[i])-65)%26)+65)
        kataEnkripsi += temp
    return kataEnkripsi

def listEnkripsiAuto (kataEnkripsi):
    listFix = []
    for kata in kataEnkripsi:
        listFix.append(kata)
    return listFix

def dekripsiAuto (listFix,listKey):
    kataDekripsi = ''
    for i in range (len(listFix)):
        temp = chr(((ord(listFix[i])-65 - ord(listKey[i])-65)%26)+65)
        kataDekripsi += temp
    return kataDekripsi

# MAIN PROGRAM #

list = bikinListKataAuto(teks)
listKey = bikinListKataAuto(kunci)
listKey = lengkapiListKeyAuto(list,listKey)

kataEnkripsi = enkripsiAuto(list,listKey)
listFix =  listEnkripsiAuto(kataEnkripsi)
kataDekripsi = dekripsiAuto(listFix,listKey)

print("Hasil Enkripsi: "+str(kataEnkripsi))
print("Hasil Dekripsi: "+str(kataDekripsi))