class String:
    def __init__(self):       
        self.s = ""
    def getString(self):
        self.s = input("Введите строку: ")
    def printString(self):
        print(self.s.upper())
handler = String()
handler.getString() 
handler.printString() 