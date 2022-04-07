from tkinter import *

def popup_menu(event):
    popup.post(event.x_root,event.y_root)
def gotofr1():
    fr1.pack(fill=BOTH,expand=True)
    fr2.pack_forget()
    fr3.pack_forget()
    root.title('窗口1')
    fr1.config(bg='lightblue')
def gotofr2():
    fr2.pack(fill=BOTH,expand=True)
    fr1.pack_forget()
    fr3.pack_forget()
    root.title('窗口2')
    fr2.config(bg='lightgreen')
def gotofr3():
    fr3.pack(fill=BOTH,expand=True)
    fr1.pack_forget()
    fr2.pack_forget()
    root.title('窗口3')
    fr3.config(bg='lightyellow')

root=Tk()  # 源码来自wb98.com
root.title('窗口1')
root.geometry('300x150+888+444')

popup=Menu(root,tearoff=0)
popup.add_command(label='窗口1',command=gotofr1) # 通过窗体右键菜单来切换不同的'窗体'
popup.add_command(label='窗口2',command=gotofr2)
popup.add_command(label='窗口3',command=gotofr3)

root.bind("<Button-3>",popup_menu)

fr1=Frame(root, relief='ridge',borderwidth=4) # 不设置边线宽，无法显示
fr1.pack(fill=BOTH,expand=True)
fr1.config(bg='lightblue')

fr2=Frame(root, relief='ridge',borderwidth=4) # 不设置边线宽，无法显示
# fr2.pack() # 先不布局定位

fr3=Frame(root, relief='ridge',borderwidth=4) # 不设置边线宽，无法显示
# fr3.pack() # 先不布局定位

but1=Button(fr1,text="窗口1按钮")
but1.pack() # 用pack()方法
but2=Button(fr2,text="窗口2按钮")
but2.grid() # 用grid()方法
but3=Button(fr3,text="窗口3按钮")
but3.place(relx=0.5,rely=0.5) # 用place()方法

but1.bind("<ButtonRelease-1>",popup_menu) # 按钮点击释放后弹出菜单
but2.bind("<ButtonRelease-1>",popup_menu)
but3.bind("<ButtonRelease-1>",popup_menu)

root.mainloop()