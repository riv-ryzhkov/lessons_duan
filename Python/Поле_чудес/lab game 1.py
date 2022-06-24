text=list(input('Input text : '))
attempt=len(text)
n=60
pole="*"*len(text)
print(pole)

while attempt:
    symbol= input('Input symbol: ')

    if text.count(symbol):
        print('\n' * 3, '!' * n)
        print('Great!!!'.center(n, ' '))
        print(('The symbol "' + symbol + '" is in the text !').center(n, ' '))
        print('!' * n)
        attempt+=1
        #for num in range(len(text)):
            #if symbol==text[num]:
                #dop=dop+symbol
            #else:
                #dop=dop+pole[num]
        print(pole)
        print()
        attempt -= 1
        print(('No symbol "'+ symbol + '" is in the text !').center(n, ' '))
        print('Try again! You have ', attempt, 'attempts.')
    else:
        print('=' * n)
        print("Sorry, you don't have any attempts...")
        print('='*n)
    
    
while "*" in pole:
    #user=input("Угадайте букву ")
    dop=""
    for num in range(len(text)):
        if user==text[num]:
            dop=dop+user
        else:
            dop=dop+pole[num]
    pole=dop
    print(pole)
