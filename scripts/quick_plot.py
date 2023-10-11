import matplotlib.pyplot as plt
import numpy as np


def quick_plot(fig, axes):
    ax = axes[0]
    x = np.linspace(0, 10, 20)
    ax.plot(x, np.sin(x), label="first set")

    ax.set_xlabel("x")
    ax.set_ylabel("y")

    # legend
    legend = ax.legend(loc="upper left", bbox_to_anchor=[0, 1])
    legend.get_frame().set_linewidth(0.4)

def main():
    plt.style.use("half_width_fig")
    fig = plt.figure()
    ax = fig.add_axes([0.15, 0.15, 0.8, 0.8])

    # making the plot
    quick_plot(fig, [ax])

    # showing or saving
    if input("save?") == "y":
        plt.savefig("lecture-notes/figures/quick_plot.png")
    plt.show()


if __name__ == "__main__":
    main()
