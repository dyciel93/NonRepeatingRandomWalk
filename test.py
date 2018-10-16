'''
2-D Random Walk that is non-repeating
The program "walks" towards a certain direction
'''

import random
import numpy as np
import matplotlib.pyplot as plt

def main():
    N = 50;
    coords = np.random.rand(100, 2)
    x = coords[:,0]
    y = coords[:,1]
    #The probability of going up, down, left, right
    prob = [0.65, 0.35, 0.45, 0.55]
    posx = [30]
    posy = [30]
    rand_location = np.random.rand(100,2)
    z = rand_location[:, 0]

    upp = prob[0] > rand_location[:, 0]
    downp = prob[1] < rand_location[:, 0]

    rightp = prob[2] > rand_location[:, 1]
    leftp = prob[3] < rand_location[: ,1]

    dict = {(posx[-1], posy[-1]): True}
    for uu, dd, rr, ll in zip(upp, downp, rightp, leftp):
        up = uu and posy[-1] < 100
        down = dd and posy[-1] > 0
        right = rr and posx[-1] < 100
        left = ll and posx[-1] > 0
        new_x = posx[-1] - left + right
        new_y = posy[-1] - down + up

        if (new_x, new_y) in dict:

        else:
            posx.append(new_x)
            posy.append(new_y)
            dict[(new_x,new_y)] = True

    x_vector = np.array(posx)
    y_vector = np.array(posy)
    print(x_vector.shape, y_vector.shape)
    # new_array = np.concatenate((x_vector,y_vector),axis = 1)
    plt.figure(1)
    plt.scatter(x_vector, y_vector)
    for i in range(x_vector.shape[0]):
        plt.text(x_vector[i], y_vector[i], str(i))
    plt.show()

    # plt.figure(1)
    #
    # plt.subplot(2,1,1)
    # plt.scatter(x, y)
    # plt.subplot(2,1,2)
    # plt.plot(x,y)
    # plt.show()

def next_step(x_pos, y_pos)
    probability = mobile
if __name__ == "__main__":
    main()