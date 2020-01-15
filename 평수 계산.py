import tkinter

window = tkinter.Tk()
window.title('평수 계산')

label1 = tkinter.Label(window, text='평수 계산').grid(row=0, column=0)
label2 = tkinter.Label(window, text='제곱 미터').grid(row=1, column=0)
label3 = tkinter.Label(window, text='평').grid(row=2, column=0)

entry1=tkinter.Entry(window)
entry1.grid(row=1,column=1)
entry2=tkinter.Entry(window)
entry2.grid(row=2,column=1)

def chg():
    sm = entry1.get()
    p=int(sm)*3/10
    entry2.delete(0,tkinter.END)
    entry2.insert(0,p)

button1=tkinter.Button(window,text='제곱미터 ▶ 평',command=chg).grid(row=3,column=1)
