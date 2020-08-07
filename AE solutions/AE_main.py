from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton,MDFloatingActionButton,MDFillRoundFlatIconButton
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.textfield import MDTextField
from kivy.core.window import Window
import sqlite3
from passlib.hash import sha256_crypt
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.list import OneLineIconListItem
from kivy.metrics import dp
from kivy.uix.image import AsyncImage
from kivymd.uix.menu import MDDropdownMenu,RightContent
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase
from kivymd.icon_definitions import md_icons

Window.size = (400,650)

helper_string = """
ScreenManager:
    LoginScreen:
    HomeScreen:
    CreateAccountScreen:
    ProfileScreen:
    viewDocumentScreen:
                        
<LoginScreen>
    name: 'login'
    
    MDLabel:
        text: "Sign in to AE_Solutions"
        font_style: "Subtitle1"
        halign: 'center'
        pos_hint: {"center_x": 0.5, "center_y": 0.8}
    
    MDTextField:
        id: username_email
        hint_text: "Enter Username or email address"
        size_hint_x: None
        width: 250
        pos_hint: {"center_x": 0.5, "center_y": 0.7}
        
    MDTextField:
        id: _password
        hint_text: "Enter password"
        helper_text: "Or click on forgot password"
        helper_text_mode: "on_focus"
        pos_hint: {"center_x": 0.5, "center_y": 0.6 }
        size_hint_x: None
        width: 250
        password: True
    MDRectangleFlatButton:
        id: sign_in
        text: 'sign in'
        pos_hint: {"center_x": 0.7, "center_y": 0.5}
        on_press: root.login(username_email.text,_password.text)
        
    
    MDRectangleFlatButton:
        text: 'Create account'
        pos_hint: {"center_x": 0.3, "center_y": 0.5}
        on_press: root.manager.current = "create_account"
    
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
        elevation_normal: 10
    MDFloatingActionButton:
        icon: "google"
        pos_hint: {"center_x": 0.65, "center_y": 0.2}
        elevation_normal: 10
 
<HomeScreen>
    name: "Homescreen"
    Screen:
        NavigationLayout:
            ScreenManager:
                Screen:
                    
                    BoxLayout:
                        orientation: "vertical"
                        
                        MDToolbar:
                            title: "AE Solutions"
                            left_action_items: [ [ "menu", lambda x: nav_drawer.toggle_nav_drawer() ] ]
                            right_action_items: [ ['dots-vertical', lambda x: root.call_back()] ]
                            elevation: 10
                            
                        MDTabs:
                            id: android_tabs
                            on_tab_switch: app.on_tab_switch(*args)
                            Tab:
                                text: "Documents"
                                    
                                ScrollView:
                                    MDList:
                                        TwoLineIconListItem:
                                            text : "I am a list"
                                            secondary_text : 'Swimming and dancing is my hubby'
                                            on_release: root.manager.current = "doc"
                                            IconLeftWidget:
                                                icon: "book"
                                            

                                
                            Tab:
                                text: "Custom document"
                            Tab:
                                text: "Payment info"
                            
                              
                       
                                                      
            MDNavigationDrawer:
                id: nav_drawer
                BoxLayout:
                    orientation: "vertical"
                    spacing: "8dp"
                    padding: "8dp"
                    
                    MDLabel:
                        text: "Username"
                        font_style:'Subtitle1'
                        size_hint_y : None
                        height: self.texture_size[1]
                        
                    MDLabel:
                        text:"Omorisiagbon@gmail.com"
                        font_style:'Caption'
                        size_hint_y : None
                        height: self.texture_size[1]
                        
                    ScrollView: 
                        MDList:
                            OneLineIconListItem:
                                on_press: root.manager.current = "profile"
                                text: "Profile"
                                IconLeftWidget:
                                    icon: "account-circle"
                                
                            OneLineIconListItem:
                                text: "My files"
                                IconLeftWidget:
                                    icon: "folder"
                                                        
                            OneLineIconListItem:
                                text: "About"
                                IconLeftWidget:
                                    icon: "note"        
                            OneLineIconListItem:
                                text: "Contact"
                                IconLeftWidget:
                                    icon: "note"     
                            OneLineIconListItem:
                                text: "License"
                                IconLeftWidget:
                                    icon: "note"                    
       
              
<Tab>:
    MDLabel:
        id: label
        text: "Tab 0"
        halign: "center" 
        
        
<viewDocumentScreen>
    name: "doc"
    Screen:
        MDTextFieldRect:
            id: text_viewer
                     
<ProfileScreen>
    name: "profile"
    Screen:
        BoxLayout:
            orientation: "vertical"
            MDToolbar:
                id : menu_caller
                title: "Profile"
                elevation: 10
            
            
            ScrollView:
                MDList:
                    TwoLineAvatarListItem:
                        text: "giftoghosa@gmail.com"
                        secondary_text: "oghogift"
                        pos_hint: {"center_x": 0.5, "center_y":0.8}
                        ImageLeftWidget:
                            source: "dog_test_2.jpg"
                    TwoLineAvatarListItem:
                        text: "Omorisiagbon oghosa gift"
                        secondary_text: "Name"
                    TwoLineAvatarListItem:
                        text: "Edo"
                        secondary_text: "State"
                    TwoLineAvatarListItem:
                        text: "Oredo"
                        secondary_text: "LGA"
                    TwoLineAvatarListItem:
                        text: "24561388902"
                        secondary_text: "NIN"
                    TwoLineAvatarListItem:
                        text: "09091493208"
                        secondary_text: "Mobile"
                    TwoLineAvatarListItem:
                        text: "1996/10/28"
                        secondary_text: "DOB"
                        
            MDBottomAppBar:
                MDToolbar:
                    type:"bottom"
                    icon: "home"
                    on_action_button: root.manager.current = "Homescreen"
                    mode: "end"
        

        
<CreateAccountScreen>
    name: "create_account"
    Screen:
        MDFillRoundFlatButton:
            text: "Login"
            pos_hint: {"center_x": 0.85, 'center_y':0.93}
            on_press: root.manager.current = "login"
            
        MDLabel:
            text: "Create account"
            font_style: "Body1"
            halign: "center"
            pos_hint: {"center_x":0.5, "center_y":0.8}
        
        MDTextFieldRound:
            id: username
            hint_text: "Username"
            pos_hint: {"center_x":0.5, "center_y":0.7}
            size_hint_x: None
            width: 250
            icon_left: "account-details"
        MDTextFieldRound:
            id: mail
            hint_text: "Email"
            pos_hint: {"center_x":0.5, "center_y":0.6}
            size_hint_x: None
            width: 250
            icon_left: "email"
        MDTextFieldRound:
            id: password
            hint_text: "Password"
            pos_hint: {"center_x":0.5, "center_y":0.5}
            size_hint_x: None
            width: 250
            icon_left: "lock"
            icon_right: "eye-off"
            password: True
        MDTextFieldRound:
            id: mobile
            hint_text: "Mobile"
            pos_hint: {"center_x":0.5, "center_y":0.4}
            size_hint_x: None
            width: 250
            icon_left: "phone"
            
        MDTextFieldRound:
            id: nin
            hint_text: "NIN"
            pos_hint: {"center_x":0.5, "center_y":0.3}
            size_hint_x: None
            width: 250
            
        MDFillRoundFlatButton:
            text: "Create"
            pos_hint: {"center_x":0.5, "center_y": 0.2}
            on_release: root.validate_account(username.text,mail.text,password.text,mobile.text)
            
        

"""

class Tab(FloatLayout, MDTabsBase):

    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        instance_tab.ids.label.text = tab_text

class RightContentCls(RightContent):
    pass

class LoginScreen(Screen):
    def login(self,*args):
        if "@" in args[0]:
            try:
                conn = sqlite3.connect("UserRecord.db")
                c = conn.cursor()
                query = "SELECT Password FROM individual_account_details WHERE Email = ?"
                data_to_be_inserted = (args[0],)
                c.execute(query,data_to_be_inserted)
                returned_password = c.fetchone()
                if (sha256_crypt.verify(args[1], returned_password[0]) == True):
                    self.manager.current = "Homescreen"

                c.close()
                conn.commit()
                conn.close()
            except (Exception, TypeError) as e:
                print(e)

        else:
            try:
                conn = sqlite3.connect("UserRecord.db")
                c = conn.cursor()
                query = "SELECT Password FROM individual_account_details WHERE Username = ?"
                data_to_be_inserted = (args[0],)
                c.execute(query,data_to_be_inserted)
                returned_password = c.fetchone()
                if (sha256_crypt.verify(args[1],returned_password[0]) == True):
                    self.manager.current = "Homescreen"

                c.close()
                conn.commit()
                conn.close()
            except (Exception, TypeError) as e:
                print(e)

class viewDocumentScreen(Screen):
    pass

class ProfileScreen(Screen):
    def on_pre_enter(self, *args):
        labels = [{"viewclass":"MDMenuItem","icon": "open-in-app","text": "Edit"}, {"viewclass":"MDMenuItem","icon": "rename-box","text": "Home"}]
        self.menu =  MDDropdownMenu(caller = self.ids.menu_caller,
                               items = labels, width_mult=4, callback = self.menu_callback)

    def menu_callback(self, instance):
        if instance.text == "Home":
            self.manager.current = "Homescreen"


class HomeScreen(Screen):
    def navigation_draw(self):
        print("navigate")

    def document_clicked(self):
        print("clickked")

    def call_back(self):
        pass

class CreateAccountScreen(Screen):
    def validate_account(self, *args):
        # contents will be stored on the database
        if args[0]!="" and args[1]!="" and args[2]!="" and args[3]!="":

            try:
                conn = sqlite3.connect("UserRecord.db")
                c = conn.cursor()
                query = "INSERT INTO individual_account_details (Username, Email, Password, Mobile) VALUES (?,?,?,?)"
                hash_password = sha256_crypt.hash(args[2])
                data_to_be_inserted = (args[0],args[1],hash_password,args[3])
                c.execute(query,data_to_be_inserted)
                args[0], args[1], args[2], args[3] = ""
                c.close()
                conn.commit()
                conn.close()

            except (Exception, TypeError) as e:
                print(e)
        else:
            pass


sm = ScreenManager()
sm.add_widget(LoginScreen(name= "login"))
sm.add_widget(HomeScreen(name = "Homescreen"))
sm.add_widget(CreateAccountScreen(name= "create_account"))

class AEApp(MDApp):
    #icons = list(md_icons.keys())[15:30]
    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.builder = Builder.load_string(helper_string)
        return self.builder

    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        instance_tab.ids.label.text = tab_text



AEApp().run()