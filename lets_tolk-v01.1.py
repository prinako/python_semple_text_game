# -*- coding: utf -8 -*-
import sys
import time
import random


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


longs = ["english", "portuguese"]
lista = [1, 2, 3, 4, 5]
n = 0
s = 0

p = 1
k = 1


print_fast("What langua do you want to chat with, English or Portuguese: ")
lang = input(" ")
lang = lang.lower()

time.sleep(0.30)
up_word = lang.upper()
print(up_word)

print_fast(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
if lang in longs:
    if lang == longs[0]:
        print_slowly("<<<<<<<<<<<< Welcome >>>>>>>>>>>>>>>>\n")
        time.sleep(0.30)
        print_fast(">>>>>>>>>>>> Loading >>>>>>>>>>>>>>>>>>\n")
        time.sleep(0.30)

        print_fast("What is your name: ")
        name = input(" ")
        print_fast("Hi " + name)
        print(name)
        print_fast(" my name is Mr itolk \n")

        print_slowly("let start " + name + '\n')
        while p > 0:
            print_fast("pls " + name + " what is you lucky number for 1 up to 5: ")
            num = int(input(" "))
            num2 = random.choice(lista)
            if num in lista:
                if num == lista:
                    print_fast("****************************************************\n")
                    y = 1
                    s += 0
                    n += y
                    print("you win ", n, " point")
                    print("i choice ", num2, " and you choose: ", num)

                else:
                    y = 1
                    n += 0
                    s += y
                    print_fast("***********************************************\n")
                    print_fast("your point is ")
                    print(n)
                    print_fast("my point is ")
                    print(s)
                    print("i choice ", num2, " and you choise: ", num)

                if n == 10:
                    print(name, "your score is", n)
                    print("My score in ", s)
                    print(name + " you win!!")
                    print_fast("<<<<<<<<<<<<<<<< GAME OVER >>>>>>>>>>>>>>>>>>>\n")
                    break

                if s == 10:
                    print(name, "your score is", n)
                    print("My score in ", s)
                    print(name + " lose!!")
                    print_fast("<<<<<<<<<<<<<<<<<<< GAME OVER >>>>>>>>>>>>>>>>>>\n")
                    break

            else:
                print_slowly("incorrect input\n")

        p += 1
        k += 1

    elif lang == longs[1]:
        print_slowly("<<<<<<<<<<<< Bem Vindo >>>>>>>>>>>>>>>>\n")
        time.sleep(0.30)
        print_fast(">>>>>>>>>>>> Loading >>>>>>>>>>>>>>>>>>\n")
        time.sleep(0.30)

        print_fast("Qual é seu nome: ")
        name = input(" ")
        print_fast("Olá " + name)
        print_fast(" Meu nome é Mr itolk \n")

        print_slowly("vamos começar " + name + '\n')
        while k > 0:
            print_fast("por favor, qual é seu número de sorte de 1 até 5: ")
            num = int(input(" "))
            num2 = random.choice(lista)
            if num in lista:
                if num == num2:
                    y = 1
                    s += 0
                    print_fast("___________________________________________\n")
                    n = n + y
                    print_fast("você ganhou ")
                    print(y, "ponto")
                    print_fast("seu atual pontos é: ")
                    print(n)
                    print_fast("meu atual pontos é: ")
                    print(s)
                    print(name, "você escoleu", num, "Eu escolei", num2)

                else:
                    print_fast("___________________________________________\n")
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
                    print(name, "seus ganhos é", n)
                    print("Meus ganhos é", s)
                    print(name, "você é o ganhador!!!")

                    print_fast("<<<<<<<<<<<<<<<<<<<<<<< GAME OVER >>>>>>>>>>>>>>>>>>>\n")
                    break

                if s == 10:
                    print(name, "seus ganhos é", n)
                    print("Meus ganhos é", s)
                    print(name, "você perdeu!!!")
                    print_fast("<<<<<<<<<<<<< GAME OVER >>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
                    break

        else:
            print_slowly("número incorreto \n")

else:
    print_slowly("input incorrect\n")
