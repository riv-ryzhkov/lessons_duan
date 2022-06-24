import random
#text=open("C:/Users/Margo/Desktop/game.txt")
text=list(input('Input text : '))
n=60
slova={}
attempt=len(text)
#for line in text:
    #slova[line]=text.read()
#vybor=random.choice(list(slova.keys()))
#slovo=vybor.strip()
#print(slova[vybor])
pole="*"*len(text)
#attempt
print(pole)

while "*" in pole:
    user=input("Угадайте букву ")
    dop=""
     
    for num in range(len(text)):
        if user==text[num]:
            dop=dop+user
            print('\n' * 3, '!' * n)
            print('Great!!!'.center(n, ' '))
            print(('The symbol "' + user + '" is in the text !').center(n, ' '))
            print('!' * n)
            attempt +=1
            print(pole)
            print()
        else:
            attempt -= 1
            print(('No symbol "'+ user + '" is in the text !').center(n, ' '))
            print('Try again! You have ', attempt, 'attempts.')
            dop=dop+pole[num]
            
        #else:
            #print('=' * n)
            #print("Sorry, you don't have any attempts...")
            #print('='*n)
            #dop=dop+pole[num]
            
    pole=dop
    print(pole)
'''
for num in range(len(text)):
    if user==text[num]:
        dop=dop+user
        print('\n' * 3, '!' * n)
        print('Great!!!'.center(n, ' '))
        print(('The symbol "' + user + '" is in the text !').center(n, ' '))
        print('!' * n)
        attempt +=1
        print(pole)
        print()
    else:
        attempt -= 1
        print(('No symbol "'+ user + '" is in the text !').center(n, ' '))
        print('Try again! You have ', attempt, 'attempts.')
        dop=dop+pole[num]
            
        #else:
            #print('=' * n)
            #print("Sorry, you don't have any attempts...")
            #print('='*n)
            #dop=dop+pole[num]
            
    #pole=dop
    print(pole)
'''
