#importing packages
from tkinter import *
from PIL import Image,ImageTk

#globaliziation
global lab_font

#function definition
def ui_11th():
    global eng_entry_11
    global maths_entry_11
    global phy_entry_11
    global che_entry_11
    global com_entry_11

    win.config(bg='#88a5d5')#ui_body_for_11th
    Frame(win,bg='#304070',height=80,width=480).grid(row=0,column=0)#header_for_11th_ui
    Frame(win,bg='#88a5d5',height=60,width=350).place(x=30,y=140)#for close name
    next.config(font=button_font,
                activeforeground='#fafafa',activebackground='grey',
                width=10,bg='#395a8e',command=ui_12th)#11th_ui_button

    #labels
    lab = Label(win,text="CBSE Marks Calculator",fg='#f1f2f6',bg='#304070',font=lab_font).place(x=95,y=25)
    det_11th = Label(win,text=' 11th marks details',bg='#88a5d5',font=('consolas',15,'bold')).place(x=119,y=100)
    lang1_11th = Label(win,text='English       ',bg='#88a5d5',font=('BatmanForeverAlternate',12)).place(x=30,y=190)
    lang2_11th = Label(win,text='Maths         ',bg='#88a5d5',font=('BatmanForeverAlternate',12)).place(x=30,y=265)
    phy_11th = Label(win,text='Phyics         ',bg='#88a5d5',font=('BatmanForeverAlternate',12)).place(x=30,y=335)
    che_11th = Label(win,text='Chemistry         ',bg='#88a5d5',font=('BatmanForeverAlternate',12)).place(x=30,y=405)
    com_11th = Label(win,text='Computer or bio         ',bg='#88a5d5',font=('BatmanForeverAlternate',12)).place(x=30,y=475)

    #entry for 11th
    eng_entry_11 = Entry(win,bg='#88a5d5',fg='#f1f2f6',font=('consolas',15,'bold'),border=0)
    eng_entry_11.place(x=30,y=220)
    maths_entry_11 = Entry(win,bg='#88a5d5',fg='#f1f2f6',font=('consolas',15,'bold'),border=0)
    maths_entry_11.place(x=30,y=295)
    phy_entry_11 = Entry(win,bg='#88a5d5',fg='#f1f2f6',font=('consolas',15,'bold'),border=0)
    phy_entry_11.place(x=30,y=365)
    che_entry_11 = Entry(win,bg='#88a5d5',fg='#f1f2f6',font=('consolas',15,'bold'),border=0)
    che_entry_11.place(x=30,y=435)
    com_entry_11 = Entry(win,bg='#88a5d5',fg='#f1f2f6',font=('consolas',15,'bold'),border=0)
    com_entry_11.place(x=30,y=505)

    return

def ui_12th():
    global eng_entry_12
    global maths_entry_12
    global phy_entry_12
    global che_entry_12
    global com_entry_12
    
    win.config(bg='#bf5af2')#ui_body_for_12th
    Frame(win,bg='#4b235e',height=80,width=480).grid(row=0,column=0)#header_for_12th_ui
    Frame(win,bg='#bf5af2',height=60,width=350).place(x=30,y=140)#for close name
    next.config(font=button_font,text='SUBMIT',
                activeforeground='#fafafa',activebackground='grey',
                width=10,bg='#7d3a9e',command=result)#12th_ui_button
    
    #labels
    lab = Label(win,text="CBSE Marks Calculator",fg='white',bg='#4b235e',font=lab_font).place(x=95,y=25)
    det_12th = Label(win,text=' 12th marks details',bg='#bf5af2',font=('consolas',15,'bold')).place(x=119,y=100)
    lang1_12th = Label(win,text='English       ',bg='#bf5af2',font=('BatmanForeverAlternate',12)).place(x=30,y=190)
    lang2_12th = Label(win,text='Maths         ',bg='#bf5af2',font=('BatmanForeverAlternate',12)).place(x=30,y=265)
    phy_12th = Label(win,text='Phyics         ',bg='#bf5af2',font=('BatmanForeverAlternate',12)).place(x=30,y=335)
    che_12th = Label(win,text='Chemistry         ',bg='#bf5af2',font=('BatmanForeverAlternate',12)).place(x=30,y=405)
    com_12th = Label(win,text='Computer or bio         ',bg='#bf5af2',font=('BatmanForeverAlternate',12)).place(x=30,y=475)

    #entry
    eng_entry_12 = Entry(win,bg='#bf5af2',fg='#f1f2f6',font=('consolas',15,'bold'),border=0)
    eng_entry_12.place(x=30,y=220)
    maths_entry_12 = Entry(win,bg='#bf5af2',fg='#f1f2f6',font=('consolas',15,'bold'),border=0)
    maths_entry_12.place(x=30,y=295)
    phy_entry_12 = Entry(win,bg='#bf5af2',fg='#f1f2f6',font=('consolas',15,'bold'),border=0)
    phy_entry_12.place(x=30,y=365)
    che_entry_12 = Entry(win,bg='#bf5af2',fg='#f1f2f6',font=('consolas',15,'bold'),border=0)
    che_entry_12.place(x=30,y=435)
    com_entry_12 = Entry(win,bg='#bf5af2',fg='#f1f2f6',font=('consolas',15,'bold'),border=0)
    com_entry_12.place(x=30,y=505)

    return

def result():
    global cbse_logo

    Frame(win,height=680,width=480,bg="#a6ebd8").place(x=0,y=0)#ui_body_for_result
    Frame(win,bg='#00bda7',height=80,width=480).grid(row=0,column=0)#header_for_result_ui

    #process
        #------- 10th Details -------
    name = name_entry.get() 
    lang1_10th, lang2_10th = lang1_entry.get(), lang2_entry.get()
    maths_10th, sci_10th, ss_10th = maths_entry.get(), sci_entry.get(), ss_entry.get()
    
    marks_10th = [lang1_10th,lang2_10th,maths_10th,sci_10th,ss_10th]
    
    first_mark = max(marks_10th)
    list1 = []
    for i in marks_10th:
        if i != first_mark:
            list1.append(i)
    second_mark = max(list1)
    list2 = []
    for j in list1:
        if j != second_mark:
            list2.append(j)
    third_mark = max(list2)
    tot = int(first_mark) + int(second_mark) + int(third_mark)
    avg = tot/3

    out_80 = avg*0.3
    out_70 = (avg*0.875)*0.3

        #------- 11th Details -------
    eng_11th, maths_11th = eng_entry_11.get(), maths_entry_11.get()
    phy_11th, che_11th, com_11th = phy_entry_11.get(), che_entry_11.get(), com_entry_11.get()

    tot_11th_eng, tot_11th_maths = int(eng_11th)*0.3, int(maths_11th)*0.3
    tot_11th_phy, tot_11th_che, tot_11th_com = int(phy_11th)*0.3, int(che_11th)*0.3, int(com_11th)*0.3

        #------- 12th Details -------
    eng_12th, maths_12th = eng_entry_12.get(), maths_entry_12.get()
    phy_12th, che_12th, com_12th = phy_entry_12.get(), che_entry_12.get(), com_entry_12.get()

    _40_12th_eng, _40_12th_maths = int(eng_12th)*0.4, int(maths_12th)*0.4
    _40_12th_phy, _40_12th_che, _40_12th_com = int(phy_12th)*0.4, int(che_12th)*0.4, int(com_12th)*0.4

    tot_12th_eng_80 = round(out_80 + tot_11th_eng + _40_12th_eng)
    tot_12th_mat_80 = round(out_80 + tot_11th_maths + _40_12th_maths)
    tot_12th_phy_70 = round(out_70 + tot_11th_phy + _40_12th_phy)
    tot_12th_che_70 = round(out_70 + tot_11th_che + _40_12th_che)
    tot_12th_com_70 = round(out_70 + tot_11th_com + _40_12th_com)

    tot_12th_eng_100 = round(out_80 + tot_11th_eng + _40_12th_eng + 20)
    tot_12th_mat_100 = round(out_80 + tot_11th_maths + _40_12th_maths + 20)
    tot_12th_phy_100 = round(out_70 + tot_11th_phy + _40_12th_phy + 30)
    tot_12th_che_100 = round(out_70 + tot_11th_che + _40_12th_che + 30)
    tot_12th_com_100 = round(out_70 + tot_11th_com + _40_12th_com + 30)

    total = tot_12th_eng_80 + tot_12th_mat_80 + tot_12th_phy_70 + tot_12th_che_70 + tot_12th_com_70 + 130

    #image
    cbse_open = Image.open('CBSE color.jpg')
    re_cbse = cbse_open.resize((120,120),Image.ANTIALIAS)
    cbse_logo = ImageTk.PhotoImage(re_cbse)

    #labels
    lab = Label(win,text="CBSE Marks Calculator",fg='white',bg='#00bda7',font=lab_font).place(x=95,y=25)
    cre_lab = Label(win,text='Created by: DhanaSelvan J U',bg='#a6ebd8',font=('times',12)).place(x=250,y=644)
    logo_lab = Label(win,image=cbse_logo,border=0)
    logo_lab.place(x=165,y=100)

    Label(win,text='-----------------------------------------------------------------------',bg='#a6ebd8',font=('times',13)).place(x=20,y=220)
    Label(win,text='Subject',bg='#a6ebd8',fg='#ff5d29',font=('consolas',12,'bold')).place(x=30,y=240)
    Label(win,text='Theory',bg='#a6ebd8',fg='#ff5d29',font=('consolas',12,'bold')).place(x=158,y=240)
    Label(win,text='Practical',bg='#a6ebd8',fg='#ff5d29',font=('consolas',12,'bold')).place(x=250,y=240)
    Label(win,text='Total',bg='#a6ebd8',fg='#ff5d29',font=('consolas',12,'bold')).place(x=369,y=240)
    Label(win,text='-----------------------------------------------------------------------',bg='#a6ebd8',font=('times',13)).place(x=20,y=260)

    eng_lab = Label(win,text='English',bg='#a6ebd8',font=('consolas',13,'bold'))
    eng_lab.place(x=40,y=280)
    maths_lab = Label(win,text='Maths',bg='#a6ebd8',font=('consolas',13,'bold'))
    maths_lab.place(x=40,y=320)
    phy_lab = Label(win,text='Phyics',bg='#a6ebd8',font=('consolas',13,'bold'))
    phy_lab.place(x=40,y=360)
    che_lab = Label(win,text='Chemistry',bg='#a6ebd8',font=('consolas',13,'bold'))
    che_lab.place(x=40,y=400)
    com_lab = Label(win,text='CS or Bio',bg='#a6ebd8',font=('consolas',13,'bold'))
    com_lab.place(x=40,y=440)
    Label(win,text='-----------------------------------------------------------------------',bg='#a6ebd8',font=('times',13)).place(x=20,y=500)
    total_lab = Label(win,text=str(total),bg='#a6ebd8',font=('consolas',12,'bold'))
    total_lab.place(x=375,y=480)
    Label(win,text='Total \t = ',bg='#a6ebd8',fg='#ff5d29',font=('consolas',12,'bold')).place(x=250,y=480)
    Label(win,text='-----------------------------------------------------------------------',bg='#a6ebd8',font=('times',13)).place(x=20,y=460)

    eng_par_lab = Label(win,text='20',bg='#a6ebd8',font=('consolas',13,'bold'))
    eng_par_lab.place(x=275,y=280)
    maths_par_lab = Label(win,text='20',bg='#a6ebd8',font=('consolas',13,'bold'))
    maths_par_lab.place(x=275,y=320)
    phy_par_lab = Label(win,text='30',bg='#a6ebd8',font=('consolas',13,'bold'))
    phy_par_lab.place(x=275,y=360)
    che_par_lab = Label(win,text='30',bg='#a6ebd8',font=('consolas',13,'bold'))
    che_par_lab.place(x=275,y=400)
    com_par_lab = Label(win,text='30',bg='#a6ebd8',font=('consolas',13,'bold'))
    com_par_lab.place(x=275,y=440)

    eng_the_lab = Label(win,text=tot_12th_eng_80,bg='#a6ebd8',font=('consolas',13,'bold'))
    eng_the_lab.place(x=175,y=280)
    maths_the_lab = Label(win,text=tot_12th_mat_80,bg='#a6ebd8',font=('consolas',13,'bold'))
    maths_the_lab.place(x=175,y=320)
    phy_the_lab = Label(win,text=tot_12th_phy_70,bg='#a6ebd8',font=('consolas',13,'bold'))
    phy_the_lab.place(x=175,y=360)
    che_the_lab = Label(win,text=tot_12th_che_70,bg='#a6ebd8',font=('consolas',13,'bold'))
    che_the_lab.place(x=175,y=400)
    com_the_lab = Label(win,text=tot_12th_com_70,bg='#a6ebd8',font=('consolas',13,'bold'))
    com_the_lab.place(x=175,y=440)

    eng_the_lab = Label(win,text=tot_12th_eng_100,bg='#a6ebd8',font=('consolas',13,'bold'))
    eng_the_lab.place(x=385,y=280)
    maths_the_lab = Label(win,text=tot_12th_mat_100,bg='#a6ebd8',font=('consolas',13,'bold'))
    maths_the_lab.place(x=385,y=320)
    phy_the_lab = Label(win,text=tot_12th_phy_100,bg='#a6ebd8',font=('consolas',13,'bold'))
    phy_the_lab.place(x=385,y=360)
    che_the_lab = Label(win,text=tot_12th_che_100,bg='#a6ebd8',font=('consolas',13,'bold'))
    che_the_lab.place(x=385,y=400)
    com_the_lab = Label(win,text=tot_12th_com_100,bg='#a6ebd8',font=('consolas',13,'bold'))
    com_the_lab.place(x=385,y=440)

    Label(win,text=name + ' your total mark in \n 12th board exam is ' + str(total) + ' out of 500',bg='#a6ebd8',font=('minion pro',13,'bold')).place(x=90,y=550)


    return

#widgets 
win = Tk()
win.title(" CBSE mark calculation")  
win.geometry('480x680')
win.resizable(0,0)
win.iconbitmap('CBSE icon.ico')
win.config(bg='#e8e8e8')

#frames
Frame(win,bg='#20c659',height=80,width=480).grid(row=0,column=0)#header_for_10th_ui
Frame(win,bg="#3b3b3b",height=2,width=220).place(x=100,y=175)
Frame(win,bg="#3b3b3b",height=2,width=100).place(x=30,y=250)
Frame(win,bg="#3b3b3b",height=2,width=100).place(x=30,y=325)
Frame(win,bg="#3b3b3b",height=2,width=100).place(x=30,y=395)
Frame(win,bg="#3b3b3b",height=2,width=100).place(x=30,y=465)
Frame(win,bg="#3b3b3b",height=2,width=100).place(x=30,y=535)

#labels
lab_font = ('consolas',20,'bold')
lab = Label(win,text="CBSE Marks Calculator",fg='white',bg='#20c659',font=lab_font).place(x=95,y=25)

det_10th = Label(win,text=' 10th marks details',bg='#e8e8e8',fg='black',font=('consolas',15,'bold')).place(x=119,y=100)

name_lab = Label(win,text='Name',bg='#e8e8e8',fg='black',font=('BatmanForeverAlternate',12)).place(x=30,y=150)
lang1_10th_lab = Label(win,text='Language - 1',bg='#e8e8e8',fg='black',font=('BatmanForeverAlternate',12)).place(x=30,y=190)
lang2_10th_lab = Label(win,text='Language - 2',bg='#e8e8e8',fg='black',font=('BatmanForeverAlternate',12)).place(x=30,y=265)
maths_10th_lab = Label(win,text='Maths',bg='#e8e8e8',fg='black',font=('BatmanForeverAlternate',12)).place(x=30,y=335)
sci_10th_lab = Label(win,text='Science',bg='#e8e8e8',fg='black',font=('BatmanForeverAlternate',12)).place(x=30,y=405)
ss_10th_lab = Label(win,text='Social Science',bg='#e8e8e8',fg='black',font=('BatmanForeverAlternate',12)).place(x=30,y=475)

#entry box
name_entry = Entry(win,bg='#e8e8e8',fg='#ff5d29',font=('consolas',15,'bold'),border=0)
name_entry.place(x=100,y=147)
lang1_entry = Entry(win,bg='#e8e8e8',fg='#ff5d29',font=('consolas',15,'bold'),border=0)
lang1_entry.place(x=30,y=220)
lang2_entry = Entry(win,bg='#e8e8e8',fg='#ff5d29',font=('consolas',15,'bold'),border=0)
lang2_entry.place(x=30,y=295)
maths_entry = Entry(win,bg='#e8e8e8',fg='#ff5d29',font=('consolas',15,'bold'),border=0)
maths_entry.place(x=30,y=365)
sci_entry = Entry(win,bg='#e8e8e8',fg='#ff5d29',font=('consolas',15,'bold'),border=0)
sci_entry.place(x=30,y=435)
ss_entry = Entry(win,bg='#e8e8e8',fg='#ff5d29',font=('consolas',15,'bold'),border=0)
ss_entry.place(x=30,y=505)

#buttons_10th_ui
button_font = ('minion pro',15,'bold')
next = Button(win,text="NEXT",bg='#075e54',fg='#f2f2f2',command=ui_11th)
next.config(font=button_font,activeforeground='#fafafa',activebackground='grey',width=10)
next.place(x=180,y=620)

win.mainloop()