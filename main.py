from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.config import Config
from kivymd.uix.pickers import MDDatePicker
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')


class CyberShieldApp(MDApp):
    screen_manager = ObjectProperty(None)

    def build(self):
        self.screen = Builder.load_file("main.kv")
        return self.screen

    def on_save(self, instance, value, date_range):
        print(instance, value, date_range)

    def on_cancel(self, instance, value):
        pass

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()

    def login_data(self):
        self.login = self.root.ids.screen_manager.get_screen("passwordmanager")
        self.website = self.login.website.text
        self.username = self.login.username.text
        self.password = self.login.passwords.text
        self.data = f"{self.website};{self.username};{self.password}\n"
        print(self.data)
        self.file = open('password_file.txt', '+a')
        self.file.write(self.data)
        self.file.close()


if __name__ == "__main__":
    app = CyberShieldApp()
    app.run()
