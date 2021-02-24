'''
This file controls the graphical user interface
'''


from importlib import util
spam_loader = util.find_spec('kivy')
if spam_loader is None:
    print('You need kivy installed to run this program')
    exit(1)


import json
import os
from asyncio import sleep
from functools import partial

from kivy import Config
from kivy.config import Config

import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from api import wrapper, config
import api

Config.set('graphics', 'resizable', 0)

from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView

from api import wrapper

gestures = {}

on_off = 'OFF'

url = 'http://192.168.137.249:1880/fail'


def load_gestures():
    global gestures
    try:
        with open('gestures.json') as f:
            filesize = os.path.getsize("gestures.json")
            if filesize == 0:
                print("File empty")
                return
            gestures = json.loads(f.read())
    except IOError:
        print("File not existing")


class RoboCopForm(BoxLayout):

    def url_manager(self):
        # '''A function that controls Fans'''
        # if self.ids.on_off_btn.text == 'OFF':
        #     self.ids.on_off_btn.text = 'ON'
        #     on_off = 'ON'
        #     # call function
        # elif self.ids.on_off_btn.text == 'ON':
        #     self.ids.on_off_btn.text = 'OFF'
        #     on_off = 'OFF'
        #     # call function
        # print(on_off)
        # # call_function
        print('manage me??')
        config.main()



    def add_new_gesture_callback(self):
        '''Only new gesture with no empty name will be saved,
        the gesture is the current position of the fingers in the ui'''
        if self.ids.new_gesture_txt.text == "":
            return
        global gestures
        gestures[self.ids.new_gesture_txt.text] = (
            self.ids.f1.value,
            self.ids.f2.value,
            self.ids.f3.value,
            self.ids.f4.value,
            self.ids.f5.value
        )
        print(gestures)
        with open("gestures.json", "w+") as write_file:
            json.dump(gestures, write_file, ensure_ascii=True, indent=4)
        self.refresh_gestures()

    def whole_hand_callback(self, touch):
        '''This callback is associated to
        the slider controlling the whole hand'''
        if self.ids.whole_hand.collide_point(*touch.pos):
            self.ids.f1.value = self.ids.whole_hand.value
            self.ids.f2.value = self.ids.whole_hand.value
            self.ids.f3.value = self.ids.whole_hand.value
            self.ids.f4.value = self.ids.whole_hand.value
            self.ids.f5.value = self.ids.whole_hand.value
            self.send_signal()

    def single_finger_callback(self, touch):
        '''This callback is associated to the movement
        of any of the five fingers'''
        if (self.ids.f1.collide_point(*touch.pos) or
                self.ids.f2.collide_point(*touch.pos) or
                self.ids.f3.collide_point(*touch.pos) or
                self.ids.f4.collide_point(*touch.pos) or
                self.ids.f5.collide_point(*touch.pos)):
            self.send_signal()

    def send_signal(self):
        '''This callback is called whenever
        the user moves one of the singular fingers
        or the slider controlling the whole hand'''

        # Make sure to uncomment the call to move_hand
        # or the signals will not be sent to the real hand,
        # they are commented so the gui will work while
        # you are still not connected properly, otherwise the app
        # would crash instantly
        fingers = {
            'f1': int(self.ids.f1.value),
            'f2': int(self.ids.f2.value),
            'f3': int(self.ids.f3.value),
            'f4': int(self.ids.f4.value),
            'f5': int(self.ids.f5.value)}
        print(json.dumps(fingers))

        wrapper.move_hand(int(self.ids.f1.value),
                          int(self.ids.f2.value),
                          int(self.ids.f3.value),
                          int(self.ids.f4.value),
                          int(self.ids.f5.value))


    def send_gesture(self, key):
        '''This callback is called when the user
        presses one of the saved gestures'''

        # Make sure to uncomment the call to move_hand
        # or the signals will not be sent to the real hand,
        # they are commented so the gui will work while
        # you are still not connected properly, otherwise the app
        # would crash instantly
        global gestures
        fingers = {
            'f1': int(gestures[key][0]),
            'f2': int(gestures[key][1]),
            'f3': int(gestures[key][2]),
            'f4': int(gestures[key][3]),
            'f5': int(gestures[key][4]),
        }
        print(json.dumps(fingers))

        wrapper.move_hand(int(gestures[key][0]),
                              int(gestures[key][1]),
                              int(gestures[key][2]),
                              int(gestures[key][3]),
                              int(gestures[key][4]))

    def refresh_gestures(self):
        '''This function is called whenever the user
        adds new gestures to update the list of buttons'''
        self.ids.gst_box.clear_widgets()
        global gestures
        load_gestures()
        layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        # Make sure the height is such that there is something to scroll.
        layout.bind(minimum_height=layout.setter('height'))
        i = 0
        for g in gestures:
            btn = Button(text=str(g), size_hint_y=None, height=40)
            btn.on_press = partial(self.send_gesture, btn.text)
            layout.add_widget(btn, index=i)
            i += 1
        scroll_root = ScrollView(size_hint=(None, None), size=(self.ids.gst_box.width, self.ids.gst_box.height))
        scroll_root.add_widget(layout)
        self.ids.gst_box.add_widget(scroll_root)


class LayoutApp(App):
    def on_start(self, **kwargs):
        def callback(a):
            self.root.refresh_gestures()

        # callback(str(5))
        Clock.schedule_once(partial(callback), 8)


if __name__ == '__main__':
    load_gestures()
    if api.first_time():
        config.main()
    Config.set('graphics', 'resizable', False)
    app = LayoutApp().run()
