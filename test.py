'''
2-D Random Walk that is non-repeating
The program "walks" towards a certain direction
'''

#TODO: Change the scatter plot with images Us


import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
import math
from PIL import Image
class footstep:
    footstep_image = Image.open("catpaw.png")

    def __init__(self):
        pass

    def rotate(self, angle): #function for rotating the footprint. The unit is in degrees, and positive values rotate the values in ccw fashion
        tempFS = self.footstep_image.rotate(angle)
        return tempFS
def gen_prob():
    prob_up = np.random.rand()
    prob_down = 1 - prob_up
    prob_right = np.random.rand()
    prob_left = 1 - prob_right
    a = [prob_up, prob_down, prob_right, prob_left]
    return a

def next_step(x_init, y_init):
    steps = 1000
    coords = np.random.rand(steps, 2)
    prob = gen_prob()
    up = prob[0] > coords[:,0]
    down = prob[1] > coords[:,0]
    right = prob[2] > coords[:,1]
    left = prob[3] > coords[:,1]
    x_pos = [x_init]
    y_pos = [y_init]
    max_vertical = 100
    min_vertical = -100
    max_horizontal = 100
    min_horizontal = 100

    for iu, id, ir, il in zip(up, down, right, left):
        min_step = 0.4
        max_step = 1
        step_size = generate_randomval(min_step, max_step)

        step_up = iu and np.bool_(y_pos[-1] < max_vertical)
        step_down = id and np.bool_(y_pos[-1]  > min_vertical)
        step_right = ir and np.bool_(x_pos[-1] < max_vertical)
        step_left = il and np.bool_(x_pos[-1] > min_vertical)
        y_pos.append(y_pos[-1] + step_size[0]*step_up - step_size[1]*step_down)
        x_pos.append(x_pos[-1] + step_size[2]*step_right - step_size[3]*step_left)


    return [x_pos, y_pos]

def generate_graph(pos):
    plt.figure("Random Steps")
    plot = plt.scatter(pos[0],pos[1])
    # Use the below code to show that
    # for i in range(0, len(pos[0])):
    #      plt.text(pos[0][i],pos[1][i],i)

    plt.title("Non Repeating Random Step")
    plt.xlabel("X Axis")
    plt.ylabel('Y Axis')
    plt.show()

def generate_randomval(min, max):
    rand_1 = min + (max-min)*np.random.rand(4)
    return rand_1

class user_interf():
    def __init__ (self):
        self.root = tk.Tk()
        frame = tk.Frame(root)
        frame.pack()
        startButton = tk.Button(frame, text = "start", fg="black", bg = "white") # TODO: Add the "command" keyword in there
        endButton = tk.Button(frame, text = "end", fg = "white") #Finish this portion #TODO: Add the "command" keyword in there
    #TODO: Create a generic function that combines two different functions
    '''
    def combine_funcs(*funcs):
        def combined_func(*args, **kwargs):
            for f in funcs:
                f(*args, **kwargs)
        return combined_func
    '''
    #TODO: Create a program for determining the directional angle at which the footstep should be pointing towards
    #this can be done using the

#Function used to calculate the rotate angle for the direction of the foot image
def find_angle(curr_x, prev_x, curr_y, prev_y):
    x_dir = curr_x - prev_x # x - component for the directional vector
    y_dir = curr_y - prev_y # y - component for the directional vector
    angle = math.atan(y_dir/x_dir) #calculate the angle in radians
    angle = angle*180/math.pi #convert the angle in radians to pi
    angle = angle - 90 # Subtract 90 degrees from the original image's angle, because the footstep is already point up wards, this makes the starting angle
    # 0 degrees with respect to the x-axis
    return angle


if __name__ == "__main__":
    # x = np.bool_(True)
    # y = True
    # z = x and y
    # print(z, type(x), type(y))
    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack()
    startButton = tk.Button(frame, text="Start", fg="black" , bg="white")
    endButton = tk.Button(frame, text="End", fg="red", bg="white")
    startButton.pack()
    endButton.pack()


    root.mainloop()

    # position = next_step(1,2)
    # generate_graph(position)