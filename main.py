from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.config import Config
from kivymd.uix.pickers import MDDatePicker
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

class CyberShieldApp(MDApp):
    screen_manager  = ObjectProperty(None)
    def build(self):
        self.screen = Builder.load_file("main.kv")
        return self.screen
    
    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_pause=self.on_pause)
        date_dialog.open()
    
    def login_data(self):
        website = self.screen.screen_manager.passwordmanager.website.text
        username = self.screen.screen_manager.passwordmanager.username.text
        password = self.screen.screen_manager.passwordmanager.password.text

        print(website)
        print(username)
        print(password)


if __name__ == "__main__":
    app = CyberShieldApp()
    app.run()
