from json import *
from werkzeug.security import *
class User():
    def __init__(self):
        name=input("username?\n")
        try:
            with open(f"{name}_user.json", "r") as f:
                exists=True
        except:
            exists=False
        if exists:
            password=input("Password?\n")
            with open(f"{name}_user.json","r") as f:
                data=load(f)
            self.password_hash=data["password-hash"]
            if check_password_hash(self.password_hash, password):
                print("Logging in...")
                try:
                    self.name=data["name"]
                    self.credits=data["credits"]
                    self.saves=data["saves"]
                    print("Logged in successfully!")
                except:
                    print("There was an error while logging in. Please try again.")
                    self.logged_in=False
                    return
                self.logged_in=True
            else:
                print("Incorrect password.")
                self.logged_in=False
                return
                    
                
        else:
                print("Please create an account.")
                self.name=input("Please make a username.\n")
                self.password=input("Please make a password.\n")
                print("Just a moment, i'm making a save file...")
                self.password_hash=generate_password_hash(self.password)
                with open(f"{self.name}_user.json","w") as f:
                    dump({"name":self.name, "password-hash":self.password_hash, "credits":100, "saves":{}},f, indent=4)
                self.credits=100
                self.saves={}
                self.logged_in=True
                print("Created!")
    def save(self):
        with open(f"{self.name}_user.json","w") as f:
                    dump({"name":self.name, "password-hash":self.password_hash, "credits":self.credits, "saves":self.saves},f, indent=4)

