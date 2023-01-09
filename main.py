from guizero import App, Text, Box, PushButton, TextBox, Combo, Window, Box, info, warn

mainwapp = App(title="Main Window", bg = "#449DD1")
time = []
babylist = []
temp = []

def tempwindow():
    def takingdata():
        temp.append(textbox1.value)
        for i in temp:
            if int(i) >= 38:
                warn("WARNING !TO HOT!", "The Baby must be kept BELOW 37.5 degrees and above 36. Remove layers of clothing or decrease temperature of room")
            elif int(i) <= 36:
                warn("WARNING !TO COLD!", "The Baby must be kept ABOVE 36 degrees and below 37.5. Use blankets or heat the room to warm the baby")

        a = len(temp)
        if a >= 2:
            tempcalc = int(temp[a-2]) - int(temp[a-1])
            if tempcalc >= 1:
                warn("WARNING", "The Baby's temperature has changed by more than 1C. Stabilize Temperature")
            elif tempcalc <= -1:
                warn("WARNING", "The Baby's temperature has changed by more than 1C. Stabilize Temperature")

        time.append(textbox2.value)
        textb=Text(tempwindow, text="Succesfully entered", color="#F9A620")
    tempwindow = Window(mainwapp, title="Temperature Window", bg = "#449DD1")
    spacebox1=Box(tempwindow, height=50, width=2)
    text1 = Text(tempwindow, text="Insert Temperature in C", size=20, color="#F9A620")
    textbox1=TextBox(tempwindow, width=50)
    spacebox2=Box(tempwindow, height=50, width=2)
    text2 = Text(tempwindow, text="Insert time", size=20, color="#F9A620")
    textbox2=TextBox(tempwindow, width=50)
    spacebox3=Box(tempwindow, height=50, width=2)
    enterpushbutton=PushButton(tempwindow, text="Enter values", command=takingdata)

    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!




def viewdata():
    a = max(temp)
    b = min(temp)
    viewdataapp = Window(mainwapp, title="Data Viewing", bg = "#449DD1")
    spacebox7=Box(viewdataapp, height=50, width=2)
    text6 = Text(viewdataapp, text="The baby's temperature:", color="#F9A620", size=20)
    text7 = Text(viewdataapp, text=str(temp), color="#F9A620", size=20)
    text9 = Text(viewdataapp, text="The time the temperatures where entered", color="#F9A620", size=20)
    text8 = Text(viewdataapp, text=str(time), color="#F9A620", size=20)
    texta1 = Text(viewdataapp, text="Highest Temperature", color="#F9A620", size=20)
    texta2 = Text(viewdataapp, text=str(a), color="#F9A620", size=20)
    textb1 = Text(viewdataapp, text="Lowest Temperature", color="#F9A620", size=20)
    textb2 = Text(viewdataapp, text=str(b), color="#F9A620", size=20)



def newbaby():
    def addingbaby():
        babylist.append(textbox3.value)
        texta=Text(newbaby, text="Succesfully entered", color="#F9A620", size=20)
    newbaby = Window(mainwapp, title="NewBaby Window", bg="#449DD1")
    spacebox4 = Box(newbaby, height=50, width=2)
    text3 = Text(newbaby, text="Insert full name of new Baby",  color="#F9A620", size=20)
    textbox3 = TextBox(newbaby, width=50)
    enterpushbutton2 = PushButton(newbaby, text="Enter Values", command=addingbaby)




spacebox4=Box(mainwapp, height=50, width=2)
textlkj= Text(mainwapp, text="Welcome to Baby App", size=50, color="#F9A620")
text3=Text(mainwapp, text="Select an option", size=20, color="#F9A620")
tempbutton = PushButton(mainwapp, text="Temperature Window", command=tempwindow)
newbabybutton = PushButton(mainwapp, text="New Baby", command=newbaby)
viewdatabutton = PushButton(mainwapp, text="View Data", command=viewdata)
tempbutton.text_size=15
newbabybutton.text_size=15
viewdatabutton.text_size=15



mainwapp.display()



















