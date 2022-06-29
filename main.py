import random


char = 'qwertyuiopasdfghjklzxcvbnm123456789QWERTYUIOPASDFGHJKLZXCVBNM'

for i in range(10000):

    first = ''.join((random.choice(char) for i in range(24)))

    sec = ''.join((random.choice(char) for i in range(6)))

    end = ''.join((random.choice(char) for i in range(27)))


    result = first + '.' + sec + '.' + end

    print(f'' + result)

    output = open('tokens.txt', 'a')
    output.write(result + '\n')