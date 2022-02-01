    for isiKosong in arrayAlphabet: 
        i = 0
        if isiKosong == 0:
            arrayBujurSangkar[bujurX][bujurY] = 1
            if bujurY==4:
                bujurX+=1
                bujurY=0
            else:
                bujurY+=1
        i = i+1  