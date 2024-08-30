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
    @DTK.ButtonFuncDef
    def AnotherButton(Event: any):
        print("woof")
    DTK.GridPreviousWidget(row=1, column=0)
    DTK.PushStylePreviousWidgetType() # gets the style from the previous button

    DTK.Label("label thing 2!")
    DTK.GridPreviousWidget(row=1, column=1)
    DTK.PushStylePreviousWidget(fgc="grey", bgc="cyan")

    DTK.End()

if __name__ == "__main__":
    main()
