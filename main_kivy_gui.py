import kivy
from kivy.uix.boxlayout import BoxLayout
from re import MULTILINE
kivy.require('1.0.6') # replace with your current kivy version !
from kivy.event import EventDispatcher
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.input.motionevent import MotionEvent
from kivy.uix.button import  Button
from kivy.graphics import (Color, Rectangle)


class HomeScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        self.cols = 4


        
        self.padding = 50
        #self.add_widget(Label(text='User Name'))
        #self.username = TextInput(multiline=False)
        #self.add_widget(self.username)
        #self.add_widget(Label(text='password'))
        #self.password = TextInput(password=True, multiline=False)To
        #self.add_widget(self.password)
        conjugate= Button(name="conjugate",text="CONJUGATE")
        conjugate.size_hint=(.2,.2)
        conjugate.halign= 'center'
        conjugate.valign='middle'
        self.add_widget(conjugate)
        self.add_widget(TextInput(multiline = False))
        conjugate.padding = (90,90)
 



class MyEventDispatcher(EventDispatcher):
        def __init__(self, **kwargs):
            self.register_event_type('on_test')
            super(MyEventDispatcher, self).__init__(**kwargs)
        def do_something(self, value):
            # when do_something is called, the 'on_test' event will be
            # dispatched with the value
            self.dispatch('on_test', value)
        def on_test(self, *args):
            print "I am dispatched", args





class ArabicConjugator(App):

    def build(self):
        return HomeScreen()


if __name__ == '__main__':
    ArabicConjugator().run()
