from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton, MDFloatingActionButton, MDFillRoundFlatIconButton
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.textfield import MDTextField
from kivy.core.window import Window
import sqlite3
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.list import OneLineIconListItem
from kivy.metrics import dp
from kivy.uix.image import AsyncImage
from kivymd.uix.menu import MDDropdownMenu, RightContent
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase
from kivymd.icon_definitions import md_icons
from kivymd.uix.bottomsheet import MDGridBottomSheet
from kivymd.toast import toast
from email.message import EmailMessage
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import string
Window.size = (400, 650)
helper_string = """
ScreenManager:
    LoginScreen:
    HomeScreen:
    CreateAccountScreen:
    ProfileScreen:
    viewDocumentScreen:
    LicenseScreen:

<LoginScreen>
    name: 'login'

    MDLabel:
        text: "Sign in to AE_Solutions"
        font_style: "Subtitle1"
        halign: 'center'
        pos_hint: {"center_x": 0.5, "center_y": 0.8}

    MDTextField:
        id: username_email
        hint_text: "Enter email address"
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
                            id: menu_caller
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
                                            on_release: root.show_bottom_sheet()
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
                                on_press: root.profile_clicked()
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
                title: "Profile"
                elevation: 10


            ScrollView:
                MDList:
                    TwoLineAvatarListItem:
                        id: gmail_n_name
                        text: ""
                        secondary_text: "Email"
                        on_press: root.show_profile()
                        pos_hint: {"center_x": 0.5, "center_y":0.8}
                        ImageLeftWidget:
                            source: "dog_test_2.jpg"
                       
                    TwoLineAvatarListItem:
                        id: Name
                        text: ""
                        secondary_text: "Name"
                    TwoLineAvatarListItem:
                        id: state
                        text: ""
                        secondary_text: "State"
                    TwoLineAvatarListItem:
                        id: lga
                        text: ""
                        secondary_text: "LGA"
                    TwoLineAvatarListItem:
                        id: nin
                        text: ""
                        secondary_text: "NIN"
                    TwoLineAvatarListItem:
                        id: mobile
                        text: ""
                        secondary_text: "Mobile"
                    TwoLineAvatarListItem:
                        id: dob
                        text: ""
                        secondary_text: "DOB"

            MDBottomAppBar:
                MDToolbar:
                    type:"bottom"
                    icon: "home"
                    on_action_button: root.manager.current = "Homescreen"
                    mode: "end"

<LicenseScreen>
    name: "license"
    Screen:
        BoxLayout:
            orientation: "vertical"
            MDToolbar:
                title: "Legal"
                left_action_items: [ [ "menu", lambda x: root.create_menu() ] ]
                elevation: 10
            
            ScrollView:
                MDList:
                    OneLineListItem
                        text: "License"
                        
                    OneLineListItem
                        text: "Legal Notices"
                    
                    OneLineListItem
                        text: "Regulatory"
                    OneLineListItem
                        text: "Terms and Conditions"
            MDRectangleFlatButton:
                text: 'I Agree'
                pos_hint: {"center_x": 0.5, "center_y": 0.6}
                on_release: root.created_account()
                        


<CreateAccountScreen>
    name: "create_account"
    Screen:
        MDFillRoundFlatButton:
            text: "Login"
            pos_hint: {"center_x": 0.85, 'center_y':0.93}
            on_press: root.login_clicked()

        MDLabel:
            text: "Create account"
            font_style: "Body1"
            halign: "center"
            pos_hint: {"center_x":0.5, "center_y":0.9}

        MDTextFieldRound:
            id: surname
            hint_text: "Surname"
            pos_hint: {"center_x":0.5, "center_y":0.8}
            size_hint_x: None
            width: 250
            icon_left: "account-details"
        MDTextFieldRound:
            id: other_names
            hint_text: "Other names"
            pos_hint: {"center_x":0.5, "center_y":0.7}
            size_hint_x: None
            width: 250
            icon_left: "account-details"
        MDTextFieldRound:
            id: email
            hint_text: "Valid email"
            pos_hint: {"center_x":0.5, "center_y":0.6}
            size_hint_x: None
            width: 250
            icon_left: "email"
            
        MDTextFieldRound:
            id: dob
            hint_text: "D.O.B"
            pos_hint: {"center_x":0.5, "center_y":0.5}
            size_hint_x: None
            width: 250
           
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
            
        MDTextFieldRound:
            id: location
            hint_text: "Location"
            pos_hint: {"center_x":0.5, "center_y":0.2}
            size_hint_x: None
            width: 250

        MDFillRoundFlatButton:
            text: "Next"
            pos_hint: {"center_x":0.5, "center_y": 0.1}
            on_release: root.next_clicked(surname.text,other_names.text,email.text,dob.text,mobile.text,nin.text,location.text)
                        
            


"""
details = []

class Tab(FloatLayout, MDTabsBase):

    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        instance_tab.ids.label.text = tab_text


class RightContentCls(RightContent):
    pass

_ID = []
class LoginScreen(Screen):
    def login(self, *args):
        if "@" in args[0]:
            try:
                conn = sqlite3.connect("UserRecord1.db")
                c = conn.cursor()
                query = "SELECT Password FROM individual_account_details WHERE Email = ?"
                data_to_be_inserted = (args[0],)
                c.execute(query, data_to_be_inserted)
                returned_password = c.fetchone()
                if (args[1] == returned_password[0]):
                    self.manager.current = "Homescreen"
                    _ID.append(args[1])

                c.close()
                conn.commit()
                conn.close()
            except (Exception, TypeError) as e:
                print(e)

        else:
           pass


class viewDocumentScreen(Screen):
    pass


class ProfileScreen(Screen):
    #def on_pre_enter(self, *args):
    #    labels = [{"viewclass": "MDMenuItem", "icon": "open-in-app", "text": "Edit"},
    #              {"viewclass": "MDMenuItem", "icon": "rename-box", "text": "Home"}]
    #    self.menu = MDDropdownMenu(caller=self.ids.menu_caller,
    #                               items=labels, width_mult=4, callback=self.menu_callback)

    #def menu_callback(self, instance):
    #    if instance.text == "Home":
    #        self.manager.current = "Homescreen"
    def show_profile(self):
        try:
            conn = sqlite3.connect("UserRecord1.db")
            c = conn.cursor()
            query = "SELECT * FROM individual_account_details WHERE Password = ?"
            c.execute(query,(_ID[0],))
            data = c.fetchone()
            c.close()
            conn.commit()
            conn.close()
            self.ids.gmail_n_name.text = data[4]
            self.ids.Name.text = data[0] + " " + data[1]
            self.ids.state.text = "yoyo"
            self.ids.lga.text = ""
            self.ids.nin.text = data[6]
            self.ids.mobile.text = data[3]
            self.ids.dob.text = data[5]
        except Exception as e:
            print(e)
        #self.ids.gmail_n_name=""
    def any(self):
        pass


class HomeScreen(Screen):
    def profile_clicked(self):
        self.manager.current = "profile"
        profile = ProfileScreen()
        profile.show_profile()
    def show_bottom_sheet(self):
        bottom_menu = MDGridBottomSheet()
        data = {
            "Facebook": "facebook-box",
            "YouTube": "youtube",
            "Twitter": "twitter-box",
            "Da Cloud": "cloud-upload",
            "Camera": "camera",
        }

        for item in data.items():
            bottom_menu.add_item(
                item[0],
                lambda x, y=item[0]: self.callback_for_menu_items(y),
                icon_src=item[1],
            )

        bottom_menu.open()

    def callback_for_menu_items(self, *args):
        toast(args[0])

    def navigation_draw(self):
        print("navigate")

    def document_clicked(self):
        print("clicked")

    def call_back(self):
        pass


class LicenseScreen(Screen):
    def create_menu(self):
        self.manager.current = "create_account"
    def created_account(self):
        if details[0]!="" and details[1]!="" and details[2]!="" and details[3]!="" and details[4]!="" and details[5]!="" and details[6]!="":
            try:
                #Generate the password
                list_random_gen = []
                for letter in range(0,7):
                    list_random_gen.append(random.choice(string.ascii_letters))
                for number in range(0,3):
                    num = random.randint(0,10)
                    list_random_gen.append(str(num))

                pass_word = ''.join(list_random_gen)
                smtp_server = "smtp.gmail.com"
                port = 587  # For starttls
                sender_email = "ltdaesolutions@gmail.com"
                password = "ae_solutions0000"
                receiver = details[2]
                message = MIMEMultipart('alternative')
                message["Subject"] = "Welcome to AE_Solutions"
                message["From"] = sender_email
                message["To"] = receiver
                text = f"""\
                            HI!

                            We are happy to see you {details[0]} {details[1]} at AE_Solutions.

                            Your password is {pass_word}

                            This is a test msg."""

                part1 = MIMEText(text, "plain")
                message.attach(part1)
                # Create a secure SSL context
                context = ssl.create_default_context()

                # Try to log in to server and send email
                try:
                    server = smtplib.SMTP(smtp_server, port)
                    server.ehlo()  # Can be omitted
                    server.starttls(context=context)  # Secure the connection
                    server.ehlo()  # Can be omitted
                    server.login(sender_email, password)
                    server.sendmail(sender_email, receiver, message.as_string())
                    toast("Account created")
                    conn = sqlite3.connect("UserRecord1.db")
                    c = conn.cursor()
                    query = "INSERT INTO individual_account_details (Surname,Othernames,Password,Mobile,Email,DOB,NIN,Location) VALUES (?,?,?,?,?,?,?,?)"
                    data_to_be_inserted = (
                    details[0], details[1], pass_word, details[4], details[2], details[3], details[5], details[6])
                    c.execute(query, data_to_be_inserted)
                    c.close()
                    conn.commit()
                    conn.close()
                    details.clear()
                    self.manager.current = "login"
                except Exception as e:
                    # Print any error messages to stdout
                    print(e)
                    toast("Connection error")
                finally:
                    server.quit()

            except (Exception, TypeError) as e:
                print(e)
        else:
            pass

class CreateAccountScreen(Screen):
    def next_clicked(self,*args):
        #root.manager.current = "license"
        details.clear()
        for _ in args:
            details.append(_)
        print(details)
        self.manager.current = "license"
    def login_clicked(self):
        self.ids.surname.text = ""
        self.ids.other_names.text = ""
        self.ids.email.text = ""
        self.ids.dob.text = ""
        self.ids.nin.text = ""
        self.ids.location.text = ""
        details.clear()
        self.manager.current = "login"



sm = ScreenManager()
sm.add_widget(LoginScreen(name="login"))
sm.add_widget(HomeScreen(name="Homescreen"))
sm.add_widget(CreateAccountScreen(name="create_account"))
sm.add_widget(LicenseScreen(name="license"))


class AEApp(MDApp):
    # icons = list(md_icons.keys())[15:30]
    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.builder = Builder.load_string(helper_string)
        return self.builder

    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        instance_tab.ids.label.text = tab_text


AEApp().run()
#gxlBwbp798