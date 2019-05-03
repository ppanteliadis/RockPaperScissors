import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

style.use('fivethirtyeight')

fig = plt.figure()


def plot(runs, wins):
    # width of the bars
    bar_width = 0.3

    # The x position of bars
    r1 = np.arange(len(runs))
    r2 = [x + bar_width for x in r1]

    # Set the range for the bar plots. Don't go higher :)
    plt.ylim(0, 16)

    # Create the bars
    # Choose colors that are eye-soothing. https://visme.co/blog/color-combinations/
    plt.bar(r1, runs, width=bar_width, color='#72A2C0', edgecolor='black', capsize=7, label='Runs')

    plt.bar(r2, wins, width=bar_width, color='#00743F', edgecolor='black', capsize=7, label='Wins')

    # general layout
    plt.xticks([r + bar_width - 0.1 for r in range(len(runs))], ['Rock', 'Paper', 'Scissors'])
    plt.ylabel('Score')
    plt.legend()

    plt.show()



