from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import ObjectProperty

class CyberShieldApp(MDApp):
    screen_manager  = ObjectProperty(None)
    def build(self):
        self.screen = Builder.load_file("main.kv")
        return self.screen
    
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
