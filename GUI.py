#import the library
import tkinter as tk

root = tk.Tk()
root.title('Aplication')
root.geometry('700x500')

label = tk.Label(root, text='put your link here')
label.pack()
textArea = tk.Text(root, height=1)
textArea.pack()

root.mainloop()