import random

input = input("Masukan text: ")
input = str(input)
listTemp = []
listKey = []
list = []
listFix = []
i=0
randomList = ['AB','BCD','CDEF','DEFGH','EFGHI']
kataEnkripsi = ""
kataDekripsi = ""

key = random.choice(randomList)

for kata in input:
    listTemp.append(kata)

for kunci in key:
    listKey.append(kunci)

count = len(listTemp)

# print(listTemp)

while i < count:
    if (ord(listTemp[i]) >= 65 and ord(listTemp[i]) <= 90):
        list.append(listTemp[i])
    i += 1

sisa = len(list)-len(listKey)

for i in range (sisa):
    listKey.append(listKey[i])

# ENKRIPSI

for i in range (len(list)):
    temp = chr(((ord(list[i])-65 + ord(listKey[i])-65)%26)+65)
    listFix.append(temp)
    kataEnkripsi += temp

# DEKRIPSI

for i in range (len(list)):
    temp = chr(((ord(listFix[i])-65 - ord(listKey[i])-65)%26)+65)
    kataDekripsi += temp

print(kataEnkripsi)
print(kataDekripsi)