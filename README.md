Py-Pong

Py-Pong is a classic Pong game implemented in Python using the Turtle module.
Overview

Py-Pong is a recreation of the classic Pong game, where players control paddles to hit a ball back and forth across the screen. The goal is to prevent the ball from passing beyond your paddle while trying to score points by making the ball pass beyond the opponent's paddle.

Key Features:

  Paddle Movement: Players control the movement of their paddles using designated keys.
  Ball Bouncing: The ball bounces off the paddles and walls, changing its direction accordingly.
  Score Tracking: The game keeps track of each player's score, updating it whenever a player scores a point.
  Game Over: The game continues until one player reaches a predetermined score limit, at which point the game ends.

How to Play:

  Run the game using python main.py.
  Control the right paddle using the "Up" and "Down" arrow keys.
  Control the left paddle using the "W" and "S" keys.
  Hit the ball with your paddle to prevent it from passing beyond your side of the screen.
  Try to score points by making the ball pass beyond your opponent's paddle.
  The game ends when one player reaches the score limit.

Implementation Details:

The game is implemented using the following classes:

  Paddle Class: Represents the paddles controlled by each player. Paddles can move up and down to hit the ball.
  Ball Class: Represents the ball that moves around the screen and bounces off paddles and walls.
  Scoreboard Class: Tracks and displays the scores of both players.
  Line Class: Draws the center line on the game screen.
