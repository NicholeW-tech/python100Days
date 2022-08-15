from tkinter import *

window = Tk()
window.title("Mile to Km converter")
window.minsize(width=500,height=380)
window.config(padx=100, pady=200)
def button_clicked():
    num = input.get()
    ans = round(int(num) * 1.6)
    ans = str(ans)
    print(ans)
    my_label3.config(text=ans)



my_label1 = Label(text="Miles", font=("Ariel", 24))
my_label1.grid(column=2, row=0)

input = Entry(width=10)
input.grid(column=1, row=0)
input.get()


my_label2 = Label(text="is equal to", font=("Ariel", 24))
my_label2.grid(column=0, row=1)


my_label3 = Label(text="0", font=("Ariel", 24))
my_label3.grid(column=1, row=1)


my_label4 = Label(text="Km", font=("Ariel", 24))
my_label4.grid(column=2, row=1)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)





window.mainloop()
