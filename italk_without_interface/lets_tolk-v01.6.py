# -*- coding: utf -8 -*-
import sys
import time
import random
import os.path


def print_slowly(text):
    for c in text:
        print(c, end='')
        sys.stdout.flush()
        time.sleep(0.10)


def print_fast(text):
    for c in text:
        print(c, end='')
        sys.stdout.flush()
        time.sleep(0.02)


def print_faster(text):
    for c in text:
        print(c, end='')
        sys.stdout.flush()
        time.sleep(0.002)


d = ('        ##########################################################\n'
     '        ##########################################################\n'
     "        ##  ##\   /##| #####     #####  #     ###   #     #  #  ##\n"
     "        ##  # #\ /# #| ##  ##      #   ####  #   #  #     #/    ##\n"
     "        ##  #  #.#  #| #####       #    #    #   #  #     #\    ##\n"
     "        ##  #   #   #| ##   ##   #####  \##   ###   ####  #  #  ##\n"
     "        ##########################################################\n"
     "        ##########################################################\n")


X = {"E": "english", "P": "portugues", "I": "ingles", "p": "portuguese"}
lista = [1, 2, 3, 4, 5]
n = 0
s = 0

p = 1
k = 1
longs = X['E'], X['P'], X['I'], X['p']

print("welcome")
have = int(input("have you alred play the before?: (1) for YES and 2 for NO "))
if have == 1:
    name = input("what is your name?: ")
    f = os.path.exists(name + ".txt")
    if f is True:
        f = open(name + ".txt")
        u = f.readlines()
        q = open("long.txt")
        long1 = q.readline()
        for w in long1:
            print(w)
            print(len(w))
            for g in u:
                print(g)
                print(len(g))
                if name in g:
                    print(name, "is in ...")
                    while k > 0:
                        print_fast("---------------------------------------------------------------------------------------------\n")
                        try:
                            w = w.upper()
                            lang = X[w]
                            lang = lang.lower()

                            time.sleep(0.30)
                            up_word = lang.upper()
                            print(up_word)

                        except:
                            lang = w
                            lang = lang.lower()
                            time.sleep(0.30)
                            up_word = lang.upper()
                            print(up_word)

                        print_fast(
                            ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
                        if lang in longs:
                            k -= 1
                            if lang == longs[0] or lang == longs[2]:
                                print_fast(
                                    "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Welcome >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
                                time.sleep(0.30)
                                print_fast(
                                    ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Loading <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n")
                                time.sleep(0.30)
                                print_fast(
                                    "---------------------------------------------------------------------------------------------\n")
                                print_faster(d)
                                print_fast(
                                    "---------------------------------------------------------------------------------------------\n")
                                time.sleep(0.50)

                                print_fast("What is your name: ")
                                name = input(" ")
                                print_fast("Hi " + name)
                                print_fast(" My name is Mr itolk \n")
                                print_slowly("let start " + name + '\n')
                                try:
                                    longin = open(name + ".txt")
                                    w = longin.readlines()
                                    q = longin.read()
                                    print(q)
                                    print(w)
                                    longin.close()
                                except FileNotFoundError:
                                    singup = open(name + ".txt", "wt")
                                    singup.write(name + "\n")
                                    singup.write(lang)
                                    singup.close()

                                while p > 0:
                                    print_fast(
                                        "******************************************************************************************\n")
                                    print_fast("Guess the number I'm thinking of from 1 to 5: ")
                                    num = int(input(" "))
                                    num2 = random.choice(lista)
                                    if num in lista:
                                        if num == num2:

                                            y = 1
                                            s += 0
                                            n += y
                                            print_fast("You've won ")
                                            print(y, 'point')
                                            print("Your actual points is: ", n)
                                            print('My actual points is: ', s)
                                            print("I chose ", num2, " and you chose: ", num)

                                        else:
                                            y = 1
                                            n += 0
                                            s += y
                                            print_fast("your point is ")
                                            print(n)
                                            print_fast("my point is ")
                                            print(s)
                                            print("I chose ", num2, " and you chose: ", num)

                                        if n == 10:
                                            print(name, "your score is", n)
                                            print("My score in ", s)
                                            print(name + " you win!!")
                                            print_fast("<<<<<<<<<<<<<<<< GAME OVER >>>>>>>>>>>>>>>>>>>\n")

                                        if s == 10:
                                            print(name, "your score is", n)
                                            print("My score in ", s)
                                            print(name + " lose!!")
                                            print_fast("<<<<<<<<<<<<<<<<<<< GAME OVER >>>>>>>>>>>>>>>>>>\n")

                                        r = int(input('Select 1 to play again or 2 to quit: '))
                                        p = r

                                        if r == 2:
                                            print('Hope to see you again soon')
                                            break

                                    else:
                                        print_slowly("incorrect input\n")

                            elif lang == longs[1] or lang == longs[3]:
                                print_slowly(
                                    "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Bem Vindo >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
                                time.sleep(0.30)
                                print_fast(
                                    ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Loading <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n")
                                time.sleep(0.30)
                                print_faster(
                                    "---------------------------------------------------------------------------------------------\n")
                                print_faster(d)
                                print_fast(
                                    "---------------------------------------------------------------------------------------------\n")
                                time.sleep(0.50)

                                print_fast("Qual é seu nome: ")
                                name = input(" ")
                                print_fast("Olá " + name)
                                print_fast(" Meu nome é Mr itolk \n")

                                print_slowly("Vamos começar " + name + '\n')
                                while p > 0:
                                    print_fast(
                                        "*************************************************************************************************\n")
                                    print_fast("Adivinhe o numero que estou pensando de 1 até 5: ")
                                    num = int(input(" "))
                                    num2 = random.choice(lista)
                                    if num in lista:
                                        if num == num2:
                                            y = 1
                                            s += 0
                                            n = n + y
                                            print_fast("você ganhou ")
                                            print(y, "ponto")
                                            print_fast("seu atual pontos é: ")
                                            print(n)
                                            print_fast("meu atual pontos é: ")
                                            print(s)
                                            print_faster(
                                                "_____________________________________________________________________________________________\n")
                                            print(name, "você escoleu", num, "Eu escolei" + num2)

                                        else:
                                            y = 1
                                            n += 0
                                            s += y

                                            print_fast("seu atual pontos é: ")
                                            print(n)
                                            print_fast("eu ganhei: ")
                                            print(y)
                                            print_fast("meu atual pontos é: ")
                                            print(s, "pontos")
                                            print(name, "você escoleu", num, "Eu escolei", num2)

                                        if n == 10:
                                            print_fast(name + "seus ganhos é ")
                                            print(n)
                                            print_fast("Meus ganhos é ")
                                            print(s)
                                            print(name, "você é o ganhador!!!")
                                            print_fast("<<<<<<<<<<<<<<<<<<<<<<< GAME OVER >>>>>>>>>>>>>>>>>>>\n")

                                        if s == 10:
                                            print(name, "seus ganhos é", n)
                                            print("Meus ganhos é", s)
                                            print(name, "você perdeu!!!")
                                            print_fast("<<<<<<<<<<<<< GAME OVER >>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")

                                        r = int(input('Digite 1 para continua ou 2 para sair: '))
                                        p = r

                                        if r == 2:
                                            print('Volta jogar mais tarde')
                                            break

                                    else:
                                        print_slowly("número incorreto \n")
                        else:
                            print_slowly("input incorrect\n")
                            print('You entered: ', lang)
                            print('Try (E) for English or (P) for Portuguese \n Usa (I) para Ingles ou (P) para Portugues')
                            print_fast('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')

        f.close()
        q.close()


while k > 0:
    print_fast("---------------------------------------------------------------------------------------------\n")
    print_fast("Choose your prefered language, (E) for English or (P) for Portuguese?: \n Qual lingua voce prefere, Ingles(I) ou Portugues(P)?:")
    w = input(" ")
    try:
        w = w.upper()
        lang = X[w]
        lang = lang.lower()

        time.sleep(0.30)
        up_word = lang.upper()
        print(up_word)

    except:
        lang = w
        lang = lang.lower()
        time.sleep(0.30)
        up_word = lang.upper()
        print(up_word)

    print_fast(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
    if lang in longs:
        k -= 1
        if lang == longs[0] or lang == longs[2]:
            print_fast("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Welcome >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
            time.sleep(0.30)
            print_fast(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Loading <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n")
            time.sleep(0.30)
            print_fast("---------------------------------------------------------------------------------------------\n")
            print_faster(d)
            print_fast("---------------------------------------------------------------------------------------------\n")
            time.sleep(0.50)

            print_fast("What is your name: ")
            name = input(" ")
            print_fast("Hi " + name)
            print_fast(" My name is Mr itolk \n")
            print_slowly("let start " + name + '\n')
            try:
                longin = open(name + ".txt")
                w = longin.readlines()
                print(name, "you already have an account")
                longin.close()
            except FileNotFoundError:
                singup = open(name + ".txt", "wt")
                singup.write(name)
                singup.close()
                singup_lang = open("long.txt", "wt")
                singup_lang.write(w)
                singup_lang.close()
            while p > 0:
                print_fast("******************************************************************************************\n")
                print_fast("Guess the number I'm thinking of from 1 to 5: ")
                num = int(input(" "))
                num2 = random.choice(lista)
                if num in lista:
                    if num == num2:

                        y = 1
                        s += 0
                        n += y
                        print_fast("You've won ")
                        print(y, 'point')
                        print("Your actual points is: ", n)
                        print('My actual points is: ', s)
                        print("I chose ", num2, " and you chose: ", num)

                    else:
                        y = 1
                        n += 0
                        s += y
                        print_fast("your point is ")
                        print(n)
                        print_fast("my point is ")
                        print(s)
                        print("I chose ", num2, " and you chose: ", num)

                    if n == 10:
                        print(name, "your score is", n)
                        print("My score in ", s)
                        print(name + " you win!!")
                        print_fast("<<<<<<<<<<<<<<<< GAME OVER >>>>>>>>>>>>>>>>>>>\n")

                    if s == 10:
                        print(name, "your score is", n)
                        print("My score in ", s)
                        print(name + " lose!!")
                        print_fast("<<<<<<<<<<<<<<<<<<< GAME OVER >>>>>>>>>>>>>>>>>>\n")

                    r = int(input('Select 1 to play again or 2 to quit: '))
                    p = r

                    if r == 2:
                        print('Hope to see you again soon')
                        break

                else:
                    print_slowly("incorrect input\n")

        elif lang == longs[1] or lang == longs[3]:
            print_slowly("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Bem Vindo >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
            time.sleep(0.30)
            print_fast(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Loading <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n")
            time.sleep(0.30)
            print_faster("---------------------------------------------------------------------------------------------\n")
            print_faster(d)
            print_fast("---------------------------------------------------------------------------------------------\n")
            time.sleep(0.50)

            print_fast("Qual é seu nome: ")
            name = input(" ")
            print_fast("Olá " + name)
            print_fast(" Meu nome é Mr itolk \n")

            print_slowly("Vamos começar " + name + '\n')
            while p > 0:
                print_fast("*************************************************************************************************\n")
                print_fast("Adivinhe o numero que estou pensando de 1 até 5: ")
                num = int(input(" "))
                num2 = random.choice(lista)
                if num in lista:
                    if num == num2:
                        y = 1
                        s += 0
                        n = n + y
                        print_fast("você ganhou ")
                        print(y, "ponto")
                        print_fast("seu atual pontos é: ")
                        print(n)
                        print_fast("meu atual pontos é: ")
                        print(s)
                        print_faster("_____________________________________________________________________________________________\n")
                        print(name, "você escoleu", num, "Eu escolei" + num2)

                    else:
                        y = 1
                        n += 0
                        s += y

                        print_fast("seu atual pontos é: ")
                        print(n)
                        print_fast("eu ganhei: ")
                        print(y)
                        print_fast("meu atual pontos é: ")
                        print(s, "pontos")
                        print(name, "você escoleu", num, "Eu escolei", num2)

                    if n == 10:
                        print_fast(name + "seus ganhos é ")
                        print(n)
                        print_fast("Meus ganhos é ")
                        print(s)
                        print(name, "você é o ganhador!!!")
                        print_fast("<<<<<<<<<<<<<<<<<<<<<<< GAME OVER >>>>>>>>>>>>>>>>>>>\n")

                    if s == 10:
                        print(name, "seus ganhos é", n)
                        print("Meus ganhos é", s)
                        print(name, "você perdeu!!!")
                        print_fast("<<<<<<<<<<<<< GAME OVER >>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")

                    r = int(input('Digite 1 para continua ou 2 para sair: '))
                    p = r

                    if r == 2:
                        print('Volta jogar mais tarde')
                        break

                else:
                    print_slowly("número incorreto \n")
    else:
        print_slowly("input incorrect\n")
        print('You entered: ', lang)
        print('Try (E) for English or (P) for Portuguese \n Usa (I) para Ingles ou (P) para Portugues')
        print_fast('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')
