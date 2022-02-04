import os
import os.path
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QFileDialog
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from numpy import array

cipherType = ""

#Enigma 
def enigma(key, teks, pilihan):
    teks = teks.replace(" ","")
    teks = teks.upper()
    hasilEnkripsi = ''
    slowRotor = [[0 for i in range (26)]for j in range (1)]
    mediumRotor = [[0 for i in range (26)]for j in range (1)]
    fastRotor = [[0 for i in range (26)]for j in range (1)]
    newSlow = [[0 for i in range (26)]for j in range (2)]
    newMedium = [[0 for i in range (26)]for j in range (2)]
    newFast = [[0 for i in range (26)]for j in range (2)]

    for i in range(26):
        slowRotor[0][i] = i+1
        mediumRotor[0][i] = i+1
        fastRotor[0][i] = i+1
        
    slowRotor.append([1,19,10,14,26,20,8,16,7,22,4,11,5,17,9,12,23,18,2,25,6,24,13,21,3,15])
    mediumRotor.append([1,6,4,15,3,14,12,23,5,16,2,22,19,11,18,25,24,13,7,10,8,21,9,26,17,20])
    fastRotor.append([8,18,26,17,20,22,10,3,13,11,4,23,5,24,9,12,25,16,19,6,15,21,2,7,1,14])


    key = key.replace(" ","")
    key = key.upper()

    if len(key)!=3:
        print("Masukkan hanya tiga huruf!")
    else:
        keySlow = ord(key[0])-65
        keyMedium = ord(key[1])-65
        keyFast = ord(key[2])-65
        j = 0
        for i in range (keySlow,26):
            newSlow[0][i] = slowRotor[0][j]
            newSlow[1][i] = slowRotor[1][j]
            j+=1
        for i in range (keySlow):
            newSlow[0][i] = slowRotor[0][j]
            newSlow[1][i] = slowRotor[1][j]
            j+=1
        j = 0
        for i in range (keyMedium,26):
            newMedium[0][i] = mediumRotor[0][j]
            newMedium[1][i] = mediumRotor[1][j]
            j+=1
        for i in range (keyMedium):
            newMedium[0][i] = mediumRotor[0][j]
            newMedium[1][i] = mediumRotor[1][j]
            j+=1
        j = 0
        for i in range (keyFast,26):
            newFast[0][i] = fastRotor[0][j]
            newFast[1][i] = fastRotor[1][j]
            j+=1
        for i in range (keyFast):
            newFast[0][i] = fastRotor[0][j]
            newFast[1][i] = fastRotor[1][j]
            j+=1

    arrayHasil = []
    for i in range (len(teks)):
        SM = 0
        MF = 0
        F = 0
        idxTeks = ord(teks[i]) - 65
        for j in range(26):
            if newSlow[0][idxTeks] == newSlow[1][j]:
                SM = j
        for j in range(26):
            if newMedium[0][SM] == newMedium[1][j]:
                MF = j   
        for j in range(26):
            if newFast[0][MF] == newFast[1][j]:
                F = j     
        arrayHasil.append(chr(F+65))
        
    for i in range (len(arrayHasil)):
        hasilEnkripsi = hasilEnkripsi + arrayHasil[i]


    arrayHasil = []
    #Dekripsi
    for i in range (len(teks)):
        FM = 0
        MS = 0
        S = 0
        idxTeks = ord(teks[i]) - 65
        for j in range(26):
            if newFast[0][j] == newFast[1][idxTeks]:
                FM = j
        for j in range(26):
            if newMedium[0][j] == newMedium[1][FM]:
                MS = j   
        for j in range(26):
            if newSlow[0][j] == newSlow[1][MS]:
                S = j     
        arrayHasil.append(chr(S+65))

    hasilDekripsi = ''   
    for i in range (len(arrayHasil)):
        hasilDekripsi = hasilDekripsi + arrayHasil[i]
    
    if pilihan == 1:
        return (hasilEnkripsi)
    else: 
        return (hasilDekripsi)

#Vigenere
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

def vigenere(inputKey,inputKata):
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

    list = bikinListKata(inputKata)
    listKey = bikinListKata(inputKey)
    listKey = lengkapiListKey(list,listKey)

    kataEnkripsi = enkripsi(list,listKey)
    listFix =  listEnkripsi(kataEnkripsi)
    kataDekripsi = dekripsi(listFix,listKey)

    return(print("Hasil Enkripsi: "+str(kataEnkripsi))+('/n')+("Hasil Dekripsi: "+str(kataDekripsi)))

def extendedVigenere(inputKey,inputKata):
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
        
    list = bikinListKata(inputKata)
    listKey = bikinListKata(inputKey)
    listKey = lengkapiListKey(list,listKey)

    kataEnkripsi = enkripsi(list,listKey)
    listFix =  listEnkripsi(kataEnkripsi)
    kataDekripsi = dekripsi(listFix,listKey)

    return(print("Hasil Enkripsi: "+str(kataEnkripsi))+('/n')+("Hasil Dekripsi: "+str(kataDekripsi)))

def autoKeyVigenere(inputKey,inputKata):
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
                listKey.append(list[i])
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

    list = bikinListKata(inputKata)
    listKey = bikinListKata(inputKey)
    listKey = lengkapiListKey(list,listKey)

    kataEnkripsi = enkripsi(list,listKey)
    listFix =  listEnkripsi(kataEnkripsi)
    kataDekripsi = dekripsi(listFix,listKey)

    return(print("Hasil Enkripsi: "+str(kataEnkripsi))+('/n')+("Hasil Dekripsi: "+str(kataDekripsi)))

#Extended
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

#Playfair
def playFair(teksKey, teksMasukan, pilih):
    arrayAlphabet = [0 for i in range(26)]
    arrayBujurSangkar = [["" for i in range(5)] for j in range(5)]
    teksKey = teksKey.replace(" ","")
    teksKey = teksKey.replace("J","")
    teksKey = teksKey.upper()
    teksMasukan = teksMasukan.upper()
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
        return("Teks Perkiraan: " + sentence + " atau " + sentence.replace("X",""))

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
    if pilih == 1:
        return(cetakArrayEnkripsi(arrayTeksEnkripsi))
    if pilih ==2:
        return(cetakArrayDekripsi(hasilTeksDekripsi))

#Running Key
def bikinListKataRunning (input):
    list = []
    for kata in input:
        if ord(kata) >= 65 and ord(kata) <= 90:
            list.append(kata)
        else:
            if ord(kata) >= 97 and ord(kata) <= 122:
                temp = chr(ord(kata)-32)
                list.append(temp)
    return list

def lengkapiListKeyRunning (list,listKey):
    sisa = len(list) - len(listKey)
    if sisa > 0:
        for i in range (sisa):
            listKey.append(listKey[i])
    return listKey

def enkripsiRunning (list,listKey):
    kataEnkripsi = ''
    for i in range (len(list)):
        temp = chr(((ord(list[i])-65 + ord(listKey[i])-65)%26)+65)
        kataEnkripsi += temp
    return kataEnkripsi

def listEnkripsiRunning (kataEnkripsi):
    listFix = []
    for kata in kataEnkripsi:
        listFix.append(kata)
    return listFix

def dekripsiRunning (listFix,listKey):
    kataDekripsi = ''
    for i in range (len(listFix)):
        temp = chr(((ord(listFix[i])-65 - ord(listKey[i])-65)%26)+65)
        kataDekripsi += temp
    return kataDekripsi

#Auto
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

class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi('landing.ui', self)
        self.vigButton.clicked.connect(self.gotoVig)
        self.extButton.clicked.connect(self.gotoExt)
        self.playButton.clicked.connect(self.gotoPlay)
        self.enigmaButton.clicked.connect(self.gotoEnigma)
    def gotoVig(self):
        widget.setCurrentIndex(1)
    def gotoExt(self):
        widget.setCurrentIndex(2)
    def gotoPlay(self):
        global cipherType 
        cipherType = "play"
        widget.setCurrentIndex(2)
    def gotoEnigma(self):
        global cipherType 
        cipherType = "enigma"
        widget.setCurrentIndex(2)

class Extended(QDialog):
    def __init__(self):
        super(Extended, self).__init__()
        loadUi('extended.ui', self)
        self.fullButton.clicked.connect(self.gotoFull)
        self.autoButton.clicked.connect(self.gotoAuto)
        self.runningButton.clicked.connect(self.gotoRunning)
        self.homeButton.clicked.connect(self.gotoHome)
    def gotoFull(self):
        global cipherType  
        cipherType = "vig"
        widget.setCurrentIndex(2)
    def gotoAuto(self):
        global cipherType 
        cipherType = "auto"
        widget.setCurrentIndex(2)
    def gotoRunning(self):
        global cipherType 
        cipherType = "running"
        widget.setCurrentIndex(2)
    def gotoHome(self):
        widget.setCurrentIndex(0)

class Text(QDialog):
    def __init__(self):
        super(Text, self).__init__()
        loadUi('haldua.ui', self)
        self.encryptButton.clicked.connect(self.gotoEncrypt)
        self.decryptButton.clicked.connect(self.gotoDecrypt)
        self.homeButton.clicked.connect(self.gotoHome)
        self.uploadButton.clicked.connect(self.upload)
        self.uploadedFile = None  
    def upload(self):
        fileName, _ = QFileDialog.getOpenFileName(
            self, "Upload CV File", "", "PDF Files (*.pdf)")
        if fileName:
            self.uploadedFile = fileName
            self.fileName.setText(os.path.basename(fileName))
        else:
            print("No file selected")  
    def gotoEncrypt(self): 
        teks = self.teks.text()
        kunci = self.kunci.text()
        teks = teks.replace(' ','')
        kunci = kunci.replace(' ','')
        if cipherType == 'play':
            keluaran = 'Hasil Enkripsi Anda: ' + playFair(kunci,teks,1)
            self.hasil.setText(keluaran)
        if cipherType == 'vig':
            list = bikinListKata(teks)
            listKey = bikinListKata(kunci)
            listKey = lengkapiListKey(list,listKey)
            kataEnkripsi = enkripsi(list,listKey)
            keluaran = 'Hasil Enkripsi Anda: ' + kataEnkripsi
            self.hasil.setText(keluaran)
        if cipherType == 'running':
            inputKata = str(input("Masukan text: "))
            inputKey = str(input("Masukan text: "))
            list = bikinListKataRunning(inputKata)
            listKey = bikinListKataRunning(inputKey)
            listKey = lengkapiListKeyRunning(list,listKey)
            kataEnkripsi = enkripsiRunning(list,listKey)
            keluaran = 'Hasil Enkripsi Anda: ' + kataEnkripsi
            self.hasil.setText(keluaran)
        if cipherType == 'full':
            list = bikinListKataExt(teks)
            listKey = bikinListKataExt(kunci)
            listKey = lengkapiListKeyExt(list,listKey)
            kataEnkripsi = enkripsiExt(list,listKey)
            keluaran = 'Hasil Enkripsi Anda: ' + kataEnkripsi
            self.hasil.setText(keluaran)
        if cipherType == 'auto':
            list = bikinListKataAuto(teks)
            listKey = bikinListKataAuto(kunci)
            listKey = lengkapiListKeyAuto(list,listKey)
            kataEnkripsi = enkripsiAuto(list,listKey)
            keluaran = 'Hasil Enkripsi Anda: ' + kataEnkripsi
            self.hasil.setText(keluaran)
        if cipherType == "enigma":
            if (len(kunci)!=3):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error")
                msg.setInformativeText('Masukkan tiga huruf untuk kunci!')
                msg.exec_()                
            else:
                kataEnkripsi = enigma(kunci, teks, 1)
                keluaran = 'Hasil Enkripsi Anda: ' + kataEnkripsi
                self.hasil.setText(keluaran)    
    def gotoDecrypt(self):
        teks = self.teks.text()
        kunci = self.kunci.text()
        teks = teks.replace(' ','')
        kunci = kunci.replace(' ','')
        if cipherType == 'play':
            if int(len(teks)%2==1):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error")
                msg.setInformativeText('Panjang Teks Harus Genap!')
                msg.exec_()
            else:
                keluaran = playFair(kunci,teks,2)
                self.hasil.setText(keluaran)
        if cipherType == 'vig':
            list = bikinListKata(teks)
            listKey = bikinListKata(kunci)
            listKey = lengkapiListKey(list,listKey)   
            kataDekripsi = dekripsi(list,listKey)
            keluaran = 'Hasil Dekripsi Anda: ' + kataDekripsi
            self.hasil.setText(keluaran)
        if cipherType == 'running':
            list = bikinListKataRunning(teks)
            listKey = bikinListKataRunning(kunci)
            listKey = lengkapiListKeyRunning(list,kunci)
            kataDekripsi = dekripsiRunning(list,listKey)
            keluaran = 'Hasil Dekripsi Anda: ' + kataDekripsi
            self.hasil.setText(keluaran)
        if cipherType == 'full':
            list = bikinListKataExt(teks)
            listKey = bikinListKataExt(kunci)
            listKey = lengkapiListKeyExt(list,listKey)
            kataDekripsi = dekripsiExt(list,listKey)
            keluaran = 'Hasil Dekripsi Anda: ' + kataDekripsi
            self.hasil.setText(keluaran)
        if cipherType == 'auto':
            list = bikinListKataAuto(teks)
            listKey = bikinListKataAuto(kunci)
            listKey = lengkapiListKeyAuto(list,listKey)
            kataDekripsi = dekripsiAuto(list,listKey)
            keluaran = 'Hasil Dekripsi Anda: ' + kataDekripsi
            self.hasil.setText(keluaran)
        if cipherType == 'enigma':
            if (len(kunci)!=3):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error")
                msg.setInformativeText('Masukkan tiga huruf untuk kunci!')
                msg.exec_() 
            else: 
                kataDekripsi = enigma(kunci, teks, 2)
                keluaran = 'Hasil Dekripsi Anda: ' + kataDekripsi
                self.hasil.setText(keluaran)            
    def gotoHome(self):
        widget.setCurrentIndex(0)
    def gotoHasil(self):
        widget.setCurrentIndex(3)

app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
widget.addWidget(Login())  # Index jadi 0   
widget.addWidget(Extended())  # Index jadi 1
widget.addWidget(Text())  # Index jadi 2
widget.setCurrentIndex(0)
widget.setFixedWidth(470)
widget.setFixedHeight(450)
widget.show()
app.exec_()


