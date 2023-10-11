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
        res=mycursor.execute(sql)
        for i in res:
            if(i[0]==u and i[1]==p):
                self.l3['text']="Login Successful"
            else:
                self.l3['text']="Login Failed"
    def clear(self):
        self.t1.delete(0)
        self.t2.delete(0)
        del self.l3['text']

window=Tk()
w=sample(window)
window.title("Login Page")
window.mainloop()