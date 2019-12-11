#python3
#main.py

import kivy, openpyxl, os

kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.properties import NumericProperty, ObjectProperty, StringProperty
from kivy.factory import Factory
from kivy.uix.popup import Popup


# Widget for the window itself
class CylinderTask(GridLayout):

    # Setup property variables for right, left, both
    right = NumericProperty(0)
    left = NumericProperty(0)
    both = NumericProperty(0)
    animal = StringProperty('')
    trial = StringProperty('')
    trialCode = StringProperty('')

    def process(self):
        self.animal = self.ids['animalBox'].text
        self.trial = self.ids['trialBox'].text
        self.trialCode = '%s%s' % (self.animal, self.trial)
        

    def completeTrial(self):
        results = (self.right, self.left, self.both)
        print('Trial Complete')
        print(results)
        print(self.trialCode)
        fName = '%s.xlsx' % self.trialCode

        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = self.trialCode
        ws['a1']= 'Right:'
        ws['b1']= self.right
        ws['a2']= 'Left:'
        ws['b2']= self.left
        ws['a3']= 'Both:'
        ws['b3']= self.both

        wb.save(filename = 'results/%s' % fName)
        wb.close()
        
        
        

    def __init__(self, **kwargs):
        super(CylinderTask, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(
            self._keyboard_closed, self, 'text')
        if self._keyboard.widget:
            # If it exists, this widget is a VKeyboard object which you can use
            # to change the keyboard layout.
            pass
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self):
        pass

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):

        key = keycode[1]

        if key == 'left':
            self.left += 1

        if key == 'right':
            self.right += 1

        if key == 'up':
            self.both += 1

        if key == 'down':
            self.left, self.right, self.both = 0, 0, 0

        if key == 'enter':
            self.completeTrial()

class CylinderTaskApp(App):

    def build(self):
        task = CylinderTask()
        return task

if __name__=='__main__':
    CylinderTaskApp().run()
