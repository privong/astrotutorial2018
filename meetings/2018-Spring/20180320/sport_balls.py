#!/usr/bin/env python3
"""
Have the user input the size of a ball and figure out what type it is.
"""

import numpy as np


def main():
    """
    main routine
    """

    # ball sizes from https://www.topendsports.com/resources/equipment-ball-size.htm
            #type    Dmin   Dmax
    balls = [('golf', 42.67, np.nan),
             ('pool', 57.15, 60.33),
             ('tennis', 65.41, 68.58),
             ('baseball', 73, 76),
             ('volleyball', 207, 213),
             ('basketball', 238.8, np.nan)]

    diam = input("What diameter is the ball? ")

    diam = float(diam)

    thisball = None

    for ball in balls:
        if np.isnan(ball[2]):
            if diam == ball[1]:
                thisball = ball[0]
                continue
            else:
                continue
        if ball[1] <= diam and ball[2] >= diam:
            thisball = ball[0]
            continue

    if thisball:
        print("The ball is a " + thisball)
    else:
        print("I don't know what kind of ball you have.")


if __name__ == "__main__":
    main()
