import socket
import tkinter as tk
from PIL import Image, ImageTk
import random
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('192.168.215.217', 12346)
client_socket.connect(server_address)
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
    player2.place(x=player_Xlocs[int(where)],y=player_Ylocs[int(where)])
    where = client_socket.recv(1024).decode('utf-8')
    player2.place(x=player_Xlocs[int(where)],y=player_Ylocs[int(where)])
    root.after(500, lambda: destroy_new_image(new_image))
    
def recvv():
    where = client_socket.recv(1024).decode('utf-8')
    player1.place(x=player1_Xlocs[int(where)],y=player_Ylocs[int(where)])
    where = client_socket.recv(1024).decode('utf-8')
    player1.place(x=player1_Xlocs[int(where)],y=player_Ylocs[int(where)])
    
    button.config(state = tk.Normal)
    
def destroy_new_image(image):
    button.config(image=button_image)
    root.update_idletasks()
    recvv()

    
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
root.mainloop()
recvv()