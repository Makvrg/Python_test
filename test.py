from tkinter import *
import requests
import random
reliefs = [SUNKEN, RAISED, GROOVE, RIDGE, FLAT]

#print(random.choice([1, 2]))
print('566')
class ButtonsApp(Tk):
    def __init__(self):
        super().__init__()
        self.img = PhotoImage(file="Voiceless_palato-alveolar_fricative_(vector).svg.png")
        self.btn = Button(self, text="Кнопка с изображением", image=self.img, compound=LEFT, command=self.disable_btn)
        self.btn.pack()
        for r in reliefs:
            self.create_btn(r)
        #for btn in self.btns:
            #btn.pack(padx=10, pady=10, side=LEFT)

    def create_btn(self, relief):
        Button(self, text=relief, relief=relief).pack(padx=10, pady=10, side=LEFT)

    def disable_btn(self):
        self.btn.config(state=DISABLED)


if __name__ == '__main__':
    app = ButtonsApp()
    #app.create_btn(SUNKEN)
    app.mainloop()
