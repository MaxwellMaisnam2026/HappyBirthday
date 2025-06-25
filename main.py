from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.uix.scrollview import ScrollView

Window.clearcolor = (1, 0.88, 0.93, 1)

class BirthdayApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        self.sound = SoundLoader.load('song.mp3')
        if self.sound:
            self.sound.loop = True
            self.sound.play()

        self.cake = Image(source='cake.png', size_hint=(1, 0.4))
        self.layout.add_widget(self.cake)

        self.date = Label(
            text="🎉 4th July 🎉",
            font_size=22,
            color=(0.6, 0, 0.3, 1),
            halign="center",
            valign="middle",
            size_hint=(1, None),
            height=30
        )
        self.layout.add_widget(self.date)

        self.scroll = ScrollView(size_hint=(1, 0.4))
        self.message = Label(
            text="💖 Tap to read a letter from my heart 💖",
            font_size=18,
            halign="left",
            valign="top",
            color=(0.5, 0, 0.3, 1),
            size_hint_y=None
        )
        self.message.bind(texture_size=self.update_text_height)
        self.scroll.add_widget(self.message)
        self.layout.add_widget(self.scroll)

        self.button = Button(
            text="For Nirushree 💝",
            font_size=20,
            size_hint=(1, 0.2),
            background_color=(1, 0.6, 0.8, 1),
            color=(1, 1, 1, 1)
        )
        self.button.bind(on_press=self.reveal_letter)
        self.layout.add_widget(self.button)

        return self.layout

    def update_text_height(self, instance, size):
        instance.height = size[1]
        instance.text_size = (self.scroll.width - 20, None)

    def reveal_letter(self, instance):
        self.button.disabled = True
        self.message.text = "..."
        Clock.schedule_once(self.show_letter, 1.5)

    def show_letter(self, dt):
        letter = (
            "Happy Birthday, Nirushree.\n\n"
            "There was a time when just the thought of you lit up something quiet inside me — something soft, something hopeful. "
            "You never belonged to me, and I never expected you to. But that didn’t stop me from caring — silently, deeply, and without asking for anything in return.\n\n"
            "Loving you was never about being chosen. It was about learning how much someone could mean, even from afar. "
            "And as time passed, I came to understand that some feelings are meant to stay unspoken — not because they're weak, but because they're pure.\n\n"
            "I don’t carry expectations anymore. Only gratitude. For the way you made me feel, for the warmth you unknowingly gave me, and for showing me what quiet love looks like.\n\n"
            "This is me letting go, not with regret, but with grace. Wherever life takes you, I hope it’s full of joy, love, and everything beautiful — just like the kind of light you carry.\n\n"
            "Some stories never start, but they still leave echoes. And in mine, you were a beautiful one."
        )
        self.message.text = ""
        self.type_line(letter, 0)

    def type_line(self, text, index):
        if index < len(text):
            self.message.text += text[index]
            Clock.schedule_once(lambda dt: self.type_line(text, index + 1), 0.02)

BirthdayApp().run()