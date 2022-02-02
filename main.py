import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from numpy import array

cipherType = ""
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


class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi('landing.ui', self)
        self.vigButton.clicked.connect(self.gotoVig)
        self.extButton.clicked.connect(self.gotoExt)
        self.playButton.clicked.connect(self.gotoPlay)
        self.enigmaButton.clicked.connect(self.gotoEnigma)
    def gotoVig(self):
        global cipherType 
        cipherType = "vig"
        widget.setCurrentIndex(2)
    def gotoExt(self):
        widget.setCurrentIndex(1)
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
    def gotoFull(self):
        global cipherType 
        cipherType = "full"
        widget.setCurrentIndex(2)
    def gotoAuto(self):
        global cipherType 
        cipherType = "auto"
        widget.setCurrentIndex(2)
    def gotoRunning(self):
        global cipherType 
        cipherType = "running"
        widget.setCurrentIndex(2)

class Text(QDialog):
    def __init__(self):
        super(Text, self).__init__()
        loadUi('haldua.ui', self)
        print(cipherType)
        self.encryptButton.clicked.connect(self.gotoEncrypt)
        self.decryptButton.clicked.connect(self.gotoDecrypt)
    def gotoEncrypt(self): 
        teks = self.teks.text()
        kunci = self.kunci.text()
        if cipherType == 'play':
            print(playFair(kunci,teks,1))
    def gotoDecrypt(self):
        teks = self.teks.text()
        kunci = self.kunci.text()
        if cipherType == 'play':
            print(playFair(kunci,teks,2))

app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
widget.addWidget(Login())  # Index jadi 0   
widget.addWidget(Extended())  # Index jadi 1
widget.addWidget(Text())  # Index jadi 2
widget.setCurrentIndex(0)
widget.setFixedWidth(450)
widget.setFixedHeight(450)
widget.show()
app.exec_()

