from kivy.app import App
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader

class AudioApp(App):
    def build(self):
        self.button = Button(text='Воспроизвести звук')
        self.button.bind(on_press=self.play_sound)
        return self.button

    def play_sound(self, instance):
        sound = SoundLoader.load('temp.mp3')
        if sound:
            sound.play()

if __name__ == '__main__':
    AudioApp().run()