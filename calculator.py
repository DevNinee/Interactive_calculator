from tkinter import *


# Build main screen

# Create a calculator class
class Calculator:


     # Create the _init_ method
     def __init__(self, master):
         """
           Method that initializes the object's attributes

         """  

         # Assign reference to the main window of the application
         self.master = master 
         
         #Add a name to the application
         master.title("Calculator")

        # Create a line where we display the equation
         self.equation = Entry(master, width=36, borderwidth=6)

        # Assign a  position for the equation line  in the main application window
         self.equation.grid(row=0, column=0, columnspan=4, padx=10, pady=10 )

        # Execute the .createButton() method
         self.createButton() 

     def createButton(self):
         """
         Method that  creates that butttons
         """  
         # Create each button object
         b0 = self.addButton(0)
         b1 = self.addButton(1)
         b2 = self.addButton(2)
         b3 = self.addButton(3)
         b4 = self.addButton(4)
         b5 = self.addButton(5)
         b6 = self.addButton(6)
         b7 = self.addButton(7)
         b8 = self.addButton(8)
         b9 = self.addButton(9)
         b_add = self.addButton('+')
         b_sub = self.addButton('-')
         b_mult = self.addButton('*')
         b_div = self.addButton('/')
         b_clear = self.addButton('c')
         b_equal  = self.addButton('=')


         # Arrange the buttons  into  rows
         row1 =  [b7,  b8,  b9,  b_add]
         row2 = [b4, b5,  b6, b_sub]
         row3 = [b1, b2, b3, b_mult]
         row4 = [b_clear, b0, b_equal,  b_div]

         # Assign each button to the  main screen of the application
         r = 1
         for row in [row1, row2, row3, row4]:
             c =  0
             for b in row:
                 b.grid(row=r, column=c, columnspan=1)
                 c += 1  
             r += 1

     def addButton(self, value):
        """
        Method that adds the buttons to the main  of  the application
        """   

        return Button(
            self.master, 
            text=value, 
            width=9,
            command=lambda: self.clickButton(str(value)))
                          
         
     def clickButton(self, value):
        """
        Method that adds actions to the buttons of the  calculator application
        """

        # Get the equation entered  by the user
        current_equation =  str(self.equation.get())

        # If a  user clicks  "c" , clear the  equation  line
        if value ==  "c":
            self.equation.delete(-1,END)

        # If a user clicks "=" compute the answer and display it in the equation line    
        elif value == "=":
             answer = str(eval(current_equation))
             self.equation.delete(-1, END)
             self.equation.insert(0, answer)


        # If user clicks any other button, add the value to the equation  line
        else:
            self.equation.delete(0, END)
            self.equation.insert(0,  current_equation + value)


if __name__ ==  "__main__":     
     
     # Create the main window of the application
    root = Tk()
    
    # Tell the calculator class to use this main window
    my_gui = Calculator(root)

    # Executable look on the application
    root.mainloop()


    
