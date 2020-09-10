import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.codeinput import CodeInput
from  kivy.clock import Clock
import random

kivy.require("1.11.1")

lista = (1, 2, 3, 4, 5)

name = "mr_itolk"

class my_sclow(ScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.layout = GridLayout(cols=1, size_hint_y=None)
        self.add_widget(self.layout)

        self.chat = Label(size_hint_y=None, markup=True)
        self.scrobar = Label()

        self.layout.add_widget(self.chat)
        self.layout.add_widget(self.scrobar)

    def update_chat(self, message, *_):
        self.chat.text += "\n" + message

        self.layout.height = self.chat.texture_size[1] + 15
        self.chat.height = self.chat.texture_size[1]
        self.chat.text_size = self.chat.width * 0.98, None
        self.scroll_to(self.scrobar)


class myPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 1
        self.rows = 3

        self.mini = Label(text="pls what is you lucky number for 1 up to 5", height=Window.size[0] * 0.1, size_hint_y=None)

        self.top_up = GridLayout(cols=1)
        self.top_up.add_widget(self.mini)
        self.add_widget(self.top_up)


        self.display = my_sclow(height=Window.size[1] * 0.8, size_hint_y=None)

        self.add_widget(self.display)

        # self.one(Label(text=" Hello is me!!..."))
        # self.add_widget(Label(text="Hello is me!!!!..."))
        self.new_input = TextInput(width=Window.size[0] * 0.8, size_hint_x=None, multiline=False)
        self.one = Button(text="OK")
        self.one.bind(on_press=self.button)

        last_line = GridLayout(cols=2)
        last_line.add_widget(self.new_input)
        last_line.add_widget(self.one)
        self.add_widget(last_line)

        self.bind(size=self.adjust_fields)

        Window.bind(on_key_dwon=self.on_key_down)

        Clock.schedule_once(self.focus_text_input, 0.1)

    def on_key_down(self, instance, keyboard, keycode, text, modifiers):
        if keycode == 40:
            self.button(None)

    def mr_italk(self):
        #info = "hey am here!!!...."

        #self.display.update_chat(info)
        #self.display.update_chat(lista)

        while self.new_input.text:
            self.n2 = random.choice(lista)
            self.n = int(self.new_input.text)
            if self.n == self.n2:
                go = str(self.n2)
                na = self.new_input.text
                self.display.update_chat(f"it is in........ computer: {go}  you: {na}")
                self.new_input.text = ''
                Clock.schedule_once(self.focus_text_input, 0.1)
                break
            else:
                go = str(self.n2)
                na = self.new_input.text
                self.display.update_chat(f"it is not in......computer: {go}  you: {na}")
                self.new_input.text = ''
                Clock.schedule_once(self.focus_text_input, 0.1)
                break

    def button(self, _):
        message = self.new_input.text
        self.remove_widget(self.top_up)
        Clock.schedule_once(self.focus_text_input, 0.1)
                #message.bind(active=self.mr_italk)

        if message:
            self.display.update_chat(f'{name} > {message}')
            n = self.new_input.text
            Clock.schedule_once(self.focus_text_input, 0.1)
            return self.mr_italk()

        Clock.schedule_once(self.focus_text_input, 0.1)

    def focus_text_input(self, *_):
        self.new_input.focus = True



        # self.add_widget(self.one)
    def adjust_fields(self, *_):

        if Window.size[1] * 0.1 < 50:
            new_height = Window.size[1] - 50
        else:
            new_height = Window.size[1] * 0.9
        self.display.height = new_height

        if Window.size[0] * 0.2 < 160:
            new_width = Window.size[0] - 160
        else:
            new_width = Window.size[0] * 0.8
        self.new_input.width = new_width

class pkApp(App):
    def build(self):
        return myPage()


if __name__ == "__main__":
    RunApp = pkApp()
    RunApp.run()
