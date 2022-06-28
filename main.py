from tkinter import *




class GUI:
    def __init__(self):
        self.root = Tk()
        self.count = 0
        self.icon = PhotoImage(file="bitcoin.png")
              
    def click(self):
        self.count += 1
        print(self.count)

    def submit(self):
        content = self.entry.get()
        print(content)
    
    def delete(self):
        self.entry.delete(0, END)
        
    def backspace(self):
        self.entry.delete(len(self.entry.get())-1, END)
    
    def main(self):
        self.root.title("interactive_gui")
        self.root.iconphoto(True, self.icon)
        self.root.geometry("1280x720")  
        self.root.configure(background='black')
        textimage = PhotoImage(file='person.png')
        textimage = textimage.subsample(3,3)
        buttonimage = PhotoImage(file='like.png')
        buttonimage = buttonimage.subsample(20,20)
        self.label = Label(self.root, 
                    text="Homie, Welcome Back!", font=("Times New Roman", 35, 'bold'),
                    bg='black', fg='green',
                    border=10, relief='sunken',
                    image= textimage,
                    compound='bottom')
        self.click_button = Button(
                    self.root, 
                    text="click if \n you're \n bored af",
                    command=self.click,
                    font=("Times New Roman", 20, 'bold'),
                    bg='black', fg='green',
                    #border=10, relief='raised',
                    image=buttonimage,
                    compound='bottom',
                    activeforeground='green',
                    #activebackground='black'
        )
        self.submit_button = Button(
                    self.root,
                    text="Submit",
                    command=self.submit,
        )
        self.delete_button = Button(
                    self.root,
                    text="Delete",
                    command=self.delete,
        )
        self.backspace_button = Button(
                    self.root,
                    text="Backspace",
                    command=self.backspace,
        )
        self.entry = Entry(
                    self.root,
                    font=("Times New Roman", 20,),
                    bg='black', fg='green',
                    border=5, relief='sunken',
                    width=30,            
        )

        self.label.pack()
        self.click_button.place(x=100, y=100)
        self.submit_button.pack(side=RIGHT)
        self.delete_button.pack(side=RIGHT)
        self.backspace_button.pack(side=RIGHT)
        #self.entry.config(show='$')
        self.entry.pack(side=RIGHT)
        
        self.root.mainloop()




if __name__ == '__main__':    
    window = GUI()
    window.main()
    #run_time = time.process_time()
    #print(f"Program run time: {run_time}")