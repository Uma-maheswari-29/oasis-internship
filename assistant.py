import datetime

def get_time():
    return datetime.datetime.now().strftime("%I:%M %p")

def get_date():
    return datetime.datetime.now().strftime("%d %B %Y")

def get_day():
    return datetime.datetime.now().strftime("%A")

def assistant():
    print("Advanced Assistant Started")
    print("Type: hello, time, date, day, about, help, exit")

    while True:
        command = input("\nYou: ").lower().strip()

        if command in ["hello", "hi"]:
            print("Assistant: Hello! How can I help you?")

        elif command == "time":
            print("Assistant: Current time is", get_time())

        elif command == "date":
            print("Assistant: Today's date is", get_date())

        elif command == "day":
            print("Assistant: Today is", get_day())

        elif command == "about":
            print("Assistant: I am an advanced assistant built using Python.")

        elif command == "help":
            print(
                "Assistant: Available commands:\n"
                "- hello / hi\n"
                "- time\n"
                "- date\n"
                "- day\n"
                "- about\n"
                "- exit"
            )

        elif command == "exit":
            print("Assistant: Goodbye! Have a nice day 😊")
            break

        else:
            print("Assistant: Sorry, I don't understand that command. Type 'help'.")

assistant()
