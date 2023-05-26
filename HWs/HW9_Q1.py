#
# Create and test a class called lamp.
# This class should have the state of either being on or off,
# and have a switch that if the light is off, it will turn it on,
# and if the light is on, it will turn it off.
#

class lamp:
    def __init__(self, light):
        self._light = light

    def switch(self):
        if self._light == 'off':
            self._light = 'on'
        else:
            self._light = 'off'


