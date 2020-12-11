radio.set_group(10)
def on_forever():
    led.toggle(0, 0)
    radio.send_value("X", input.acceleration(Dimension.X))
    radio.send_value("Y", input.acceleration(Dimension.Y))
    radio.send_value("Z", input.acceleration(Dimension.Z))
    radio.send_value("Compass", input.compass_heading())
    basic.pause(50)
basic.forever(on_forever)
