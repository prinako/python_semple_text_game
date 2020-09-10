import kivy
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout
from kivy.app import App

kivy.require("1.11.1")

# ...
class jk(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2

        self.my = CheckBox()
        self.add_widget(self.my)

    def on_checkbox_active(checkbox, value):
        if value:
            print('The checkbox', checkbox, 'is active')
        else:
            print('The checkbox', checkbox, 'is inactive')

    checkbox = CheckBox()
    checkbox.bind(active=on_checkbox_active)


class myapp(App):
    def build(self):
        return jk


if __name__ == "__main__":
    myapp().run()
