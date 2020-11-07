# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import time

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x=100
y=100
z=100
mc.player.setTilePos(x,y,z)
time.sleep(3)
y = y + 100
mc.player.setTilePos(x,y,z)