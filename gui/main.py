from tkinter import * 
from tkinter import ttk
from db import *

main = Tk('Assignment')
main.geometry("400x250")

data = get_account_data()

frame = Frame(main)
frame.pack()
tbl = ttk.Treeview(frame)
tbl['columns'] = ['col1','col2', 'col3']

for col in tbl['columns']:
    tbl.column(col,anchor=CENTER, width=80)
    tbl.heading(col,text=col,anchor=CENTER)

for i,rec in enumerate(data):
    tbl.insert(parent='',index='end',iid=i,text='',values=rec)
    tbl.pack()

# for i,rec in enumerate(data):
#     for j in range(len(header)):
#         e = Label(main,width=10, text=rec[j],borderwidth=2,relief='ridge', anchor="w") 
#         e.grid(row=i, column=j) 
#         e.pack()
        # e.insert(END, rec[j])

main.mainloop()
