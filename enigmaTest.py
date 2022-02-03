key = str(input("Masukkan Key = "))
teks = str(input('Masukkan Teks: '))
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
            # print(newFast[1][idxTeks])
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

print(enigma(key,teks,2))
