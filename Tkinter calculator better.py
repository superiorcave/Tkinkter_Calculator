from tkinter import *

root=Tk()

root.title("Cal")
class Button_c:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def draw(self):
        button = Button(root, text = self.name , command = self.func)
        button.grid(row = self.x, column = self.y)

    def func(self):
        if self.name != 'c' and self.name != '=':
            old = label.cget('text')
            new = str(old) + self.name
            label.config(text = new)
        elif self.name == 'c':
            label.config(text = '')
        else:
            ans = eval(label.cget('text'))
            label.config(text = ans)


label = Label(root, text = '', font = ('Arial', 12, 'bold'))
label.grid(row = 0, column = 0)

c = Button_c('c', 0, 3)
c.draw()


arr = [
['1', '2', '3', '+'],
['4', '5', '6', '-'],
['7', '8', '9', '*'],
['0', '.', '=', '/']
]

for i in range(len(arr)):
    for j in range(len(arr[i])):
        x = Button_c(arr[i][j], i+1, j)
        x.draw()
        

root.mainloop()
