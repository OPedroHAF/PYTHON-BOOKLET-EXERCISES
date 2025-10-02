#An algorithm of taking a shower

def room():
    items_list = []
    print("There are some things in your room, do you wish to take any of them?")
    print("1. Towel")
    print("2. Clothes")
    print("3. Cellphone")
    option = int(input("Select an option (1-3): "))
    if option == 1:
        items_list.append("Towel")
def light_switch():
    light = "off"
    while light == "off":
        while True:
            askLight = input("The light is off, do you wish to turn it on?(Y/N):")
            if askLight != 'Y' and askLight != 'N':
                print("Please enter Y or N")
            elif askLight == 'Y':
                light = "on"
                print("The light is now on")
                break
            else:
                print("The light is still off")



print("You woke up and decided to take a shower because soon you have to go to work")

light_switch()
print("")

