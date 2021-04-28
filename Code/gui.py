# Loading the required packages

from tkinter import *
from chatbot import *

# Function to create the chat window and chat with the user

def chatting():
    chatWindow = Tk()
    chatWindow.geometry("500x500")
    chatWindow.title("Chatbot")
    chatWindow["background"] = "#5BC8AF"

    # Add text to the chat window
    bot_ele = Text(chatWindow, fg="black", bg="#5BC8AF", width=100, height=20, font=(16))
    bot_ele.insert("1.0", "Hi there! You are now interacting with a chatbot.\n")
    bot_ele.insert("2.0", "Enter a number based on what you want to do:\n")
    bot_ele.insert("3.0", "1. Chat with the bot\n")
    bot_ele.insert("4.0", "2. Analyze the sentiment and detect the language of the text\n")
    bot_ele.pack()

    input_ele = Entry(chatWindow, fg="black", bg="white", width=100)
    input_ele.pack()

    ele = Label(chatWindow, text="", width=100, height=3, bg="#5BC8AF")
    ele.pack()

    # Create a button and add an action to it
    ele = Button(text="Send",
        width=5,
        height=2,
        highlightbackground="black",
        fg="#F18D9E",
        command = lambda: interact(bot_ele, input_ele))
    ele.pack()

    chatWindow.mainloop()

# Function to interact with the chatbot program based on the choice of the user

def interact(bot_ele, input_ele):

    global check, choice
    print("Hello")
    response = input_ele.get()
    print(response)
    print(check)
    # Check if this is the user's first input
    if check == 1:
        print(response)
        choice = response
        print(choice)
        if choice == "1":
            print("hi")
            bot_ele.insert("1.0", "I can answer any questions you may have about linguistics.\nType in your question. If want to exit, type bye.\n")
            bot_ele.delete("3.0", END)
            bot_ele.delete("4.0", END)
            check += 1
        elif choice == "2":
            bot_ele.insert("1.0", "Enter some text to be analyzed.\n")
            bot_ele.delete("2.0", END)
            bot_ele.delete("3.0", END)
            bot_ele.delete("4.0", END)
            check += 1
        else:
            bot_ele.insert("1.0", "Invalid choice, enter again")
            bot_ele.delete("2.0", END)
            bot_ele.delete("3.0", END)
            bot_ele.delete("4.0", END)
    else:
        received = bot(choice, response)
        bot_ele.delete("1.0", END)
        bot_ele.delete("2.0", END)
        bot_ele.insert("1.0", received)

    input_ele.delete(0, END)

# Close the first window that opened

def closeWindow():
    mainWindow.destroy()
    chatting()

# Create the main window (first window the user sees)

mainWindow = Tk()
mainWindow.geometry("500x500")
mainWindow.title("Chatbot")
mainWindow["background"] = "#5BC8AF"
ele = Label(mainWindow, text="Welcome to the chatbot!", width=100, height=13, bg="#5BC8AF")
ele.pack()
check = 1

# Create a button to begin chatting and attach an action to it
ele = Button(text="Start Chatting",
    width=20,
    height=2,
    bg="#F18D9E",
    fg="#F18D9E",
    command=closeWindow)
ele.pack()
mainWindow.mainloop()
