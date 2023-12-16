# Snake-And-Ladder

Your assembly language program is a simple Snake and Ladder game. Here's an overview of the key components and functionality in your code:

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
