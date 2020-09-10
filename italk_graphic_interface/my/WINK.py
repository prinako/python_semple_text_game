# -*- coding: utf -8 -*-

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.checkbox import CheckBox
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
import socket
from _thread import *
import errno
import sys
import random
import time
import os

kivy.require('1.11.1')

lista = (1, 2, 3, 4, 5)

name2 = "Mr itolk"
name3 = "Mr itolk's"


class UserPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2

        REGISTER = os.path.exists('prev_details.txt')
        if REGISTER:
            with open("prev_details.txt", "r") as f:
                d = f.read().split(",")
                prev_ip_addr = d[0]
                prev_port = d[1]
                prev_username = d[2]

            self.add_widget(Label())
            self.add_widget(Label())

            self.add_widget(Label(text="Name:"))
            self.Name = TextInput(text=prev_username, multiline=False)
            self.add_widget(self.Name)
            Clock.schedule_once(self.focus_text_input)

            #self.gama = f'Mr_italk'

            self.ip_addr = TextInput(text=prev_ip_addr, multiline=False)
            #self.add_widget(Label(text="Choose Your Language"))
            #self.add_widget(Label())
            self.add_widget(Label(text="SERVER IP :"))
            self.add_widget(self.ip_addr)

            self.port = TextInput(text=prev_port, multiline=False)
            self.add_widget(Label(text="SERVER PORT :"))
            self.add_widget(self.port)
        else:
            self.add_widget(Label())
            self.add_widget(Label())

            self.add_widget(Label(text="Name:"))
            self.Name = TextInput(multiline=False)
            self.add_widget(self.Name)
            Clock.schedule_once(self.focus_text_input)

            # self.gama = f'Mr_italk'

            self.ip_addr = TextInput(multiline=False)
            # self.add_widget(Label(text="Choose Your Language"))
            # self.add_widget(Label())
            self.add_widget(Label(text="SERVER IP :"))
            self.add_widget(self.ip_addr)

            self.port = TextInput(multiline=False)
            self.add_widget(Label(text="SERVER PORT :"))
            self.add_widget(self.port)

        self.start = Button(text="Start")
        self.add_widget(self.start)
        self.start.bind(on_press=self.start_button)


       # self.lbl_active = Label(text="Please choose your language")
        #self.add_widget(self.lbl_active)

        Window.bind(on_key_dwon=self.on_key_down)

        if os.path.exists('you.txt'):
            os.remove('you.txt')
            os.remove('itolk.txt')

        usaname = self.Name.text
        ip = self.ip_addr.text
        port = self.port.text

    def on_key_down(self, instance, keyboard, keycode, text, modifiers):
        if keycode == 40:
            self.start_button(None)

    def focus_text_input(self, *_):
        self.Name.focus = True

    def start_button(self, instance):
        username = self.Name.text
        ip_addr = self.ip_addr.text
        port = self.port.text
        with open("prev_details.txt", "w") as f:
            f.write(f"{ip_addr},{port},{username}")

        if username == '':
            info = f'Pleas check your Name and try again'
            Chat_app.wlecome_page.update_info(info)
            Chat_app.screen_manager.current = "wlecome"
            return Clock.schedule_once(self.erron_in, 2)

        if ip_addr == '':
            info = f'Pleas check the Server IP and try again'
            Chat_app.wlecome_page.update_info(info)
            Chat_app.screen_manager.current = "wlecome"
            return Clock.schedule_once(self.erron_in, 3)

        if port == '':
            info = f'Pleas check the Server PORT and try again'
            Chat_app.wlecome_page.update_info(info)
            Chat_app.screen_manager.current = "wlecome"
            return Clock.schedule_once(self.erron_in, 3)

        info = f"{username} you are connecting... to the server with {ip_addr}:{port} please wait for a second"
        Chat_app.wlecome_page.update_info(info)
        Chat_app.screen_manager.current = "wlecome"

        Clock.schedule_once(self.connect, 2)

    def erron_in(self, *_):
        Chat_app.screen_manager.current = "user"

    def connect(self, _):
        username = self.Name.text
        ip_addr = self.ip_addr.text
        port = int(self.port.text)
        ADRRS = (ip_addr, port)
        client_socket.connect(ADRRS)

        username = username.encode('utf-8')
        username_header = f'{len(username):<{HEADER}}'.encode('utf-8')
        client_socket.send(username_header + username)

        Chat_app.create_chat_page()
        Chat_app.screen_manager.current = "Chat"


class ScrolBar(ScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.layout = GridLayout(cols=1, size_hint_y=None)
        self.add_widget(self.layout)

        self.chat_history = Label(size_hint_y=None, markup=True)
        self.scroll_to_point = Label()

        self.layout.add_widget(self.chat_history)
        self.layout.add_widget(self.scroll_to_point)

    def update_chat_history(self, message, *_):
        self.chat_history.text += '\n' + message

        self.layout.height = self.chat_history.texture_size[1] + 15
        self.chat_history.height = self.chat_history.texture_size[1]
        self.chat_history.text_size = (self.chat_history.width * 0.98, None)

        self.scroll_to(self.scroll_to_point)

    def update_chat_history_layout(self, _=None):
        self.layout.height = self.chat_history.texture_size[1] + 15
        self.chat_history.height = self.chat_history.texture_size[1]
        self.chat_history.text_size = (self.chat_history.width * 0.98, None)


class ChatPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 1
        self.rows = 2

        self.history = ScrolBar(height=Window.size[1] * 0.9, size_hint_y=None)
        self.add_widget(self.history)

        # We are going to use 1 column and 2 rows
        self.new_message = TextInput(width=Window.size[0] * 0.8, size_hint_x=None, multiline=False)
        self.send = Button(text="Send")
        self.send.bind(on_press=self.send_message)

        bottom_line = GridLayout(cols=2)
        bottom_line.add_widget(self.new_message)
        bottom_line.add_widget(self.send)
        self.add_widget(bottom_line)


        Window.bind(on_key_down=self.on_key_down)

        Window.bind(on_key_down1=self.mr_itolkRun)

        Clock.schedule_once(self.focus_text_input, 0.1)

        self.bind(size=self.adjust_fields)
        if True:
            start_new_thread(self.reciver_for_sever, (self,))
            #self.reciver_for_sever()
            #self.recive_thread = threading.Thread(target=self.reciver_for_sever)
            #self.recive_thread.start()
            #self.recive_thread.join()

        if Chat_app.user_page.Name.text:
            self.history.update_chat_history(
                f"> [color=a499ec] Guess the number I'm thinking of from 1 to 5 [/color]\n")



    def adjust_fields(self, *_):

        if Window.size[1] * 0.1 < 50:
            new_height = Window.size[1] - 50
        else:
            new_height = Window.size[1] * 0.9
        self.history.height = new_height

        if Window.size[0] * 0.2 < 160:
            new_width = Window.size[0] - 160
        else:
            new_width = Window.size[0] * 0.8
        self.new_message.width = new_width

        Clock.schedule_once(self.history.update_chat_history_layout, 0.01)

    def on_key_down(self, instance, keyboard, keycode, text, modifiers):
        if keycode == 40:
            self.send_message(None)

    def send_message(self, _):
        message = self.new_message.text
        self.new_message.text = ''

        Clock.schedule_once(self.focus_text_input, 0.1)

        if message:
            Clock.schedule_once(self.focus_text_input, 0.1)
            self.history.update_chat_history(f'> [color=d2d020] {Chat_app.user_page.Name.text}[/color] [color=a499ec]'
                                             f' chose: [/color] {message}')
            return self.send_to_server(message)

        Clock.schedule_once(self.focus_text_input, 0.1)

    def focus_text_input(self, *_):
        self.new_message.focus = True

    def reciver_for_sever(self, *_):

        while True:
            try:

                user_header = client_socket.recv(HEADER)

                if not len(user_header):
                    self.history.update_chat_history(f'[color=dd2020] connection closed by the server [/color]')
                    sys.exit()

                user_length = int(user_header.decode("utf-8").strip())
                user = client_socket.recv(user_length).decode('utf-8')

                msg_header = client_socket.recv(HEADER)
                msg_length = int(msg_header.decode('utf-8').strip())
                msg = client_socket.recv(msg_length).decode('utf-8')

                self.history.update_chat_history(f' [color=20dd20] {user} [/color] > [color=a499ec] {msg} [/color]')

            except IOError as e:
                if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                    self.history.update_chat_history('[color=dd2020] Reading error: {} [/color]'.format(str(e)))
                break
        #self.reciver_for_sever.close()

    def send_to_server(self, message):
        Clock.schedule_once(self.focus_text_input, 0.1)
        #message = self.new_message.text
        message = f"{message}"
        message = message.encode('utf-8')
        message_header = f"{len(message):<{HEADER}}".encode('utf-8')
        client_socket.send(message_header + message)


class ChatPage_in_por(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 1
        self.rows = 2

        self.history = ScrolBar(height=Window.size[1] * 0.9, size_hint_y=None)
        self.add_widget(self.history)

        # We are going to use 1 column and 2 rows
        self.new_message = TextInput(width=Window.size[0] * 0.8, size_hint_x=None, multiline=False)
        self.send = Button(text="Send")
        self.send.bind(on_press=self.send_message)

        bottom_line = GridLayout(cols=2)
        bottom_line.add_widget(self.new_message)
        bottom_line.add_widget(self.send)
        self.add_widget(bottom_line)

        Window.bind(on_key_down=self.on_key_down)

        Window.bind(on_key_down1=self.mr_itolkRun)

        Clock.schedule_once(self.focus_text_input, 0.1)

        self.bind(size=self.adjust_fields)

        self.history.update_chat_history(
            f'> [color=a499ec] Adivinhe o numero que estou pensando'
            f' de 1 até 5 [/color]')

    def adjust_fields(self, *_):

        if Window.size[1] * 0.1 < 50:
            new_height = Window.size[1] - 50
        else:
            new_height = Window.size[1] * 0.9
        self.history.height = new_height

        if Window.size[0] * 0.2 < 160:
            new_width = Window.size[0] - 160
        else:
            new_width = Window.size[0] * 0.8
        self.new_message.width = new_width

        Clock.schedule_once(self.history.update_chat_history_layout, 0.01)

    def on_key_down(self, instance, keyboard, keycode, text, modifiers):
        if keycode == 40:
            self.send_message(None)

    def send_message(self, _):
        message = self.new_message.text
        # self.new_message.text = ''
        Clock.schedule_once(self.focus_text_input, 0.1)

        if message:
            Clock.schedule_once(self.focus_text_input, 0.1)
            self.history.update_chat_history(f'> [color=d2d020] {Chat_app.user_page.Name.text}[/color] [color=a499ec]'
                                             f' escoleu: [/color] {message}')
            self.mr_itolkRun()

        Clock.schedule_once(self.focus_text_input, 0.1)

    def focus_text_input(self, *_):
        self.new_message.focus = True

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

                self.history.update_chat_history(f'[color=dd2020]{info}[/color] > número incorreto'
                                                 f'[color=d2d020] {Chat_app.user_page.Name.text} [/color]'
                                                 f' voce digitou um alfabeto, o JOGO aceita apenas números\n')
                self.adjust_fields()
                self.history.update_chat_history(
                    f"> [color=a499ec] Adivinhe o numero que estou pensando de 1 até 5 [/color]\n")
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
                                    f'> [color=20dd20]  {name2}[/color] [color=a499ec] escoleu: [/color]'
                                    f' {num2str}\n')

                                self.history.update_chat_history(
                                    f"> [color=d2d020] {Chat_app.user_page.Name.text} [/color]"
                                    f" [color=a499ec] , você ganhou {y} ponto [/color]\n")

                                self.history.update_chat_history(
                                    f"> [color=d2d020] {Chat_app.user_page.Name.text} [/color]"
                                    f" [color=a499ec] seu pontos atual é: {str(u)} [/color]")
                                self.history.update_chat_history(
                                    f"> [color=20dd20] {name2} [/color] [color=a499ec] pontos atual é:"
                                    f" {str(itolk)} [/color]\n")

                                self.adjust_fields()
                                time.sleep(0.30)
                                self.history.update_chat_history(
                                    f"> [color=a499ec] Adivinhe o numero que estou pensando de 1 até 5 [/color]\n")
                                self.new_message.text = ''
                                Clock.schedule_once(self.focus_text_input, 0.1)
                                time.sleep(0.10)

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
                            f'> [color=20dd20] {name2}[/color] [color=a499ec] escoleu: [/color]'
                            f' {num2str}\n')

                        self.history.update_chat_history(f"> [color=d2d020] {Chat_app.user_page.Name.text} [/color]"
                                                         f" [color=a499ec] , você ganhou {y} ponto [/color]\n")

                        self.history.update_chat_history(f"> [color=d2d020] {Chat_app.user_page.Name.text} [/color]"
                                                         f" [color=a499ec] seu pontos atual é: {str(n)} [/color]")
                        self.history.update_chat_history(
                            f"> [color=20dd20] {name2} [/color] [color=a499ec] pontos atual é:"
                            f" {str(s)} [/color]\n")

                        self.adjust_fields()
                        time.sleep(0.30)
                        self.history.update_chat_history(
                            f"> [color=a499ec] Adivinhe o numero que estou pensando de 1 até 5 [/color]\n")
                        self.new_message.text = ''
                        Clock.schedule_once(self.focus_text_input, 0.1)
                        time.sleep(0.10)


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
                                    f'> [color=20dd20] {name2}[/color] [color=a499ec] escoleu: [/color]'
                                    f' {num2str}\n')

                                self.history.update_chat_history(
                                    f"> [color=20dd20] {name2} [/color] [color=a499ec] ganhou {y}"
                                    f" pontos [/color]\n")

                                self.history.update_chat_history(
                                    f"> [color=d2d020] {Chat_app.user_page.Name.text} [/color]"
                                    f" [color=a499ec] seu pontos atual é: {str(u)} [/color]")

                                self.history.update_chat_history(
                                    f"> [color=20dd20] {name2} [/color] [color=a499ec] pontos atual é:"
                                    f" {str(itolk)} [/color]\n")

                                self.adjust_fields()
                                time.sleep(0.30)
                                self.history.update_chat_history(
                                    f"> [color=a499ec] Adivinhe o numero que estou pensando de 1 até 5 [/color]\n")
                                self.new_message.text = ''
                                Clock.schedule_once(self.focus_text_input, 0.1)
                                time.sleep(0.10)

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
                            f'> [color=20dd20] {name2}[/color] [color=a499ec] escoleu: [/color]'
                            f' {num2str}\n')

                        self.history.update_chat_history(
                            f"> [color=20dd20] {name2} [/color] [color=a499ec] ganhou {y}"
                            f" pontos [/color]\n")

                        self.history.update_chat_history(f"> [color=d2d020] {Chat_app.user_page.Name.text} [/color]"
                                                         f" [color=a499ec] seu pontos atual é: {str(n)} [/color]")

                        self.history.update_chat_history(
                            f"> [color=20dd20] {name2} [/color] [color=a499ec] pontos atual é:"
                            f" {str(s)} [/color]\n")

                        self.adjust_fields()
                        time.sleep(0.30)
                        self.history.update_chat_history(
                            f"> [color=a499ec] Adivinhe o numero que estou pensando de 1 até 5 [/color]\n")
                        self.new_message.text = ''
                        Clock.schedule_once(self.focus_text_input, 0.1)
                        time.sleep(0.10)

                self.n = open("you.txt")
                n = self.n.readline()
                self.s = open('itolk.txt')
                s = self.s.readline()
                for self.n in n:
                    for self.s in s:
                        self.n = int(self.n)
                        self.s = int(self.s)
                        if self.n == 5:
                            n = str(self.n)
                            s = str(self.s)
                            self.history.update_chat_history(f"> [color=d2d020] {Chat_app.user_page.Name.text} [/color]"
                                                             f" [color=a499ec] seu ganhos é: {n} [/color]")
                            self.history.update_chat_history(f"> [color=20dd20] {name2} [/color] [color=a499ec] "
                                                             f"ganhos é: {s} [/color]\n")

                            self.history.update_chat_history(f"> [color=d2d020] {Chat_app.user_page.Name.text} [/color]"
                                                             f" [color=a499ec] você GANHOU!!! [/color]\n")
                            self.history.update_chat_history(f"> [color=20dd20] {name2} [/color]"
                                                             f" [color=a499ec] PERDEU!!! [/color]\n")

                            if os.path.exists('you.txt'):
                                os.remove('you.txt')
                                os.remove('itolk.txt')

                        if self.s == 5:
                            n = str(self.n)
                            s = str(self.s)
                            self.history.update_chat_history(f"> [color=20dd20] {name2} [/color] [color=a499ec] "
                                                             f" ganhos é: {s} [/color]")
                            self.history.update_chat_history(f"> [color=d2d020] {Chat_app.user_page.Name.text} [/color]"
                                                             f" [color=a499ec] seu ganhos é: {n} [/color]\n")

                            self.history.update_chat_history(f"> [color=20dd20] {name2} [/color]"
                                                             f" [color=a499ec] GANHOU!!! [/color]\n")

                            self.history.update_chat_history(f"> [color=d2d020] {Chat_app.user_page.Name.text} [/color]"
                                                             f" [color=a499ec] você PERDEU!!! [/color]\n")

                            if os.path.exists('you.txt'):
                                os.remove('you.txt')
                                os.remove('itolk.txt')
            else:
                self.history.update_chat_history(f'[color=dd2020]{info}[/color] > número incorreto\n')
                self.adjust_fields()
                time.sleep(0.30)
                self.history.update_chat_history(
                    f"> [color=a499ec] Adivinhe o numero que estou pensando de 1 até 5 [/color]\n")
                self.new_message.text = ''
                Clock.schedule_once(self.focus_text_input, 0.1)
                time.sleep(0.10)


class game_over_page(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 1
        self.rows = 2

        self.n = open("you.txt")
        n = self.n.readline()
        self.s = open('itolk.txt')
        s = self.s.readline()
        for self.n in n:
            for self.s in s:
                self.n = self.n
                self.s = self.s
                self.g_over = Label(height=Window.size[1]*0.9, size_hint_y=None, text=f"GAME OVER!!!..\n your secor is {n} \n mr_itolk secor is {s}")
                self.add_widget(self.g_over)

                self.exitbotton = Button(text='EXIT')
                self.exitbotton.bind(on_press=self.exit)
                self.replaybotton = Button(text='REPLAY')
                self.replaybotton.bind(on_press=self.replay)

                bottom_line = GridLayout(cols=2)
                bottom_line.add_widget(self.exitbotton)
                bottom_line.add_widget(self.replaybotton)
                self.add_widget(bottom_line)

    def exit(self, _):
        if os.path.exists('you.txt'):
            os.remove('you.txt')
            os.remove('itolk.txt')
        Clock.schedule_once(sys.exit(), 1)

    def replay(self, _):
        if os.path.exists('you.txt'):
            os.remove('you.txt')
            os.remove('itolk.txt')
        Chat_app.create_chat_page()
        Chat_app.screen_manager.current = "Chat"



class WlecomePage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.message = Label(halign="center", valign="middle", font_size=30)
        self.message.bind(width=self.update_text_width)
        self.add_widget(self.message)

    def update_info(self, message):
        self.message.text = message

    def update_text_width(self, *_):
        self.message.text_size = (self.message.width * 0.9, None)


class Mr_Itolk(App):
    def build(self):
        self.screen_manager = ScreenManager()

        self.user_page = UserPage()
        screen = Screen(name="user")
        screen.add_widget(self.user_page)
        self.screen_manager.add_widget(screen)

        self.wlecome_page = WlecomePage()
        screen = Screen(name="wlecome")
        screen.add_widget(self.wlecome_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager

    def create_chat_page(self):
        self.chat_page = ChatPage()
        screen = Screen(name='Chat')
        screen.add_widget(self.chat_page)
        self.screen_manager.add_widget(screen)

    def Game_Over(self):
        self.game_Over = game_over_page()
        screen = Screen(name='end_of_game')
        screen.add_widget(self.game_Over)
        self.screen_manager.add_widget(screen)


def show_error(message):
    Chat_app.wlecome_page.update_info(message)
    Chat_app.screen_manager.current = 'Info'
    Clock.schedule_once(sys.exit, 10)

HEADER = 10
#IP = '127.0.0.1'
#PORT = 1234
#ADRR = (IP, PORT)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#client_socket.connect(ADRR)

if __name__ == "__main__":
    Chat_app = Mr_Itolk()
    Chat_app.run()
