from DearTk import DearTk

DTK = DearTk()

def main():
    DTK.Begin("Calculator (parent)", "200x200")

    DTK.Button("this is supposed to be red")
    @DTK.ButtonFuncDef
    def RedButton(Event: any):
        print("meow")
    DTK.GridPreviousWidget(row=0, column=0)
    DTK.PushStylePreviousWidget(fgc="red", bgc="yellow")  # this style now exists ONLY for buttons

    DTK.Label("label thing!")
    DTK.GridPreviousWidget(row=0, column=1)
    DTK.PushStylePreviousWidget(fgc="#001a00", bgc="#c8c8c8")

    DTK.BeginToplevel("guh (child)")
    DTK.Button("another button")
    @DTK.ButtonFuncDef # shorthand for DTK.SetBinding("Button")
    def AnotherButton(Event: any):
        print("woof")
    DTK.GridPreviousWidget(row=1, column=0)
    DTK.PushStylePreviousWidgetType() # gets the style from the previous button

    DTK.Label("label thing 2!")
    DTK.SetBinding("Double-Button") # https://instructobit.com/tutorial/51/Python-Tkinter-event-handling for more info
    @DTK.BindActionFuncDef
    def AnotherLabel(Event: any):
        print("woof (label)")
    DTK.GridPreviousWidget(row=1, column=1)
    DTK.PushStylePreviousWidget(fgc="grey", bgc="cyan") # same as above, this style exists ONLY for labels

    DTK.Button("buttonese")
    DTK.GridPreviousWidget(row=2, column=1)
    DTK.PushStylePreviousWidget(fgc="black", bgc="yellow") # new style for buttons

    DTK.Label("another label!")
    DTK.GridPreviousWidget(row=2, column=0)
    DTK.PushStylePreviousWidgetType() # gets the style from the previous label

    DTK.Button("button but better")
    DTK.GridPreviousWidget(row=2, column=2)
    DTK.PushStylePreviousWidgetType() # gets style from the previous button

    DTK.End()

if __name__ == "__main__":
    main()
