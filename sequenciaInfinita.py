limiteAprox = int(input())


interacoes = 0
#e = 0
    
while interacoes < limiteAprox:
    

    if interacoes == 0:
        fat = 1
        e = 1.0
    else:
        #fatorial
        fat = interacoes
        valor = interacoes
        while valor > 1:
            valor -= 1
            fat = fat * valor
            
        e = e + (1 / fat)
    interacoes += 1
    
    
    
print(e)