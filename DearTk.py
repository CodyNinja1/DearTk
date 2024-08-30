import tkinter as tk
from tkinter import ttk

class DTKStyle:
    def __repr__(self):
        return f"({self.name}: {self.bgc}, {self.fgc}, {self.padding})"

    def __init__(self, padding: int, fgc: str, bgc: str, name: str = ""):
        self.name = name
        self.padding = padding
        self.fgc = fgc
        self.bgc = bgc
    
    def SetName(self, name: str):
        self.name = name

class DearTk:
    def __init__(self):
        self.binding: str = ""
        self.useTopLevel: int = -1
        self.toplevels: list[tk.Tk] = []
        self.window: tk.Tk = None
        self.previousWidget: tk.Widget = None
        self.widgetAmount: int = 1
        self.styles: dict[str, list[DTKStyle]] = {}
        self.widgets: dict[str, list[tk.Widget]] = {}

    def GetWindow(self):
        if self.useTopLevel == -1: return self.window
        if self.useTopLevel < len(self.toplevels): return self.toplevels[self.useTopLevel]
        else: raise Exception("No window is active!")

    def ButtonFuncDef(self, buttonFunc) -> None:
        self.previousWidget.bind("<Button>", buttonFunc)
    
    def BindActionFuncDef(self, bindFunc) -> None:
        self.window.bind(f"<{self.binding}>", bindFunc)

    def BindActionPreviousWidgetFuncDef(self, bindFunc) -> None:
        self.previousWidget.bind(f"<{self.binding}>", bindFunc)
    
    def SetBinding(self, binding="") -> None:
        self.binding = binding

    def Begin(self, windowTitle = "tk", geometry="") -> None:
        self.window = tk.Tk()
        self.window.title(windowTitle)
        self.window.geometry(geometry)

    def BeginToplevel(self, windowTitle = "tk") -> None:
        if (self.window == None): raise Exception("Use Begin() before using BeginTopLevel()!")
        self.toplevels.append(tk.Toplevel(self.window))
        self.toplevels[-1].title(windowTitle)
        self.useTopLevel = len(self.toplevels) - 1

    def Update(self):
        self.GetWindow().update_idletasks()

    def End(self) -> None:
        self.GetWindow().mainloop()
        if self.useTopLevel == -1: self.window = None
        else: 
            self.EndTopLevel()

    def EndTopLevel(self) -> None:
        del self.toplevels[self.useTopLevel]
        self.useTopLevel -= 1

    def IncreaseWidgetAmount(self) -> None:
        self.widgetAmount += 1

    def AppendWidget(self) -> None:
        try:
            self.widgets[self.previousWidget.winfo_class()].append(self.previousWidget)
        except KeyError:
            self.widgets[self.previousWidget.winfo_class()] = []
            self.widgets[self.previousWidget.winfo_class()].append(self.previousWidget)
        self.IncreaseWidgetAmount()

    def LabelVar(self, label: tk.StringVar) -> None:
        win: tk.Tk = None
        if (self.useTopLevel == -1): win = self.window
        else: win = self.toplevels[self.useTopLevel]

        if (win == None): raise Exception("Use Begin() before using LabelVar()!")
        self.previousWidget = ttk.Label(win, text=label)
        self.AppendWidget()

    def Label(self, label: str) -> None:
        win: tk.Tk = None
        if (self.useTopLevel == -1): win = self.window
        else: win = self.toplevels[self.useTopLevel]

        if (win == None): raise Exception("Use Begin() before using Label()!")
        self.previousWidget = ttk.Label(win, text=label)
        self.AppendWidget()

    def ButtonVar(self, buttonLabel: tk.StringVar) -> None:
        win: tk.Tk = None
        if (self.useTopLevel == -1): win = self.window
        else: win = self.toplevels[self.useTopLevel]

        if (win == None): raise Exception("Use Begin() before using ButtonVar()!")
        self.previousWidget = ttk.Button(win, text=buttonLabel)
        self.AppendWidget()
    
    def Button(self, buttonLabel: str, **kwargs) -> None:
        win: tk.Tk = None
        if (self.useTopLevel == -1): win = self.window
        else: win = self.toplevels[self.useTopLevel]

        if (win == None): raise Exception("Use Begin() before using Button()!")
        self.previousWidget = ttk.Button(win)
        self.previousWidget.config(kwargs)
        self.previousWidget.config(text=buttonLabel)
        self.AppendWidget()
    
    def PackPreviousWidget(self, **kwargs) -> None:
        self.previousWidget.pack(kwargs)
    
    def GridPreviousWidget(self, **kwargs) -> None:
        self.previousWidget.grid(kwargs)
    
    def PlacePreviousWidget(self, **kwargs) -> None:
        self.previousWidget.place(kwargs)

    def GetStyleNameFromPreviousWidget(self) -> str:
        return str(len(self.styles[self.previousWidget.winfo_class()]) - 1) + "." + self.previousWidget.winfo_class()

    def PushStylePreviousWidget(self, bgc="", fgc="", paddingv=-1) -> None:
        style: DTKStyle = DTKStyle(paddingv, fgc, bgc)

        print(style)

        try:
            self.styles[self.previousWidget.winfo_class()].append(style)
        except KeyError:
            self.styles[self.previousWidget.winfo_class()] = []
            self.styles[self.previousWidget.winfo_class()].append(style)

        style.SetName(self.GetStyleNameFromPreviousWidget())

        print(self.styles)

        ttk.Style().configure(style=style.name, padding=style.padding, background=style.bgc, foreground=style.fgc)
        self.previousWidget.configure(style=style.name)
    
    def PushStylePreviousWidgetType(self, idx: int = -1) -> None:
        style: DTKStyle = self.styles[self.previousWidget.winfo_class()][idx]

        ttk.Style().configure(style=style.name, padding=style.padding, background=style.bgc, foreground=style.fgc)
        self.previousWidget.configure(style=style.name)

    def PopStylePreviousWidget(self) -> None:
        if (len(self.styles[self.previousWidget.winfo_class()]) == 0): raise Exception("No styles to pop!")
        if (len(self.styles[self.previousWidget.winfo_class()]) > 1): 
            del self.styles[self.previousWidget.winfo_class()][-1]
            style: DTKStyle = self.styles[self.previousWidget.winfo_class()][-1]
            ttk.Style(self.GetWindow()).configure(style=self.GetStyleNameFromPreviousWidget(), padding=style.padding, background=style.bgc, foreground=style.fgc)
            self.previousWidget.configure(style=self.GetStyleNameFromPreviousWidget())

    # def PushStyle(self, bgc="#ffffff", fgc="#000000", paddingv=-1) -> None:
    #     self.styles.append(DTKStyle(paddingv, fgc, bgc))
    #     ttk.Style(self.GetWindow()).configure(str(len(self.styles) - 1) + ".TButton", background=bgc, foreground=fgc)
    #     self.previousWidget.configure(style=str(len(self.styles) - 1) + ".TButton")
    #     print("pushed style " + str(len(self.styles) - 1) + ".TButton")

    # def ResetStyle(self) -> None:
    #     ttk.Style().theme_use("default")
