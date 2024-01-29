from tkinter import*
from PIL import Image,ImageTk
import speech_to_text
import action
import text_to_speech

root = Tk()
root.title("AI Assistant")
root.geometry("550x675")
root.resizable(False , False)
root.config(bg="pink")


def ask():
    bot_val=action.actions()
    if bot_val=="ok sir":
        root.destroy()

def send():
    print("send")

def Delete():
    print("delete")
#frame

frame=LabelFrame(root,padx=100,pady=7, borderwidth=3, relief="raised")
frame.config(bg="#6F8FAF")
frame.grid(row=0, column=1, padx=55 ,pady=10)

#textlevel
text_lable= Label(frame, text="AI ASSISTANT", font=("Comic Sans Ms",14,"bold"), bd="5")
text_lable.grid(row=0,column=0,padx=20,pady=10)

#image
image=ImageTk.PhotoImage(Image.open("image/aiii.png"))
image_label=Label(frame ,image=image)
image_label.grid(row=4,column=0,pady=20)


#adding some text
text=Text(root, font=('courier 10 bold'),bg="#6F8FAF")
text.grid(row=2,column=0)
text.place(x=75,y=300,width=375,height=100)

#entry
entry=Entry(root,justify=CENTER)
entry.place(x=75,y=420,width=375,height=30)


#button
Button1= Button(root, text="ASK",bg="#6F8FAF",pady=16,padx=40,borderwidth=3,relief=SOLID,command=ask)
Button1.place(x=70,y=575)
Button2= Button(root,text="SEND",bg="#6F8FAF",pady=16,padx=40,borderwidth=3,relief=SOLID,command=send)
Button2.place(x=400,y=575)
Button3= Button(root,text="DELETE",bg="#6F8FAF",pady=16,padx=40,borderwidth=3,relief=SOLID,command=Delete)
Button3.place(x=225,y=575)

root.mainloop()