global G_CONST
G_CONST = -9.81


def dhdt(t, h, h_0, K_fan=0):
    # kinetic equation, undriven:
    # 0.5*g*t^2 + h'(t)*t - h(t) + h_0 = 0
    # kinetic equation, driven:
    # 0.5*g*t^2 + h'(t)*t - h(t) + h_0 = K_fan/h(t)
    if t <= 0.00001:
        return 0
    elif h < 0.01:
        return 0
    else:
        return  (0.5*G_CONST*t**2 - h + h_0 + K_fan/h)/t

