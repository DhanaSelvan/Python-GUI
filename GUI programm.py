#...package importing.
from tkinter import *
from PIL import Image, ImageTk

#...funtions....
def clear():

    e1.delete(0,'end')
    e2.delete(0,'end')

    if count > 0 :
        pho_label.destroy()
        fin_lab.destroy()
    else:
        pho_label.destroy()

    btn1['state'] = NORMAL

    return [True]

def info():

    global pho_label
    global fin_lab
    global count
    global img

    nam1,nam2 = e1.get(),e2.get()
    nam1,nam2 = nam1.lower(),nam2.lower()
    nam1,nam2 = nam1.replace(' ',''),nam2.replace(' ','')

    for i in nam1:
        for j in nam2:
            if i==j:
                nam1 = nam1.replace(i,'',1)
                nam2 = nam2.replace(j,'',1)
                break
            else:
                nam1,nam2 = nam1,nam2

    rem = nam1 + nam2
    count = len(rem)

    if count > 0:
        relation = ["Friends","Lovers","Affectionate","Marriage","Enemies","Sister"]

        a = len(relation)

        while len(relation)>1:

            c = count%len(relation)
            index = c-1                           

            if index>=0:
                left = relation[:index]
                right = relation[index+1:]
                relation = right + left

            else:
                relation = relation[:len(relation)-1]

        if relation[0]== "Friends":
            img1 = Image.open("1.jpg")
            re_img = img1.resize((225,125),Image.ANTIALIAS)
            img = ImageTk.PhotoImage(re_img)
            fin_lab = Label(win,text=relation[0],fg="#141414",border=0,font=('consolas',15),bg='#18c2e6')
            fin_lab.place(x=295,y=490)

        elif relation[0] == "Lovers":
            img1 = Image.open("2.jpg")
            re_img = img1.resize((225,125),Image.ANTIALIAS)
            img = ImageTk.PhotoImage(re_img)
            fin_lab = Label(win,text=relation[0],fg="#141414",border=0,font=('consolas',15),bg='#18c2e6')
            fin_lab.place(x=295,y=490)

        elif relation[0] == "Affectionate":
            img1 = Image.open("3.jpg")
            re_img = img1.resize((225,125),Image.ANTIALIAS)
            img = ImageTk.PhotoImage(re_img)
            fin_lab = Label(win,text=relation[0],fg="#141414",border=0,font=('consolas',15),bg='#18c2e6')
            fin_lab.place(x=295,y=490)

        elif relation[0] == "Marriage":
            img1 = Image.open("4.jpg")
            re_img = img1.resize((225,125),Image.ANTIALIAS)
            img = ImageTk.PhotoImage(re_img)
            fin_lab = Label(win,text=relation[0],fg="#141414",border=0,font=('consolas',15),bg='#18c2e6')
            fin_lab.place(x=295,y=490)

        elif relation[0] == "Enemies":
            img1 = Image.open("5.jpg")
            re_img = img1.resize((225,125),Image.ANTIALIAS)
            img = ImageTk.PhotoImage(re_img)
            fin_lab = Label(win,text='',fg="#141414",border=0,font=('consolas',15),bg='#18c2e6')
            fin_lab.place(x=295,y=490)

        else:
            img1 = Image.open("6.jpg")
            re_img = img1.resize((225,125),Image.ANTIALIAS)
            img = ImageTk.PhotoImage(re_img)
            fin_lab = Label(win,text='',fg="#141414",border=0,font=('consolas',15),bg='#18c2e6')
            fin_lab.place(x=295,y=490)
        
        pho_label = Label(win,image=img,border=0)
        pho_label.place(x=60,y=430)
        pho_label.config()

    else:
        pho_label = Label(win,text="!...Please enter other names...!",fg="#141414",border=0,font=('consolas',15),bg='#18c2e6')
        pho_label.place(x=65,y=460)
    
    btn1['state'] = DISABLED

    return 

#windows and widgets initialisation
win = Tk()
win.geometry('480x650')
win.title('FLAMES Game')
win.configure(bg="#73eafa")
win.overrideredirect(True)
win.resizable(0,0)

#widgets
Frame(win,width=380,height=550,bg='#18c2e6').place(x=50,y=50)

l1 = Label(win,text="FLAMES",fg="#68fcbc",border=0,font=('consolas',35,'bold'),bg='#18c2e6')
l1.place(x=155,y=65)

l2 = Label(win,text="Your name",fg="#141414",border=0,font=('consolas',15),bg='#18c2e6')
l2.place(x=80,y=150)

l3 = Label(win,text="Your crush's name",fg="#141414",border=0,font=('consolas',15),bg='#18c2e6')
l3.place(x=80,y=250)

l4 = Label(win,text="Relationship status",fg="#2f26ff",border=0,font=('consolas',17,'bold'),bg='#18c2e6')
l4.place(x=120,y=390)

e1 = Entry(win,width=27,border=0)
e1.config(font=('consolas',17),bg='white',fg='#fa7e5c')
e1.place(x=70,y=190)

e2 = Entry(win,width=27,border=0)
e2.config(font=('consolas',17),bg='white',fg='#fa7e5c')
e2.place(x=70,y=290)

btn1 = Button(win,text="Submit",command=info)
btn1.place(x=205,y=350)
btn2 = Button(win,text="Clear all",command=clear)
btn2.place(x=205,y=560)

exit = Button(win,text="Close window",bg="red",fg="#fff674",border=0,command=win.quit)
exit.configure(activebackground='#7383c8',activeforeground='white',pady=4,padx=10)
exit.place(x=188,y=615)

win.mainloop()