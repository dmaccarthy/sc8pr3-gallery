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
Robot Parking Simulation from sc8pr 2.2 and 3.0

For remote control, use your arrow keys to adjust the yellow robot’s motors and the space bar to stop.
"""

from sc8pr.robot.park import ParkingLot

def brain(robot):
    """Complete this function to control the robot.
        Pass this function to the 'ParkingLot.run'
        function below as its only argument.
    """
    robot.motors = 0.2, -0.2
    while robot.active:
        robot.updateSensors()

def play():
    "Run the simulation"
    print(__doc__)
    ParkingLot.run(
        # brain   # Omit for remote control
    )

if __name__ == "__main__": play()
