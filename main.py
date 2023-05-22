from kivymd.app import MDApp
from kivy.lang import Builder


class CyberShieldApp(MDApp):

    data = {
        "Application" : "android",
        "Website" : "web"
    }
    def build(self):
        return Builder.load_file("main.kv")


if __name__ == "__main__":
    app = CyberShieldApp()
    app.run()
