# 0.0.0.0 to 255.255.255.255

# IP address is basically divided into two parts: X1. X2. X3. X4
# 1. [X1. X2. X3] is the Network ID
# 2. [X4] is the Host ID

# Works in IPv4

from random import randint

def generateIP(times):
    arrayIP = []

    for i in range(times):
        rndArr = [randint(0, 255), randint(0, 255), randint(0, 255), randint(0, 255)] # IP's can only go upto 255
        if rndArr[0] == 192: # Use these how you wish fonta
            privateip = true
        elif rndArr[0] == 172 and rndArr == 16:
            privateip = true
        elif rndArr[0] == 10:
            privateip= true
        else:
            pass
        finalIP = '.'.join(str(x) for x in rndArr)
        arrayIP.append(finalIP)
    
    return arrayIP

#print(generateIP(5))
