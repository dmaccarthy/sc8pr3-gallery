# Copyright 2015-2025 D.G. MacCarthy <http://dmaccarthy.github.io>
#
# This file is part of "sc8pr3-gallery".
#
# "sc8pr3-gallery" is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# "sc8pr3-gallery" is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with "sc8pr3-gallery". If not, see <http://www.gnu.org/licenses/>.

from sc8pr import Sketch, Image, Graphic, CENTER
from sc8pr.shape import Line
from sc8pr.sprite import CostumeImage
from sc8pr.gui.dialog import MessageBox
from sc8pr.misc.cursors import cross, circle
from sc8pr.util import ondrag

TITLE = "Tic-Tac-Toe"

def setup(game):
    "Create Tic-Tac-Toe board with 100 pixel squares and 20 pixel margins"

    # Load costumes for X's and O's, and logo
    img = Image.fromZip("xo", "img.data").tiles(3)
    game.alien = Image.fromZip("alien").config(height=36)

    # Create and position X's and O's, one per square
    for s in range(9):
        pos = 70 + 100 * (s % 3), 70 + 100 * (s // 3)
        game += CostumeImage(img).bind(contains=Graphic.contains,
            onclick=clickSquare).config(pos=pos, width=100)

    # Draw the board and start game
    for pts in [((20,120), (320,120)), ((20,220), (320,220)),
        ((120,20), (120,320)), ((220,20), (220,320))]: game += Line(*pts)
    startGame(game)

def setCursor(game):
    n = 0 if game.playerWin else game.playerTurn
    game.cursor = [True, cross, circle][n]

def startGame(game):
    "Set initial game state"
    game.playerWin = None
    game.playerTurn = 1
    for sp in game.instOf(CostumeImage): sp.costumeNumber = 0
    setCursor(game)

def clickSquare(sq, ev):
    "Handle CLICK events on any square"
    if sq.costumeNumber == 0: # Square is vacant?
        game = sq.sketch

        # Assign square to current player
        n = game.playerTurn
        sq.costumeNumber = n

        # Check for game over
        squares = list(game.instOf(CostumeImage))
        if winner(squares, n): game.playerWin = n
        elif 0 not in [sp.costumeNumber for sp in squares]:
            game.playerWin = 0
        else:
            game.playerTurn = 3 - n
            setCursor(game)

def winner(squares, n):
    "Check if player n occupies 3 squares in a row"
    for sq in [(0,1,2), (3,4,5), (6,7,8), (0,3,6),
            (1,4,7), (2,5,8), (0,4,8), (2,4,6)]:
        if sum(1 for s in sq if squares[s].costumeNumber == n) == 3:
            return True

def ondraw(game, ev=None):
    "Check game over status after each frame"
    n = game.playerWin
    if n is not None:
        setCursor(game)
        gameover(game, n)
        game.playerWin = None

def gameover(game, n):
    "Compose Game Over dialog"
    msg = "Player {} Wins".format(n) if n else "It's a draw"
    msg += "!\nDo you want to play again?"
    game["Cover"] = game.cover()
    game.cursor = True
    img = game.alien
    dlg = MessageBox(msg, buttons=["Yes","No"], align=CENTER).bind(onaction,
        ondrag).title("Game Over").config(pos=game.center)
    game += dlg.insertTop(img)

def onaction(msgbox, ev):
    "Game Over dialog event handler"
    game = msgbox.sketch
    game -= msgbox, game["Cover"]
    if msgbox.command.layer: game.quit = True
    else: startGame(game)

def play(): Sketch((340,340)).bind(setup, ondraw).play(TITLE)

if __name__ == "__main__": play()
