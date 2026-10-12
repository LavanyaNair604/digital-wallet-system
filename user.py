class User:
    def __init__(self):
        self.user_name = ""
        self.wallet_color = ""
        self.wallet_balance = 0.0
        self.wallet_keychain = ""
        self.bedazzle = False

    def set_user_name(self):
        self.user_name = input("Enter your name: ")
        print("Hello " + self.user_name + "!" + "Lets first decorate your wallet before we start using it.")

    def set_wallet_color(self):
        self.wallet_color = input("Enter your desired wallet color: ")
        print("Your wallet color is " + self.wallet_color + ".")

    def set_wallet_keychain(self):
        self.wallet_keychain = input("Enter your wallet keychain: ")
        print("Your wallet keychain is " + self.wallet_keychain + ".")

    def set_bedazzle(self):
        bedazzle_input = input("Do you want to bedazzle your wallet? (yes/no): ")
        if bedazzle_input.lower() == "yes":
            self.bedazzle = True
            print("⋆˙⟡ ⋆˙⟡ Your wallet is now bedazzled!⋆˙⟡ ⋆˙⟡")
        else:
            self.bedazzle = False
            print("Your wallet is not bedazzled.")

user = User()
user.set_user_name()
user.set_wallet_color()
user.set_wallet_keychain()
user.set_bedazzle()