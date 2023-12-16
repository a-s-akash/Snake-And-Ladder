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
