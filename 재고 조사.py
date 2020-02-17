from tkinter import *

class MyFrame(Frame):
    def __init__(self, master):
        Frame.__init__(self,master)

        label = Label(label, text="test")
        label.pack(side(LEFT))


def main():
    window= Tk()
    window.title("YUN DAE HEE")
    window.geometry("640x400+3190+640")
    myframe = Myframe(window)
    window.mainloop()
if __name__ == '__main__':
    main()


