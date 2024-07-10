from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

kv_string = '''
BoxLayout:
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
        text: "hw4!"
'''
class whApp(App):
    def build(self):
        return Builder.load_string(kv_string)

if __name__ == '__main__':
    #this is to make the Kivy window always on top
    from kivy.core.window import Window
    Window.always_on_top = True
    whApp().run()
