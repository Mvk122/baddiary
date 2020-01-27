import json 
from tkinter import *
from tkinter import ttk
filename = 'diarycontents.json'


def loadfile(filename):
    with open(filename , 'r') as f:
        jsondata = json.load(f)
    return jsondata 


def getentries(jsondata, dictname):
    entries = []
    for entry in jsondata[dictname]:
        entries.append(entry)
    return entries 


def updatelabel(state):
    global Title
    global diaryentries
    value = state.widget.get(state.widget.curselection())
    entrytext = diaryentries['entries'][value][0]
    Title.config(text=value)
    entryText.config(text=entrytext)


def addentry(jsondata, entryname, entry):
    assert type(entry) == list
    assert len(entry) == 2 
    jsondata['entries'][entryname] = entry


def addentrybutton():
    global diaryentries
    def submit():
        addentry(diaryentries, e1.get(), [ e2.get('1.0', END), 'placeholder'])


    win1 = Toplevel()
    titlelabel = Label(win1, text="Add an entry")
    titlelabel.pack()
    lbl1 = Label(win1, text="Entry Title")
    lbl1.pack()
    e1 = Entry(win1)
    e1.pack()

    lbl2 = Label(win1, text="Entry Text")
    lbl2.pack()
    e2 = Text(win1, height=5)
    e2.pack()
    win1.geometry('600x300')
    button1 = Button(win1, text="test", command=submit)
    button1.pack()


    
diaryentries = loadfile(filename)
app = Tk()
app.title("Diary")
app.geometry("500x500")

#Getting entries from dict and adding to listbox
entrylist = Listbox(app)
entries = getentries(diaryentries, 'entries')
for entry in entries:
    entrylist.insert(END, entry)
entrylist.grid(row=0, column=0)
entrylist.bind('<<ListboxSelect>>', updatelabel)


#Code for current shown entry
Title = Label(app, text="No entry selected")
Title.grid(row=0, column=1)
entryText = Label(app, text="No entry selected")
entryText.grid(row=1, column=1)

#Code to add entries
addentrybutton = Button(app, text="Add entry", command= addentrybutton)
addentrybutton.grid(row=1 , column=0)

if __name__ == "__main__":
    app.mainloop()
    with open(filename, 'w+') as f:
        json.dump(diaryentries, f)