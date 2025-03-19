# dont fool or it will fool you
import webbrowser
def number_generator():
    print("Welcome to my very well made number guesser!")
    while True:
        user_input = input("Enter a number and I will try guess!: ")

        # Silly validation to make sure you dont type letters owo
        if user_input.lstrip('-').isdigit():
            number = int(user_input)
            print(f"Calculating the number you might of entered fr...")
            print(f"HEHE! It's: {number}, Thanks for using >w<")
            webbrowser.open("https://t8xh.cc", new=1)
            break
        else:
            print("i hate you type a number or else....")
            webbrowser.open("https://t8xh.cc", new=1)
number_generator()