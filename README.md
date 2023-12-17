# Snake-And-Ladder

# Assembly_language

1. **Board Layout:**
   - The game board is displayed using ASCII characters, with the Snake and Ladder positions marked.
   - The layout is shown using a combination of characters and strings stored in the data segment.

2. **Players and Input:**
   - Player names are input at the beginning of the game.
   - Players are denoted as 'A' and 'B'.
   - Player turns are determined using the `who` variable.
   - Players input a number (1-6) to roll the dice and move forward on the board.

3. **Game Flow:**
   - The game continues until one of the players reaches or exceeds position 30.
   - The program checks the player's position and performs the necessary actions, such as climbing ladders or going down snakes.
   - Players take turns, and the game keeps track of their positions using the `where`, `ca`, and `cb` variables.

4. **Winning Condition:**
   - When a player reaches position 30, they are declared the winner.
   - The winner's name is displayed along with a congratulatory message.

5. **Printing and Output:**
   - The `print_str` subroutine is used to print strings to the screen.
   - The `position` subroutine updates the screen with the current positions of players.

6. **Data Segment:**
   - Strings for the game layout, player names, and various messages are stored in the data segment.
   - Arrays like `ac`, `ar`, `bc`, and `br` hold the information about the positions of snakes and ladders.

7. **Subroutines:**
   - Subroutines like `clr_set_a` and `clr_set_b` are used to clear the previous position of players and set their new positions.
   - The `string_input` subroutine is used to get player names from the user.

8. **Ending the Game:**
   - When the game ends, it displays a "Game Over" message and announces the winner.

9. **Trophy and Awards:**
   - Upon winning, the program displays a congratulatory message, and the winner's name is announced.

10. **Miscellaneous:**
    - The game uses a combination of jumps, loops, and condition checks to control the flow.
    - Int 10h is used for video services to display characters on the screen.
    - Int 21h is used for reading characters from the keyboard.

Please note that the code is written in x86 Assembly Language and may be executed in a DOS environment. Understanding assembly language requires familiarity with x86 architecture and instruction set.


# Python

1. **Server Code (server.py):**
   - The server creates two sockets (`server_socket1` and `server_socket2`) to listen for connections on different ports (12345 and 12346).
   - It accepts connections from two clients (`connection1` and `connection2`).
   - There are two players (`player1_loc` and `player2_loc`) who move on a Snake and Ladder board. The game continues until one of the players reaches position 30.
   - The `checksnakeandladder` function checks if a player has landed on a snake or ladder and adjusts their position accordingly.
   - The game logic is implemented using a loop where players take turns rolling a die (`run`) and moving on the board.

2. **Client 1 Code (client1.py):**
   - This client connects to the server using a socket on port 12345.
   - It uses Tkinter for the graphical user interface (GUI) to display the Snake and Ladder board.
   - When the player clicks the "Roll Dice" button, a random number is generated, and the client sends this value to the server.
   - The client receives the updated position from the server and moves the player on the board accordingly.
   - If a player reaches position 30, a window appears asking for the player's name and email. The server sends a certificate and email to the player.

3. **Client 2 Code (client2.py):**
   - Similar to Client 1 but connects to the server on port 12346.
   - It also has a GUI for the Snake and Ladder board and handles the game logic.

4. **Certificate Generation Code (certificate.py):**
   - Generates a certificate image using the Pillow library.
   - Takes a template image (`certi.png`) and adds the player's name to it.
   - Saves the modified image as `output.png`.

5. **Email Sending Code (emaill.py):**
   - Sends an email to the player using the smtplib library.
   - Attaches the certificate image to the email.
   - The email contains a congratulatory message.

In summary, this code implements a basic Snake and Ladder game with a server-client architecture. Players interact with the game through a graphical user interface, and the server manages the game state, communication, and certificate/email sending when a player wins.


# Output details

# For Assembly Code

![image](https://github.com/a-s-akash/Snake-And-Ladder/assets/149227673/3292a9fb-c8d4-44f6-934f-d95120b2f427)
![image](https://github.com/a-s-akash/Snake-And-Ladder/assets/149227673/24573e64-8743-4923-b1bf-b7aab6db7c02)

# For Python Code

**Server.py**

![image](https://github.com/a-s-akash/Snake-And-Ladder/assets/149227673/1f41e864-7484-4bcb-9567-e4a8d020cee7)
![image](https://github.com/a-s-akash/Snake-And-Ladder/assets/149227673/a20f94c2-47f3-4e6a-9272-3cbdb432f1fa)
![image](https://github.com/a-s-akash/Snake-And-Ladder/assets/149227673/f72171cb-42e7-4890-a8dc-8cd294498bde)
![image](https://github.com/a-s-akash/Snake-And-Ladder/assets/149227673/44dde36d-2024-486d-aaa7-f95c7b579abb)

**client1.py**

![image](https://github.com/a-s-akash/Snake-And-Ladder/assets/149227673/b71b4636-da7f-4836-8f5e-24327ee05fc0)
![image](https://github.com/a-s-akash/Snake-And-Ladder/assets/149227673/818cf50d-fa22-40f7-98f9-f18b6bf169e5)
![image](https://github.com/a-s-akash/Snake-And-Ladder/assets/149227673/2d359262-d668-4bc9-9dfc-1ec27f5fb695)
![image](https://github.com/a-s-akash/Snake-And-Ladder/assets/149227673/0851614a-431d-4b95-8699-6e05a2c4daa5)

**client2.py**

![image](https://github.com/a-s-akash/Snake-And-Ladder/assets/149227673/acd3da65-75dc-455f-b32c-6af79ff7e134)
![image](https://github.com/a-s-akash/Snake-And-Ladder/assets/149227673/c3dab938-cd4d-4d22-b95d-07b4ef291799)
![image](https://github.com/a-s-akash/Snake-And-Ladder/assets/149227673/bf556c3b-5257-4de9-96fe-e8cd049056c8)
![image](https://github.com/a-s-akash/Snake-And-Ladder/assets/149227673/d3336f59-eb09-444f-8ec6-cab22af8a265)
![image](https://github.com/a-s-akash/Snake-And-Ladder/assets/149227673/3d74c2f4-48f1-4fee-b36b-3516e97ce9d2)
![image](https://github.com/a-s-akash/Snake-And-Ladder/assets/149227673/5b355e2c-798e-447a-98f3-f562f7487fe9)
![image](https://github.com/a-s-akash/Snake-And-Ladder/assets/149227673/eed1e590-eec9-4f7e-9054-948ad017344c)
![image](https://github.com/a-s-akash/Snake-And-Ladder/assets/149227673/b3f018da-295f-475c-bee0-1a38d61c10a1)

















