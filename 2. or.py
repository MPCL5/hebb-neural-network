import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
from hebb import Hebb

data = [
    {'inputs': [1, 1], 'result': 1},
    {'inputs': [1, -1], 'result': 1},
    {'inputs': [-1, 1], 'result': 1},
    {'inputs': [-1, -1], 'result': -1},
]


def drawPlot(weights, biace):
    w2 = 1
    handler = 0

    if weights[0] != 0:
        w2 = -weights[1] / weights[0]
        biace = -biace / weights[0]
        handler = 1

    dotX = [item['inputs'][0] for item in data]
    dotY = [item['inputs'][1] for item in data]

    x = np.linspace(-5, 5, 20)
    fig, ax = plt.subplots()  # Create a figure and an axes.

    loc = plticker.MultipleLocator(base=1)
    ax.xaxis.set_major_locator(loc)
    ax.yaxis.set_major_locator(loc)

    ax.plot(handler*x, w2 * x + biace)  # Plot more data on the axes...
    # Plot more data on the axes...
    ax.plot(dotX, dotY, 'o', color='tab:brown')
    ax.set_xlabel('x1')  # Add an x-label to the axes.
    ax.set_ylabel('x2')  # Add a y-label to the axes.
    ax.set_title('And Hebb neural network')  # Add a title to the axes.
    ax.grid(linewidth=1, mew=1, ms=1, markevery=1, zorder=1)

    plt.show()


if __name__ == '__main__':
    neuralHebb = Hebb(2, lambda x: -1 if x < 0 else 1)
    # neuralHebb.trainAll(data)
    for item in data:
        neuralHebb.train_one(item['inputs'], item['result'])
        drawPlot(neuralHebb.get_weights(), neuralHebb.get_bias())

    # print(neuralHebb.calculateOne([1,1]))
    # print(neuralHebb.calculateOne([1,-1]))
    # print(neuralHebb.calculateOne([-1,1]))
    # print(neuralHebb.calculateOne([-1,-1]))
