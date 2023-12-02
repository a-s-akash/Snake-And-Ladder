import tkinter as tk
from certificate import certi
from emaill import mailer
def submit():
    nm = entry1.get().title()
    ml = entry2.get()
    window.destroy()
    certi(nm)
    mailer(nm,ml)
window = tk.Tk()
window.title("Winner-details")
window_width = 470
window_height = 200
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
entry1_label = tk.Label(window, text="Name",font=('arial',20))
entry1_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry1 = tk.Entry(window,font=('arial',20))
entry1.grid(row=0, column=1, padx=10, pady=10, sticky="w")
entry2_label = tk.Label(window, text="Email ID",font=('arial',20))
entry2_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
entry2 = tk.Entry(window,font=('arial',20))
entry2.grid(row=1, column=1, padx=10, pady=10, sticky="w")
submit_button = tk.Button(window, text="Submit", command=submit,font=('arial',20))
submit_button.grid(row=2, column=0, columnspan=2, pady=10)
window.mainloop()