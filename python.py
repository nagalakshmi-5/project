from tkinter import *
import mysql.connector
mydb=mysql.connector.connect(
host="localhost",
user="root",
password="Chandana@123",
database="lucky"
)
mycursor=mydb.cursor()
class sample:
    def __init__(self,w):
        self.l1=Label(w,text="User Name")
        self.l2=Label(w,text="Password")
        self.l3=Label(w)
        self.t1=Entry()
        self.t2=Entry(show="*")
        self.l1.place(x=100,y=50)
        self.t1.place(x=200,y=50)
        self.l2.place(x=100,y=100)
        self.t2.place(x=200,y=100)
        self.b1=Button(w,text="Login",command=self.login)
        self.b2=Button(w,text="Clear",command=self.clear)
        self.b1.place(x=100,y=150)
        self.b2.place(x=200,y=150)
        self.l3.place(x=100,y=200)
    def login(self):
        u=self.t1.get()
        p=self.t2.get()
        sql="select * from passwords;"
        mycursor.execute(sql)
        res=mycursor.fetchall()
        mydb.commit()
        d=[]
        d1=[]
        c=0
        for i in res:
            d.append(i[0])
        for j in res:
            d1.append([j[1]])
        for k in range(len(d)):
            if(d[k]==u and d1[k][0]==p):
                c+=1
                self.l3['text']="Successful Login"
        if(c!=1):
            self.l3['text']="Login Failed.. Please Try Again."
    def clear(self):
        self.t1.delete(0,END)
        self.t2.delete(0,END)
        self.l3.config(text="")

window=Tk()
w=sample(window)
window.title("Login Page")
window.mainloop()