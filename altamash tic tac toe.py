import tkinter.messagebox
from tkinter import*

root=Tk()
root.geometry("1350x700")
root.title("ALTAMASH GAME")
root.configure(background="grey")

tops=Frame(root,bg="grey",pady=2,width=1350,height=100,relief=RIDGE)
tops.grid(row=0,column=0)

lbtitle=Label(tops,font=("arial",50,"bold"),text="ALTAMASH GAMES",bd=21,bg="dark grey",fg="black",justify=CENTER)
lbtitle.grid(row=0,column=0)


mainframe=Frame(root,bg="grey",pady=2,width=1350,height=600,relief=RIDGE)
mainframe.grid(row=1,column=0)

leftframe=Frame(mainframe,bd=10,width=750,height=500,pady=2,padx=10,bg="grey",relief=RIDGE)
leftframe.pack(side=LEFT)

rightframe=Frame(mainframe,bd=10,width=560,height=500,padx=10,pady=2,bg="dark grey",relief=RIDGE)
rightframe.pack(side=RIGHT)

rightframe1=Frame(rightframe,bd=10,width=560,height=200,padx=10,pady=2,bg="grey",relief=RIDGE)
rightframe1.grid(row=0,column=0)

rightframe2=Frame(rightframe,bd=10,width=560,height=200,padx=10,pady=2,bg="dark grey",relief=RIDGE)
rightframe2.grid(row=1,column=0)

playerX=IntVar()
player0=IntVar()

playerX.set(0)
player0.set(0)

button=StringVar()
click=True

def checker(buttons):
    global click
    if buttons["text"]=="" and click ==True:
        buttons["text"]="X"
        click=False
        scorekeeper()
    elif buttons["text"]=="" and click ==False:
        buttons["text"]="0"
        click=True
        scorekeeper()



def scorekeeper():
    if(button1["text"]=="X"and button2["text"]=="X" and button3["text"]=="X"):
        button1.configure(background="powder blue")
        button2.configure(background="powder blue")
        button3.configure(background="powder blue")
        n = float(playerX.get())
        score = ( n + 1 )
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X ","you won")

    if(button4["text"]=="X"and button5["text"]=="X" and button6["text"]=="X"):
        button4.configure(background="powder blue")
        button5.configure(background="powder blue")
        button6.configure(background="powder blue")
        n=float(playerX.get())
        score = ( n + 1 )
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X ","you won")

    if(button7["text"]=="X"and button8["text"]=="X" and button9["text"]=="X"):
        button7.configure(background="powder blue")
        button8.configure(background="powder blue")
        button9.configure(background="powder blue")
        n=float(playerX.get())
        score = ( n + 1 )
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X ","you won")


    if(button3["text"]=="X"and button5["text"]=="X" and button7["text"]=="X"):
        button3.configure(background="powder blue")
        button5.configure(background="powder blue")
        button7.configure(background="powder blue")
        n = float(playerX.get())
        score = ( n + 1 )
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X ","you won")

    if(button1["text"]=="X"and button5["text"]=="X" and button9["text"]=="X"):
        button1.configure(background="powder blue")
        button5.configure(background="powder blue")
        button9.configure(background="powder blue")
        n=float(playerX.get())
        score = ( n + 1 )
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X ","you won")

    if(button1["text"]=="X"and button4["text"]=="X" and button7["text"]=="X"):
        button1.configure(background="powder blue")
        button4.configure(background="powder blue")
        button7.configure(background="powder blue")
        n=float(playerX.get())
        score = ( n + 1 )
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X ","you won")   

    if(button2["text"]=="X"and button5["text"]=="X" and button8["text"]=="X"):
        button2.configure(background="powder blue")
        button5.configure(background="powder blue")
        button8.configure(background="powder blue")
        n = float(playerX.get())
        score = ( n + 1 )
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X ","you won")

    if(button3["text"]=="X"and button6["text"]=="X" and button9["text"]=="X"):
        button3.configure(background="powder blue")
        button6.configure(background="powder blue")
        button9.configure(background="powder blue")
        n=float(playerX.get())
        score = ( n + 1 )
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X ","you won")









        

    if(button1["text"]=="0"and button2["text"]=="0" and button3["text"]=="0"):
        button1.configure(background="powder blue")
        button2.configure(background="powder blue")
        button3.configure(background="powder blue")
        n=float(player0.get())
        score = ( n + 1 )
        player0.set(score)
        tkinter.messagebox.showinfo("Winner 0 ","you won")   


    if(button4["text"]=="0"and button5["text"]=="0" and button6["text"]=="0"):
        button4.configure(background="powder blue")
        button5.configure(background="powder blue")
        button6.configure(background="powder blue")
        n = float(player0.get())
        score = ( n + 1 )
        player0.set(score)
        tkinter.messagebox.showinfo("Winner 0 ","you won")

    if(button7["text"]=="0"and button8["text"]=="0" and button9["text"]=="0"):
        button7.configure(background="powder blue")
        button8.configure(background="powder blue")
        button9.configure(background="powder blue")
        n=float(player0.get())
        score = ( n + 1 )
        player0.set(score)
        tkinter.messagebox.showinfo("Winner 0","you won")

    if(button3["text"]=="0"and button5["text"]=="0" and button7["text"]=="0"):
        button3.configure(background="powder blue")
        button5.configure(background="powder blue")
        button7.configure(background="powder blue")
        n=float(player0.get())
        score = ( n + 1 )
        player0.set(score)
        tkinter.messagebox.showinfo("Winner 0 ","you won")



        
    if(button1["text"]=="0"and button5["text"]=="0" and button9["text"]=="0"):
        button1.configure(background="powder blue")
        button5.configure(background="powder blue")
        button9.configure(background="powder blue")
        n = float(player0.get())
        score = ( n + 1 )
        player0.set(score)
        tkinter.messagebox.showinfo("Winner 0 ","you won")

    if(button1["text"]=="0"and button4["text"]=="0" and button7["text"]=="0"):
        button1.configure(background="powder blue")
        button4.configure(background="powder blue")
        button7.configure(background="powder blue")
        n=float(player0.get())
        score = ( n + 1 )
        player0.set(score)
        tkinter.messagebox.showinfo("Winner 0","you won")

    if(button2["text"]=="0"and button5["text"]=="0" and button8["text"]=="0"):
        button2.configure(background="powder blue")
        button5.configure(background="powder blue")
        button8.configure(background="powder blue")
        n=float(player0.get())
        score = ( n + 1 )
        player0.set(score)
        tkinter.messagebox.showinfo("Winner 0 ","you won")

    if(button3["text"]=="0"and button6["text"]=="0" and button9["text"]=="0"):
        button3.configure(background="powder blue")
        button6.configure(background="powder blue")
        button9.configure(background="powder blue")
        n=float(player0.get())
        score = ( n + 1 )
        player0.set(score)
        tkinter.messagebox.showinfo("Winner 0 ","you won")   
                 
               
             
         

               
             
         



def reset():
    button1["text"]=""
    button2["text"]=""
    button3["text"]=""
    button4["text"]=""
    button5["text"]=""
    button6["text"]=""
    button7["text"]=""
    button8["text"]=""
    button9["text"]=""


    button1.configure(background="gainsboro")
    button2.configure(background="gainsboro")
    button3.configure(background="gainsboro")
    button4.configure(background="gainsboro")
    button5.configure(background="gainsboro")
    button6.configure(background="gainsboro")
    button7.configure(background="gainsboro")
    button8.configure(background="gainsboro")
    button9.configure(background="gainsboro")

    
def newgame():
    reset()
    playerX.set(0)
    player0.set(0)

lbplayerX=Label(rightframe1,font=("arial",40,"bold"),text="player X:",padx=2,pady=2,bg="grey")
lbplayerX.grid(row=0,column=0,sticky=W)

txtplayerX=Entry(rightframe1,font=("arial",40,"bold"),bd=2,fg="black",textvariable=playerX,width=14,justify=LEFT).grid(row=0,column=1)

lbplayer0=Label(rightframe1,font=("arial",40,"bold"),text="player 0:",padx=2,pady=2,bg="grey")
lbplayer0.grid(row=1,column=0,sticky=W)

txtplayer0=Entry(rightframe1,font=("arial",40,"bold"),bd=2,fg="black",textvariable=player0,width=14,justify=LEFT).grid(row=1,column=1)



btnreset=Button(rightframe2,text="RESET",font=("times 26 bold"),height=3,width=20,bg="gainsboro",command=reset)
btnreset.grid(row=0,column=0)

btnnewgame=Button(rightframe2,text="NEWGAME",font=("times 26 bold"),height=3,width=20,bg="gainsboro",command=newgame)
btnnewgame.grid(row=1,column=0)






button1=Button(leftframe,text="",font=("times 26 bold"),height=3,width=8,bg="gainsboro",command=lambda:checker(button1))
button1.grid(row=1,column=0,sticky=S+N+E+W)

button2=Button(leftframe,text="",font=("times 26 bold"),height=3,width=8,bg="gainsboro",command=lambda:checker(button2))
button2.grid(row=1,column=1,sticky=S+N+E+W)

button3=Button(leftframe,text="",font=("times 26 bold"),height=3,width=8,bg="gainsboro",command=lambda:checker(button3))
button3.grid(row=1,column=2,sticky=S+N+E+W)

button4=Button(leftframe,text="",font=("times 26 bold"),height=3,width=8,bg="gainsboro",command=lambda:checker(button4))
button4.grid(row=2,column=0,sticky=S+N+E+W)

button5=Button(leftframe,text="",font=("times 26 bold"),height=3,width=8,bg="gainsboro",command=lambda:checker(button5))
button5.grid(row=2,column=1,sticky=S+N+E+W)

button6=Button(leftframe,text="",font=("times 26 bold"),height=3,width=8,bg="gainsboro",command=lambda:checker(button6))
button6.grid(row=2,column=2,sticky=S+N+E+W)

button7=Button(leftframe,text="",font=("times 26 bold"),height=3,width=8,bg="gainsboro",command=lambda:checker(button7))
button7.grid(row=3,column=0,sticky=S+N+E+W)

button8=Button(leftframe,text="",font=("times 26 bold"),height=3,width=8,bg="gainsboro",command=lambda:checker(button8))
button8.grid(row=3,column=1,sticky=S+N+E+W)

button9=Button(leftframe,text="",font=("times 26 bold"),height=3,width=8,bg="gainsboro",command=lambda:checker(button9))
button9.grid(row=3,column=2,sticky=S+N+E+W) 


root.mainloop()
