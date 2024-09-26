import plant, system_model, pid
import numpy as np
import matplotlib.pyplot as plt
import sys


ball1 = plant.Plant(100, 1)
ball2 = plant.Plant(100, 1)

fan = plant.Fan(0)

step_size = 0.0001 # sec
h_ref = 10
Kp, Ki, Kd = -50, 0, -30
pid = pid.PID(Kp, Ki, Kd, step_size)

t_arr = np.arange(0,60,step_size)
h_arr1 = []
h_arr2 = []
control_arr = []

for t in t_arr:
    control = (pid.control(h_ref, ball2.h))
    control_arr.append(control)
    fan.setFan(control)

    h_arr1.append(ball1.h)
    h_arr2.append(ball2.h)
    
    dhdt1 = system_model.dhdt(t, ball1.h, ball1.h_0)
    dhdt2 = system_model.dhdt(t, ball2.h, ball2.h_0, fan.K_fan)
    
    ball1.set_h(ball1.h + step_size*dhdt1)
    ball2.set_h(ball2.h + step_size*dhdt2)
    
    # print(t,ball1.h,ball2.h)


plt.plot(t_arr,h_arr1)
plt.plot(t_arr,h_arr2)
# plt.plot(t_arr,control_arr)
plt.show()

a = input("")
if a is not None:
    sys.exit()