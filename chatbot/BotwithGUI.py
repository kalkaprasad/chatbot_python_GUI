from tkinter import *
from rivescript import RiveScript
import os.path
import tkinter as tk
from tkinter import messagebox
file = os.path.dirname(__file__)
brain = os.path.join(file,'brain')
bot = RiveScript()
bot.load_directory(brain)
bot.sort_replies()
# while True:
#     msg = input(str('you> '))
#     if msg == 'q':
#         quit()
#     else:
#          print('Bot>'+bot.reply('localuser', msg))
#
main = Tk()
main.geometry("500x650")
main.title("MY CHAT BOT")
main.title("Shaheed Bhagat Singh State technical Campus B.tech CSE 2027-2021")
mycolor2 = '#40E0D0'  # or use hex if you prefer
p1 = tk.PhotoImage(file='sbsicon.png')
main.iconphoto(False, p1)
# Setting icon of master window

photoL = Label(main)
photoL.pack(pady=5)

def ask_from_bot():

    q = askquestion.get()
    if(askquestion.get()==""):
        messagebox.showerror("Please ask question","Write  your question")
        return  False

    answer_from_bot = bot.reply('localuser', str(q))
    msgs.insert(END, "you : " + q)
    print (type(answer_from_bot))
    msgs.insert(END, "bot : " + str(answer_from_bot))
    askquestion.delete(0, END)

    print("clicked")

frame = Frame(main)
sc = Scrollbar(frame)
msgs = Listbox(frame, width=80, height=15, yscrollcommand=sc.set)

sc.pack(side=RIGHT,fill=Y)
msgs.pack(side=LEFT, fill=BOTH, pady=10)
frame.pack()

#creating text field

askquestion = Entry(main, font=("Verdana",20))
askquestion.pack(fill=X, pady=10)

# replyq = Entry(main, font=("Verdana",20))
# replyq.pack(fill=X, pady=10)

btn = Button(main, text="Ask from bot",font=("Verdana",20),command=ask_from_bot)
btn.pack()

#creating a function
def enter_function(event):
    btn.invoke()

main.bind('<Return>' , enter_function)
main.mainloop()

