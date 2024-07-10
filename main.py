from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
import psutil
from kivy.uix.filechooser import FileChooser
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import whisper
import pathlib

kv_string = '''
#:import psutil psutil
#:import pathlib pathlib
<CustomBoxLayout@BoxLayout>:
    orientation: 'vertical'
    BoxLayout: 
        orientation: 'horizontal'
        size_hint: (1,0.2)
        Label:
            id: selectedtextID
            text: "selected file: "
            multiline: True
            do_wrap: True
            valign: 'center'
            text_size: self.size
        TextInput:
            id: textinputID
            multiline: False
            valign: 'center'
            padding_y: [self.height / 2.0 - (self.line_height / 2.0) * len(self._lines), 0]
            text: ""
        Button:
            text: "Transcribe!"
            on_release:
                root.transcribe()
    Spinner:
        size_hint: 1, 0.1
        pos_hint: {'center': (.5, .5)}
        text: 'Choose drive:'
        values: ['Choose drive: ' + var.device for var in psutil.disk_partitions()]
        on_text:
            print("The spinner {} has text {}".format(self, self.text))
            driveletter = self.text.replace('Choose drive: ', '') #all this does is remove the 'Choose drive: ' in front
            root.ids['fc'].path = driveletter
            print(driveletter)
            print(self.values)
    FileChooser:
        id: fc
        on_selection: 
            # root.ids['selectedtextID'].text = str(self.selection)
            root.ids['selectedtextID'].text = "selected file: " + self.selection[0] if len(self.selection) > 0 else "selected file: "
            root.ids['textinputID'].text = pathlib.Path(self.selection[0]).stem + " whisper transcript" if len(self.selection) > 0 else ""

        FileChooserIconLayout

CustomBoxLayout:
'''

class CustomBoxLayout(BoxLayout):
    def transcribe(self, *args):
        #make sure there is a selection in the filechooser
        if len(self.ids['fc'].selection) > 0:
            self.run_whisper()
        else:
            self.popup_open()

    def run_whisper(self, *args):
        try: 
            filename = self.ids['selectedtextID'].text.replace('selected file: ', '')
            transcript_name = pathlib.Path(self.ids['selectedtextID']).parent / self.ids['textinputID'].text + ".txt"
            print("????",transcript_name)
                # os.path.join(
                #     os.path.split(self.ids['selectedtextID'].text)[0],
                #     self.ids['textinputID'].text,
                #     ".txt")
            # model = whisper.load_model("medium")
            # result = model.transcribe(filename, fp16=False)
            # f = open(transcript_name, "w") 
            # with f as f:
            #     f.write(result["text"])
        except Exception as e:
            import traceback
            print("error is "+ str(e))
            print(str(traceback.format_exc()))
            self.popup_open()

    def popup_open(self,*args):
        popup = Popup(title='Something went wrong.', 
                content=
                    Label(
                        text='Please check the filetype and destination. \nPress any key to close.', 
                        multiline= True), 
                    size_hint=(None, None), 
                    size=(400, 400))
        popup.open()

class whApp(App):
    def build(self):
        return Builder.load_string(kv_string)

if __name__ == '__main__':
    #this is to make the Kivy window always on top
    from kivy.core.window import Window
    Window.always_on_top = True
    whApp().run()
