#!/usr/bin/python

""" Startup script to initialize pwm channels

The flight controller failsafe triggers if signal parameters (freq, duty cycle)
fall outside a certain range. This script initializes the signals to be within
the accepted range.
"""

import Adafruit_PCA9685

TGT_PERIOD = 0.022 # target period (s)
MIN_W = 0.0011     # positive pulse width (s) for min value
MID_W = 0.0015     # positive pulse width (s) for mid value
MAX_W = 0.0019     # positive pulse width (s) for max value

TICKS = 4096       # 4096 ticks per period

k = 0.023/0.022    # calibrate to your specific feather board

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(1./(0.022*k)) # 22ms period
pwm.set_all_pwm(0, int(TICKS*(MID_W/TGT_PERIOD)))
