#numero incial
#numero final

'''
n = 5
12345
22345
33345
44445
55555
'''

linhaFinal = int(input())
linhaAtual = 1
numFinal = linhaFinal

while linhaAtual <= linhaFinal:
    
    numAtual = 1
    cnt = 1
    
    while numAtual <= numFinal:
            
        
        while cnt <= linhaAtual:
            print(linhaAtual, end='')
            cnt += 1
            numAtual += 1
            
        if numAtual <= numFinal:
            print(numAtual, end='')
        numAtual += 1 
    
    print()
    linhaAtual += 1
