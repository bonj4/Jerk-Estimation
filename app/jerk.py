# import libs
import numpy as np
import time
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Rectangle
# import cv2

# configure fig and ax 
fig, ax = plt.subplots(figsize=(6,6))
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)
ax.set_aspect('equal')
# add ellipse to plot
ellipse_static = Ellipse(xy=(0, 0), width=15, height=30, angle=0, alpha=0.5, fill=False, edgecolor='r')
ax.add_artist(ellipse_static)
# add rectangle to plot
rect= Rectangle((-2,-2), 4, 4, linewidth=1, edgecolor='b',fill=False)
ax.add_artist(rect)

# add text for jerk mag info
text_obj = ax.text(-20, 18, '', ha='left')

# cv2.namedWindow('frame')

def set_rec(jerk_list):
    # swap none varibales to 0
    jerk_list = np.nan_to_num(jerk_list, nan=0)
    jerkX,jerkY,_=jerk_list*10e8
    print('jerkX',jerkX)
    print('jerkY',jerkY)
    # update rect position
    rect.set_xy((jerkX-2, jerkY-2))
    # update text info
    text_obj.set_text(
        f"Jerk_mag= {np.linalg.norm([jerkX, jerkY]):0.4f}$*10e-8 ms^3$")
    # draw
    plt.draw()
    plt.pause(0.001)




def main():
    # initialize variables
    position = np.zeros((3,))
    velocity = np.zeros((3,))
    acceleration = np.zeros((3,))
    jerk = np.zeros((3,))
    last_time = time.time()
    jerk_list=[]
    iter=100
    for i in range(iter):

        # simulate a new position update (replace this with your actual position data)
        position += abs(np.random.randn(3))
        
        # calculate the time difference between frames
        current_time = time.time()
        time_diff = current_time - last_time
        last_time = current_time

        # calculate the velocity, acceleration, and jerk arrays for each axis using numpy.gradient
        velocity = np.gradient(position, time_diff, axis=0)
        acceleration = np.gradient(velocity, time_diff, axis=0)
        jerk = np.gradient(acceleration, time_diff, axis=0)
        
        set_rec(jerk)
if __name__=="__main__":
    import time
    s=time.perf_counter()
    main()
    print('time s.',time.perf_counter()-s)