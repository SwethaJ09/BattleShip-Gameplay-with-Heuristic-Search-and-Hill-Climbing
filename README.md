# Battleship Game with AI  

This project is a Python implementation of the classic Battleship game, enhanced with AI capabilities using heuristic search algorithms and hill climbing for strategic decision-making.  

## Features  
- **Randomized Ship Placement:** Ships are placed randomly with no overlaps.  
- **Turn-Based Gameplay:** Players take turns making moves, aiming to sink all opponent ships.  
- **AI Strategies:**  
  - *Random AI*: Chooses moves randomly.  
  - *Basic AI*: Considers hits, misses, and proximity to optimize moves.  
- **Interactive GUI:** Built with Pygame, offering an intuitive interface for players.  

## How to Play  

### Prerequisites  
1. Install Python 3.9+  
2. Install Pygame using pip:  
   ```bash
   pip install pygame
Gameplay Instructions
Start the Game:

Ships are automatically placed on the game board.
The game begins with Player 1's turn (human or AI).
Making Moves:

Click on the grid squares to guess where the opponent’s ships are hidden.
The result of your guess will be displayed:
Hit (H): Successful hit on an opponent's ship.
Miss (M): The guess missed any ship.
Sink (S): You sank an opponent's ship.
AI Moves:

The computer will make moves based on its selected strategy (Random or Basic AI).
Game Over:

The game ends when one player successfully sinks all opponent ships.
Restart or Quit
Press Return to restart the game.
Press Escape to quit.
Key Bindings
Left Mouse Click: Make a move on the selected grid.
Spacebar: Pause or resume the game.
Return Key: Restart the game.
Escape Key: Quit the game.
