from tkinter import *
#Entry widget which needs a special password 
#you need it to start the crypting 

#PASSWORD
#Enter password:
#entry
#sumbit button 
#check if entry == PASSWORD



#button to get back 
def back():
    #Delete everything on screen
    cryp_text.destroy()
    restart.destroy()
    encrypt_or_decrypt()

def encrypt_yes():
    global cryp_text, restart
    #Delete buttons and heading
    d.destroy()
    e.destroy()
    yes_or_no.destroy()
    #Get the Entry input
    text = StringVar(root)

    #encrypt the input with ascii code
    def encrypt():
        global cryp_text, restart
        get_letters = list(entry1.get())

        #changed to ascii code 
        x = [ord(character) + 4 for character in get_letters]
        #to test if the numbers are correct print(x)

        #print(x)
            
        #output the encrypted text 
        a = [chr(character) for character in x]
        
        #print the text normal to the user
        f = ""
        for i in a:
            f = f + i
        cryp_text = Label(root, text= f, font="Times 40 bold", bg="black", fg="white")
        cryp_text.pack(pady= 200)

    #Deletes the entry and sumbit and deploys a restart button
        entry1.destroy()
        submit.destroy()
        restart = Button(root, text="Restart", font="Times 20 bold", bg="black", fg="white", command= back)
        restart.pack(side= RIGHT, pady = 30, padx = 30)

    #Gui entry
    entry1 = Entry(root, font="Times 40 bold", bg="black", fg="white", textvariable = text)
    entry1.pack(pady= 40)
    #Gui submit button to check answer
    submit = Button(root, text="Submit",font="Times 20 bold", bg="black", fg="white", command= encrypt)
    submit.configure(borderwidth= 5)
    submit.pack()
    


def decrypt_yes():
    global cryp_text, restart
    d.destroy()
    e.destroy()
    yes_or_no.destroy()

    text = StringVar(root)

    def decrypt():
        global cryp_text, restart 
        get_letters = list(entry1.get())
        #text in ascii code 
        x = [ord(character) - 4 for character in get_letters ]

        #prints the crypted text on the screen
        b = [chr(character) for character in x]
        
        s = ""
        for i in b:
            s = s + i
        
        cryp_text = Label(root, text= s, font="Times 40 bold", bg="black", fg="white")
        cryp_text.pack(pady= 200)

        #Delets the entry and sumbit and deploys a restart button 
        entry1.destroy()
        submit.destroy()
        restart = Button(root, text="Restart", font="Times 20 bold", bg="black", fg="white", command= back)
        restart.pack(side= RIGHT, pady = 30, padx = 30)

    entry1 = Entry(root, font="Times 40 bold", bg="black", fg="white", textvariable = text)
    entry1.pack(pady= 40)
    #Gui submit button to check answer
    submit = Button(root, text="Submit",font="Times 25 bold", bg="black", fg="white", command= decrypt)
    submit.configure(borderwidth= 5)
    submit.pack()

    
#do you want to encrypt or decrypt 
def encrypt_or_decrypt():
    global e, yes_or_no, encrypt_yes, d
    #question label
    yes_or_no = Label(root, text= "Encrypt or Decrypt?", font="Times 40 bold", bg="black", fg="white")
    yes_or_no.pack(pady= 70)

    #Button for encrypt
    e = Button(root, text = "Encrypt",font="Times 40 bold", bg="black", fg="white", command = encrypt_yes)
    e.pack(side = LEFT,padx = 120 )
    #Button for decrypt
    d = Button(root, text = "Decrypt",font="Times 40 bold", bg="black", fg="white", command = decrypt_yes)
    d.pack(side =LEFT, padx= 112)


#GUI
root = Tk()
root.title("Security")
#size
root.geometry("900x700")
#background
root.configure(bg = "black")
#user can´t change the window
root.resizable(height=FALSE, width = FALSE)

#Gui title
title = Label(root, text="Crypter--Crypt your informations", font="Times 40 bold underline", bg="black", fg="white")
title.pack()


encrypt_or_decrypt()

#runs the hole gui
root.mainloop()



