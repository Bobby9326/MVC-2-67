# app.py
import tkinter as tk
from View import PetView
from Model import PetModel
from Controller import PetController

def main():
    root = tk.Tk() 
    model = PetModel() # สร้าง model
    view = PetView(root) # สร้าง view
    controller = PetController(model, view) # สร้าง controllerโดยส่ง model และ  view
    root.mainloop()

if __name__ == "__main__":
    main()