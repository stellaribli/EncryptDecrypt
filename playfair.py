from numpy import array

arrayAlphabet = [0 for i in range(26)]
arrayBujurSangkar = [["" for i in range(5)] for j in range(5)]
teksKey = input("Masukkan Key: ")
teksKey = teksKey.replace(" ","")
teksKey = teksKey.replace("J","")
print(teksKey)
keyBaru = ""
bujurX = 0
bujurY = 0
#Create Bujur Sangkar
for huruf in teksKey:
    index = ord(huruf)-65
    if arrayAlphabet[index] == 0:
        arrayAlphabet[index] = 1
        arrayBujurSangkar[bujurX][bujurY] = huruf
        if bujurY==4:
            bujurX+=1
            bujurY=0
        else:
            bujurY+=1
i=0
if not (bujurY==4 and bujurX==4):
    for isiKosong in arrayAlphabet: 
        if isiKosong == 0 and i!=9:
            arrayBujurSangkar[bujurX][bujurY] = chr(i+65)
            if bujurY==4:
                bujurX+=1
                bujurY=0
            else:
                bujurY+=1
        i+=1

teksPesan = input("Masukkan Pesan: ")
teksPesan = teksPesan.replace("J","")

arrayTeks = []

currentNumber = 0 

ind = 0
while ind<(len(teksPesan)-1):
    if teksPesan[ind] == teksPesan[ind+1]:
        arrayTeks.append([teksPesan[ind],'X'])
        ind+=1
    else:
        arrayTeks.append([teksPesan[ind],teksPesan[ind+1]])
        ind+=2
if ind<len(teksPesan):
    arrayTeks.append([teksPesan[ind],'X'])
    
print(ind)
print(arrayTeks)