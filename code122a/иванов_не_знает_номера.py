def reshulya():
    command = int(input(" If you не говорите по-английски, введите текст в кавычках (да, я дуралей)"
                        " \n Please input the type of problem with a number: \n"
                        " 1 - Text problem \n"
                        " 2 - Picture problem \n"
                        " 3 - Sound problem \n If a variable is unknown, enter 0 \n"
                        " All inputs are considered to be in bits \n"))
    if command == 1 or command == 2:
        print("hello")
        N = int(input("Power of the alphabet(number of colours: "))
        I = int(input("Informational weight of the message: "))
        i = int(input("Informational weight of a single character: "))
        k1 = int(input("If this is the only number of characters, press enter for k2 and k3\n"
                       "The first number of characters(number of characters in a line): "))
        k2 = int(input("The second number of charcters(number of lines): "))
        k3 = int(input("The third number of characters(number of pages): "))
        if k2 == 0:
            k = k1
        elif k3 == 0:
            k = k1 * k2
        else:
            k = k1 * k2 * k3
            if i == 0:
                while N > 0:
                    N = N // 2
                    i = i + 1
                    print (i)
        if k == 0:
            k = I / i
            print (k)
        if N == 0:
            N = pow(2,i)
            print(N)
        if I == 0:
            I = k * i
            print(I)
    if command == 0:
        print("Так нельзя, дурашка")
    if command == 3:
        N = int(input("коло-во уровней дискретизации"))
        i = int(input("глубюина звука"))
        D = int(input("частота дискретизации"))
        T = int(input("Длительность файла"))
        V = int(input("объём звукогого файла"))
        k = int(input("кол-во каналов(моно = 1, стерео = 2)"))
        if k != 2:
            k = 1
        if N != int("") and i == int(""):
            while N > 0:
                N = N // 2
                i = i + 1
            print(i)
        else:
            i = V / D / k / T
            print(i)
        if N == 0:
            N = pow(2, i)
            print(N)
        if D == 0:
            D = V / k / i / T
            print(D)
        if T == 0:
            T = V / k / i / D
            print(T)
        if k == 0:
            k = V / D / i / T
            print(k)
        if V == 0:
            V = D * k * i * T
            print(V)
            print('See you later alligator')
