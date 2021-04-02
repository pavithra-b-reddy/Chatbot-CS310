from tkinter import *
from gui import *



def chatting():
    chatWindow = Tk()
    chatWindow.geometry("500x500")
    chatWindow.title("Chatbot")
    chatWindow["background"] = "#5BC8AF"

    bot_ele = Text(chatWindow, fg="red", bg="white", width=100)
    bot_ele.insert("1.0", "Hi there! You are now interacting with a chatbot.\n")
    bot_ele.insert("2.0", "Enter a number based on what you want to do:\n")
    bot_ele.insert("3.0", "1. Chat with the bot\n")
    bot_ele.insert("4.0", "2. Analyze the sentiment and detect the language of the text\n")
    bot_ele.pack()

    input_ele = Entry(chatWindow, fg="red", bg="#5BC8AF", width=100)
    input_ele.pack()

    check = 1

    ele = Button(text="Send",
        width=5,
        height=2,
        bg="black",
        fg="white",
        command = lambda: interact(bot_ele, input_ele, check))
    ele.pack()

    chatWindow.mainloop()

def interact(bot_ele, input_ele, check):
    print("Hello")
    response = input_ele.get()
    print(response)
    print(check)
    if check == 1:
        print(response)
        choice = response
        print(choice)
        if choice == "1":
            print("hi")
            bot_ele.insert("1.0", "I can answer any questions you may have about machine intelligence.\nType in your question. If want to exit, type bye.\n")
            bot_ele.delete("3.0", END)
            bot_ele.delete("4.0", END)
    else:
        received = bot(choice, response)
        bot_ele.delete("1.0", END)
        bot_ele.delete("2.0", END)
        bot_ele.insert("1.0", received)

    input_ele.delete(0, END)
    check += 1


def closeWindow():
    mainWindow.destroy()
    chatting()


mainWindow = Tk()
mainWindow.geometry("500x500")
mainWindow.title("Chatbot")
mainWindow["background"] = "#5BC8AF"
ele = Label(mainWindow, text="Welcome to the chatbot!")
ele.pack()

ele = Button(text="Start Chatting",
    width=20,
    height=2,
    bg="#F18D9E",
    fg="white",
    command=closeWindow)
ele.pack()
mainWindow.mainloop()
