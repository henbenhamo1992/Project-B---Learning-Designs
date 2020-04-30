from scipy.integrate import odeint
from scipy.signal import StateSpace
import numpy as np

def motor_ss(J ,b ,K ,R ,L ):
    A = np.array([[-b/J, K/J], [-K/L, -R/L]])
    B = np.array([[0], [1/L]])
    C = np.array([1, 0])
    D = np.array(0)
    return StateSpace(A,B,C,D)


theta_dot = motor_ss(0.01,0.1,0.01,1,0.5)
print(theta_dot)
