from tkinter import *




class GUI:
    def __init__(self):
        self.root = Tk()
        self.count = 0
        self.icon = PhotoImage(file="bitcoin.png")
        self.x = IntVar()
        self.food = ['pizza', 'burger', 'fries', 'steak']
        self.y = IntVar()
        pizza_image=PhotoImage(file='pizza.png')
        pizza_image = pizza_image.subsample(40,40)
        burger_image=PhotoImage(file='burger.png')
        burger_image = burger_image.subsample(40,40)
        fries_image=PhotoImage(file='fries.png')
        fries_image = fries_image.subsample(85,48)
        steak_image=PhotoImage(file='steak.png')
        steak_image=steak_image.subsample(40,30)
        
        
        self.food_image = [pizza_image, burger_image, fries_image, steak_image]



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

    def display(self):
        if self.x.get() == 1:
            print('I am glad that You are doing great! :)')
        else:
            print('I am sorry that you are not doing great:<')

    def display2(self):
        if self.y.get() == 0:
            print('You ordered the pizza :)')
        elif self.y.get() == 1:
            print('You ordered the burger :)')
        elif self.y.get() == 2:
            print('You ordered the fries :)')
        elif self.y.get() == 3:
            print('You ordered the steak :)')   
    
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
                    compound='bottom',
                    padx = 15, pady = 15)
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
        self.check_box = Checkbutton(
                    self.root,
                    text="Check me if you are doing great",
                    variable= self.x,
                    onvalue=1,
                    offvalue=0,
                    command=self.display,
                    font=("Arial", 20,),
                    bg='black', fg='green',
                    activebackground='black',
                    activeforeground='green',
                    padx=15, pady=12,
        )
        for i in range(len(self.food)):
            radio_button = Radiobutton(
                    self.root,
                    text=self.food[i],
                    fg='green', bg='black',
                    font=("Times New Roman", 20,),
                    variable= self.y,
                    value=i,
                    command=self.display2,
                    padx=10,
                    width=300,
                    indicatoron=0,
                    image=self.food_image[i],
                    compound='left',
            )
            radio_button.pack(anchor=W, side=BOTTOM)
        

        self.label.pack()
        self.click_button.place(x=100, y=100)
        self.submit_button.pack(side=RIGHT)
        self.delete_button.pack(side=RIGHT)
        self.backspace_button.pack(side=RIGHT)
        #self.entry.config(show='$')
        self.entry.pack(side=RIGHT)
        self.check_box.place(x=50, y=350)
        self.root.mainloop()




if __name__ == '__main__':    
    window = GUI()
    window.main()
    #run_time = time.process_time()
    #print(f"Program run time: {run_time}")