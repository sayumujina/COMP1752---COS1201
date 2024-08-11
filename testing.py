from tkinter import *

root = Tk()

def retrieve(index):    
    global values
    if index == 'all':
        for value in values:
            print(value.get())
    else:
        print(values[index].get())

values = []
def saveClear():
    global entry_list, values
    list_var = Variable()
    listbox = Listbox(root, listvariable = list_var)
    for entry in entry_list:
        listbox.insert(END,entry.get())
        entry.set('')
    values.append(list_var)
    listbox.pack(padx = 10, pady = 10)

entry_list = []
for _ in range(5):
    ent_var = StringVar()
    entry = Entry(root, textvariable = ent_var)
    entry_list.append(ent_var)
    entry.pack(padx = 10, pady = 10)

but = Button(root, text = 'Save and Clear', command = saveClear)
but.pack(padx = 10, pady = 10)

root.mainloop()
retrieve('all') #OR specify the index that you wish to retrieve