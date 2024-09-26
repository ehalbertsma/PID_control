


class Plant:

    def __init__(self, h, m):
        self.h = h
        self.h_0 = h
        self.m = m


    def __repr__(self):
        print(self.h)

    def set_h(self, h):
        self.h = max(0, h)


class Fan:

    def __init__(self, K_fan):
        self.K_fan = K_fan

    def __repr__(self):
        print(self.K_fan)

    def setFan(self, K_fan):
        self.K_fan = max(0, K_fan)

    def fanForce(self, m, h):
        # the fan force is equal to fan speed divided by distance to object
        return self.K_fan/h