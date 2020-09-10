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
        # self.start.bind(on_press=self.start_button)
        # self.add_widget(Label())
        self.add_widget(self.start)

        self.lbl_active = Label(text="please choose your language")
        self.add_widget(self.lbl_active)

        self.por.bind(active=self.on_checkbox_Active2)
        self.eng.bind(active=self.on_checkbox_Active)



    def on_checkbox_Active(self, checkboxInstance, isActive):
        self.remove_widget(self.lbl_active)
        #noname = self.Name.text
        if isActive:

            # self.start = Button(text="Start")
            self.start.bind(on_press=self.start_button)
            # self.add_widget(Label())
            # self.add_widget(self.start)
            #self.eng = 1


           # print("Checkbox Checked")

        else:
            self.start.unbind(on_press=self.start_button)
            # self.lbl_active.text = "Checkbox is OFF"
            self.add_widget(self.lbl_active)

           # print("Checkbox unchecked")

    def on_checkbox_Active2(self, checkboxInstance, isActive):
        self.remove_widget(self.lbl_active)
        #noname = self.Name.text
        if isActive:

            # self.start = Button(text="Start")
            self.start.bind(on_press=self.start_button)
            # self.add_widget(Label())
            # self.add_widget(self.start)
            self.por = 1
            #print("Checkbox Checked")

        else:
            self.start.unbind(on_press=self.start_button)
            # self.lbl_active.text = "Checkbox is OFF"
            self.add_widget(self.lbl_active)

            #print("Checkbox unchecked")

    def start_button(self, instance):
        Name = self.Name.text

        if self.por == 1:
            self.por = "Portuguese"
            por = self.por
            info = f"Bem Vimdo {Name} \n Você escoleu {por}"
            Chat_app.wlecome_page.update_info(info)
            Chat_app.screen_manager.current = "wlecome"

        else:
            self.eng = "English"
            eng = self.eng
            info = f"Welcome {Name} \n You choose {eng}"
            Chat_app.wlecome_page.update_info(info)
            Chat_app.screen_manager.current = "wlecome"

        Clock.schedule_once(self.connect, 1)

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

        self.layout.height = self.chat_history.texture_size[1] + 20
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

        Clock.schedule_once(self.focus_text_input, 1)

        self.bind(size=self.adjust_fields)

        if Chat_app.user_page.eng:
            self.history.update_chat_history(
                f"[color=20dd20]{name2}[/color] > Guess the number I'm thinking of from 1 to 5")

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
        #self.new_message.text = ''

        if message:
            self.history.update_chat_history(f'[color=d2d020]{Chat_app.user_page.Name.text}[/color] > {message}')
            self.mr_itolkRun()
        Clock.schedule_once(self.focus_text_input, 0.1)


    def focus_text_input(self, *_):
        self.new_message.focus = True

   # def on_key_down1(self, instance, keyboard, keycode, text, modifiers):
        #if keycode == 40:
            #self.mr_itolkRun()

    def mr_itolkRun(self):
        # info = "hey am here!!!...."

        # self.display.update_chat(info)
        # self.display.update_chat(lista)

        while self.new_message.text:
            self.n2 = random.choice(lista)
            info = 'Info'
            try:
                self.n = int(self.new_message.text)
            except:

                self.history.update_chat_history(f'[color=dd2020]{info}[/color] > Input incorrect'
                                                 f' {Chat_app.user_page.Name.text} entered alphabet but the GAME only '
                                                 f'support numbers')
                self.history.update_chat_history(
                    f"[color=20dd20]{name2}[/color] > Guess the number I'm thinking of from 1 to 5")
                self.new_message.text = ''
                Clock.schedule_once(self.focus_text_input, 0.1)
                time.sleep(0.10)
                break

            if self.n in lista:

                if self.n == self.n2:
                    go = str(self.n2)
                    na = self.new_message.text
                    self.history.update_chat_history(f'[color=20dd20]{name2}[/color] > it is in........ computer chose: '
                                                     f'{go}  you chose: {na}')
                    time.sleep(0.30)
                    self.history.update_chat_history(
                        f"[color=20dd20]{name2}[/color] > Guess the number I'm thinking of from 1 to 5")
                    self.new_message.text = ''
                    Clock.schedule_once(self.focus_text_input, 0.1)
                    time.sleep(0.10)
                    break

                else:
                    go = str(self.n2)
                    na = self.new_message.text
                    self.history.update_chat_history(f'[color=20dd20]{name2}[/color] > is not in......computer chose: '
                                                     f'{go}  you chose: {na}')
                    time.sleep(0.30)
                    self.history.update_chat_history(
                        f"[color=20dd20]{name2}[/color] > Guess the number I'm thinking of from 1 to 5")
                    self.new_message.text = ''
                    Clock.schedule_once(self.focus_text_input, 0.1)
                    time.sleep(0.10)
                    break
            else:
                self.history.update_chat_history(f'[color=dd2020]{info}[/color] > The number you'
                                                 f' entry is incorrect')
                time.sleep(0.30)
                self.history.update_chat_history(
                    f"[color=20dd20]{name2}[/color] > Guess the number I'm thinking of from 1 to 5")
                self.new_message.text = ''
                Clock.schedule_once(self.focus_text_input, 0.1)
                time.sleep(0.10)
                break

        #message = f'Hello >>>>{name}'
        # Update chat history with username and message, green color for username
        #self.history.update_chat_history(f'[color=20dd20]{Chat_app.user_page.gama}[/color] > {message}')


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


def show_error(message):
    info = f"You did not enter your Name..."
    Chat_app.wlecome_page.update_info(info)
    Chat_app.screen_manager.current = 'wlecome'
    Clock.schedule_once(sys.exit, 0.2)


if __name__ == "__main__":
    Chat_app = Mr_Itolk()
    Chat_app.run()
