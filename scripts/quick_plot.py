import matplotlib.pyplot as plt
import numpy as np


def quick_plot(fig, axes):
    ax = axes[0]
    x = np.linspace(0, 1, 10)
    ax.plot(x, np.sin(x))

    ax.set_xlabel("x")

def main():
    plt.style.use("half_width_fig")
    fig = plt.figure()
    ax = fig.add_axes([0.15, 0.15, 0.8, 0.8])

    # making the plot
    quick_plot(fig, [ax])

    # showing or saving
    if input("save?") == "y":
        plt.savefig("figures/quick_plot.png")
    plt.show()


if __name__ == "__main__":
    main()
