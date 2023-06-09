import time
list_1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
#list_2 = list_1[0:5]
#print(list_2)
temp_down = []

n = 0
while True:
    list_2 = list_1[n*10:(n+1)*10]
    
    # lage en inheining for dem som at bare dem kan gå på en gang
    while True:
        time.sleep(0.5)
        for episode in range(len(list_2)):
            # prøv å last ned den første linken i listen
            # noter det ned om den komm ned og ikke gjør noe om den ikke kom ned
            # om den kom ned lagre navnet i en list som skal bli generert via n og episode
            # se i downloads etter en fil med uten . part som ikke er i listen med filer som blir lastet ned
    
    
    
    
    
    n += 1
    if len(list_1) < n*10:
        break