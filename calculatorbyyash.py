# This line imports the tkinter module, which provides the functionality to create graphical user interfaces 
# (GUIs) in Python.
from tkinter import *
 #This function creates a new Frame object with a blue background and a border of size 4. It packs the frame 
 # onto the source widget using the specified side parameter, and then returns the frame.
def iCalc(source, side):
    storeObj = Frame(source, borderwidth=4, bd=4, bg="black")
    storeObj.pack(side=side, expand =YES, fill =BOTH)
    return storeObj
 #This function creates a new Button object with the specified text and command parameters 
 # (which can be a function or a lambda expression). 
 # It packs the button onto the source widget using the specified side parameter, and then returns the button.
def button(source, side, text, command=None):
    storeObj = Button(source, text=text, command=command)
    storeObj.pack(side=side, expand = YES, fill=BOTH)
    return storeObj
 #This class definition creates a new frame with a bold Arial font and packs it onto the root window. 
 # It also sets the title of the window to 'Calculator'.
class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'arial 20 bold')
        self.pack(expand = YES, fill =BOTH)
        self.master.title('Calculator')
 #This code creates a StringVar object to hold the text entered by the user. It then creates an Entry widget 
 # with the specified properties (relief, textvariable, justify, bd, and bg) and packs it onto the 
 # frame using the TOP parameter.
        display = StringVar()
        Entry(self, relief=RIDGE, textvariable=display,
          justify='right'
          , bd=30, bg="white").pack(side=TOP,
                                          expand=YES, fill=BOTH)
 #This code creates a "Clear" button by iterating over the list of characters ["C"], 
 # creating a frame for the button using iCalc(), and then creating a button inside that frame using button(). 
 # The button sets the value of the display variable to an empty string when clicked using a lambda expression.
        for clearButton in (["C"]):
            erase = iCalc(self, TOP)
            for ichar in clearButton:
                button(erase, LEFT, ichar, lambda
                    storeObj=display, q=ichar: storeObj.set(''))
 #This code creates the numeric buttons by iterating over a list of strings representing the rows of 
 # the buttons. For each row, it creates a new frame using iCalc(), and then creates buttons for each character 
 # in the row using button(). The buttons append the clicked character to the current value of 
 # display using a lambda expression.
        for numButton in ("789/", "456*", "123-", "0.+"):
         FunctionNum = iCalc(self, TOP)
         for iEquals in numButton:
            button(FunctionNum, LEFT, iEquals, lambda
                storeObj=display, q=iEquals: storeObj
                   .set(storeObj.get() + q))
 #This loop creates the equals button ("=") and binds the calc() function to the button's ButtonRelease-1 event.
 #  The calc() function evaluates the expression in the display string variable
        EqualButton = iCalc(self, TOP)
        for iEquals in "=":
            if iEquals == '=':
                btniEquals = button(EqualButton, LEFT, iEquals)
                btniEquals.bind('<ButtonRelease-1>', lambda e,s=self,
                                storeObj=display: s.calc(storeObj), '+')
 
 
            else:
                btniEquals = button(EqualButton, LEFT, iEquals,
                                    lambda storeObj=display, s=' %s ' % iEquals: storeObj.set
                                    (storeObj.get() + s))
 
    def calc(self, display):
            try:
                display.set(eval(display.get()))
            except:
                display.set("ERROR")
 
 
if __name__=='__main__':
 app().mainloop()