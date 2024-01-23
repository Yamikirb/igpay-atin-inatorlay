CC=input('give words for pig:')

dog=0
cat=0
bird=0

words = CC.split()
print(words)
    
for i in words:
    dog=0
    cat=0

    BB=words[bird]



    for letter in BB:
        if letter == 'a' or letter =='e' or letter =='i' or letter =='u' or letter =='o':
            break
        dog+=1
        cat+=1

    first=CC[bird]
    bird+=1


    sub = BB[dog:]
    print(sub,end='-')

    dog=0
    while dog != cat:
        first=BB[dog]
        print(first,end='')
        dog+=1

    firstletter=BB[0]
    if firstletter== 'a' or firstletter =='e' or firstletter =='i' or firstletter =='u' or firstletter =='o':
        print('yay ',end='')
    else:
        print('ay ',end='')

    
