class Phone:
    def __init__(self,brand,model,battary_level):
           self.brand = brand
           self.model = model
           self.battery_level = battary_level


    def power_on(self):
          print(f"{self.brand}: {self.model} is on")

    def power_off(self):
          print(f"{self.brand}: {self.model} is off")
    
    def install_app(self, app_name):
        print(f"Installed {app_name}.")

    def check_battery(self):
        print(f"Battery level: {self.battery_level}%")


def main():
    my_phone = Phone("Samsung", "Galaxy S21", 85)

    my_phone.power_on()
    my_phone.check_battery()
    my_phone.install_app("WhatsApp")
    my_phone.install_app("Instagram")
    my_phone.power_off()


if __name__ == "__main__":
    main()
