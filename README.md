# Min-Max-and-Alpha-Beta-Pruning-Tic-Tac-Toe
Project Description
This project implements two adversarial search algorithms - MiniMax and MiniMax with Alpha-Beta
Pruning - applied to the game of Tic-Tac-Toe. The program simulates both human vs. computer and
computer vs. computer gameplay. Algorithms are implemented exactly as per the pseudocode from
course lectures.

Algorithms Implemented
- MiniMax
- MiniMax with Alpha-Beta Pruning

Command Line Interface
Usage: python name.py ALGO FIRST MODE
ALGO: 1 = MiniMax, 2 = Alpha-Beta
FIRST: X or O
MODE: 1 = Human vs Computer, 2 = Computer vs Computer

Game Details
The 3x3 board is represented using positions 1 to 9. The user is prompted for moves and the
program validates inputs. On computer moves, it prints the selected move and number of nodes
generated.

Experimental Results
Nine games were run with each human first move. The number of nodes expanded by each
algorithm was recorded.
| Move | MiniMax Nodes | Alpha-Beta Nodes |
|------|----------------|-------------------|
| 1 | 60692 | 4821 |
| 2 | 65016 | 2842 |
| 3 | 60692 | 5061 |
| 4 | 64844 | 5037 |
| 5 | 56494 | 3213 |
| 6 | 65016 | 4821 |
| 7 | 60692 | 2004 |
| 8 | 65308 | 3222 |
| 9 | 60692 | 5011 |

Conclusion
Both algorithms correctly determine optimal moves in Tic-Tac-Toe. Alpha-Beta Pruning significantly
reduces the number of evaluated nodes, improving efficiency. It is preferred for larger games with
deeper trees.

FAQ
Q: What happens if I input an invalid move?
A: You'll be re-prompted until a valid input is provided.
Q: Can I quit mid-game?
A: Yes. Enter 0 when prompted to exit.

Author:
Anshul Dani
