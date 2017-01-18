import Tkinter as tk

def show_values():
    print (w1.get(), w2.get())

master = tk.Tk()
w1 = tk.Scale(master, from_=0, to=42, tickinterval=8)
w1.set(19)
w1.pack()
w2 = tk.Scale(master, from_=0, to=200,tickinterval=10, orient=tk.HORIZONTAL)
w2.set(23)
w2.pack()
tk.Button(master, text='Show', command=show_values).pack()

counter = 0 
def counter_label(label):
  counter = 0
  def count():
    global counter
    counter += 1
    label.config(text=str(counter))
    label.after(1000, count)
  count()
 
master.title("Counting Seconds")
label = tk.Label(master, fg="dark green")
label.pack(side=tk.LEFT)
counter_label(label)
button = tk.Button(master, text='Stop', width=25, command=master.destroy)
button.pack()
master.mainloop()
