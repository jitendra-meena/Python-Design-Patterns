class Device:
    def turn_on(self): pass

class TV(Device):
    def turn_on(self):
        return "TV is ON"

class Remote:
    def __init__(self, device):
        self.device = device

    def press_power(self):
        return self.device.turn_on()

remote = Remote(TV())
print(remote.press_power())
