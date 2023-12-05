import socket
from certificate import certi
from emaill import mailer
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
while True:
    if player1_loc != 30 and player2_loc != 30:
        current += 1
        further = 0
        if current % 2 == 0:
            print("jaya")
            run = connection1.recv(1024).decode('utf-8')
            run = int(run)
            print("run:",run)
            if astarted == 0:
                if run == 1:
                    astarted = 1
            if astarted == 1:
                if player1_loc+run <= 30:
                    player1_loc+=run
                    player1_loc_ = checksnakeandladder(player1_loc)
                    response = f'{player1_loc_}'
                    connection1.send(response.encode('utf-8'))
                    connection2.send(response.encode('utf-8'))
                    player1_loc = player1_loc_
                else:
                    response = f'{player1_loc}'
                    connection1.send(response.encode('utf-8'))
                    connection2.send(response.encode('utf-8'))
            else:
                response = f'{player1_loc}'
                connection1.send(response.encode('utf-8'))
                connection2.send(response.encode('utf-8'))
        else:
            print("Boopal")
            run = connection2.recv(1024).decode('utf-8')
            run = int(run)
            print("run:",run)
            if bstarted == 0:
                if run == 1:
                    bstarted = 1
            if bstarted == 1:
                if player2_loc+run <= 30:
                    player2_loc += run
                    player2_loc_ = checksnakeandladder(player2_loc)
                    response = f'{player2_loc_}'
                    connection2.send(response.encode('utf-8'))
                    connection1.send(response.encode('utf-8'))
                    player2_loc = player2_loc_
                else:
                    response = f'{player2_loc}'
                    connection2.send(response.encode('utf-8'))
                    connection1.send(response.encode('utf-8'))
            else:
                response = f'{player2_loc}'
                connection2.send(response.encode('utf-8'))
                connection1.send(response.encode('utf-8'))
    else:
        if player1_loc == 30:
            response = 'a'
            connection1.send(response.encode('utf-8'))
            connection2.send(response.encode('utf-8'))
            nm = connection1.recv(1024).decode('utf-8')
            ml = connection1.recv(1024).decode('utf-8')
        elif player2_loc == 30:
            response = 'b'
            connection2.send(response.encode('utf-8'))
            connection1.send(response.encode('utf-8'))
            nm = connection2.recv(1024).decode('utf-8')
            ml = connection2.recv(1024).decode('utf-8')
        certi(nm)
        mailer(nm,ml)