import antivirus
import encrypt_password
from kivymd.app import MDApp
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.config import Config
from kivy.properties import ObjectProperty
from kivymd.uix.pickers import MDDatePicker
from kivy.uix.floatlayout import FloatLayout
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')


class MyAppApp(MDApp):
    screen_manager = ObjectProperty(None)

    def build(self):
        self.icon = 'app-logo.png'
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.accent_palette = "Amber"
        self.screen = Builder.load_file("main.kv") 
        return self.screen

    """
    Functions for settings
    """

    def theme_select(self):
        self.theme_cls.theme_style = (
            "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        )
    def on_save(self, instance, value, date_range):
        date_selection = self.root.ids.screen_manager.get_screen("settings")
        date_label = date_selection.date_label.text
        date_selection.date_label.text = f"{value}"
        print(instance, value, date_range)

    def on_cancel(self, instance, value):
        cancel = self.root.ids.screen_manager.get_screen("settings")
        date_label = cancel.date_label.text
        cancel.date_label.text = "Select Date"
        print(date_label)

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()

    """
    Functions for AntiVirus
    """

    def scan_files(self):
        antivirus.folder_scanner("C:\\Users\\Yogesh P\\Desktop\\CyberShield\\")

    def progress_bar(self, *args):
        # value = 0
        # self.root.ids.progress_bar.value = 0
        value = self.root.ids.progress_bar.value
        Clock.schedule_interval(self.progress_bar, 0.25)
        try:
            value += 0.5
            self.root.ids.progress_bar.value = value
        except:
            Clock.unschedule(self.progress_bar)

    """
    Functions for password manager
    """

    def encrypt(self):
        encrypt_password.Encrypt_Password.encrypt()

    def decrypt(self):
        encrypt_password.Encrypt_Password.decrypt()
        

    def login_data(self):
        login = self.root.ids.screen_manager.get_screen("passwordmanager")
        website = login.website.text
        username = login.username.text
        password = login.passwords.text
        data = f"{website},{username},{password}\n"
        print(data)
        file = open('password_file.csv', '+a')
        file.write(data)
        file.close()


if __name__ == "__main__":
    app = MyAppApp()
    app.run()
