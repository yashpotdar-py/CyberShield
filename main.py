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
        login = self.root.ids.screen_manager.get_screen("passwordmanager")
        website = login.website.text
        username = login.username.text
        password = login.passwords.text

        print(website)
        print(username)
        print(password)


if __name__ == "__main__":
    app = CyberShieldApp()
    app.run()
