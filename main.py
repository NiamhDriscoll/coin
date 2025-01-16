def on_gesture_shake():
    global Flip_coin
    basic.show_leds("""
        . # # # .
        # . . . #
        # . # . #
        # . . . #
        . # # # .
        """)
    basic.pause(100)
    basic.show_leds("""
    . . # . .
    . . # . .
    . . # . .
    . . # . .
    . . # . .
    """)
    basic.pause(100)
    basic.show_leds("""
    . # # # .
    # . # . #
    # # # # #
    # . # . #
    . # # # .
    """)
    basic.pause(100)
    basic.show_leds("""
    . . # . .
    . . # . .
    . . # . .
    . . # . .
    . . # . .
    """)
    basic.pause(100)
    basic.show_leds("""
    . # # # .
    # . . . #
    # . # . #
    # . . . #
    . # # # .
    """)
    Flip_coin = randint(1, 2)
    if Flip_coin == 1:
        basic.show_leds("""
            . # # # .
            # . # . #
            # # # # #
            # . # . #
            . # # # .
            """)
    else:
        basic.show_leds("""
            . # # # .
            # . . . #
            # . # . #
            # . . . #
            . # # # .
            """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

Flip_coin = 0
basic.show_leds("""
    . # # # .
    # . . . #
    # . # . #
    # . . . #
    . # # # .
    """)