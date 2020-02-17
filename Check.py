import tkinter as tk
from tkinter import filedialog
import pickle

frame = tk.Tk()
frame.title("표준PC 재고 수량")
frame.geometry("900x400+1000+641")
frame.resizable(False, False)
##############################################################
##############################################################
class Counter:
    def __init__(self):
        self.count = 0
    def countUp(self):
        if self.count >= 99:
            self.count = 99
        else:
            self.count += 1
        return self.count
    def countDown(self):
        if self.count > 0:
            self.count -= 1
        else:
            self.count = 0
        return self.count
    
MainLabel_Mainboard = tk.Label(frame, text = "Mainboard",anchor="w",relief="groove",width=55,padx=20,bg="white",fg="#BF00FF")
MainLabel_Mainboard.place(x=10,y=10)

MainLabel_VGA = tk.Label(frame, text = "VGA",anchor="w",relief="groove",width=55,padx=20,bg="white",fg="#BF00FF")
MainLabel_VGA.place(x=460,y=10)

MainLabel_SSD = tk.Label(frame, text = "SSD",anchor="w",relief="groove",width=55,padx=20,bg="white",fg="#BF00FF")
MainLabel_SSD.place(x=10,y=140)

MainLabel_Case = tk.Label(frame, text = "Case",anchor="w",relief="groove",width=55,padx=20,bg="white",fg="#BF00FF")
MainLabel_Case.place(x=460,y=140)

MainLabel_Power = tk.Label(frame, text = "Power",anchor="w",relief="groove",width=55,padx=20,bg="white",fg="#BF00FF")
MainLabel_Power.place(x=10,y=270)
############################################구분선#################################################
## 메인보드 제조사 입력 칸 ##
Sub_MbArr = []
for i in range(10):
    SubMbLabel = tk.Entry(frame , width=10)
    Sub_MbArr.insert(i, SubMbLabel)
    
Sub_MbArr[1].place(x=15,y=40)
Sub_MbArr[2].place(x=155,y=40)
Sub_MbArr[3].place(x=296,y=40)
Sub_MbArr[4].place(x=15,y=70)
Sub_MbArr[5].place(x=155,y=70)
Sub_MbArr[6].place(x=296,y=70)
Sub_MbArr[7].place(x=15,y=100)
Sub_MbArr[8].place(x=155,y=100)
Sub_MbArr[9].place(x=296,y=100)

StringVar_MB1 = tk.StringVar()
StringVar_MB2 = tk.StringVar()
StringVar_MB3 = tk.StringVar()
StringVar_MB4 = tk.StringVar()
StringVar_MB5 = tk.StringVar()
StringVar_MB6 = tk.StringVar()
StringVar_MB7 = tk.StringVar()
StringVar_MB8 = tk.StringVar()
StringVar_MB9 = tk.StringVar()

Sub_MbArr[1]["textvariable"] = StringVar_MB1
Sub_MbArr[2]["textvariable"] = StringVar_MB2
Sub_MbArr[3]["textvariable"] = StringVar_MB3
Sub_MbArr[4]["textvariable"] = StringVar_MB4
Sub_MbArr[5]["textvariable"] = StringVar_MB5
Sub_MbArr[6]["textvariable"] = StringVar_MB6
Sub_MbArr[7]["textvariable"] = StringVar_MB7
Sub_MbArr[8]["textvariable"] = StringVar_MB8
Sub_MbArr[9]["textvariable"] = StringVar_MB9

## 메인보드 카운트 ##
Cnt_MbArr = []
for i in range(10):
    CountMb_Cu = tk.Label(frame, text = "0",bg="black",fg="white",width=2)
    Cnt_MbArr.insert(i, CountMb_Cu)
    
Cnt_MbArr[1].place(x=90,y=40)
Cnt_MbArr[2].place(x=230,y=40)
Cnt_MbArr[3].place(x=372,y=40)
Cnt_MbArr[4].place(x=90,y=70)
Cnt_MbArr[5].place(x=230,y=70)
Cnt_MbArr[6].place(x=372,y=70)
Cnt_MbArr[7].place(x=90,y=100)
Cnt_MbArr[8].place(x=230,y=100)
Cnt_MbArr[9].place(x=372,y=100)


## 메인보드 카운트 오버라이딩 ##
CntOv_Mb1 = Counter()
CntOv_Mb2 = Counter()
CntOv_Mb3 = Counter()
CntOv_Mb4 = Counter()
CntOv_Mb5 = Counter()
CntOv_Mb6 = Counter()
CntOv_Mb7 = Counter()
CntOv_Mb8 = Counter()
CntOv_Mb9 = Counter()
## 메인보드 버튼 Up ##
MbButton1_Up = tk.Button(frame, overrelief="solid",text="▲" ,width=1,
                        command=lambda : Cnt_MbArr[1].config(text=str(CntOv_Mb1.countUp())), repeatdelay=1000, repeatinterval=100)
MbButton2_Up = tk.Button(frame, overrelief="solid",text="▲" ,width=1,
                       command=lambda : Cnt_MbArr[2].config(text=str(CntOv_Mb2.countUp())), repeatdelay=1000, repeatinterval=100)
MbButton3_Up = tk.Button(frame, overrelief="solid",text="▲" ,width=1,
                       command=lambda : Cnt_MbArr[3].config(text=str(CntOv_Mb3.countUp())), repeatdelay=1000, repeatinterval=100)
MbButton4_Up = tk.Button(frame, overrelief="solid",text="▲" ,width=1,
                       command=lambda : Cnt_MbArr[4].config(text=str(CntOv_Mb4.countUp())), repeatdelay=1000, repeatinterval=100)
MbButton5_Up = tk.Button(frame, overrelief="solid",text="▲" ,width=1,
                       command=lambda : Cnt_MbArr[5].config(text=str(CntOv_Mb5.countUp())), repeatdelay=1000, repeatinterval=100)
MbButton6_Up = tk.Button(frame, overrelief="solid",text="▲" ,width=1,
                       command=lambda : Cnt_MbArr[6].config(text=str(CntOv_Mb6.countUp())), repeatdelay=1000, repeatinterval=100)
MbButton7_Up = tk.Button(frame, overrelief="solid",text="▲" ,width=1,
                       command=lambda : Cnt_MbArr[7].config(text=str(CntOv_Mb7.countUp())), repeatdelay=1000, repeatinterval=100)
MbButton8_Up = tk.Button(frame, overrelief="solid",text="▲" ,width=1,
                       command=lambda : Cnt_MbArr[8].config(text=str(CntOv_Mb8.countUp())), repeatdelay=1000, repeatinterval=100)
MbButton9_Up = tk.Button(frame, overrelief="solid",text="▲" ,width=1,
                       command=lambda : Cnt_MbArr[9].config(text=str(CntOv_Mb9.countUp())), repeatdelay=1000, repeatinterval=100)

MbButton1_Up.place(x=112,y=37)
MbButton2_Up.place(x=253,y=37)
MbButton3_Up.place(x=395,y=37)
MbButton4_Up.place(x=112,y=67)
MbButton5_Up.place(x=253,y=67)
MbButton6_Up.place(x=395,y=67)
MbButton7_Up.place(x=112,y=97)
MbButton8_Up.place(x=253,y=97)
MbButton9_Up.place(x=395,y=97)

## 메인보드 버튼 Down ##
MbButton1_Down = tk.Button(frame, overrelief="solid",text="▼" ,width=1,
                       command=lambda : Cnt_MbArr[1].config(text=str(CntOv_Mb1.countDown())), repeatdelay=1000, repeatinterval=100)
MbButton2_Down = tk.Button(frame, overrelief="solid",text="▼" ,width=1,
                       command=lambda : Cnt_MbArr[2].config(text=str(CntOv_Mb2.countDown())), repeatdelay=1000, repeatinterval=100)
MbButton3_Down = tk.Button(frame, overrelief="solid",text="▼" ,width=1,
                       command=lambda : Cnt_MbArr[3].config(text=str(CntOv_Mb3.countDown())), repeatdelay=1000, repeatinterval=100)
MbButton4_Down = tk.Button(frame, overrelief="solid",text="▼" ,width=1,
                       command=lambda : Cnt_MbArr[4].config(text=str(CntOv_Mb4.countDown())), repeatdelay=1000, repeatinterval=100)
MbButton5_Down = tk.Button(frame, overrelief="solid",text="▼" ,width=1,
                       command=lambda : Cnt_MbArr[5].config(text=str(CntOv_Mb5.countDown())), repeatdelay=1000, repeatinterval=100)
MbButton6_Down = tk.Button(frame, overrelief="solid",text="▼" ,width=1,
                       command=lambda : Cnt_MbArr[6].config(text=str(CntOv_Mb6.countDown())), repeatdelay=1000, repeatinterval=100)
MbButton7_Down = tk.Button(frame, overrelief="solid",text="▼" ,width=1,
                       command=lambda : Cnt_MbArr[7].config(text=str(CntOv_Mb7.countDown())), repeatdelay=1000, repeatinterval=100)
MbButton8_Down = tk.Button(frame, overrelief="solid",text="▼" ,width=1,
                       command=lambda : Cnt_MbArr[8].config(text=str(CntOv_Mb8.countDown())), repeatdelay=1000, repeatinterval=100)
MbButton9_Down = tk.Button(frame, overrelief="solid",text="▼" ,width=1,
                       command=lambda : Cnt_MbArr[9].config(text=str(CntOv_Mb9.countDown())), repeatdelay=1000, repeatinterval=100)

MbButton1_Down.place(x=132,y=37)
MbButton2_Down.place(x=273,y=37)
MbButton3_Down.place(x=415,y=37)
MbButton4_Down.place(x=132,y=67)
MbButton5_Down.place(x=273,y=67)
MbButton6_Down.place(x=415,y=67)
MbButton7_Down.place(x=132,y=97)
MbButton8_Down.place(x=273,y=97)
MbButton9_Down.place(x=415,y=97)
##########################################구분선########################################################
## VGA 제조사 입력 칸 ##
Sub_VgaArr = []
for i in range(10):
    SubVgaLabel = tk.Entry(frame , width=10)
    Sub_VgaArr.insert(i, SubVgaLabel)

Sub_VgaArr[1].place(x=465,y=40)
Sub_VgaArr[2].place(x=605,y=40)
Sub_VgaArr[3].place(x=746,y=40)
Sub_VgaArr[4].place(x=465,y=70)
Sub_VgaArr[5].place(x=605,y=70)
Sub_VgaArr[6].place(x=746,y=70)
Sub_VgaArr[7].place(x=465,y=100)
Sub_VgaArr[8].place(x=605,y=100)
Sub_VgaArr[9].place(x=746,y=100)

StringVar_Vga1 = tk.StringVar()
StringVar_Vga2 = tk.StringVar()
StringVar_Vga3 = tk.StringVar()
StringVar_Vga4 = tk.StringVar()
StringVar_Vga5 = tk.StringVar()
StringVar_Vga6 = tk.StringVar()
StringVar_Vga7 = tk.StringVar()
StringVar_Vga8 = tk.StringVar()
StringVar_Vga9 = tk.StringVar()

Sub_VgaArr[1]["textvariable"] = StringVar_Vga1
Sub_VgaArr[2]["textvariable"] = StringVar_Vga2
Sub_VgaArr[3]["textvariable"] = StringVar_Vga3
Sub_VgaArr[4]["textvariable"] = StringVar_Vga4
Sub_VgaArr[5]["textvariable"] = StringVar_Vga5
Sub_VgaArr[6]["textvariable"] = StringVar_Vga6
Sub_VgaArr[7]["textvariable"] = StringVar_Vga7
Sub_VgaArr[8]["textvariable"] = StringVar_Vga8
Sub_VgaArr[9]["textvariable"] = StringVar_Vga9

## VGA 카운트 ##
Cnt_VgaArr = []
for i in range(10):
    CountVga_Cu = tk.Label(frame, text = "0",bg="black",fg="white",width=2)
    Cnt_VgaArr.insert(i, CountVga_Cu)
    
Cnt_VgaArr[1].place(x=540,y=40)
Cnt_VgaArr[2].place(x=680,y=40)
Cnt_VgaArr[3].place(x=822,y=40)
Cnt_VgaArr[4].place(x=540,y=70)
Cnt_VgaArr[5].place(x=680,y=70)
Cnt_VgaArr[6].place(x=822,y=70)
Cnt_VgaArr[7].place(x=540,y=100)
Cnt_VgaArr[8].place(x=680,y=100)
Cnt_VgaArr[9].place(x=822,y=100)
## VGA 카운트 오버라이딩 ##
CntOv_Vga1 = Counter()
CntOv_Vga2 = Counter()
CntOv_Vga3 = Counter()
CntOv_Vga4 = Counter()
CntOv_Vga5 = Counter()
CntOv_Vga6 = Counter()
CntOv_Vga7 = Counter()
CntOv_Vga8 = Counter()
CntOv_Vga9 = Counter()
## VGA 버튼 Up ##
VgaButton1_Up = tk.Button(frame, overrelief="solid",text="▲" ,width=1,
                        command=lambda : Cnt_VgaArr[1].config(text=str(CntOv_Vga1.countUp())), repeatdelay=1000, repeatinterval=100)
VgaButton2_Up = tk.Button(frame, overrelief="solid",text="▲" ,width=1,
                       command=lambda : Cnt_VgaArr[2].config(text=str(CntOv_Vga2.countUp())), repeatdelay=1000, repeatinterval=100)
VgaButton3_Up = tk.Button(frame, overrelief="solid",text="▲" ,width=1,
                       command=lambda : Cnt_VgaArr[3].config(text=str(CntOv_Vga3.countUp())), repeatdelay=1000, repeatinterval=100)
VgaButton4_Up = tk.Button(frame, overrelief="solid",text="▲" ,width=1,
                       command=lambda : Cnt_VgaArr[4].config(text=str(CntOv_Vga4.countUp())), repeatdelay=1000, repeatinterval=100)
VgaButton5_Up = tk.Button(frame, overrelief="solid",text="▲" ,width=1,
                       command=lambda : Cnt_VgaArr[5].config(text=str(CntOv_Vga5.countUp())), repeatdelay=1000, repeatinterval=100)
VgaButton6_Up = tk.Button(frame, overrelief="solid",text="▲" ,width=1,
                       command=lambda : Cnt_VgaArr[6].config(text=str(CntOv_Vga6.countUp())), repeatdelay=1000, repeatinterval=100)
VgaButton7_Up = tk.Button(frame, overrelief="solid",text="▲" ,width=1,
                       command=lambda : Cnt_VgaArr[7].config(text=str(CntOv_Vga7.countUp())), repeatdelay=1000, repeatinterval=100)
VgaButton8_Up = tk.Button(frame, overrelief="solid",text="▲" ,width=1,
                       command=lambda : Cnt_VgaArr[8].config(text=str(CntOv_Vga8.countUp())), repeatdelay=1000, repeatinterval=100)
VgaButton9_Up = tk.Button(frame, overrelief="solid",text="▲" ,width=1,
                       command=lambda : Cnt_VgaArr[9].config(text=str(CntOv_Vga9.countUp())), repeatdelay=1000, repeatinterval=100)

VgaButton1_Up.place(x=562,y=37)
VgaButton2_Up.place(x=702,y=37)
VgaButton3_Up.place(x=845,y=37)
VgaButton4_Up.place(x=562,y=67)
VgaButton5_Up.place(x=702,y=67)
VgaButton6_Up.place(x=845,y=67)
VgaButton7_Up.place(x=562,y=97)
VgaButton8_Up.place(x=702,y=97)
VgaButton9_Up.place(x=845,y=97)

## VGA 버튼 Down ##
VgaButton1_Down = tk.Button(frame, overrelief="solid",text="▼" ,width=1,
                       command=lambda : Cnt_VgaArr[1].config(text=str(CntOv_Vga1.countDown())), repeatdelay=1000, repeatinterval=100)
VgaButton2_Down = tk.Button(frame, overrelief="solid",text="▼" ,width=1,
                       command=lambda : Cnt_VgaArr[2].config(text=str(CntOv_Vga2.countDown())), repeatdelay=1000, repeatinterval=100)
VgaButton3_Down = tk.Button(frame, overrelief="solid",text="▼" ,width=1,
                       command=lambda : Cnt_VgaArr[3].config(text=str(CntOv_Vga3.countDown())), repeatdelay=1000, repeatinterval=100)
VgaButton4_Down = tk.Button(frame, overrelief="solid",text="▼" ,width=1,
                       command=lambda : Cnt_VgaArr[4].config(text=str(CntOv_Vga4.countDown())), repeatdelay=1000, repeatinterval=100)
VgaButton5_Down = tk.Button(frame, overrelief="solid",text="▼" ,width=1,
                       command=lambda : Cnt_VgaArr[5].config(text=str(CntOv_Vga5.countDown())), repeatdelay=1000, repeatinterval=100)
VgaButton6_Down = tk.Button(frame, overrelief="solid",text="▼" ,width=1,
                       command=lambda : Cnt_VgaArr[6].config(text=str(CntOv_Vga6.countDown())), repeatdelay=1000, repeatinterval=100)
VgaButton7_Down = tk.Button(frame, overrelief="solid",text="▼" ,width=1,
                       command=lambda : Cnt_VgaArr[7].config(text=str(CntOv_Vga7.countDown())), repeatdelay=1000, repeatinterval=100)
VgaButton8_Down = tk.Button(frame, overrelief="solid",text="▼" ,width=1,
                       command=lambda : Cnt_VgaArr[8].config(text=str(CntOv_Vga8.countDown())), repeatdelay=1000, repeatinterval=100)
VgaButton9_Down = tk.Button(frame, overrelief="solid",text="▼" ,width=1,
                       command=lambda : Cnt_VgaArr[9].config(text=str(CntOv_Vga9.countDown())), repeatdelay=1000, repeatinterval=100)

VgaButton1_Down.place(x=582,y=37)
VgaButton2_Down.place(x=722,y=37)
VgaButton3_Down.place(x=865,y=37)
VgaButton4_Down.place(x=582,y=67)
VgaButton5_Down.place(x=722,y=67)
VgaButton6_Down.place(x=865,y=67)
VgaButton7_Down.place(x=582,y=97)
VgaButton8_Down.place(x=722,y=97)
VgaButton9_Down.place(x=865,y=97)
########################################################구분선##################################################
## SSD 제조사 입력 칸 ##
Sub_SsdArr = []
for i in range(10):
    SubSsdLabel = tk.Entry(frame , width=10)
    Sub_SsdArr.insert(i, SubSsdLabel)

Sub_SsdArr[1].place(x=15,y=170)
Sub_SsdArr[2].place(x=155,y=170)
Sub_SsdArr[3].place(x=296,y=170)
Sub_SsdArr[4].place(x=15,y=200)
Sub_SsdArr[5].place(x=155,y=200)
Sub_SsdArr[6].place(x=296,y=200)
Sub_SsdArr[7].place(x=15,y=230)
Sub_SsdArr[8].place(x=155,y=230)
Sub_SsdArr[9].place(x=296,y=230)

StringVar_Ssd1 = tk.StringVar()
StringVar_Ssd2 = tk.StringVar()
StringVar_Ssd3 = tk.StringVar()
StringVar_Ssd4 = tk.StringVar()
StringVar_Ssd5 = tk.StringVar()
StringVar_Ssd6 = tk.StringVar()
StringVar_Ssd7 = tk.StringVar()
StringVar_Ssd8 = tk.StringVar()
StringVar_Ssd9 = tk.StringVar()

Sub_SsdArr[1]["textvariable"] = StringVar_Ssd1
Sub_SsdArr[2]["textvariable"] = StringVar_Ssd2
Sub_SsdArr[3]["textvariable"] = StringVar_Ssd3
Sub_SsdArr[4]["textvariable"] = StringVar_Ssd4
Sub_SsdArr[5]["textvariable"] = StringVar_Ssd5
Sub_SsdArr[6]["textvariable"] = StringVar_Ssd6
Sub_SsdArr[7]["textvariable"] = StringVar_Ssd7
Sub_SsdArr[8]["textvariable"] = StringVar_Ssd8
Sub_SsdArr[9]["textvariable"] = StringVar_Ssd9

## SSD 카운트 ##
Cnt_SsdArr = []
for i in range(10):
    CountSsd_Cu = tk.Label(frame, text = "0",bg="black",fg="white",width=2)
    Cnt_SsdArr.insert(i, CountSsd_Cu)
    
Cnt_SsdArr[1].place(x=90,y=170)
Cnt_SsdArr[2].place(x=230,y=170)
Cnt_SsdArr[3].place(x=372,y=170)
Cnt_SsdArr[4].place(x=90,y=200)
Cnt_SsdArr[5].place(x=230,y=200)
Cnt_SsdArr[6].place(x=372,y=200)
Cnt_SsdArr[7].place(x=90,y=230)
Cnt_SsdArr[8].place(x=230,y=230)
Cnt_SsdArr[9].place(x=372,y=230)
## SSD 카운트 오버라이딩 ##
CntOv_Ssd1 = Counter()
CntOv_Ssd2 = Counter()
CntOv_Ssd3 = Counter()
CntOv_Ssd4 = Counter()
CntOv_Ssd5 = Counter()
CntOv_Ssd6 = Counter()
CntOv_Ssd7 = Counter()
CntOv_Ssd8 = Counter()
CntOv_Ssd9 = Counter()
## SSD 버튼 Up ##
SsdButton1_Up = tk.Button(frame, overrelief="solid",text="▲" ,width=1,
                        command=lambda : Cnt_SsdArr[1].config(text=str(CntOv_Ssd1.countUp())), repeatdelay=1000, repeatinterval=100)
SsdButton2_Up = tk.Button(frame, overrelief="solid",text="▲" ,width=1,
                       command=lambda : Cnt_SsdArr[2].config(text=str(CntOv_Ssd2.countUp())), repeatdelay=1000, repeatinterval=100)
SsdButton3_Up = tk.Button(frame, overrelief="solid",text="▲" ,width=1,
                       command=lambda : Cnt_SsdArr[3].config(text=str(CntOv_Ssd3.countUp())), repeatdelay=1000, repeatinterval=100)
SsdButton4_Up = tk.Button(frame, overrelief="solid",text="▲" ,width=1,
                       command=lambda : Cnt_SsdArr[4].config(text=str(CntOv_Ssd4.countUp())), repeatdelay=1000, repeatinterval=100)
SsdButton5_Up = tk.Button(frame, overrelief="solid",text="▲" ,width=1,
                       command=lambda : Cnt_SsdArr[5].config(text=str(CntOv_Ssd5.countUp())), repeatdelay=1000, repeatinterval=100)
SsdButton6_Up = tk.Button(frame, overrelief="solid",text="▲" ,width=1,
                       command=lambda : Cnt_SsdArr[6].config(text=str(CntOv_Ssd6.countUp())), repeatdelay=1000, repeatinterval=100)
SsdButton7_Up = tk.Button(frame, overrelief="solid",text="▲" ,width=1,
                       command=lambda : Cnt_SsdArr[7].config(text=str(CntOv_Ssd7.countUp())), repeatdelay=1000, repeatinterval=100)
SsdButton8_Up = tk.Button(frame, overrelief="solid",text="▲" ,width=1,
                       command=lambda : Cnt_SsdArr[8].config(text=str(CntOv_Ssd8.countUp())), repeatdelay=1000, repeatinterval=100)
SsdButton9_Up = tk.Button(frame, overrelief="solid",text="▲" ,width=1,
                       command=lambda : Cnt_SsdArr[9].config(text=str(CntOv_Ssd9.countUp())), repeatdelay=1000, repeatinterval=100)

SsdButton1_Up.place(x=112,y=167)
SsdButton2_Up.place(x=253,y=167)
SsdButton3_Up.place(x=395,y=167)
SsdButton4_Up.place(x=112,y=197)
SsdButton5_Up.place(x=253,y=197)
SsdButton6_Up.place(x=395,y=197)
SsdButton7_Up.place(x=112,y=227)
SsdButton8_Up.place(x=253,y=227)
SsdButton9_Up.place(x=395,y=227)

## SSD 버튼 Down ##
SsdButton1_Down = tk.Button(frame, overrelief="solid",text="▼" ,width=1,
                       command=lambda : Cnt_SsdArr[1].config(text=str(CntOv_Ssd1.countDown())), repeatdelay=1000, repeatinterval=100)
SsdButton2_Down = tk.Button(frame, overrelief="solid",text="▼" ,width=1,
                       command=lambda : Cnt_SsdArr[2].config(text=str(CntOv_Ssd2.countDown())), repeatdelay=1000, repeatinterval=100)
SsdButton3_Down = tk.Button(frame, overrelief="solid",text="▼" ,width=1,
                       command=lambda : Cnt_SsdArr[3].config(text=str(CntOv_Ssd3.countDown())), repeatdelay=1000, repeatinterval=100)
SsdButton4_Down = tk.Button(frame, overrelief="solid",text="▼" ,width=1,
                       command=lambda : Cnt_SsdArr[4].config(text=str(CntOv_Ssd4.countDown())), repeatdelay=1000, repeatinterval=100)
SsdButton5_Down = tk.Button(frame, overrelief="solid",text="▼" ,width=1,
                       command=lambda : Cnt_SsdArr[5].config(text=str(CntOv_Ssd5.countDown())), repeatdelay=1000, repeatinterval=100)
SsdButton6_Down = tk.Button(frame, overrelief="solid",text="▼" ,width=1,
                       command=lambda : Cnt_SsdArr[6].config(text=str(CntOv_Ssd6.countDown())), repeatdelay=1000, repeatinterval=100)
SsdButton7_Down = tk.Button(frame, overrelief="solid",text="▼" ,width=1,
                       command=lambda : Cnt_SsdArr[7].config(text=str(CntOv_Ssd7.countDown())), repeatdelay=1000, repeatinterval=100)
SsdButton8_Down = tk.Button(frame, overrelief="solid",text="▼" ,width=1,
                       command=lambda : Cnt_SsdArr[8].config(text=str(CntOv_Ssd8.countDown())), repeatdelay=1000, repeatinterval=100)
SsdButton9_Down = tk.Button(frame, overrelief="solid",text="▼" ,width=1,
                       command=lambda : Cnt_SsdArr[9].config(text=str(CntOv_Ssd9.countDown())), repeatdelay=1000, repeatinterval=100)

SsdButton1_Down.place(x=132,y=167)
SsdButton2_Down.place(x=273,y=167)
SsdButton3_Down.place(x=415,y=167)
SsdButton4_Down.place(x=132,y=197)
SsdButton5_Down.place(x=273,y=197)
SsdButton6_Down.place(x=415,y=197)
SsdButton7_Down.place(x=132,y=227)
SsdButton8_Down.place(x=273,y=227)
SsdButton9_Down.place(x=415,y=227)
################################################구분선################################################
## CASE 제조사 입력 칸 ##
Sub_CaseArr = []
for i in range(10):
    SubCaseLabel = tk.Entry(frame , width=10)
    Sub_CaseArr.insert(i, SubCaseLabel)

Sub_CaseArr[1].place(x=465,y=170)
Sub_CaseArr[2].place(x=605,y=170)
Sub_CaseArr[3].place(x=746,y=170)
Sub_CaseArr[4].place(x=465,y=200)
Sub_CaseArr[5].place(x=605,y=200)
Sub_CaseArr[6].place(x=746,y=200)
Sub_CaseArr[7].place(x=465,y=230)
Sub_CaseArr[8].place(x=605,y=230)
Sub_CaseArr[9].place(x=746,y=230)

StringVar_Case1 = tk.StringVar()
StringVar_Case2 = tk.StringVar()
StringVar_Case3 = tk.StringVar()
StringVar_Case4 = tk.StringVar()
StringVar_Case5 = tk.StringVar()
StringVar_Case6 = tk.StringVar()
StringVar_Case7 = tk.StringVar()
StringVar_Case8 = tk.StringVar()
StringVar_Case9 = tk.StringVar()

Sub_CaseArr[1]["textvariable"] = StringVar_Case1
Sub_CaseArr[2]["textvariable"] = StringVar_Case2
Sub_CaseArr[3]["textvariable"] = StringVar_Case3
Sub_CaseArr[4]["textvariable"] = StringVar_Case4
Sub_CaseArr[5]["textvariable"] = StringVar_Case5
Sub_CaseArr[6]["textvariable"] = StringVar_Case6
Sub_CaseArr[7]["textvariable"] = StringVar_Case7
Sub_CaseArr[8]["textvariable"] = StringVar_Case8
Sub_CaseArr[9]["textvariable"] = StringVar_Case9

## CASE 카운트 ##
Cnt_CaseArr = []
for i in range(10):
    CountCase_Cu = tk.Label(frame, text = "0",bg="black",fg="white",width=2)
    Cnt_CaseArr.insert(i, CountCase_Cu)
    
Cnt_CaseArr[1].place(x=540,y=170)
Cnt_CaseArr[2].place(x=680,y=170)
Cnt_CaseArr[3].place(x=822,y=170)
Cnt_CaseArr[4].place(x=540,y=200)
Cnt_CaseArr[5].place(x=680,y=200)
Cnt_CaseArr[6].place(x=822,y=200)
Cnt_CaseArr[7].place(x=540,y=230)
Cnt_CaseArr[8].place(x=680,y=230)
Cnt_CaseArr[9].place(x=822,y=230)
## CASE 카운트 오버라이딩 ##
CntOv_Case1 = Counter()
CntOv_Case2 = Counter()
CntOv_Case3 = Counter()
CntOv_Case4 = Counter()
CntOv_Case5 = Counter()
CntOv_Case6 = Counter()
CntOv_Case7 = Counter()
CntOv_Case8 = Counter()
CntOv_Case9 = Counter()
## CASE 버튼 Up ##
CaseButton1_Up = tk.Button(frame, overrelief="solid",text="▲" ,width=1,
                        command=lambda : Cnt_CaseArr[1].config(text=str(CntOv_Case1.countUp())), repeatdelay=1000, repeatinterval=100)
CaseButton2_Up = tk.Button(frame, overrelief="solid",text="▲" ,width=1,
                       command=lambda : Cnt_CaseArr[2].config(text=str(CntOv_Case2.countUp())), repeatdelay=1000, repeatinterval=100)
CaseButton3_Up = tk.Button(frame, overrelief="solid",text="▲" ,width=1,
                       command=lambda : Cnt_CaseArr[3].config(text=str(CntOv_Case3.countUp())), repeatdelay=1000, repeatinterval=100)
CaseButton4_Up = tk.Button(frame, overrelief="solid",text="▲" ,width=1,
                       command=lambda : Cnt_CaseArr[4].config(text=str(CntOv_Case4.countUp())), repeatdelay=1000, repeatinterval=100)
CaseButton5_Up = tk.Button(frame, overrelief="solid",text="▲" ,width=1,
                       command=lambda : Cnt_CaseArr[5].config(text=str(CntOv_Case5.countUp())), repeatdelay=1000, repeatinterval=100)
CaseButton6_Up = tk.Button(frame, overrelief="solid",text="▲" ,width=1,
                       command=lambda : Cnt_CaseArr[6].config(text=str(CntOv_Case6.countUp())), repeatdelay=1000, repeatinterval=100)
CaseButton7_Up = tk.Button(frame, overrelief="solid",text="▲" ,width=1,
                       command=lambda : Cnt_CaseArr[7].config(text=str(CntOv_Case7.countUp())), repeatdelay=1000, repeatinterval=100)
CaseButton8_Up = tk.Button(frame, overrelief="solid",text="▲" ,width=1,
                       command=lambda : Cnt_CaseArr[8].config(text=str(CntOv_Case8.countUp())), repeatdelay=1000, repeatinterval=100)
CaseButton9_Up = tk.Button(frame, overrelief="solid",text="▲" ,width=1,
                       command=lambda : Cnt_CaseArr[9].config(text=str(CntOv_Case9.countUp())), repeatdelay=1000, repeatinterval=100)

CaseButton1_Up.place(x=562,y=167)
CaseButton2_Up.place(x=702,y=167)
CaseButton3_Up.place(x=845,y=167)
CaseButton4_Up.place(x=562,y=197)
CaseButton5_Up.place(x=702,y=197)
CaseButton6_Up.place(x=845,y=197)
CaseButton7_Up.place(x=562,y=227)
CaseButton8_Up.place(x=702,y=227)
CaseButton9_Up.place(x=845,y=227)

## CASE 버튼 Down ##
CaseButton1_Down = tk.Button(frame, overrelief="solid",text="▼" ,width=1,
                       command=lambda : Cnt_CaseArr[1].config(text=str(CntOv_Case1.countDown())), repeatdelay=1000, repeatinterval=100)
CaseButton2_Down = tk.Button(frame, overrelief="solid",text="▼" ,width=1,
                       command=lambda : Cnt_CaseArr[2].config(text=str(CntOv_Case2.countDown())), repeatdelay=1000, repeatinterval=100)
CaseButton3_Down = tk.Button(frame, overrelief="solid",text="▼" ,width=1,
                       command=lambda : Cnt_CaseArr[3].config(text=str(CntOv_Case3.countDown())), repeatdelay=1000, repeatinterval=100)
CaseButton4_Down = tk.Button(frame, overrelief="solid",text="▼" ,width=1,
                       command=lambda : Cnt_CaseArr[4].config(text=str(CntOv_Case4.countDown())), repeatdelay=1000, repeatinterval=100)
CaseButton5_Down = tk.Button(frame, overrelief="solid",text="▼" ,width=1,
                       command=lambda : Cnt_CaseArr[5].config(text=str(CntOv_Case5.countDown())), repeatdelay=1000, repeatinterval=100)
CaseButton6_Down = tk.Button(frame, overrelief="solid",text="▼" ,width=1,
                       command=lambda : Cnt_CaseArr[6].config(text=str(CntOv_Case6.countDown())), repeatdelay=1000, repeatinterval=100)
CaseButton7_Down = tk.Button(frame, overrelief="solid",text="▼" ,width=1,
                       command=lambda : Cnt_CaseArr[7].config(text=str(CntOv_Case7.countDown())), repeatdelay=1000, repeatinterval=100)
CaseButton8_Down = tk.Button(frame, overrelief="solid",text="▼" ,width=1,
                       command=lambda : Cnt_CaseArr[8].config(text=str(CntOv_Case8.countDown())), repeatdelay=1000, repeatinterval=100)
CaseButton9_Down = tk.Button(frame, overrelief="solid",text="▼" ,width=1,
                       command=lambda : Cnt_CaseArr[9].config(text=str(CntOv_Case9.countDown())), repeatdelay=1000, repeatinterval=100)

CaseButton1_Down.place(x=582,y=167)
CaseButton2_Down.place(x=722,y=167)
CaseButton3_Down.place(x=865,y=167)
CaseButton4_Down.place(x=582,y=197)
CaseButton5_Down.place(x=722,y=197)
CaseButton6_Down.place(x=865,y=197)
CaseButton7_Down.place(x=582,y=227)
CaseButton8_Down.place(x=722,y=227)
CaseButton9_Down.place(x=865,y=227)
################################################구분선##############################################
## POWER 제조사 입력 칸 ##
Sub_PowerArr = []
for i in range(10):
    Sub_PowerLabel = tk.Entry(frame , width=10)
    Sub_PowerArr.insert(i, Sub_PowerLabel)

Sub_PowerArr[1].place(x=15,y=300)
Sub_PowerArr[2].place(x=155,y=300)
Sub_PowerArr[3].place(x=296,y=300)
Sub_PowerArr[4].place(x=15,y=330)
Sub_PowerArr[5].place(x=155,y=330)
Sub_PowerArr[6].place(x=296,y=330)
Sub_PowerArr[7].place(x=15,y=360)
Sub_PowerArr[8].place(x=155,y=360)
Sub_PowerArr[9].place(x=296,y=360)

StringVar_Power1 = tk.StringVar()
StringVar_Power2 = tk.StringVar()
StringVar_Power3 = tk.StringVar()
StringVar_Power4 = tk.StringVar()
StringVar_Power5 = tk.StringVar()
StringVar_Power6 = tk.StringVar()
StringVar_Power7 = tk.StringVar()
StringVar_Power8 = tk.StringVar()
StringVar_Power9 = tk.StringVar()

Sub_PowerArr[1]["textvariable"] = StringVar_Power1
Sub_PowerArr[2]["textvariable"] = StringVar_Power2
Sub_PowerArr[3]["textvariable"] = StringVar_Power3
Sub_PowerArr[4]["textvariable"] = StringVar_Power4
Sub_PowerArr[5]["textvariable"] = StringVar_Power5
Sub_PowerArr[6]["textvariable"] = StringVar_Power6
Sub_PowerArr[7]["textvariable"] = StringVar_Power7
Sub_PowerArr[8]["textvariable"] = StringVar_Power8
Sub_PowerArr[9]["textvariable"] = StringVar_Power9

## POWER 카운트 ##
Cnt_PowerArr = []
for i in range(10):
    CountPower_Cu = tk.Label(frame, text = "0",bg="black",fg="white",width=2)
    Cnt_PowerArr.insert(i, CountPower_Cu)
    
Cnt_PowerArr[1].place(x=90,y=300)
Cnt_PowerArr[2].place(x=230,y=300)
Cnt_PowerArr[3].place(x=372,y=300)
Cnt_PowerArr[4].place(x=90,y=330)
Cnt_PowerArr[5].place(x=230,y=330)
Cnt_PowerArr[6].place(x=372,y=330)
Cnt_PowerArr[7].place(x=90,y=360)
Cnt_PowerArr[8].place(x=230,y=360)
Cnt_PowerArr[9].place(x=372,y=360)
## POWER 카운트 오버라이딩 ##
CntOv_Power1 = Counter()
CntOv_Power2 = Counter()
CntOv_Power3 = Counter()
CntOv_Power4 = Counter()
CntOv_Power5 = Counter()
CntOv_Power6 = Counter()
CntOv_Power7 = Counter()
CntOv_Power8 = Counter()
CntOv_Power9 = Counter()
## POWER 버튼 Up ##
PowerButton1_Up = tk.Button(frame, overrelief="solid",text="▲" ,width=1,
                        command=lambda : Cnt_PowerArr[1].config(text=str(CntOv_Power1.countUp())), repeatdelay=1000, repeatinterval=100)
PowerButton2_Up = tk.Button(frame, overrelief="solid",text="▲" ,width=1,
                       command=lambda : Cnt_PowerArr[2].config(text=str(CntOv_Power2.countUp())), repeatdelay=1000, repeatinterval=100)
PowerButton3_Up = tk.Button(frame, overrelief="solid",text="▲" ,width=1,
                       command=lambda : Cnt_PowerArr[3].config(text=str(CntOv_Power3.countUp())), repeatdelay=1000, repeatinterval=100)
PowerButton4_Up = tk.Button(frame, overrelief="solid",text="▲" ,width=1,
                       command=lambda : Cnt_PowerArr[4].config(text=str(CntOv_Power4.countUp())), repeatdelay=1000, repeatinterval=100)
PowerButton5_Up = tk.Button(frame, overrelief="solid",text="▲" ,width=1,
                       command=lambda : Cnt_PowerArr[5].config(text=str(CntOv_Power5.countUp())), repeatdelay=1000, repeatinterval=100)
PowerButton6_Up = tk.Button(frame, overrelief="solid",text="▲" ,width=1,
                       command=lambda : Cnt_PowerArr[6].config(text=str(CntOv_Power6.countUp())), repeatdelay=1000, repeatinterval=100)
PowerButton7_Up = tk.Button(frame, overrelief="solid",text="▲" ,width=1,
                       command=lambda : Cnt_PowerArr[7].config(text=str(CntOv_Power7.countUp())), repeatdelay=1000, repeatinterval=100)
PowerButton8_Up = tk.Button(frame, overrelief="solid",text="▲" ,width=1,
                       command=lambda : Cnt_PowerArr[8].config(text=str(CntOv_Power8.countUp())), repeatdelay=1000, repeatinterval=100)
PowerButton9_Up = tk.Button(frame, overrelief="solid",text="▲" ,width=1,
                       command=lambda : Cnt_PowerArr[9].config(text=str(CntOv_Power9.countUp())), repeatdelay=1000, repeatinterval=100)

PowerButton1_Up.place(x=112,y=297)
PowerButton2_Up.place(x=253,y=297)
PowerButton3_Up.place(x=395,y=297)
PowerButton4_Up.place(x=112,y=327)
PowerButton5_Up.place(x=253,y=327)
PowerButton6_Up.place(x=395,y=327)
PowerButton7_Up.place(x=112,y=357)
PowerButton8_Up.place(x=253,y=357)
PowerButton9_Up.place(x=395,y=357)

## POWER 버튼 Down ##
PowerButton1_Down = tk.Button(frame, overrelief="solid",text="▼" ,width=1,
                       command=lambda : Cnt_PowerArr[1].config(text=str(CntOv_Power1.countDown())), repeatdelay=1000, repeatinterval=100)
PowerButton2_Down = tk.Button(frame, overrelief="solid",text="▼" ,width=1,
                       command=lambda : Cnt_PowerArr[2].config(text=str(CntOv_Power2.countDown())), repeatdelay=1000, repeatinterval=100)
PowerButton3_Down = tk.Button(frame, overrelief="solid",text="▼" ,width=1,
                       command=lambda : Cnt_PowerArr[3].config(text=str(CntOv_Power3.countDown())), repeatdelay=1000, repeatinterval=100)
PowerButton4_Down = tk.Button(frame, overrelief="solid",text="▼" ,width=1,
                       command=lambda : Cnt_PowerArr[4].config(text=str(CntOv_Power4.countDown())), repeatdelay=1000, repeatinterval=100)
PowerButton5_Down = tk.Button(frame, overrelief="solid",text="▼" ,width=1,
                       command=lambda : Cnt_PowerArr[5].config(text=str(CntOv_Power5.countDown())), repeatdelay=1000, repeatinterval=100)
PowerButton6_Down = tk.Button(frame, overrelief="solid",text="▼" ,width=1,
                       command=lambda : Cnt_PowerArr[6].config(text=str(CntOv_Power6.countDown())), repeatdelay=1000, repeatinterval=100)
PowerButton7_Down = tk.Button(frame, overrelief="solid",text="▼" ,width=1,
                       command=lambda : Cnt_PowerArr[7].config(text=str(CntOv_Power7.countDown())), repeatdelay=1000, repeatinterval=100)
PowerButton8_Down = tk.Button(frame, overrelief="solid",text="▼" ,width=1,
                       command=lambda : Cnt_PowerArr[8].config(text=str(CntOv_Power8.countDown())), repeatdelay=1000, repeatinterval=100)
PowerButton9_Down = tk.Button(frame, overrelief="solid",text="▼" ,width=1,
                       command=lambda : Cnt_PowerArr[9].config(text=str(CntOv_Power9.countDown())), repeatdelay=1000, repeatinterval=100)

PowerButton1_Down.place(x=132,y=297)
PowerButton2_Down.place(x=273,y=297)
PowerButton3_Down.place(x=415,y=297)
PowerButton4_Down.place(x=132,y=327)
PowerButton5_Down.place(x=273,y=327)
PowerButton6_Down.place(x=415,y=327)
PowerButton7_Down.place(x=132,y=357)
PowerButton8_Down.place(x=273,y=357)
PowerButton9_Down.place(x=415,y=357)
###################################################구분선#######################################################
## 메뉴바 ##
def close():
   frame.quit()
   frame.destroy()

def Main_Item():
    Main_Data = []
    
    Main_Data.append("MainBoard\n")
    Main_Data.append("VGA\n")
    Main_Data.append("SSD\n")
    Main_Data.append("Case\n")
    Main_Data.append("Power\n")

    return Main_Data

def Sub_Item():
    Sub_Data = []
    #########################MainBoard##################
    Sub_Data.append(Sub_MbArr[1].get() +" : "+ str(CntOv_Mb1.count) +'\n')
    Sub_Data.append(Sub_MbArr[2].get() +" : "+ str(CntOv_Mb2.count) +'\n')
    Sub_Data.append(Sub_MbArr[3].get() +" : "+ str(CntOv_Mb3.count) +'\n')
    Sub_Data.append(Sub_MbArr[4].get() +" : "+ str(CntOv_Mb4.count) +'\n')
    Sub_Data.append(Sub_MbArr[5].get() +" : "+ str(CntOv_Mb5.count) +'\n')
    Sub_Data.append(Sub_MbArr[6].get() +" : "+ str(CntOv_Mb6.count) +'\n')
    Sub_Data.append(Sub_MbArr[7].get() +" : "+ str(CntOv_Mb7.count) +'\n')
    Sub_Data.append(Sub_MbArr[8].get() +" : "+ str(CntOv_Mb8.count) +'\n')
    Sub_Data.append(Sub_MbArr[9].get() +" : "+ str(CntOv_Mb9.count) +'\n')
    ######################VGA######################
    Sub_Data.append(Sub_VgaArr[1].get() +" : "+ str(CntOv_Vga1.count) +'\n')
    Sub_Data.append(Sub_VgaArr[2].get() +" : "+ str(CntOv_Vga2.count) +'\n')
    Sub_Data.append(Sub_VgaArr[3].get() +" : "+ str(CntOv_Vga3.count) +'\n')
    Sub_Data.append(Sub_VgaArr[4].get() +" : "+ str(CntOv_Vga4.count) +'\n')
    Sub_Data.append(Sub_VgaArr[5].get() +" : "+ str(CntOv_Vga5.count) +'\n')
    Sub_Data.append(Sub_VgaArr[6].get() +" : "+ str(CntOv_Vga6.count) +'\n')
    Sub_Data.append(Sub_VgaArr[7].get() +" : "+ str(CntOv_Vga7.count) +'\n')
    Sub_Data.append(Sub_VgaArr[8].get() +" : "+ str(CntOv_Vga8.count) +'\n')
    Sub_Data.append(Sub_VgaArr[9].get() +" : "+ str(CntOv_Vga9.count) +'\n')
    ######################SSD########################
    Sub_Data.append(Sub_SsdArr[1].get() +" : "+ str(CntOv_Ssd1.count) +'\n')
    Sub_Data.append(Sub_SsdArr[2].get() +" : "+ str(CntOv_Ssd2.count) +'\n')
    Sub_Data.append(Sub_SsdArr[3].get() +" : "+ str(CntOv_Ssd3.count) +'\n')
    Sub_Data.append(Sub_SsdArr[4].get() +" : "+ str(CntOv_Ssd4.count) +'\n')
    Sub_Data.append(Sub_SsdArr[5].get() +" : "+ str(CntOv_Ssd5.count) +'\n')
    Sub_Data.append(Sub_SsdArr[6].get() +" : "+ str(CntOv_Ssd6.count) +'\n')
    Sub_Data.append(Sub_SsdArr[7].get() +" : "+ str(CntOv_Ssd7.count) +'\n')
    Sub_Data.append(Sub_SsdArr[8].get() +" : "+ str(CntOv_Ssd8.count) +'\n')
    Sub_Data.append(Sub_SsdArr[9].get() +" : "+ str(CntOv_Ssd9.count) +'\n')
    ######################Case#############################
    Sub_Data.append(Sub_CaseArr[1].get() +" : "+ str(CntOv_Case1.count) +'\n')
    Sub_Data.append(Sub_CaseArr[2].get() +" : "+ str(CntOv_Case2.count) +'\n')
    Sub_Data.append(Sub_CaseArr[3].get() +" : "+ str(CntOv_Case3.count) +'\n')
    Sub_Data.append(Sub_CaseArr[4].get() +" : "+ str(CntOv_Case4.count) +'\n')
    Sub_Data.append(Sub_CaseArr[5].get() +" : "+ str(CntOv_Case5.count) +'\n')
    Sub_Data.append(Sub_CaseArr[6].get() +" : "+ str(CntOv_Case6.count) +'\n')
    Sub_Data.append(Sub_CaseArr[7].get() +" : "+ str(CntOv_Case7.count) +'\n')
    Sub_Data.append(Sub_CaseArr[8].get() +" : "+ str(CntOv_Case8.count) +'\n')
    Sub_Data.append(Sub_CaseArr[9].get() +" : "+ str(CntOv_Case9.count) +'\n')
    #######################Power#########################
    Sub_Data.append(Sub_PowerArr[1].get() +" : "+ str(CntOv_Power1.count) +'\n')
    Sub_Data.append(Sub_PowerArr[2].get() +" : "+ str(CntOv_Power2.count) +'\n')
    Sub_Data.append(Sub_PowerArr[3].get() +" : "+ str(CntOv_Power3.count) +'\n')
    Sub_Data.append(Sub_PowerArr[4].get() +" : "+ str(CntOv_Power4.count) +'\n')
    Sub_Data.append(Sub_PowerArr[5].get() +" : "+ str(CntOv_Power5.count) +'\n')
    Sub_Data.append(Sub_PowerArr[6].get() +" : "+ str(CntOv_Power6.count) +'\n')
    Sub_Data.append(Sub_PowerArr[7].get() +" : "+ str(CntOv_Power7.count) +'\n')
    Sub_Data.append(Sub_PowerArr[8].get() +" : "+ str(CntOv_Power8.count) +'\n')
    Sub_Data.append(Sub_PowerArr[9].get() +" : "+ str(CntOv_Power9.count) +'\n')

    return Sub_Data

def Div_Item():
    Div_Data = []
    Div_Data.append("-----------------------------------------------------------------------------------------\n")
    return Div_Data
######################################저장########################
def  save():
    File = open("재고.txt", 'w')
    MainItem = Main_Item()
    DivItem = Div_Item()
    SubItem = Sub_Item()
    for i in range(1):
            for j in range(5):
                    File.write(str(DivItem[i]))
                    File.write(str(MainItem[j]))
                    for x in range(9):
                        if j == 0:
                            File.write(str(SubItem[x]))
                        elif j == 1:
                            File.write(str(SubItem[x+9]))
                        elif j == 2:
                            File.write(str(SubItem[x+18]))
                        elif j == 3:
                            File.write(str(SubItem[x+27]))
                        elif j == 4:
                            File.write(str(SubItem[x+36]))
    File.close()
##############################다른이름으로 저장############################     
def Save_as():
    Files = [('Text Document', '*.txt'),('All Files', '*.*')] 
    File = filedialog.asksaveasfile(filetypes = Files ,mode='w', defaultextension=Files)
    MainItem = Main_Item()
    DivItem = Div_Item()
    SubItem = Sub_Item()
    if File is None: 
        return
    for i in range(1):
            for j in range(5):
                    File.write(str(DivItem[i]))
                    File.write(str(MainItem[j]))
                    for x in range(9):
                        if j == 0:
                            File.write(str(SubItem[x]))
                        elif j == 1:
                            File.write(str(SubItem[x+9]))
                        elif j == 2:
                            File.write(str(SubItem[x+18]))
                        elif j == 3:
                            File.write(str(SubItem[x+27]))
                        elif j == 4:
                            File.write(str(SubItem[x+36]))
    File.close()
############################################################
def Data():
    data = []
    data_len = len(Sub_MbArr)
    for i in range(data_len):
        text = Sub_MbArr[i].get()
        data.append(text)
    for i in range(data_len):
        text = Sub_VgaArr[i].get()
        data.append(text)
    for i in range(data_len):
        text = Sub_SsdArr[i].get()
        data.append(text)
    for i in range(data_len):
        text = Sub_PowerArr[i].get()
        data.append(text)
    for i in range(data_len):
        text = Sub_CaseArr[i].get()
        data.append(text)
        
    data.append(CntOv_Mb1.count)
    data.append(CntOv_Mb2.count)
    data.append(CntOv_Mb3.count)
    data.append(CntOv_Mb4.count)
    data.append(CntOv_Mb5.count)
    data.append(CntOv_Mb6.count)
    data.append(CntOv_Mb7.count)
    data.append(CntOv_Mb8.count)
    data.append(CntOv_Mb9.count)
    data.append(CntOv_Vga1.count)
    data.append(CntOv_Vga2.count)
    data.append(CntOv_Vga3.count)
    data.append(CntOv_Vga4.count)
    data.append(CntOv_Vga5.count)
    data.append(CntOv_Vga6.count)
    data.append(CntOv_Vga7.count)
    data.append(CntOv_Vga8.count)
    data.append(CntOv_Vga9.count)
    data.append(CntOv_Ssd1.count)
    data.append(CntOv_Ssd2.count)
    data.append(CntOv_Ssd3.count)
    data.append(CntOv_Ssd4.count)
    data.append(CntOv_Ssd5.count)
    data.append(CntOv_Ssd6.count)
    data.append(CntOv_Ssd7.count)
    data.append(CntOv_Ssd8.count)
    data.append(CntOv_Ssd9.count)
    data.append(CntOv_Power1.count)
    data.append(CntOv_Power2.count)
    data.append(CntOv_Power3.count)
    data.append(CntOv_Power4.count)
    data.append(CntOv_Power5.count)
    data.append(CntOv_Power6.count)
    data.append(CntOv_Power7.count)
    data.append(CntOv_Power8.count)
    data.append(CntOv_Power9.count)
    data.append(CntOv_Case1.count)
    data.append(CntOv_Case2.count)
    data.append(CntOv_Case3.count)
    data.append(CntOv_Case4.count)
    data.append(CntOv_Case5.count)
    data.append(CntOv_Case6.count)
    data.append(CntOv_Case7.count)
    data.append(CntOv_Case8.count)
    data.append(CntOv_Case9.count)

    return data
##############################################################
def st_Save():
    data = Data()
    data_len = len(data)
    
    print(data_len)
    with open("savedtext.dat", "wb") as pickle_file:
        pickle.dump(data, pickle_file, pickle.HIGHEST_PROTOCOL)
    
def st_load():
    with open("savedtext.dat", "rb") as pickle_file:
        data = pickle.load(pickle_file)
        
    StringVar_MB1.set(data[1])
    StringVar_MB2.set(data[2])
    StringVar_MB3.set(data[3])
    StringVar_MB4.set(data[4])
    StringVar_MB5.set(data[5])
    StringVar_MB6.set(data[6])
    StringVar_MB7.set(data[7])
    StringVar_MB8.set(data[8])
    StringVar_MB9.set(data[9])
    StringVar_Vga1.set(data[11])
    StringVar_Vga2.set(data[12])
    StringVar_Vga3.set(data[13])
    StringVar_Vga4.set(data[14])
    StringVar_Vga5.set(data[15])
    StringVar_Vga6.set(data[16])
    StringVar_Vga7.set(data[17])
    StringVar_Vga8.set(data[18])
    StringVar_Vga9.set(data[19])
    StringVar_Ssd1.set(data[21])
    StringVar_Ssd2.set(data[22])
    StringVar_Ssd3.set(data[23])
    StringVar_Ssd4.set(data[24])
    StringVar_Ssd5.set(data[25])
    StringVar_Ssd6.set(data[26])
    StringVar_Ssd7.set(data[27])
    StringVar_Ssd8.set(data[28])
    StringVar_Ssd9.set(data[29])
    StringVar_Power1.set(data[31])
    StringVar_Power2.set(data[32])
    StringVar_Power3.set(data[33])
    StringVar_Power4.set(data[34])
    StringVar_Power5.set(data[35])
    StringVar_Power6.set(data[36])
    StringVar_Power7.set(data[37])
    StringVar_Power8.set(data[38])
    StringVar_Power9.set(data[39])
    StringVar_Case1.set(data[41])
    StringVar_Case2.set(data[42])
    StringVar_Case3.set(data[43])
    StringVar_Case4.set(data[44])
    StringVar_Case5.set(data[45])
    StringVar_Case6.set(data[46])
    StringVar_Case7.set(data[47])
    StringVar_Case8.set(data[48])
    StringVar_Case9.set(data[49])

    for i in range(50,95):
        if i < 60:
            Cnt_MbArr[i-50].config(text = str(data[i-1]))
        elif 69 > i > 59:
            Cnt_VgaArr[i-59].config(text = str(data[i-1]))
        elif 78 > i > 68:
            Cnt_SsdArr[i-68].config(text = str(data[i-1]))
        elif 87 > i > 77:
            Cnt_PowerArr[i-77].config(text = str(data[i-1]))
        elif 95 > i > 86:
            Cnt_CaseArr[i-86].config(text = str(data[i-1]))

############################################################

menubar = tk.Menu(frame)
menu_1=tk.Menu(frame, tearoff=0)
menu_1.add_command(label="Save",command=save)
menu_1.add_command(label="Save_as", command=Save_as)
menu_1.add_command(label="st_Save", command=st_Save)
menu_1.add_command(label="st_load", command=st_load)
menu_1.add_separator()
menu_1.add_command(label="종료", command=close)
menubar.add_cascade(label="파일", menu=menu_1)

frame.config(menu=menubar)
        
        
frame.mainloop()



