from numpy import array


print(ord("A")) #65
print(ord("Z")) #90

arrayAlphabet = [0 for i in range(26)]
arrayBujurSangkar = [["" for i in range(5)] for j in range(5)]
teksKey = input("Masukkan Key: ")
teksKey = teksKey.replace(" ","")
teksKey = teksKey.replace("J","")
print(teksKey)
keyBaru = ""
bujurX = 0
bujurY = 0
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

print(arrayBujurSangkar)
# if bujurX!=4 and bujurY !=4:
#     for isiKosong in arrayAlphabet: 
#         i = 0
#         if isiKosong == 0:
#             arrayBujurSangkar[bujurX][bujurY] = 1
#             if bujurY==4:
#                 bujurX+=1
#                 bujurY=0
#             else:
#                 bujurY+=1
#         i = i+1  
# print(arrayAlphabet)
# print(arrayBujurSangkar)
# def playfairKey(teks):
#     for i in teks:
        

