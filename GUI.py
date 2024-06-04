#import the library
import tkinter as tk
import automation

root = tk.Tk()
root.title('Aplication')
root.geometry('700x500')

label = tk.Label(root, text='put your link here')
label.pack()
textArea = tk.Text(root, height=1)
textArea.pack()
sendButton = tk.Button(root, text='Send', command=lambda: automation.callBoth(textArea.get(1.0, tk.END)))
sendButton.pack()

root.mainloop()