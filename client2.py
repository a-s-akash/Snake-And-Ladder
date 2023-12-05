import socket
import tkinter as tk
from PIL import Image, ImageTk
import random

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('192.168.4.217' ,12346)
client_socket.connect(server_address)
#pc
#player1_Xlocs = [580, 712, 844, 976, 1108, 1240, 1240, 1108, 976, 844, 712, 580, 590, 712, 844, 976, 1108, 1240, 1240,1108, 976, 844, 712, 580, 580, 712, 844, 976, 1108, 1240, 490, 712, 844, 976, 1108, 1240]
#player_Ylocs = [730, 730, 730, 730, 730, 730, 610, 610, 610, 610, 610, 610, 490, 490, 490, 490, 490, 490, 370, 370,370, 370, 370, 370, 250, 250, 250, 250, 250, 250]
#player2_Xlocs = [640,772,904,1036,1168,1300,1300,1168,1036,904,772,640,640,772,904,1036,1168,1300,1300,1168,1036,904,772,640,640,772,904,1036,1168,1300,640,772,904,1036,1168,1300]
#lap
# player1_Xlocs = [420,552,684,816,948,1080,1080,948,816,684,552,420,420,552,684,816,948,1080,1080,948,816,684,552,420,420,552,684,816,948,1080]
# player_Ylocs =  [650,650,650,650,650,650,530,530,530,530,530,530,410,410,410,410,410,410,290,290,290,290,290,290,170,170,170,170,170,170]
# player2_Xlocs = [480,612,744,876,1008,1140,1140,1008,876,744,612,480,480,612,744,876,1008,1140,1140,1008,876,744,612,480,480,612,744,876,1008,1140]
#others
player1_Xlocs =[430,390,522,654,786,918,1050,1050,918,786,654,522,390,390,522,654,786,918,1050,1050,918,786,654,522,390,390,522,654,786,918,1050,390,522,654,786,918,1050]
player_Xlocs = [490,440,572,704,836,968,1100,1100,968,836,704,572,440,440,572,704,836,968,1100,1100,968,836,704,572,440,440,572,704,836,968,1100,440,572,704,836,968,1100]
player_Ylocs =  [730,640,640,640,640,640,640,510,510,510,510,510,510,380,380,380,380,380,380,250,250,250,250,250,250,120,120,120,120,120,120]
def on_button_click():
    run = random.randint(1, 6)
    message = f'{run}'
    new_image = ImageTk.PhotoImage(Image.open(f'{run}.jpg').resize((80, 80)))
    button.config(image=new_image)
    client_socket.send(message.encode('utf-8'))   
    where = client_socket.recv(1024).decode('utf-8')
    print (where,"2")
    if where=='a':
        lose(1)
    elif where=='b':
        won(1)
    player2.place(x=player_Xlocs[int(where)],y=player_Ylocs[int(where)])
    root.after(500, lambda: destroy_new_image(new_image))

def destroy_new_image(image):
    button.config(image=button_image)
    root.update_idletasks()
    recvv()

def recvv():
    print ("hello") 
    where = client_socket.recv(1024).decode('utf-8')
    print (where)
    if where == 'a':
        lose(1)
    elif where=='b':
        won()
    player1.place(x=player1_Xlocs[int(where)],y=player_Ylocs[int(where)])
def won():
    root.destroy()
    def on_button_click1():
        nm = entry1.get()
        ml = entry2.get()
        client_socket.send(nm.encode('utf-8'))
        client_socket.send(ml.encode('utf-8'))   
        window.destroy()
        lose(2)
    window = tk.Tk()
    window.config(bg="#1e1f1f")
    window.title("Snake-And-Ladder")
    window_width = 300
    window_height = 200
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    window.geometry(f"{window_width+120}x{window_height+90}+{x_position}+{y_position}")
    label11 = tk.Label(window, text="You Have Won the Match",font=("arial",25),fg="green",bg="#1e1f1f")
    label11.pack(pady=5)
    label1 = tk.Label(window, text="Enter Your Name",font=("arial",20),bg="#1e1f1f",fg="white")
    label1.pack(pady=5)
    entry1 = tk.Entry(window,font=("arial",20))
    entry1.pack(pady=5)
    label2 = tk.Label(window, text="Your Email-ID:",font=("arial",20),bg="#1e1f1f",fg="white")
    label2.pack(pady=5)
    entry2 = tk.Entry(window,font=("arial",20))
    entry2.pack(pady=5)
    button = tk.Button(window, text="  Submit  ", command=on_button_click1,font=("arial",12))
    button.pack(pady=10)
    label = tk.Label(window, text="")
    label.pack(padx=20, pady=20)
    window.mainloop()    
def lose(a):
    if a==1:
        root.destroy()
    def on_button_click2():
        window.destroy()
    window = tk.Tk()
    window.title("Snake-And-Ladder")
    window.config(bg="#1e1f1f")
    window_width = 300
    window_height = 200
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    window.geometry(f"{window_width+180}x{window_height-10}+{x_position}+{y_position}")
    if a==1:
        label = tk.Label(window, text="You have been lossed!",font=('arial',20),bg="#1e1f1f",fg="red")
    elif a==2:
        label = tk.Label(window, text="Shortly you will receive a mail!",font=('arial',20),bg="#1e1f1f",fg="white")
    label.pack(padx=50, pady=50)
    button = tk.Button(window, text="    OK    ", command=on_button_click2)
    button.pack(pady=10)
    window.mainloop()
root = tk.Tk()
root.title("Snake and Ladder")
root.attributes("-fullscreen", True)
background_image = ImageTk.PhotoImage(Image.open('a.jpg').resize((800, 600)))
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=0.9)
player1 = tk.Label(root, text=" A ", font=("Helvetica", 20), bg="white")
player1.place(x=430, y=730)
player2 = tk.Label(root, text=" B ", font=("Helvetica", 20), bg="white")
player2.place(x=490, y=730)
button_image = ImageTk.PhotoImage(Image.open('b.jpg').resize((80, 80)))
button = tk.Button(root, image=button_image, command=on_button_click)
button.place(relx=0.5, rely=0.90, anchor="center")
root.bind("<Escape>", lambda event: root.destroy())
root.after(100,recvv)
root.mainloop()