import math
import numpy as np
import matplotlib.pyplot as plt

def min_max( list ):
    return np.array( [ ( value - list.min() ) / ( list.max() - list.min() ) for value in list ] )

def meanSquareError( m, b, list ):
    sum = 0
    for pair in list:
        sum += (pair[1] - (m * pair[0] + b)) ** 2
    return sum / len(list)

def gradient( m, b, list, alpha ):
    mSum = 0
    for pair in list:
        mSum += pair[0] * (pair[1] - (m * pair[0] + b))
        pass
    mSum = (-2 / len(list)) * mSum

    bSum = 0
    for pair in list:
        bSum += (pair[1] - (m * pair[0] + b))
        pass
    bSum = (-2 / len(list)) * bSum

    m = m - alpha * mSum
    b = b - alpha * bSum

    return (m,b)

def model():
    data = np.genfromtxt( "input.txt", delimiter = ',' )
    normData = min_max( data )
    m = np.random.randint(10)
    b = np.random.randint(10)
    alpha = 0.01
    itteration = 0
    while(meanSquareError(m,b,normData) > 0.01):
        m, b = gradient(m, b, normData, alpha)
        itteration += 1
        if(itteration % 200 == 0):
            plt.plot(normData[:,0], b + m * normData[:,0], color='red')
    print(itteration, math.floor(meanSquareError(m,b,normData)*100)/100)
    print("Y = "+ str(math.floor(m*100)/100) + "X + " + str(math.floor(b*100)/100) )
    plt.scatter(normData[:,0], normData[:,1])
    plt.plot(normData[:,0], b + m * normData[:,0], color='green')
    plt.show()

model()
