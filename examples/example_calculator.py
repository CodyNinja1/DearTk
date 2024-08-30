from DearTk import DearTk
import tkinter as tk

DTK = DearTk()

class Calculator:
    def __init__(self, label: tk.Widget) -> None:
        self.currentOperation: str = ""
        self.num1: float = 0
        self.num2: float = 0
        self.useNum2: bool = False
        self.useDecimal: bool = False
        self.resultLabel: tk.Widget = label
        self.Ans: bool = False
    
    def HandleOp(self, op: str) -> None:
        self.currentOperation = op
        self.Switch()

    def UpdateLabel(self, num: float) -> None:
        self.resultLabel.configure(text=str(num))

    def Reset(self) -> None:
        self.currentOperation: str = ""
        self.num1: float = 0
        self.num2: float = 0
        self.useNum2: bool = False
        self.useDecimal: bool = False

    def HandleNum(self, num: float) -> None:
        if not self.useDecimal:
            if not self.useNum2:
                self.num1 *= 10
                self.num1 += num
                self.UpdateLabel(self.num1)
            else:
                self.num2 *= 10
                self.num2 += num
                self.UpdateLabel(self.num2)

    def PosNSwitch(self) -> None:
        if not self.useNum2:
            self.num1 *= -1
            self.UpdateLabel(self.num1)
        else:
            self.num2 *= 1
            self.UpdateLabel(self.num2)

    def Switch(self) -> None:
        self.useNum2 = not self.useNum2
    
    def Calculate(self) -> None:
        if self.currentOperation == "+":
            self.UpdateLabel(self.num1 + self.num2)
            self.Ans = True
            self.num1 = self.num1 + self.num2
            self.num2 = 0
            self.useNum2 = False
        elif self.currentOperation == "-":
            self.UpdateLabel(self.num1 - self.num2)
            self.Ans = True
            self.num1 = self.num1 - self.num2
            self.num2 = 0
            self.useNum2 = False
        elif self.currentOperation == "*":
            self.UpdateLabel(self.num1 * self.num2)
            self.Ans = True
            self.num1 = self.num1 * self.num2
            self.num2 = 0
            self.useNum2 = False
        else:
            self.UpdateLabel(self.num1 / self.num2)
            self.Ans = True
            self.num1 = self.num1 / self.num2
            self.num2 = 0
            self.useNum2 = False

def main():
    DTK.Begin("Calculator", "90x180")

    resultLabel = DTK.Label("0")
    Calc = Calculator(resultLabel)
    DTK.PlacePreviousWidget(x=0, y=0)
    DTK.FontPreviousWidget()

    DTK.Button("+", width=3)
    @DTK.ButtonFuncDef
    def Op(Event: any):
        Calc.HandleOp("+")
    DTK.PlacePreviousWidget(x=0, y=20)

    DTK.Button("-", width=3)
    @DTK.ButtonFuncDef
    def Op(Event: any):
        Calc.HandleOp("-")
    DTK.PlacePreviousWidget(x=30, y=20)

    DTK.Button("*", width=3)
    @DTK.ButtonFuncDef
    def Op(Event: any):
        Calc.HandleOp("*")
    DTK.PlacePreviousWidget(x=60, y=20)

    DTK.Button("/", width=3)
    @DTK.ButtonFuncDef
    def Op(Event: any):
        Calc.HandleOp("/")
    DTK.PlacePreviousWidget(x=90, y=20)

    DTK.Button("1", width=3)
    @DTK.ButtonFuncDef
    def AddNum(Event: any):
        Calc.HandleNum(1)
    DTK.PlacePreviousWidget(x=0, y=50)

    DTK.Button("2", width=3)
    @DTK.ButtonFuncDef
    def AddNum(Event: any):
        Calc.HandleNum(2)
    DTK.PlacePreviousWidget(x=30, y=50)

    DTK.Button("3", width=3)
    @DTK.ButtonFuncDef
    def AddNum(Event: any):
        Calc.HandleNum(3)
    DTK.PlacePreviousWidget(x=60, y=50)

    DTK.Button("CE", width=3)
    @DTK.ButtonFuncDef
    def Reset(Event: any):
        Calc.Reset()
    DTK.PlacePreviousWidget(x=90, y=50)

    DTK.Button("4", width=3)
    @DTK.ButtonFuncDef
    def AddNum(Event: any):
        Calc.HandleNum(4)
    DTK.PlacePreviousWidget(x=0, y=80)

    DTK.Button("5", width=3)
    @DTK.ButtonFuncDef
    def AddNum(Event: any):
        Calc.HandleNum(5)
    DTK.PlacePreviousWidget(x=30, y=80)

    DTK.Button("6", width=3)
    @DTK.ButtonFuncDef
    def AddNum(Event: any):
        Calc.HandleNum(6)
    DTK.PlacePreviousWidget(x=60, y=80)

    DTK.Button("+/-", width=3)
    @DTK.ButtonFuncDef
    def PosN(Event: any):
        Calc.PosNSwitch()
    DTK.PlacePreviousWidget(x=90, y=80)

    DTK.Button("7", width=3)
    @DTK.ButtonFuncDef
    def AddNum(Event: any):
        Calc.HandleNum(7)
    DTK.PlacePreviousWidget(x=0, y=110)

    DTK.Button("8", width=3)
    @DTK.ButtonFuncDef
    def AddNum(Event: any):
        Calc.HandleNum(8)
    DTK.PlacePreviousWidget(x=30, y=110)

    DTK.Button("9", width=3)
    @DTK.ButtonFuncDef
    def AddNum(Event: any):
        Calc.HandleNum(9)
    DTK.PlacePreviousWidget(x=60, y=110)


    DTK.Button("=", width=3)
    @DTK.ButtonFuncDef
    def Calculate(Event: any):
        Calc.Calculate()
    DTK.PlacePreviousWidget(x=90, y=110)

    DTK.Button("0", width=3)
    @DTK.ButtonFuncDef
    def AddNum(Event: any):
        Calc.HandleNum(0)
    DTK.PlacePreviousWidget(x=30, y=140)

    DTK.End()

if __name__ == "__main__":
    main()
