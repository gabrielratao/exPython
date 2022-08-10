n = int(input())
cnt = 0
i = 1
while i <= n:
    if n % i == 0:
        cnt += 1
    i += 1

if cnt == 2:
    print('É primo!')
else:
    print('Não é primo!')