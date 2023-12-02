import tkinter as tk
from PIL import Image, ImageTk
import random
import socket
server_socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address1 = ('0.0.0.0', 12345)
server_address2 = ('0.0.0.0', 12346)
server_socket1.bind(server_address1)
server_socket2.bind(server_address2)
server_socket1.listen(1)
server_socket2.listen(1)
connection1, client_address1 = server_socket1.accept()
connection2, client_address2 = server_socket2.accept()

print("Connected to", client_address1)
print("Connected to", client_address2)
player1_loc = player2_loc = pos = 0
astarted = bstarted = 0
current = -1

#pc
player1_Xlocs = [580, 712, 844, 976, 1108, 1240, 1240, 1108, 976, 844, 712, 580, 590, 712, 844, 976, 1108, 1240, 1240,1108, 976, 844, 712, 580, 580, 712, 844, 976, 1108, 1240, 490, 712, 844, 976, 1108, 1240]
player_Ylocs = [730, 730, 730, 730, 730, 730, 610, 610, 610, 610, 610, 610, 490, 490, 490, 490, 490, 490, 370, 370,370, 370, 370, 370, 250, 250, 250, 250, 250, 250]
player2_Xlocs = [640,772,904,1036,1168,1300,1300,1168,1036,904,772,640,640,772,904,1036,1168,1300,1300,1168,1036,904,772,640,640,772,904,1036,1168,1300,640,772,904,1036,1168,1300]
#lap
# player1_Xlocs = [420,552,684,816,948,1080,1080,948,816,684,552,420,420,552,684,816,948,1080,1080,948,816,684,552,420,420,552,684,816,948,1080]
# player_Ylocs =  [650,650,650,650,650,650,530,530,530,530,530,530,410,410,410,410,410,410,290,290,290,290,290,290,170,170,170,170,170,170]
# player2_Xlocs = [480,612,744,876,1008,1140,1140,1008,876,744,612,480,480,612,744,876,1008,1140,1140,1008,876,744,612,480,480,612,744,876,1008,1140]

def checksnakeandladder(pos):
    if pos == 17:
        return 4
    elif pos == 19:
        return 7
    elif pos == 21:
        return 9
    elif pos == 27:
        return 1
    elif pos == 3:
        return 22
    elif pos == 5:
        return 8
    elif pos == 11:
        return 26
    elif pos == 20:
        return 29
    else:
        return pos

# def checksnakeandladder(pos):
#     if pos == 17:
#         return [8,9,4]
#     elif pos == 19:
#         return [18,7]
#     elif pos == 21:
#         return [16,15,10,9]
#     elif pos == 27:
#         return [22,23,24,13,12,1]
#     elif pos == 3:
#         return [10,15,22]
#     elif pos == 5:
#         return [8]
#     elif pos == 11:
#         return [14,23,26]
#     elif pos == 20:
#         return [29]
#     else:
#         return 'pos'

#def on_button_click():
while True:
    #global player1_loc, player2_loc, current, player1_Xlocs, player_Ylocs, player2_Xlocs, astarted, bstarted, further

    if player1_loc < 30 and player2_loc < 30:
        current += 1
        #run = random.randint(1, 6)
        #new_image = ImageTk.PhotoImage(Image.open(f'{run}.png').resize((80, 80)))
        #button.config(image=new_image)
        further = 0
        if current % 2 == 0:
            run = connection1.recv(1024).decode('utf-8')
            run = int(run)
            if astarted == 0:
                if run == 1:
                    astarted = 1
                else:
                    response = f'{player1_loc}'
                    connection1.send(response.encode('utf-8'))
                    connection1.send(response.encode('utf-8'))
                    connection2.send(response.encode('utf-8'))
                    connection2.send(response.encode('utf-8'))
            if astarted == 1:
                if player1_loc+run < 30:
                    #move_player(player1, player1_Xlocs, player_Ylocs,player1_loc,player1_loc+run)
                    #player1.place(x=player1_Xlocs[player1_loc+run],y=player_Ylocs[player1_loc+run])
                    response = f'{player1_loc+run}'
                    connection1.send(response.encode('utf-8'))
                    connection2.send(response.encode('utf-8'))
                    player1_loc += run
                    player1_loc_ = checksnakeandladder(player1_loc)
                    #snkldr(player1, player1_Xlocs, player_Ylocs,player1_loc_,0)
                    #player1.place(x=player1_Xlocs[player1_loc_],y=player_Ylocs[player1_loc_])
                    response = f'{player1_loc_}'
                    connection1.send(response.encode('utf-8'))
                    connection2.send(response.encode('utf-8'))
                    player1_loc = player1_loc_
                else:
                    player1_loc -= run
        else:
            run = connection2.recv(1024).decode('utf-8')
            run = int(run)
            if bstarted == 0:
                if run == 1:
                    bstarted = 1
                else:
                    response = f'{player2_loc}'
                    connection2.send(response.encode('utf-8'))
                    connection2.send(response.encode('utf-8'))
                    connection1.send(response.encode('utf-8'))
                    connection1.send(response.encode('utf-8'))
            if bstarted == 1:
                if player2_loc+run < 30:
                    #move_player(player2, player2_Xlocs, player_Ylocs,player2_loc,player2_loc+run)
                    #player2.place(x=player2_Xlocs[player2_loc+run],y=player_Ylocs[player2_loc+run])
                    response = f'{player2_loc+run}'
                    connection2.send(response.encode('utf-8'))
                    connection1.send(response.encode('utf-8'))
                    player2_loc += run
                    player2_loc_ = checksnakeandladder(player2_loc)
                    #snkldr(player2, player2_Xlocs, player_Ylocs,player2_loc_,0)
                    #player2.place(x=player2_Xlocs[player2_loc_],y=player_Ylocs[player2_loc_])
                    response = f'{player2_loc_}'
                    connection2.send(response.encode('utf-8'))
                    connection1.send(response.encode('utf-8'))
                    player2_loc = player2_loc_
                else:
                    player2_loc -= run
        #root.after(500, lambda: destroy_new_image(new_image))
        #if player1_loc ==29 or player2_loc ==29:
            #root.after(500, lambda: root.destroy())
            

def snkldr(player, xs , ys , paths , it):
    if it<len(paths):
        print(paths[it])
        player.place(x=xs[paths[it]], y=ys[paths[it]])
        root.after(500, lambda: snkldr(player, xs , ys , paths, it+1))

def move_player(player, xs , ys , fromm , target):
    if fromm <= target:
        print(fromm,'>')
        player.place(x=xs[fromm], y=ys[fromm])
        root.after(5, lambda: move_player(player, xs , ys , fromm+1 , target))

def destroy_new_image(image):
    button.config(image=button_image)
    root.update_idletasks()

# root = tk.Tk()
# root.title("Snake and Ladder")
# root.attributes("-fullscreen", True)
# background_image = ImageTk.PhotoImage(Image.open('a.jpg').resize((800, 600)))
# background_label = tk.Label(root, image=background_image)
# background_label.place(x=0, y=0, relwidth=1, relheight=0.9)
# player1 = tk.Label(root, text=" A ", font=("Helvetica", 20), bg="white")
# player1.place(x=430, y=730)
# player2 = tk.Label(root, text=" B ", font=("Helvetica", 20), bg="white")
# player2.place(x=490, y=730)
# button_image = ImageTk.PhotoImage(Image.open('b.jpg').resize((80, 80)))
# button = tk.Button(root, image=button_image, command=on_button_click)
# button.place(relx=0.5, rely=0.90, anchor="center")
# root.bind("<Escape>", lambda event: root.destroy())
# root.mainloop()

# i = 0
# while True:
#     if i % 2 == 0:
#         data = connection1.recv(1024).decode('utf-8')
#         if not data:
#             break
#         print("Receiver:", data)
#         response = input("Sender: ")
#         connection1.send(response.encode('utf-8'))
#     else:
#         data = connection2.recv(1024).decode('utf-8')
#         if not data:
#             break
#         print("Receiver:", data)
#         response = input("Sender: ")
#         connection2.send(response.encode('utf-8'))
#     i += 1