import csv
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.config import Config
from kivymd.uix.pickers import MDDatePicker
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')


class CyberShieldApp(MDApp):
    screen_manager = ObjectProperty(None)

    def build(self):
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Purple"
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
    Functions for password manager
    """

    def encrypt(self):
        f = open("password_file.csv")
        for row in csv.reader(f):
            print(row[2])

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

    def label(self, data):
        x = CyberShieldApp.login_data()
        return x


if __name__ == "__main__":
    app = CyberShieldApp()
    app.run()
