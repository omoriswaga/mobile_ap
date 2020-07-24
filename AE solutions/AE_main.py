from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton,MDFloatingActionButton,MDFillRoundFlatIconButton
from kivy.uix.screenmanager import Screen, ScreenManager

helper_string = """
ScreenManager:
    LoginScreen:
                        
<LoginScreen>
    name: 'login'
    
    MDLabel:
        text: "Sign in to AE_Solutions"
        font_style: "Subtitle1"
        halign: 'center'
        pos_hint: {"center_x": 0.5, "center_y": 0.8}
    
    MDTextField:
        hint_text: "Enter Username or email address"
        size_hint_x: None
        width: 250
        pos_hint: {"center_x": 0.5, "center_y": 0.7}
        
    MDTextField:
        hint_text: "Enter password"
        helper_text: "Or click on forgot password"
        helper_text_mode: "on_focus"
        pos_hint: {"center_x": 0.5, "center_y": 0.6 }
        size_hint_x: None
        width: 250
    MDRectangleFlatButton:
        text: 'sign in'
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        
    MDFlatButton:
        text: 'Forgot password?'
        pos_hint: {"center_x": 0.5, "center_y": 0.4}
        
    MDLabel:
        text: "___________ or ___________"
        halign: 'center'
        pos_hint: {"center_x": 0.5, "center_y": 0.35}
    MDLabel:
        text: "Signup with"
        font_style: 'Body2'
        halign: "center"
        pos_hint: {"center_x": 0.5, "center_y": 0.3}
        
    MDFloatingActionButton:
        icon: "facebook"
        pos_hint: {"center_x": 0.35, "center_y": 0.2}
    MDFloatingActionButton:
        icon: "google"
        pos_hint: {"center_x": 0.65, "center_y": 0.2}
 
"""

class LoginScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(LoginScreen(name= "login"))

class AEApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        builder = Builder.load_string(helper_string)
        return builder

AEApp().run()