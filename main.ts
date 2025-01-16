input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
    basic.showLeds(`
        . # # # .
        # . . . #
        # . # . #
        # . . . #
        . # # # .
        `)
    basic.pause(100)
    basic.showLeds(`
    . . # . .
    . . # . .
    . . # . .
    . . # . .
    . . # . .
    `)
    basic.pause(100)
    basic.showLeds(`
    . # # # .
    # . # . #
    # # # # #
    # . # . #
    . # # # .
    `)
    basic.pause(100)
    basic.showLeds(`
    . . # . .
    . . # . .
    . . # . .
    . . # . .
    . . # . .
    `)
    basic.pause(100)
    basic.showLeds(`
    . # # # .
    # . . . #
    # . # . #
    # . . . #
    . # # # .
    `)
    Flip_coin = randint(1, 2)
    if (Flip_coin == 1) {
        basic.showLeds(`
            . # # # .
            # . # . #
            # # # # #
            # . # . #
            . # # # .
            `)
    } else {
        basic.showLeds(`
            . # # # .
            # . . . #
            # . # . #
            # . . . #
            . # # # .
            `)
    }
    
})
let Flip_coin = 0
basic.showLeds(`
    . # # # .
    # . . . #
    # . # . #
    # . . . #
    . # # # .
    `)
