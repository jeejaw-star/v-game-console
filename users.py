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
            password_hash=data["password-hash"]
            if check_password_hash(password_hash, password):
                print("Logging in...")
                try:
                    self.name=data["name"]
                    self.credits=data["credits"]
                    self.saves=data["saves"]
                    print("Logged in successfully!")
                except:
                    print("There was an error while logging in. Please try again.")
                    return
                self.logged_in=True
            else:
                print("Incorrect password.")
                return
                    
                
        else:
                print("Please create an account.")
                self.name=input("Please make a username.")
                password=input("Please make a password.")
                print("Just a moment, i'm making a save file...")
                with open(f"{self.name}_user.json","w") as f:
                    dump({"name":self.name, "password-hash":generate_password_hash(password), "credits":100, "saves":{}},f, indent=4)
                self.credits=100
                self.saves={}
                self.logged_in=True
                print("Created!")
