basic.show_string("RECEIVER")
radio.set_group(10)

def on_received_value(name, value):
    led.toggle(0, 0)
    serial.write_value(name, value)
radio.on_received_value(on_received_value)
