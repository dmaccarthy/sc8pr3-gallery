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

from sc8pr import Sketch, Image, BOTTOM, TOP
from sc8pr.sprite import Sprite
from sc8pr.text import Text, Font
from sc8pr.effect import Assemble, Dissolve, Squash, Tint, Pixelate, Checkerboard, Bar
from sc8pr.effect.math import Noise, ClockHand, Wedge, Wipe, PaintDrops, Waves
from sc8pr.effect.stamp import Pupil, Spiral

DT = 150

def setup(sk):
    font = dict(font=Font.mono(), fontSize=36, color="red")
    sk.bg = "#e0e0ff"
    sk.effectList = [
        [Dissolve().time(0, DT), ClockHand().time(2*DT, DT)],
        [Pupil().time(2*DT, 3*DT), Checkerboard().time(4*DT, 3*DT)],
        [Noise().time(4*DT, 5*DT), Wipe().time(6*DT, 5*DT)],
        [Waves().time(6*DT, 7*DT), Wedge().time(8*DT, 7*DT)],
        [Squash(BOTTOM).time(8*DT, 9*DT), Pixelate().time(10*DT, 9*DT), Tint().time(10*DT, 9*DT)],
        [Bar().time(10*DT, 11*DT), Assemble().time(12*DT, 11*DT)],
        [PaintDrops(24).time(12*DT, 13*DT), Spiral().time(14*DT, 13*DT)],
        [Tint().time(14*DT, 15*DT), Tint().time(16*DT, 15*DT)]
    ]
    sk.textList = [
        "Dissolve", "ClockHand", "Pupil", "Checkerboard", "Noise", "Wipe", "Waves",
        "Wedge", "Squash", "Pixelate", "Bar", "Assemble", "PaintDrops", "Spiral", "Tint", "Tint"
    ]
    sk.quitTime = DT * len(sk.textList)
    w, h = sk.size
    imgs = Image.fromZip("aliens", "img.data").tiles(2, 2)
    sk += Sprite(imgs).config(
        height = 0.7 * h,
        pos = (w / 2, h - 12),
        anchor = BOTTOM,
        costumeTime = 15,
        costumeSequence = (0, 0, 1, 2, 3, 3, 2, 1, 0),
        effects = sk.effectList[0]
    )
    sk += Text(sk.textList[0]).config(
        pos = (w / 2, 18),
        anchor = TOP,
        **font
    )

def ondraw(sk, ev):
    f = sk.frameCount
    if f >= sk.quitTime:
        sk.purge()
        if f == sk.quitTime + DT // 3:
            sk.quit = True
    else:
        i = f // DT
        if f % DT == 0 and i < len(sk.textList):
            if i % 2 == 0:
                sk[0].effects = sk.effectList[i//2]
            sk[1].config(data=sk.textList[i])
    
def play():
    Sketch().bind(setup, ondraw).play(caption="sc8pr 3 Effects", mode=False)

if __name__ == "__main__": play()
