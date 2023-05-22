from kivymd.app import MDApp
from kivy.lang import Builder


class CyberShieldApp(MDApp):

    data = {
        "Application" : "android",
        "Website" : "web"
    }
    def build(self):
        return Builder.load_file("main.kv")
    
    def login_data(self):
        website = self.screen_manager.password.website.text
        username = self.username.text
        password = self.password.text

        print(website)
        print(username)
        print(password)


if __name__ == "__main__":
    app = CyberShieldApp()
    app.run()
