from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
from kivy.utils import get_color_from_hex

def darken (intuple ,rate):
    dark = tuple(c * rate for c in intuple[:3]) + (intuple[3],)
    return dark

class topRect(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            bcolor = (0, 1, 0, 1)
            self.color = Color(*darken(bcolor, 0.7))
            self.rect = Rectangle(size=(450, 90), pos=(0, 810))


class AthkarApp(App):
    def build(self):
        window = Window
        window.size = (450, 900)
        color = (0, 1, 1, 1)
        window.clearcolor = darken(color, 0.3)
        flayout = FloatLayout()
        topRectVar = topRect()
        titleAthkar = Label(text="Athkar", pos=(0, 600))
        flayout.add_widget(topRectVar)
        flayout.add_widget(titleAthkar)
        return flayout

if __name__ == "__main__":
    AthkarApp().run()