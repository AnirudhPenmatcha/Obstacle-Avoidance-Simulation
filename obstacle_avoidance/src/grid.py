import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

def detect_obstacle(disparity):

    right_sum = 0
    right_count = 0
    left_sum = 0
    left_count = 0
    middle_count = 0
    threshold = 1
    middle_percentage_threshold = 35
    kernel = np.ones((12,12),np.uint8)


    rows, cols = disparity.shape
    print("Dimensions of the image : ", rows, cols)

    #disparity = cv.disparityEx(disparity, cv.MORPH_OPEN, kernel)

    #plt.imshow(disparity,'gray')
    #plt.show()


    r = rows//3
    p = cols//3



    # Middle Obstacle Check

    middle = disparity[::, p: 2*p]
    row_2, column_2 = middle.shape
    print(row_2, column_2)

    for m in range(row_2):
        for n in range(column_2):
            if middle[m, n] > threshold:
                middle_count += 1

    print(middle_count, (middle_percentage_threshold*(row_2*column_2))/100)

    if middle_count < (middle_percentage_threshold*(row_2*column_2))/100:
        print("Continue Forward")
        return 0
    else:

    # Average of the left pixels

        left = disparity[::, 0: p]
        row_1, column_1 = left.shape
        print(row_1, column_1)

        for m in range(row_1):
            for n in range(column_1):
                if not(np.isnan(left[m, n])):
                    left_sum += left[m, n]
                    left_count += 1


        left_average = left_sum/left_count
        print(left_average)

    # Average of the right pixels

        right = disparity[::, 2*p: 3*p]
        row_3, column_3 = right.shape
        print(row_3, column_3)

        for m in range(row_3):
            for n in range(column_3):
                if not(np.isnan(right[m, n])):
                    right_sum += right[m, n]
                    right_count += 1


        right_average = right_sum/right_count
        print(right_average)

        if left_average > right_average:
            print("Turn Left")
            return 1
        else:
            print("Turn Right")
            return 2
