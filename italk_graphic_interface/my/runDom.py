import  random
import  time
import os
from WINK import ChatPage

lista = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
class Game(ChatPage):
    def __init__(self):
        pass
    def mr_itolkRun(self):
        Clock.schedule_once(self.focus_text_input, 0.1)

        self.s = 0
        self.n = 0

        while self.new_message.text:
            self.num2 = random.choice(lista)
            info = 'Info'
            try:
                self.num = int(self.new_message.text)

            except:
                self.history.update_chat_history(f'[color=dd2020]{info}[/color] > Incorrect Input'
                                                 f'[color=d2d020] {Chat_app.user_page.Name.text} [/color]'
                                                 f' You entered an alphabet. The GAME only support numbers\n')
                self.adjust_fields()
                self.history.update_chat_history(
                    f"> [color=a499ec] Guess the number I'm thinking of from 1 to 5 [/color]\n")
                self.new_message.text = ''
                Clock.schedule_once(self.focus_text_input, 0.1)
                time.sleep(0.10)
                break

            if self.num in lista:

                if self.num == self.num2:

                    self.f = os.path.exists("you.txt")
                    if self.f is True:
                        self.f = open("you.txt")
                        u = self.f.readline()
                        self.q = open("itolk.txt")
                        itolk = self.q.readline()
                        for self.u in u:
                            for self.itolk in itolk:
                                u = int(self.u)
                                itolk = int(self.itolk)
                                self.y = 1
                                itolk += 0
                                u += self.y
                                y = str(self.y)
                                self.f.close()
                                self.q.close()

                                singup = open("you.txt", "wt")
                                singup.write(str(u))
                                singup.close()
                                singup_lang = open("itolk.txt", "wt")
                                singup_lang.write(str(itolk))
                                singup_lang.close()

                                num2str = str(self.num2)
                                num = self.new_message.text
                                self.history.update_chat_history(
                                    f'> [color=20dd20] {name2}[/color] [color=a499ec] chose: [/color]'
                                    f' {num2str}\n')

                                self.history.update_chat_history(
                                    f"> [color=d2d020] {Chat_app.user_page.Name.text} [/color]"
                                    f" [color=a499ec] you've won {y} point [/color]\n")

                                self.history.update_chat_history(
                                    f"> [color=d2d020] {Chat_app.user_page.Name.text} [/color]"
                                    f" [color=a499ec] your score is: {str(u)} [/color]")
                                self.history.update_chat_history(
                                    f"> [color=20dd20] {name3} [/color] [color=a499ec] score is:"
                                    f" {str(itolk)} [/color]\n")

                                self.adjust_fields()
                                time.sleep(0.30)


                    else:
                        self.y = 1
                        self.s += 0
                        self.n += self.y
                        y = str(self.y)

                        n = self.n
                        s = self.s
                        singup = open("you.txt", "wt")
                        singup.write(str(n))
                        singup.close()
                        singup_lang = open("itolk.txt", "wt")
                        singup_lang.write(str(s))
                        singup_lang.close()

                        num2str = str(self.num2)
                        num = self.new_message.text
                        self.history.update_chat_history(
                            f'> [color=20dd20] {name2}[/color] [color=a499ec] chose: [/color]'
                            f' {num2str}\n')

                        self.history.update_chat_history(f"> [color=d2d020] {Chat_app.user_page.Name.text} [/color]"
                                                         f" [color=a499ec] you've won {y} point [/color]\n")

                        self.history.update_chat_history(f"> [color=d2d020] {Chat_app.user_page.Name.text} [/color]"
                                                         f" [color=a499ec] your score is: {str(n)} [/color]")
                        self.history.update_chat_history(
                            f"> [color=20dd20] {name3} [/color] [color=a499ec] score is:"
                            f" {str(s)} [/color]\n")

                        self.adjust_fields()
                        time.sleep(0.30)



                else:

                    self.f = os.path.exists("you.txt")
                    if self.f is True:
                        self.f = open("you.txt")
                        u = self.f.readline()
                        self.q = open("itolk.txt")
                        itolk = self.q.readline()
                        for self.u in u:
                            for self.itolk in itolk:
                                self.u = int(self.u)
                                self.itolk = int(self.itolk)
                                self.y = 1
                                self.itolk += self.y
                                self.u += 0

                                u = str(self.u)
                                itolk = str(self.itolk)
                                y = str(self.y)
                                self.f.close()
                                self.q.close()

                                singup = open("you.txt", "wt")
                                singup.write(u)
                                singup.close()
                                singup_lang = open("itolk.txt", "wt")
                                singup_lang.write(itolk)
                                singup_lang.close()

                                num2str = str(self.num2)
                                self.history.update_chat_history(
                                    f'> [color=20dd20] {name2}[/color] [color=a499ec] chose: [/color]'
                                    f' {num2str}\n')

                                self.history.update_chat_history(
                                    f"> [color=20dd20] {name2} [/color] [color=a499ec] won {y}"
                                    f" point [/color]\n")

                                self.history.update_chat_history(
                                    f"> [color=d2d020] {Chat_app.user_page.Name.text} [/color]"
                                    f" [color=a499ec] your score is: {str(u)} [/color]")

                                self.history.update_chat_history(
                                    f"> [color=d2d020] {name3} [/color] [color=a499ec] score is:"
                                    f" {str(itolk)} [/color]\n")

                                self.adjust_fields()
                                time.sleep(0.30)


                    else:
                        self.y = 1
                        self.n += 0
                        self.s += self.y
                        y = str(self.y)

                        n = str(self.n)
                        s = str(self.s)

                        singup = open("you.txt", "wt")
                        singup.write(n)
                        singup.close()
                        singup_lang = open("itolk.txt", "wt")
                        singup_lang.write(s)
                        singup_lang.close()

                        num2str = str(self.num2)
                        self.history.update_chat_history(
                            f'> [color=20dd20] {name2}[/color] [color=a499ec] chose: [/color]'
                            f' {num2str}\n')

                        self.history.update_chat_history(
                            f"> [color=20dd20] {name2} [/color] [color=a499ec] won {y}"
                            f" point [/color]\n")

                        self.history.update_chat_history(f"> [color=d2d020] {Chat_app.user_page.Name.text} [/color]"
                                                         f" [color=a499ec] your score is: {str(n)} [/color]")

                        self.history.update_chat_history(
                            f"> [color=d2d020] {name3} [/color] [color=a499ec] score is:"
                            f" {str(s)} [/color]\n")

                        self.adjust_fields()
                        time.sleep(0.30)

                self.n = open("you.txt")
                n = self.n.readline()
                self.s = open('itolk.txt')
                s = self.s.readline()
                for self.n in n:
                    for self.s in s:
                        self.n = int(self.n)
                        self.s = int(self.s)
                        if self.n == 5:

                            Chat_app.Game_Ovoer()
                            Chat_app.screen_manager.current = "end_of_game"

                            n = str(self.n)
                            s = str(self.s)
                            self.history.update_chat_history(f"> [color=d2d020] {Chat_app.user_page.Name.text} [/color]"
                                                             f" [color=a499ec] your score is: {n} [/color]")
                            self.history.update_chat_history(f"> [color=20dd20] {name3} [/color] [color=a499ec] "
                                                             f"score is: {s} [/color]\n")

                            self.history.update_chat_history(f"> [color=d2d020] {Chat_app.user_page.Name.text} [/color]"
                                                             f" [color=a499ec] you WON!!! [/color]\n")
                            self.history.update_chat_history(f"> [color=20dd20] {name2} [/color]"
                                                             f" [color=a499ec] LOST!!! [/color]\n")

                            if os.path.exists('you.txt'):
                                os.remove('you.txt')
                                os.remove('itolk.txt')

                        if self.s == 5:

                            Chat_app.Game_Ovoer()
                            Chat_app.screen_manager.current = "end_of_game"

                            n = str(self.n)
                            s = str(self.s)
                            self.history.update_chat_history(f"> [color=20dd20] {name3} [/color] [color=a499ec] "
                                                             f"score is: {s} [/color]")
                            self.history.update_chat_history(f"> [color=d2d020] {Chat_app.user_page.Name.text} [/color]"
                                                             f" [color=a499ec] your score is: {n} [/color]\n")

                            self.history.update_chat_history(f"> [color=20dd20] {name2} [/color]"
                                                             f" [color=a499ec] WON!!! [/color]\n")

                            self.history.update_chat_history(f"> [color=d2d020] {Chat_app.user_page.Name.text} [/color]"
                                                             f" [color=a499ec] you LOST!!! [/color]\n")

                            if os.path.exists('you.txt'):
                                os.remove('you.txt')
                                os.remove('itolk.txt')

                self.history.update_chat_history(
                    f"> [color=a499ec] Guess the number I'm thinking of from 1 to 5 [/color]\n")
                self.new_message.text = ''
                Clock.schedule_once(self.focus_text_input, 0.1)
                time.sleep(0.10)

            else:
                self.history.update_chat_history(f'[color=dd2020]{info}[/color] > The number you'
                                                 f' entered is incorrect\n')
                self.adjust_fields()
                time.sleep(0.30)
                self.history.update_chat_history(
                    f"> [color=a499ec] Guess the number I'm thinking of from 1 to 5 [/color]\n")
                self.new_message.text = ''
                Clock.schedule_once(self.focus_text_input, 0.1)
                time.sleep(0.10)
