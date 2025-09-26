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
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with "sc8pr3-gallery".  If not, see <http://www.gnu.org/licenses/>.


# Ensure main.py is in current directory...
import os
os.chdir(os.path.split(__file__)[0])

from sc8pr import Sketch, Image, LEFT, BOTTOM
from sc8pr.sprite import Sprite
from sc8pr.text import Text, Font
from sc8pr.gui.button import Button
from sc8pr.gui.radio import Radio
import asterShield, electric, fakeCursor, chimp, park, \
    soccer, rockPaperScissors, ticTacToe, hanoi, transition

descriptions = [
    "Destroy the asteroids before\nthey destroy your spaceship",
    "A physics simulation\nabout Coulomb’s Law",
    "Demo of an animated cursor",
    "Recreation of the “Monkey Fever”\nexercise from the pygame tutorial.\nDifficult to play remotely due to\nmouse delay!",
    "Park the robot without crashing or\nprogram the robot to park by itself",
    "Play soccer against a robot or\nprogram the robot to play by itself",
    "Rock beats scissors.\nScissors beats paper.\nPaper beats rock.",
    "Get three X’s or O’s in a row",
    "An animated solution to the\nrecursive disk-moving problem",
    "Demo of sc8pr 3’s transition effects"
]

def demo_dialog(sk):   # sk is the sketch
    "Create a dialog for the user to choose a demo"
    font = {"font": Font.sans(), "fontSize": 16}

    # Make radio buttons for each demo
    labels = ("Asteroid Shield", "Electric Force", "Fake Cursor", "Monkey Fever",
        "Robot Parking", "Robot Soccer", "Rock-Paper-Scissors", "Tic-Tac-Toe",
        "Towers of Hanoi", "Transition Effects")
    radio = Radio(labels, txtConfig=font).bind(onchange)

    # Adjust sketch size if necessary and position radios
    hMin = radio.height + 16
    if sk.height < hMin: sk.size = (sk.width, hMin)
    x, y = sk.center
    sk["Radio"] = radio.config(pos=(8, y), anchor=LEFT)

    # Create Text object for description
    x += sk[0].width / 2 + 16
    sk["Text"] = Text(descriptions[0]).config(pos=(x, y-40), **font)

    # Create 'Play' Button
    icon = Sprite(Image.fromZip("ship", "img.data")).config(spin=0.5)
    button = Button((128, 48), 2).textIcon("Play", icon)
    button[-1].config(**font)  # Specify font for button text
    y += hMin / 2 - 12
    sk["Play"] = button.config(pos=(x, y), anchor=BOTTOM).bind(onaction)

    # Do not re-run this setup!
    sk.bind(setup=None)

def onchange(radio, ev):
    "Change the description when a new radio button is selected"
    text = descriptions[radio.selected.layer]
    radio.sketch["Text"].config(data=text)

def onquit(sk, ev):
    "Quit the program"
    sk.quit = True
    sk.running = False

def onaction(button, ev):
    "Close the dialog when the 'Play' button is clicked"
    button.sketch.quit = True

def main():
    "Display the choices and then run the selected demo"
    modules = (asterShield, electric, fakeCursor, chimp, park,
        soccer, rockPaperScissors, ticTacToe, hanoi, transition)
    sk = Sketch((640, 240)).config(running=True)
    sk.bind(onquit, setup=demo_dialog)
    while sk.running:
        sk.play("sc8pr 3.0 Gallery", mode=False).config(quit=False)
        if sk.running:
            sk["Play"].status = 0
            choice = sk["Radio"].selected.layer
            modules[choice].play()

main()
