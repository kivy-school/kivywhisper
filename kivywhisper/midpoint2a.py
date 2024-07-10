from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
import psutil
kv_string = '''
<CustomBoxLayout@BoxLayout>:
    orientation: 'vertical'
    BoxLayout: 
        orientation: 'horizontal'
        size_hint: (1,0.2)
        Button:
            text: "hw!"
        Button:
            text: "hw2!"
        Button:
            text: "hw3!"
    Button: 
        id: drivechooserID
        text: "set drive"
        on_release: root.make_dropdown() 
    FileChooser:
        id: fc
        FileChooserIconLayout

CustomBoxLayout:
'''

class CustomBoxLayout(BoxLayout):
    def make_dropdown(self, *args):
        # import pdb
        # pdb.set_trace()
        drive_dropdown = DropDown()
        #list comprehension to make button per drive:
        #syntax: [x for x in list]
        [drive_dropdown.add_widget(Button(text=var.device, size_hint_y=None, height=44)) for var in psutil.disk_partitions()]
        # drive_dropdown.add_widget(Button(text='???', size_hint_y=None, height=44))
        drive_dropdown.open(App.get_running_app().root.ids['drivechooserID'])
        # drive_dropdown.open()

class whApp(App):
    def build(self):
        return Builder.load_string(kv_string)

if __name__ == '__main__':
    #this is to make the Kivy window always on top
    from kivy.core.window import Window
    Window.always_on_top = True
    whApp().run()
