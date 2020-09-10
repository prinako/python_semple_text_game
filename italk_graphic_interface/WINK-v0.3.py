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
import sys
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
import random
import time
import os

kivy.require('1.11.1')

lista = (1, 2, 3, 4, 5)

name2 = "Mr_itolk"


class UserPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        self.row_force_default = True
        self.row_default_height = 40

        self.add_widget(Label())
        self.add_widget(Label())

        self.add_widget(Label(text="Name:"))
        self.Name = TextInput(multiline=False)
        self.add_widget(self.Name)
        Clock.schedule_once(self.focus_text_input)

        self.gama = f'Mr_italk'

        self.eng = CheckBox(group="check")
        self.add_widget(Label(text="Chose Your Language"))
        self.add_widget(Label())
        self.add_widget(Label(text="English"))
        self.add_widget(self.eng)

        self.por = CheckBox(group="check")
        self.add_widget(Label(text="Portuguese"))
        self.add_widget(self.por)

        self.start = Button(text="Start")
        self.add_widget(self.start)

        self.lbl_active = Label(text="please choose your language")
        self.add_widget(self.lbl_active)

        self.por.bind(active=self.on_checkbox_Active2)
        self.eng.bind(active=self.on_checkbox_Active)

        Window.bind(on_key_dwon=self.on_key_down)

        if os.path.exists('you.txt'):
            os.remove('you.txt')
            os.remove('itolk.txt')

    def on_key_down(self, instance, keyboard, keycode, text, modifiers):
        if keycode == 40:
            self.start_button(None)

    def focus_text_input(self, *_):
        self.Name.focus = True

    def on_checkbox_Active(self, checkboxInstance, isActive):
        self.remove_widget(self.lbl_active)

        if isActive:

            self.start.bind(on_press=self.start_button)

        else:
            self.start.unbind(on_press=self.start_button)
            self.add_widget(self.lbl_active)

    def on_checkbox_Active2(self, checkboxInstance, isActive):
        self.remove_widget(self.lbl_active)

        if isActive:

            self.start.bind(on_press=self.start_button)
            self.por = 1


        else:
            self.start.unbind(on_press=self.start_button)
            self.add_widget(self.lbl_active)

    def start_button(self, instance):
        Name = self.Name.text

        if self.por == 1:
            self.por = "Portuguese"
            por = self.por
            info = f"Bem Vimdo {Name} \n Você escoleu {por}"
            Chat_app.wlecome_page.update_info(info)
            Chat_app.screen_manager.current = "wlecome"

            Clock.schedule_once(self.connect1, 1)

        else:
            self.eng = "English"
            eng = self.eng
            info = f"Welcome {Name} \n You choose {eng}"
            Chat_app.wlecome_page.update_info(info)
            Chat_app.screen_manager.current = "wlecome"

            Clock.schedule_once(self.connect, 1)

    def connect1(self, _):
        username = self.Name.text

        if username == '':
            return show_error

        Chat_app.create_chat_page_in_por()
        Chat_app.screen_manager.current = "Chat_in_por"

    def connect(self, _):
        username = self.Name.text

        if username == '':
            return show_error

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

        if Chat_app.user_page.eng:
            self.history.update_chat_history(
                f"> [color=a499ec] Guess the number I'm thinking of from 1 to 5 [/color]\n")

        else:
            self.history.update_chat_history(
                f'[color=20dd20]{name2}[/color] > Adivinhe o numero que estou pensando de 1 até 5')

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
        Clock.schedule_once(self.focus_text_input, 0.1)

        if message:
            Clock.schedule_once(self.focus_text_input, 0.1)
            self.history.update_chat_history(f'[color=d2d020]{Chat_app.user_page.Name.text}[/color] > [color=a499ec]'
                                             f' chose: [/color] {message}')
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
                self.history.update_chat_history(f'[color=dd2020]{info}[/color] > Input incorrect'
                                                 f'[color=d2d020] {Chat_app.user_page.Name.text} [/color]'
                                                 f' entered alphabet but the GAME only support numbers\n')
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
                                    f'[color=20dd20]{name2}[/color] > [color=a499ec] chose: [/color]'
                                    f' {num2str}')

                                self.history.update_chat_history(
                                    f"> [color=d2d020] {Chat_app.user_page.Name.text} [/color]"
                                    f" [color=a499ec] You've won {y} point [/color]\n")

                                self.history.update_chat_history(
                                    f"> [color=d2d020] {Chat_app.user_page.Name.text} [/color]"
                                    f" [color=a499ec] your score is: {str(u)} [/color]\n")
                                self.history.update_chat_history(
                                    f"> [color=d2d020] {name2} [/color] [color=a499ec] your score is:"
                                    f" {str(itolk)} [/color]\n")

                                self.adjust_fields()
                                time.sleep(0.30)
                                self.history.update_chat_history(
                                    f"> [color=a499ec] Guess the number I'm thinking of from 1 to 5 [/color]\n")
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
                            f'[color=20dd20]{name2}[/color] > [color=a499ec] chose: [/color]'
                            f' {num2str}')

                        self.history.update_chat_history(f"> [color=d2d020] {Chat_app.user_page.Name.text} [/color]"
                                                         f" [color=a499ec] You've won {y} point [/color]\n")

                        self.history.update_chat_history(f"> [color=d2d020] {Chat_app.user_page.Name.text} [/color]"
                                                         f" [color=a499ec] your score is: {str(n)} [/color]\n")
                        self.history.update_chat_history(
                            f"> [color=d2d020] {name2} [/color] [color=a499ec] your score is:"
                            f" {str(s)} [/color]\n")

                        self.adjust_fields()
                        time.sleep(0.30)
                        self.history.update_chat_history(
                            f"> [color=a499ec] Guess the number I'm thinking of from 1 to 5 [/color]\n")
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
                                    f'[color=20dd20]{name2}[/color] > [color=a499ec] chose: [/color]'
                                    f' {num2str}')

                                self.history.update_chat_history(
                                    f"> [color=20dd20] {name2} [/color] [color=a499ec] You've won {y}"
                                    f" point [/color]\n")

                                self.history.update_chat_history(
                                    f"> [color=d2d020] {Chat_app.user_page.Name.text} [/color]"
                                    f" [color=a499ec] your score is: {str(u)} [/color]\n")

                                self.history.update_chat_history(
                                    f"> [color=d2d020] {name2} [/color] [color=a499ec] your score is:"
                                    f" {str(itolk)} [/color]\n")

                                self.adjust_fields()
                                time.sleep(0.30)
                                self.history.update_chat_history(
                                    f"> [color=a499ec] Guess the number I'm thinking of from 1 to 5 [/color]\n")
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
                            f'[color=20dd20]{name2}[/color] > [color=a499ec] chose: [/color]'
                            f' {num2str}')

                        self.history.update_chat_history(
                            f"> [color=20dd20] {name2} [/color] [color=a499ec] You've won {y}"
                            f" point [/color]\n")

                        self.history.update_chat_history(f"> [color=d2d020] {Chat_app.user_page.Name.text} [/color]"
                                                         f" [color=a499ec] your score is: {str(n)} [/color]\n")

                        self.history.update_chat_history(
                            f"> [color=d2d020] {name2} [/color] [color=a499ec] your score is:"
                            f" {str(s)} [/color]\n")

                        self.adjust_fields()
                        time.sleep(0.30)
                        self.history.update_chat_history(
                            f"> [color=a499ec] Guess the number I'm thinking of from 1 to 5 [/color]\n")
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

                            Chat_app.Game_Ovoer()
                            Chat_app.screen_manager.current = "end_of_game"

                            self.history.update_chat_history(f"> [color=d2d020] {Chat_app.user_page.Name.text} [/color]"
                                                             f" [color=a499ec] your score is: {n} [/color]\n")
                            self.history.update_chat_history(f"> [color=20dd20] {name2} [/color] [color=a499ec] your "
                                                             f"score is: {s} [/color]\n")

                            self.history.update_chat_history(f"> [color=d2d020] {Chat_app.user_page.Name.text} [/color]"
                                                             f" [color=a499ec] you win!! [/color]\n")
                            self.history.update_chat_history(f"> [color=d2d020] {name2} [/color]"
                                                             f" [color=a499ec] you lose!! [/color]\n")

                            if os.path.exists('you.txt'):
                                os.remove('you.txt')
                                os.remove('itolk.txt')

                        if self.s == 5:
                            Chat_app.Game_Ovoer()
                            Chat_app.screen_manager.current = "end_of_game"

                            n = str(self.n)
                            s = str(self.s)
                            self.history.update_chat_history(f"> [color=20dd20] {name2} [/color] [color=a499ec] your "
                                                             f"score is: {s} [/color]\n")
                            self.history.update_chat_history(f"> [color=d2d020] {Chat_app.user_page.Name.text} [/color]"
                                                             f" [color=a499ec] your score is: {n} [/color]\n")

                            self.history.update_chat_history(f"> [color=d2d020] {name2} [/color]"
                                                             f" [color=a499ec] you win!! [/color]\n")

                            self.history.update_chat_history(f"> [color=d2d020] {Chat_app.user_page.Name.text} [/color]"
                                                             f" [color=a499ec] you lose!! [/color]\n")

                            if os.path.exists('you.txt'):
                                os.remove('you.txt')
                                os.remove('itolk.txt')

            else:
                self.history.update_chat_history(f'[color=dd2020]{info}[/color] > The number you'
                                                 f' entry is incorrect\n')
                self.adjust_fields()
                time.sleep(0.30)
                self.history.update_chat_history(
                    f"> [color=a499ec] Guess the number I'm thinking of from 1 to 5 [/color]\n")
                self.new_message.text = ''
                Clock.schedule_once(self.focus_text_input, 0.1)
                time.sleep(0.10)


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
            self.history.update_chat_history(f'[color=d2d020]{Chat_app.user_page.Name.text}[/color] > [color=a499ec]'
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
                                                 f' digitou alfabeto, o Jogo aceita apenas números\n')
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
                                    f'[color=20dd20]{name2}[/color] > [color=a499ec] escoleu: [/color]'
                                    f' {num2str}')

                                self.history.update_chat_history(
                                    f"> [color=d2d020] {Chat_app.user_page.Name.text} [/color]"
                                    f" [color=a499ec] , você ganhou {y} ponto [/color]\n")

                                self.history.update_chat_history(
                                    f"> [color=d2d020] {Chat_app.user_page.Name.text} [/color]"
                                    f" [color=a499ec] seu pontos atual é: {str(u)} [/color]\n")
                                self.history.update_chat_history(
                                    f"> [color=d2d020] {name2} [/color] [color=a499ec] seu pontos atual é:"
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
                            f'[color=20dd20]{name2}[/color] > [color=a499ec] escoleu: [/color]'
                            f' {num2str}')

                        self.history.update_chat_history(f"> [color=d2d020] {Chat_app.user_page.Name.text} [/color]"
                                                         f" [color=a499ec] , você ganhou {y} ponto [/color]\n")

                        self.history.update_chat_history(f"> [color=d2d020] {Chat_app.user_page.Name.text} [/color]"
                                                         f" [color=a499ec] seu pontos atual é: {str(n)} [/color]\n")
                        self.history.update_chat_history(
                            f"> [color=d2d020] {name2} [/color] [color=a499ec] yseu pontos atual é:"
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
                                    f'[color=20dd20]{name2}[/color] > [color=a499ec] escoleu: [/color]'
                                    f' {num2str}')

                                self.history.update_chat_history(
                                    f"> [color=20dd20] {name2} [/color] [color=a499ec] , você ganhou {y}"
                                    f" ponts [/color]\n")

                                self.history.update_chat_history(
                                    f"> [color=d2d020] {Chat_app.user_page.Name.text} [/color]"
                                    f" [color=a499ec] seu pontos atual é: {str(u)} [/color]\n")

                                self.history.update_chat_history(
                                    f"> [color=d2d020] {name2} [/color] [color=a499ec] seu pontos atual é:"
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
                            f'[color=20dd20]{name2}[/color] > [color=a499ec] escoleu: [/color]'
                            f' {num2str}')

                        self.history.update_chat_history(
                            f"> [color=20dd20] {name2} [/color] [color=a499ec] , você ganhou {y}"
                            f" ponto [/color]\n")

                        self.history.update_chat_history(f"> [color=d2d020] {Chat_app.user_page.Name.text} [/color]"
                                                         f" [color=a499ec] seu pontos atual é: {str(n)} [/color]\n")

                        self.history.update_chat_history(
                            f"> [color=d2d020] {name2} [/color] [color=a499ec] seu pontos atual é:"
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
                                                             f" [color=a499ec] seus ganhos é: {n} [/color]\n")
                            self.history.update_chat_history(f"> [color=20dd20] {name2} [/color] [color=a499ec] seus "
                                                             f"ganhos é: {s} [/color]\n")

                            self.history.update_chat_history(f"> [color=d2d020] {Chat_app.user_page.Name.text} [/color]"
                                                             f" [color=a499ec] você é o ganhador!!! [/color]\n")
                            self.history.update_chat_history(f"> [color=d2d020] {name2} [/color]"
                                                             f" [color=a499ec] você perdeu!!! [/color]\n")

                            if os.path.exists('you.txt'):
                                os.remove('you.txt')
                                os.remove('itolk.txt')

                        if self.s == 5:
                            n = str(self.n)
                            s = str(self.s)
                            self.history.update_chat_history(f"> [color=20dd20] {name2} [/color] [color=a499ec] seus"
                                                             f" ganhos é: {s} [/color]\n")
                            self.history.update_chat_history(f"> [color=d2d020] {Chat_app.user_page.Name.text} [/color]"
                                                             f" [color=a499ec] seus ganhos é: {n} [/color]\n")

                            self.history.update_chat_history(f"> [color=d2d020] {name2} [/color]"
                                                             f" [color=a499ec] você é o ganhador!!! [/color]\n")

                            self.history.update_chat_history(f"> [color=d2d020] {Chat_app.user_page.Name.text} [/color]"
                                                             f" [color=a499ec] você perdeu!!! [/color]\n")

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

    def create_chat_page_in_por(self):
        self.chat_page_in_por = ChatPage_in_por()
        screen = Screen(name='Chat_in_por')
        screen.add_widget(self.chat_page_in_por)
        self.screen_manager.add_widget(screen)

    def Game_Ovoer(self):
        self.game_Over = game_over_page()
        screen = Screen(name='end_of_game')
        screen.add_widget(self.game_Over)
        self.screen_manager.add_widget(screen)


def show_error(message):
    info = f"You did not enter your Name..."
    Chat_app.wlecome_page.update_info(info)
    Chat_app.screen_manager.current = 'wlecome'
    Clock.schedule_once(sys.exit, 0.2)


if __name__ == "__main__":
    Chat_app = Mr_Itolk()
    Chat_app.run()
