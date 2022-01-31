import random

input = input("Masukan text: ")
input = str(input)
listTemp = []
listKey = []
list = []
listFix = []
i=0
randomList = ['AB','BCD','CDEF','DEFGH','EFGHI']
kataAkhir = ""

key = random.choice(randomList)

for kata in input:
    listTemp.append(kata)

for kunci in key:
    listKey.append(kunci)

count = len(listTemp)

# print(listTemp)

while i < count:
    if (ord(listTemp[i]) >= 65 or ord(listTemp[i]) <= 90):
        list.append(listTemp[i])
    i += 1

sisa = len(list)-len(listKey)

for i in range (sisa):
    listKey.append(listKey[i])

for i in range (len(list)):
    temp = chr(((ord(list[i])-64 + ord(listKey[i])-64)%26) +64)
    kataAkhir += temp

print(kataAkhir)