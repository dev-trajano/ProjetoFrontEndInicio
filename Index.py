#Importar as bibliotecas
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBaser
#Criar Nossa Janela

jan = Tk ()
jan.title ("JTA Systems - Acess Panel")
jan.geometry ("600x300")
jan.configure (background = "BLACK")
jan.resizable (width = False, height = False)
jan.attributes("-alpha", 0.9)
jan.iconbitmap(default = "icons/LogoIcon.ico") 
#=========== Carregando Imagens ==

logo = PhotoImage (file = "icons/logo.png")

#=========== Widgets =============

LefFrame = Frame (jan, width = 300, height = 300, bg = "Orange", relief = "raise")
LefFrame.pack (side = LEFT) 

RightFrame = Frame ( jan, width = 295, height = 300, bg = "Orange", relief = "raise")
RightFrame.pack (side = RIGHT)

LogoLabel = Label ( LefFrame, image = logo, bg = "Orange", relief = "raise")
LogoLabel.place (x = 10, y = 50)

UserLabel = Label ( RightFrame, text = "Username:", font = ("Century  Gothic", 13), bg ="Orange", fg = "BLACK")
UserLabel.place (x = 20, y = 70)

UserEntry = ttk.Entry (RightFrame, width = 30)
UserEntry.place (x = 105, y = 70)

PassLabel = Label (RightFrame, text = "password:", font = ("Century Gothic", 13),bg = "Orange", fg = "BLACK")
PassLabel.place (x = 20, y = 100)

PassEntry = ttk.Entry (RightFrame, width = 30, show = "*")
PassEntry.place ( x = 105, y = 100)

def Login():
    User = UserEntry.get()
    Pass = PassEntry.get()
    DataBaser.cursor.execute("""
    SELECT * FROM Users 
    WHERE User = ? and Password = ?
    """, (User, Pass))
    print ("Selecionou")
    VerifyLogin = DataBaser.cursor.fetchone()
    try:
        if (User in VerifyLogin and Pass in VerifyLogin):
            messagebox.showinfo(title = "Login", message = "Acesso Confirmado. Bem Vido!")
    except:
        messagebox.showinfo(title = "Login", message = "Acesso Negado. Verifique se Esta Cadrastado no Sistema!")

#======== Botoes =========

LoginButton = ttk.Button(RightFrame, text = "Login", width = 13, command = Login)
LoginButton.place (x = 190, y = 225)

def Register():
    #removendo windgets de login
    LoginButton.place(x = 5000)
    RegisterButton.place (x = 5000)
    
    #inserindo widgets de cadastro
    NomeLabel = Label (RightFrame, text = "Nome:", font= ("Century Gothic", 13), bg = "Orange", fg = "black")
    NomeLabel.place (x = 20, y = 10)

    NomeEntry = Entry(RightFrame, width = 30)
    NomeEntry.place(x = 75, y = 10)
    
    EmailLabel = Label (RightFrame, text = "Email:",font = ("Century githic",13), bg = "Orange",fg = "black")
    EmailLabel.place(x = 20 , y= 40)

    EmailEntry = Entry(RightFrame, width = 30)
    EmailEntry.place(x= 75 , y =40)

    def RegisterToDataBase():
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Pass = PassEntry.get()
        
        if(Name == "" and Email =="" and User == "" and Pass == ""):
            messagebox.showerror(title = "Register Erro", message = "Preencha Todos os Campos" ) 
        else:
            DataBaser.cursor.execute("""
            INSERT INTO Users (Name, Email, User, Password) VALUES(?, ?, ?, ?)
            """, (Name, Email, User, Pass))
            DataBaser.conn.commit()
            messagebox.showinfo(title = "Resister Info", message = "Conta Criada Com Sucesso")
        
    Register = ttk.Button(RightFrame, text ="Register", width = 13, command = RegisterToDataBase)
    Register.place( x = 190, y = 225)

    def BackToLogin():
        #Removendo Widgets de cadastro
        NomeLabel.place(x = 5000)
        NomeEntry.place(x = 5000)
        EmailLabel.place(x = 5000)
        EmailEntry.place(x = 5000)
        Register.place(x = 5000)
        Back.place(x = 5000)
        
        #Trasendo de volta Widgets
        LoginButton.place(x = 190)
        RegisterButton.place (x = 190, y = 265)

    Back = ttk.Button(RightFrame, text = "Back", width = 13, command = BackToLogin)
    Back.place(x = 190, y = 265)


RegisterButton = ttk.Button(RightFrame, text = "Register", width = 13, command = Register )
RegisterButton.place ( x = 190, y = 265)


jan.mainloop()
