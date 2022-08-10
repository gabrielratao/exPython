def maiores(lista):
    maior = lista[0]

    if len(lista) == 1:
        segundoMaior = lista[0]
        segundoMaior = 'nenhum'
    
        
    if len(lista) > 1:
        if maior < lista[1]:
            maior = lista[1]
            segundoMaior = lista[0]
        else:
            segundoMaior = lista[1]
    
    
        
    cnt = 2
    while cnt < len(lista):
    
        if lista[cnt] > maior:
            segundoMaior = maior
            maior = lista[cnt]
            
        
        elif lista[cnt] > segundoMaior:
            segundoMaior = lista[cnt]
            
            
            
        cnt += 1
   
    
    return [maior, segundoMaior]
    

lista = [10, 2, 36, 4, 3, 0, 9, 8, 7]
print(maiores(lista))