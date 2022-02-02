from numpy import array

arrayAlphabet = [0 for i in range(26)]
arrayBujurSangkar = [["" for i in range(5)] for j in range(5)]
teksKey = input("Masukkan Key: ")
teksKey = teksKey.replace(" ","")
teksKey = teksKey.replace("J","")
keyBaru = ""
bujurX = 0
bujurY = 0

#Def Cari Lokasi Alphabet
def locateAlphabet(array,alphabet):
    for lokasiAlphabetSatu in range(5):
        for lokasiAlphabetDua in range(5):
            if array[lokasiAlphabetSatu][lokasiAlphabetDua] == alphabet:
                return lokasiAlphabetSatu,lokasiAlphabetDua

#Def Cetak Array
def cetakArrayEnkripsi(array):
    sentence = ""
    for i in range(len(array)):
        sentence = sentence + array[i][0] + array[i][1] + " " 
    return (sentence)
def cetakArrayDekripsi(array):
    sentence = ""
    for i in range(len(array)):
        sentence = sentence + array[i][0] + array[i][1] 
    print("Teks Perkiraan 1: " + sentence)
    print ("Teks Perkiraan 2: " + sentence.replace("X",""))

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

teksMasukan = input("Masukkan Pesan: ")

#ENKRIPSI
teksPesan = teksMasukan
teksPesan = teksPesan.replace("J","")
teksPesan = teksPesan.replace(" ","")

#Teks Menjadi Array
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

#Proses Enkripsi
arrayTeksEnkripsi = []
jumlahPasangan = len(arrayTeks)
for i in range(jumlahPasangan):
    inisialSatu = arrayTeks[i][0]
    inisialDua = arrayTeks[i][1]
    lokasiAlphabetSatu = locateAlphabet(arrayBujurSangkar,inisialSatu)
    lokasiAlphabetDua = locateAlphabet(arrayBujurSangkar,inisialDua)
    if lokasiAlphabetDua[0] == lokasiAlphabetSatu[0]:
        if lokasiAlphabetSatu[1] != 4:
            satu = (arrayBujurSangkar[lokasiAlphabetDua[0]][lokasiAlphabetSatu[1]+1])
        if lokasiAlphabetDua[1] != 4:
            dua = (arrayBujurSangkar[lokasiAlphabetDua[0]][lokasiAlphabetDua[1]+1])
        if lokasiAlphabetSatu[1] == 4:
            satu = (arrayBujurSangkar[lokasiAlphabetDua[0]][0])
        if lokasiAlphabetDua[1] == 4:
            dua = (arrayBujurSangkar[lokasiAlphabetDua[0]][0])
        arrayTeksEnkripsi.append([satu,dua]) 
    elif lokasiAlphabetDua[1] == lokasiAlphabetSatu[1]:
        if lokasiAlphabetSatu[0] != 4:
            satu = (arrayBujurSangkar[lokasiAlphabetSatu[0]+1][lokasiAlphabetSatu[1]])
        if lokasiAlphabetDua[0] != 4:
            dua = (arrayBujurSangkar[lokasiAlphabetDua[0]+1][lokasiAlphabetDua[1]])
        if lokasiAlphabetSatu[0] == 4:
            satu = (arrayBujurSangkar[0][lokasiAlphabetSatu[1]])
        if lokasiAlphabetDua[0] == 4:
            dua = (arrayBujurSangkar[0][lokasiAlphabetDua[1]])
        arrayTeksEnkripsi.append([satu,dua])
    else: 
        satu = arrayBujurSangkar[lokasiAlphabetSatu[0]][lokasiAlphabetDua[1]]
        dua = arrayBujurSangkar[lokasiAlphabetDua[0]][lokasiAlphabetSatu[1]]
        arrayTeksEnkripsi.append([satu,dua])

#Dekripsi
teksDekripsi = teksMasukan
teksDekripsi = teksDekripsi.replace(" ","")
#Ubah jadi Matrix
arrayPasanganDekripsi = []
if int(len(teksDekripsi)%2==1):
    print("Panjang teks harus genap!")
else:
    
    teksDekripsi = teksDekripsi.replace(" ","")
    idxDekripsi = 0
    while idxDekripsi<len(teksDekripsi):
        arrayPasanganDekripsi.append([teksDekripsi[idxDekripsi],teksDekripsi[idxDekripsi+1]])
        idxDekripsi+=2

#Proses Dekripsi
hasilTeksDekripsi = []
for i in range(int(len(arrayPasanganDekripsi))):
    inisialSatu = arrayPasanganDekripsi[i][0]
    inisialDua = arrayPasanganDekripsi[i][1]
    lokasiAlphabetSatu = locateAlphabet(arrayBujurSangkar,inisialSatu)
    lokasiAlphabetDua = locateAlphabet(arrayBujurSangkar,inisialDua)    
    if lokasiAlphabetDua[0] == lokasiAlphabetSatu[0]:
        if lokasiAlphabetSatu[1] != 0:
            satu = (arrayBujurSangkar[lokasiAlphabetDua[0]][lokasiAlphabetSatu[1]-1])
        if lokasiAlphabetDua[1] != 0:
            dua = (arrayBujurSangkar[lokasiAlphabetDua[0]][lokasiAlphabetDua[1]-1])
        if lokasiAlphabetSatu[1] == 0:
            satu = (arrayBujurSangkar[lokasiAlphabetDua[0]][4])
        if lokasiAlphabetDua[1] == 0:
            dua = (arrayBujurSangkar[lokasiAlphabetDua[0]][4])
        hasilTeksDekripsi.append([satu,dua]) 
    elif lokasiAlphabetDua[1] == lokasiAlphabetSatu[1]:
        if lokasiAlphabetSatu[0] != 0:
            satu = (arrayBujurSangkar[lokasiAlphabetSatu[0]-1][lokasiAlphabetSatu[1]])
        if lokasiAlphabetDua[0] != 0:
            dua = (arrayBujurSangkar[lokasiAlphabetDua[0]-1][lokasiAlphabetDua[1]])
        if lokasiAlphabetSatu[0] == 0:
            satu = (arrayBujurSangkar[4][lokasiAlphabetSatu[1]])
        if lokasiAlphabetDua[0] == 0:
            dua = (arrayBujurSangkar[4][lokasiAlphabetDua[1]])
        hasilTeksDekripsi.append([satu,dua])
    else: 
        satu = arrayBujurSangkar[lokasiAlphabetSatu[0]][lokasiAlphabetDua[1]]
        dua = arrayBujurSangkar[lokasiAlphabetDua[0]][lokasiAlphabetSatu[1]]
        hasilTeksDekripsi.append([satu,dua])
 
print(cetakArrayEnkripsi(arrayTeksEnkripsi))
cetakArrayDekripsi(hasilTeksDekripsi)