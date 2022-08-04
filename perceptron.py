### 我李健立自己思考解決、絕無抄襲 ###
import numpy as np
import matplotlib.pyplot as plt
def OR(x1,x2):
    L = w31*x1+w32*x2-b3
    if L > 0 : return 1
    else : return 0

def NAND(x1,x2):
    L = w21*x1+w22*x2-b2
    if L > 0 : return 1
    else : return 0

def AND(x1,x2):
    L = w11*x1+w12*x2-b1
    if L > 0 : return 1
    else : return 0
    
def XOR(x1,x2):
    return AND(NAND(x1,x2) , OR(x1,x2))

plt.figure(1,figsize = (14,9))
for i in range(1,10):
    while True:
        w11,w12,b1 = np.random.uniform(-9,9,3)
        if -b1 <= 0 and w11-b1 <= 0 and w12-b1 <= 0 and w11+w12-b1 > 0 :  #設定(0,0),(1,0),(0,1),(1,1)的情況
            break 
    while True:
        w21,w22,b2 = np.random.uniform(-9,9,3)
        if -b2 > 0 and w21-b2 > 0 and w22-b2 > 0 and w21+w22-b2 <= 0 :
            break
    while True:
        w31,w32,b3 = np.random.uniform(-9,9,3)
        if -b3 <= 0 and w31-b3 > 0 and w32-b3 > 0 and w31+w32-b3 > 0 :
            break
    X = np.arange(-1,2,0.1)   #數線範圍設定在[-1,2)之間，每次前進0.1
    Y = np.arange(-1,2,0.1)
    rx , ry = [],[]
    gx , gy = [],[]
    for x in X:
        for y in Y:
            if XOR(x,y) > 0 :  #若XOR傳遞訊號則畫上紅點，否則畫上綠點
                rx.append(x)
                ry.append(y)
            else :
                gx.append(x)
                gy.append(y)
    plt.subplot(3,3,i)
    plt.scatter(rx,ry , c = 'r' , s = 35)
    plt.scatter(gx,gy , c = 'g' , s = 35)
    plt.scatter([0,1],[1,0] , c = 'w' , edgecolors = 'r' , linewidths = 2 , s = 35)
    plt.scatter([0,1],[0,1] , c = 'w' , edgecolors = 'g' , linewidths = 2 , s = 35)
    
plt.tight_layout()
plt.show()


