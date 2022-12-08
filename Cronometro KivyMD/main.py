# Youtube: Magno Efren

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from kivy.clock import Clock
from kivymd.uix.pickers import MDColorPicker
from typing import Union

from kivy.core.window import Window
Window.size = (350, 580)

class Ui(ScreenManager):
	pass

class MainApp(MDApp):
    style = True
    state = False
    seconds = 0

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"
        Builder.load_file('style.kv')
        Clock.schedule_interval(self.update, 0)
        return Ui()

    def update(self, event):
        if self.state:
            self.seconds +=event
            minutes, seconds = divmod(self.seconds, 60)
            part_seconds = int(seconds*100%100)
            seconds = int(seconds)
            minutes = int(minutes)

            if len(str(part_seconds)) ==1:
                part_seconds = '0' + str(part_seconds)
            if len(str(seconds)) ==1:
                seconds = '0' +str(seconds)
            if len(str(minutes))==1:
                minutes = '0' +str(minutes)

            self.root.ids.numero.text = '{}:{}'.format(minutes, seconds)
            self.root.ids.ms_numero.text = '.{}'.format(part_seconds)

    def button_state(self,event):
        if  self.state:
            self.state = False
            self.root.ids.control.icon = 'play-circle-outline' #stop-circle-outline
        elif not self.state:
            self.state = True
            self.root.ids.control.icon = 'pause-circle-outline' #

    def button_reset(self, event):
        self.seconds = 0
        self.state = False
        self.root.ids.numero.text = '00:00'
        self.root.ids.ms_numero.text = '.00'

    def open_color_picker(self):
        color_picker = MDColorPicker(size_hint=(0.5, 0.8))
        color_picker.open()
        color_picker.bind(on_release=self.get_selected_color,)

    def update_color(self, color):
        self.root.ids.numero.color = color
        self.root.ids.ms_numero.color = color
        self.root.ids.control.md_bg_color = color
        self.root.ids.estado.md_bg_color = color
        self.root.ids.reset.md_bg_color = color

    def get_selected_color(self,
        instance_color_picker: MDColorPicker,
        type_color: str,
        selected_color: Union[list, str],):
        self.update_color(selected_color[:-1] + [1])


if __name__=="__main__":
	MainApp().run()
