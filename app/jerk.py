# import libs
import numpy as np
import time
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Rectangle
import sys
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
    jerkX,jerkY,_=jerk_list/100
    print('jerkX',jerkX)
    print('jerkY',jerkY)
    # update rect position
    rect.set_xy((jerkX-2, jerkY-2))
    # update text info
    text_obj.set_text(
        f"Jerk_mag= {np.linalg.norm([jerkX, jerkY]):0.4f}$ m/s^3$")
    # draw
    plt.draw()
    plt.pause(0.001)




def main():
    # initialize variables
    if len(sys.argv)>1:
        iter =int(sys.argv[1])
    else:     iter=100
    position = np.zeros((3,))
    prev_pos = np.zeros((3,))
    prev_vel = np.zeros((3,))
    prev_acc = np.zeros((3,))
    jerk = np.zeros((3,))
    last_time = time.time()
    jerk_list=[]
    for i in range(iter):

        # simulate a new position update (replace this with your actual position data)
        position = abs(np.random.randn(3))
        # calculate the time difference between frames
        current_time = time.time()
        elapsed_time = current_time - last_time
        last_time = current_time
        # Calculate velocity for each axis using previous position data
        vel = (position ) / elapsed_time
        # # Calculate acceleration for each axis using previous velocity data
        acc = (vel - prev_vel) / elapsed_time
        # # Calculate jerk for each axis using previous acceleration data
        jerk = (acc - prev_acc) / elapsed_time
        # # Store current velocity and acceleration data as previous data for next iteration
        prev_pos=position 
        prev_vel = vel
        prev_acc = acc
        
        set_rec(jerk)
        time.sleep(0.1)
        print(np.linalg.norm(jerk))

        
if __name__=="__main__":
    import time
    s=time.perf_counter()
    main()
    print('time s.',time.perf_counter()-s)