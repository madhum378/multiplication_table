from tkinter import *
import time
root=Tk()
root.title('tables')
n=int(input("please ENTER TABLE NUMBER:"))
def tab():
    for i in range(1,6):
        #s1=(n,"*",i,"=",n*i,'\n')
        s1=[(n,"*",i,"=",n*i,'\n') for i in range(1,11)]# , if i=='{' print('.') ]
        print()
        label.config(text=s1)
      
            

        
#widget=Label(root,text="hello")
widget1=Label(root,text="Thank you",font="Times 32",fg='green')
    
    
label=Label(root,font=("ds-digital",40),background="black",foreground="cyan")
label.pack(anchor="center")
#widget.pack(expand=YES,fill=BOTH)
widget1.pack(expand=YES,fill=BOTH)
tab()
mainloop()
