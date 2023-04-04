from tkinter import * 
import random

rt=Tk()

rt.title("Random Number Generator")
rt.geometry("500x500")

items_list = Label(rt)
random_numbers = Label(rt)

list1= ["camera","light snacks","mosquito spray","water bottle","sunscreen"]
items_list["text"] = "Listed Items : " + str(list1)
