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

"""

This program demonstrates how a Graphic can be used in place of a cursor.

"""

from sc8pr import Sketch, Image
from sc8pr.sprite import Sprite

class FakeCursor(Sketch):

    @staticmethod
    def updateFakeCursor(gr, ev=None):
        "Follow the mouse"
        gr.config(pos=gr.sketch.mouse.pos, layer=-1)

    def fakeCursor(self, gr):
        "Use a graphic to mimic the cursor"
        self.cursor = False
        self += gr.bind(ondraw=self.updateFakeCursor).config(hoverable=False, wrap=0)

    def setup(self):
        gr = Sprite(Image.fromZip("ship", "img.data")).config(width=32, spin=1)
        self.fakeCursor(gr)

def play(): FakeCursor().play("Fake Cursor")

if __name__ == "__main__": play()
