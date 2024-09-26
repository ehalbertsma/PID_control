class PID:

    def __init__(self, Kp, Kd, Ki, step_size):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd

        self.step_size = step_size

        # integral of the error
        self.I_e = 0
        self.prev_e = 0

    def error(self, x_ref, x_current):
        return x_ref - x_current

    def integral_e(self, error):
        self.I_e += error*self.step_size
        return self.I_e
    
    def derivative_e(self, error):
        prev_e = self.prev_e
        self.prev = error
        return (prev_e - error)/self.step_size

    def control(self, x_ref, x_current):
        e = self.error(x_ref,x_current)
        print(e)
        I_e = self.integral_e(e)
        derivative_e = self.derivative_e(e)

        offset = 10000

        return (self.Kp*e + self.Ki*I_e + self.Kd*derivative_e + offset)