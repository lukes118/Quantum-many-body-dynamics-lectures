import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl


def arrowed_spines(fig, ax, x_label="x", y_label="f(x)"):
    xmin, xmax = ax.get_xlim() 
    ymin, ymax = ax.get_ylim()

    # removing the default axis on all sides:
    for side in ['bottom','right','top','left']:
        ax.spines[side].set_visible(False)

    # removing the axis ticks
    plt.xticks([]) # labels 
    plt.yticks([])
    ax.xaxis.set_ticks_position('none') # tick markers
    ax.yaxis.set_ticks_position('none')

    # get width and height of axes object to compute 
    # matching arrowhead length and width
    dps = fig.dpi_scale_trans.inverted()
    bbox = ax.get_window_extent().transformed(dps)
    width, height = bbox.width, bbox.height

    # manual arrowhead width and length
    hw = 1./20.*(ymax-ymin) 
    hl = 1./20.*(xmax-xmin)
    lw = 1. # axis line width
    ohg = 0.3 # arrow overhang

    # compute matching arrowhead length and width
    yhw = hw/(ymax-ymin)*(xmax-xmin)* height/width 
    yhl = hl/(xmax-xmin)*(ymax-ymin)* width/height

    # draw x and y axis
    ax.arrow(xmin, 0, xmax-xmin, 0., fc='k', ec='k', lw = lw, 
             head_width=hw, head_length=hl, overhang = ohg, 
             length_includes_head= True, clip_on = False) 

    ax.arrow(0, ymin, 0., ymax-ymin, fc='k', ec='k', lw = lw, 
             head_width=yhw, head_length=yhl, overhang = ohg, 
             length_includes_head= True, clip_on = False)
    
    x_range = xmax - xmin
    y_range = ymax - ymin
    ax.text(xmax - 0.1*x_range, -0.1*y_range, x_label, fontsize=14)
    ax.text(- 0.14*x_range, y_range - 0.1*y_range, y_label, fontsize=14)

def main():
    # plot
    plt.style.use("half_width_fig")
    fig = plt.figure()
    ax = fig.add_axes([0.04, 0.04, 0.9, 0.9])

    x = np.arange(-2., 10.0, 0.01)
    ax.plot(x, x**2, '-', linewidth=1)

    arrowed_spines(fig, ax)
    
    # viewing and saving
    if input("save?") == "y":
        plt.savefig("figures/tikz_plt.pdf")
    plt.show()

if __name__ == '__main__':
    main()
