from kivy.app import App
from kivy.lang import Builder

kv_string = '''
Button:
    test: "hw!"
'''
class whApp(App):
    def build(self):
        return Builder.load_string(kv_string)

if __name__ == '__main__':
    #this is to make the Kivy window always on top
    from kivy.core.window import Window
    Window.always_on_top = True
    whApp().run()
