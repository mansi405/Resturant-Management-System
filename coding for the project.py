from tkinter import *
from tkinter import messagebox
master=Tk()

my_label=Label(master,text="WELCOME TO OUR RESTAURANT!",fg="black",bg="orange",pady=5)
my_label.pack()

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="mansi.goyal")
mycursor=mydb.cursor()
mycursor.execute("create database if not exists food_resto")
mydb=mysql.connector.connect(host="localhost",user="root",password="mansi.goyal",database="food_resto")
mycursor1=mydb.cursor()
mycursor2=mydb.cursor()
mycursor1.execute("create table if not exists customer(email_id char(30), name char(20), mobile_number bigint)")
mycursor2.execute("create table if not exists orders(email_id char(30), item_ordered char(50))")

e=StringVar()
e1=StringVar()
e2=IntVar()
e3=StringVar()
ebox = Entry()
e1box = Entry()
e2box = Entry()
e3box = Entry()

def registration():
    top = Toplevel()
    top.configure(bg="lightblue")
    top.geometry("900x700")
    top.title("REGISTRATION")
    
    my_label1=Label(top,text="ENTER YOUR EMAIL ID:",fg="black",bg="goldenrod",padx=107.4,pady=10)
    my_label1.grid(row=0,column=0)

    ebox=Entry(top,textvariable=e,width=40)
    ebox.grid(row=0,column=1)
        
    my_label2=Label(top,text="ENTER YOUR FULL NAME:",bg="goldenrod",padx=100,pady=10).grid(row=1,column=0)
    
    e1box=Entry(top,textvariable=e1,width=40)
    e1box.grid(row=1,column=1)
    
    my_label3=Label(top,text="ENTER YOUR MOBILE NUMBER:",bg="goldenrod",padx=85,pady=10).grid(row=2,column=0)
    
    e2box=Entry(top,textvariable=e2,width=40)
    e2box.grid(row=2,column=1)
    
    button1=Button(top,text="NEXT",bg="white",command=next1)
    button1.grid(row=6,column=1)
    
button=Button(master,text="REGISTRATION",bg="lightblue",command=registration)
button.pack()

def exit_program():
    exit()
button_exit_program=Button(master,text="EXIT",bg="lightblue",command=exit_program)
button_exit_program.pack()


def next1():
    mycursor=mydb.cursor()
    mycursor.execute("INSERT INTO customer VALUES('"+e.get()+"','"+ e1.get() +"',"+str(e2.get())+ ")")
    mydb.commit()

    top = Toplevel()
    top.configure(bg="pink")
    top.geometry("500x300")
    top.title("MENU")

    my_label4=Label(top,text="TODAY'S MENU",fg="black",bg="pink",padx=190,pady=35).grid(row=2,column=2)
    
    button1=Button(top,text="CHINESE",bg="pink",command=chinese,padx=5,pady=5)
    button1.grid(row=6,column=2)
    
    button2=Button(top,text="SOUTH INDIAN",bg="pink",command=south_indian,padx=5,pady=5)
    button2.grid(row=5,column=2)
    
    button3=Button(top,text="MUGHLAI",bg="pink",command=mughlai,padx=5,pady=5)
    button3.grid(row=7,column=2)
    
    button4=Button(top,text="ITALIAN",bg="pink",command=italian,padx=5,pady=5)
    button4.grid(row=9,column=2)
    
    button5=Button(top,text="DESSERTS",bg="pink",command=desserts,padx=5,pady=5)
    button5.grid(row=11,column=2)

    button6=Button(top,text="BEVERAGES",bg="pink",command=beverages,padx=5,pady=5)
    button6.grid(row=13,column=2)

    my_label6=Label(top,text="ENTER YOUR ORDER(ITEM,QUANTITY)",fg="black",bg="pink",padx=200,pady=35).grid(row=15,column=2)

    e3box=Entry(top,textvariable=e3,width=50)
    e3box.grid(row=15,column=3)

    button7=Button(top,text="SUBMIT",bg="lightblue",command=submit,padx=10,pady=10)
    button7.grid(row=16,column=2)

    button8=Button(top,text="UPDATE",bg="lightblue",command=update,padx=10,pady=10)
    button8.grid(row=16,column=3)

    button9=Button(top,text="CANCEL",bg="lightblue",command=cancel,padx=10,pady=10)
    button9.grid(row=16,column=4)

def submit():
    mycursor=mydb.cursor()
    mycursor.execute("INSERT INTO orders VALUES('"+e.get()+"','"+ e3.get()+ "')")
    mydb.commit()
    messagebox.showinfo("Confirmation", "Your order for " + e3.get() + " is confirmed and will be delivered shortly.")

def update():
    mycursor=mydb.cursor()
    mycursor.execute("UPDATE orders SET item_ordered= '" + e3.get() + "' WHERE email_id = '" + e.get() + "'")
    mydb.commit()
    messagebox.showinfo("Confirmation", "Your order has been updated for " + e3.get() + " and will be delivered shortly.")

def cancel():
    mycursor=mydb.cursor()
    mycursor.execute("DELETE FROM orders WHERE email_id = '" + e.get() + "'")
    mydb.commit()
    messagebox.showinfo("Confirmation", "Your order for " + e3.get() + " has been cancelled.")

def chinese():
    top=Toplevel()
    top.configure(bg="Coral")
    top.geometry("500x300")
    top.title("CHINESE")

    my_label5=Label(top,text="NOODLES",bg="coral",padx=5,pady=5).grid(row=0,column=0)
    my_label6=Label(top,text="SPRING ROLL",bg="coral",padx=5,pady=5).grid(row=1,column=0)
    my_label7=Label(top,text="SOUP",bg="coral",padx=5,pady=5).grid(row=2,column=0)
    my_label8=Label(top,text="MANCHURIAN",bg="coral",padx=5,pady=5).grid(row=3,column=0)
    my_label9=Label(top,text="FRIED RICE",bg="coral",padx=5,pady=5).grid(row=4,column=0)

    my_label10=Label(top,text="RS. 250",bg="coral",padx=5,pady=5).grid(row=0,column=1)
    my_label11=Label(top,text="RS. 80",bg="coral",padx=5,pady=5).grid(row=1,column=1)
    my_label12=Label(top,text="RS. 120",bg="coral",padx=5,pady=5).grid(row=2,column=1)
    my_label13=Label(top,text="RS. 180",bg="coral",padx=5,pady=5).grid(row=3,column=1)
    my_label14=Label(top,text="RS. 170",bg="coral",padx=5,pady=5).grid(row=4,column=1)

    my_label15=Label(top,text="FULL PLATE",bg="coral",padx=5,pady=5).grid(row=0,column=2)
    my_label16=Label(top,text="6 PEICES",bg="coral",padx=5,pady=5).grid(row=1,column=2)
    my_label17=Label(top,bg="coral",padx=5,pady=5).grid(row=2,column=2)
    my_label18=Label(top,text="HALF PLATE",bg="coral",padx=5,pady=5).grid(row=3,column=2)
    my_label19=Label(top,text="HALF PLATE",bg="coral",padx=5,pady=5).grid(row=4,column=2)

def south_indian():
    top=Toplevel()
    top.configure(bg="Coral")
    top.geometry("500x300")
    top.title("SOUTH INDIAN")

    my_label5=Label(top,text="MASALA DOSA",bg="coral",padx=5,pady=5).grid(row=0,column=0)
    my_label6=Label(top,text="UTTAPAM",bg="coral",padx=5,pady=5).grid(row=1,column=0)
    my_label7=Label(top,text="IDLI SAMBAR",bg="coral",padx=5,pady=5).grid(row=2,column=0)
    my_label8=Label(top,text="VADA SAMBAR",bg="coral",padx=5,pady=5).grid(row=3,column=0)
    my_label9=Label(top,text="RICE",bg="coral",padx=5,pady=5).grid(row=4,column=0)

    my_label10=Label(top,text="RS. 180",bg="coral",padx=5,pady=5).grid(row=0,column=1)
    my_label11=Label(top,text="RS. 200",bg="coral",padx=5,pady=5).grid(row=1,column=1)
    my_label12=Label(top,text="RS. 160",bg="coral",padx=5,pady=5).grid(row=2,column=1)
    my_label13=Label(top,text="RS. 120",bg="coral",padx=5,pady=5).grid(row=3,column=1)
    my_label14=Label(top,text="RS. 150",bg="coral",padx=5,pady=5).grid(row=4,column=1)

    my_label15=Label(top,bg="coral",padx=5,pady=5).grid(row=0,column=2)
    my_label16=Label(top,bg="coral",padx=5,pady=5).grid(row=1,column=2)
    my_label17=Label(top,text="4 PEICES",bg="coral",padx=5,pady=5).grid(row=2,column=2)
    my_label18=Label(top,text="3 PEICES",bg="coral",padx=5,pady=5).grid(row=3,column=2)
    my_label19=Label(top,text="HALF PLATE",bg="coral",padx=5,pady=5).grid(row=4,column=2)
    

def mughlai():
    top=Toplevel()
    top.configure(bg="Coral")
    top.geometry("500x300")
    top.title("MUGHLAI")

    my_label5=Label(top,text="CHICKEN TIKKA",bg="coral",padx=5,pady=5).grid(row=0,column=0)
    my_label6=Label(top,text="BIRYANI",bg="coral",padx=5,pady=5).grid(row=1,column=0)
    my_label7=Label(top,text="BUTTER CHICKEN",bg="coral",padx=5,pady=5).grid(row=2,column=0)
    my_label8=Label(top,text="CHICKEN KORMA",bg="coral",padx=5,pady=5).grid(row=3,column=0)
    my_label9=Label(top,text="MUTTON SEEKH",bg="coral",padx=5,pady=5).grid(row=4,column=0)

    my_label10=Label(top,text="RS. 280",bg="coral",padx=5,pady=5).grid(row=0,column=1)
    my_label11=Label(top,text="RS. 140",bg="coral",padx=5,pady=5).grid(row=1,column=1)
    my_label12=Label(top,text="RS. 160",bg="coral",padx=5,pady=5).grid(row=2,column=1)
    my_label13=Label(top,text="RS. 150",bg="coral",padx=5,pady=5).grid(row=3,column=1)
    my_label14=Label(top,text="RS.  80",bg="coral",padx=5,pady=5).grid(row=4,column=1)

    my_label15=Label(top,text="6 PEICES",bg="coral",padx=5,pady=5).grid(row=0,column=2)
    my_label16=Label(top,text="FULL PLATE",bg="coral",padx=5,pady=5).grid(row=1,column=2)
    my_label17=Label(top,text="FULL PLATE",bg="coral",padx=5,pady=5).grid(row=2,column=2)
    my_label18=Label(top,text="FULL PLTATE",bg="coral",padx=5,pady=5).grid(row=3,column=2)
    my_label19=Label(top,text="2 PEICES",bg="coral",padx=5,pady=5).grid(row=4,column=2)
    
    
def italian():
    top=Toplevel()
    top.configure(bg="Coral")
    top.geometry("500x300")
    top.title("ITALAIAN")

    my_label5=Label(top,text="SPAGHETTI",bg="coral",padx=5,pady=5).grid(row=0,column=0)
    my_label6=Label(top,text="BURGER",bg="coral",padx=5,pady=5).grid(row=1,column=0)
    my_label7=Label(top,text="PIZZA",bg="coral",padx=5,pady=5).grid(row=2,column=0)
    my_label8=Label(top,text="SALSA",bg="coral",padx=5,pady=5).grid(row=3,column=0)
    my_label9=Label(top,text="SOUP",bg="coral",padx=5,pady=5).grid(row=4,column=0)

    my_label10=Label(top,text="RS. 240",bg="coral",padx=5,pady=5).grid(row=0,column=1)
    my_label11=Label(top,text="RS. 50",bg="coral",padx=5,pady=5).grid(row=1,column=1)
    my_label12=Label(top,text="RS. 260",bg="coral",padx=5,pady=5).grid(row=2,column=1)
    my_label13=Label(top,text="RS. 180",bg="coral",padx=5,pady=5).grid(row=3,column=1)
    my_label14=Label(top,text="RS. 140",bg="coral",padx=5,pady=5).grid(row=4,column=1)

    my_label15=Label(top,text="FULL PLATE",bg="coral",padx=5,pady=5).grid(row=0,column=2)
    my_label16=Label(top,bg="coral",padx=5,pady=5).grid(row=1,column=2)
    my_label17=Label(top,text="8 INCHES",bg="coral",padx=5,pady=5).grid(row=2,column=2)
    my_label18=Label(top,bg="coral",padx=5,pady=5).grid(row=3,column=2)
    my_label19=Label(top,bg="coral",padx=5,pady=5).grid(row=4,column=2)

def desserts():
    top=Toplevel()
    top.configure(bg="Coral")
    top.geometry("500x300")
    top.title("DESSERTS")

    my_label5=Label(top,text="PANCAKES",bg="coral",padx=5,pady=5).grid(row=0,column=0)
    my_label6=Label(top,text="WAFFLES",bg="coral",padx=5,pady=5).grid(row=1,column=0)
    my_label7=Label(top,text="PASTERIES",bg="coral",padx=5,pady=5).grid(row=2,column=0)
    my_label8=Label(top,text="ICE CREAM",bg="coral",padx=5,pady=5).grid(row=3,column=0)
    my_label9=Label(top,text="SWEETS",bg="coral",padx=5,pady=5).grid(row=4,column=0)

    my_label10=Label(top,text="RS. 120",bg="coral",padx=5,pady=5).grid(row=0,column=1)
    my_label11=Label(top,text="RS. 120",bg="coral",padx=5,pady=5).grid(row=1,column=1)
    my_label12=Label(top,text="RS. 120",bg="coral",padx=5,pady=5).grid(row=2,column=1)
    my_label13=Label(top,text="RS. 150",bg="coral",padx=5,pady=5).grid(row=3,column=1)
    my_label14=Label(top,text="RS. 200",bg="coral",padx=5,pady=5).grid(row=4,column=1)

def beverages():
    top=Toplevel()
    top.configure(bg="Coral")
    top.geometry("500x300")
    top.title("BEVERAGES")

    my_label5=Label(top,text="SHAKES",bg="coral",padx=5,pady=5).grid(row=0,column=0)
    my_label6=Label(top,text="SOFT DRINKS",bg="coral",padx=5,pady=5).grid(row=1,column=0)
    my_label7=Label(top,text="COCKTAILS",bg="coral",padx=5,pady=5).grid(row=2,column=0)
    my_label8=Label(top,text="TEA/COFFEE",bg="coral",padx=5,pady=5).grid(row=3,column=0)
    my_label9=Label(top,text="MINERAL WATER",bg="coral",padx=5,pady=5).grid(row=4,column=0)

    my_label10=Label(top,text="RS. 140",bg="coral",padx=5,pady=5).grid(row=0,column=1)
    my_label11=Label(top,text="RS. 80",bg="coral",padx=5,pady=5).grid(row=1,column=1)
    my_label12=Label(top,text="RS. 100",bg="coral",padx=5,pady=5).grid(row=2,column=1)
    my_label13=Label(top,text="RS. 60",bg="coral",padx=5,pady=5).grid(row=3,column=1)
    my_label14=Label(top,text="RS. 30",bg="coral",padx=5,pady=5).grid(row=4,column=1)

        





