import  random
import  time
import os

class Randoms():
    def __init__(self, msg):

        self.n = 0
        self.s = 0
        self.lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        lista  = str(self.lista)


        self.num1 = random.choice(self.lista)
        num1 = str(self.num1)
        self.lista.remove(self.num1)
        print(self.lista)
        self.num2 = random.choice(self.lista)
        self.lista.remove(self.num2)
        print(self.lista)
        self.num3 = random.choice(self.lista)
        self.lista.remove(self.num3)
        print(self.lista)
        self.num4 = random.choice(self.lista)
        self.num = [self.num1, self.num2, self.num3, self.num4]
        self.num = list(self.num)
        print(self.num)

        self.u = msg.split(' ')
        print(self.u)
        self.user1 = int(self.u[0])

        self.user2 = int(self.u[1])
        self.user3 = int(self.u[2])
        self.user4 = int(self.u[3])
        q = (self.user1, self.user2, self.user3, self.user4)
        q = list(q)
        print(q)

        if self.user1 in self.num:
            self.num.remove(self.user1)
            print(self.user1)
            print(self.num)

        if self.user2 in self.num:
            self.num.remove(self.user2)
            print(self.user2)
            print(self.num)

        if self.user3 in self.num:
            self.num.remove(self.user3)
            print(self.user3)
            print(self.num)

        if self.user4 in self.num:
            self.num.remove(self.user4)
            print(self.user4)
            print(self.num)

            #print(user)
            #if user == num:
             #   y = 1
              #  n += y
               # s = 0
        #print(user)
