import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from PIL import ImageTk,Image

root = Tk() 
 
canvas = Canvas(root, width = 800, height = 500)
my_pic =  Image.open("background.jpg")
reside = my_pic.resize((800,500),Image.ANTIALIAS)
new_pic = ImageTk.PhotoImage(reside)
canvas.create_image(0,0,anchor=NW,image=new_pic)
canvas.pack()

data = pd.read_csv('DataPersentaseAngkaKelulusan.csv')
print (data)
data['jenjang'] = data['jenjang'].str.replace(" ", "")

data_sd = data[data['jenjang'] == 'SD']
data_smp = data[data['jenjang'] == 'SMP']
data_sma = data[data['jenjang'] == 'SMA']
data_smk = data[data['jenjang'] == 'SMK']

data_sd = data_sd.reset_index(drop = True)
data_smp = data_smp.reset_index(drop = True)
data_sma = data_sma.reset_index(drop = True)
data_smk = data_smk.reset_index(drop = True)

def show_dataset():
    open=Toplevel()
    data = pd.read_csv('DataPersentaseAngkaKelulusan.csv')
    label_dataset = Label(open, text= data, font=('arial', 12, 'italic'))
    label_dataset.pack()
    
def show_dataframe ():
    open=Toplevel() 

    label_sd = Label(open, text= data_sd, font=('arial', 12, 'italic'))
    label_smp = Label(open, text= data_smp,  font=('arial', 12, 'italic'))
    label_sma = Label(open, text= data_sma,  font=('arial', 12, 'italic'))
    label_smk = Label(open, text= data_smk,  font=('arial', 12, 'italic'))
    
    label_sd.pack()
    label_smp.pack()
    label_sma.pack()
    label_smk.pack()

def show_diagram():

    #SD
    x1 = data_sd.tahun_ajaran
    y1 = data_sd.persentase
    #SMP
    x2 = data_smp.tahun_ajaran
    y2 = data_smp.persentase
    #SMA
    x3 = data_sma.tahun_ajaran
    y3 = data_sma.persentase
    #SMK
    x4 = data_smk.tahun_ajaran
    y4 = data_smk.persentase
    
    plt.plot(x1,y1, color='yellow', marker='p',label="data SD")
    plt.plot(x2,y2, color='blue', marker='*',label="data SMP")
    plt.plot(x3,y3, color='black', marker='o',label="data SMA")
    plt.plot(x4,y4, color='red', marker='+',label="data SMK")
    plt.title('Diagram persentase kelulusan tiap jenjang')
    plt.legend()
    plt.show()

button_show_dataset = Button(text='Tampilkan dataset',command=show_dataset, bg='blue',fg='white', border='5',width=20)
canvas.create_window(100,30,window=button_show_dataset)

button_diagram = Button(text='Tampilkan diagram',command=show_diagram, bg='blue',fg='white', border='5',width=20)
canvas.create_window(300,30,window=button_diagram)

button_show_dataframe = Button(text='tampilkan dataframe',command=show_dataframe, bg='blue',fg='white', border='5',width=20)
canvas.create_window(500,30,window=button_show_dataframe)

button_exit = Button(text='exit',command=exit, bg='blue',fg='white', border='5',width=20)
canvas.create_window(700,30,window=button_exit)
root.mainloop()