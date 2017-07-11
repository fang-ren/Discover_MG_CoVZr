__author__ = "Travis Williams"
# University of South Carolina
# Jason Hattrick-Simpers group
# Starting Date: June, 2016

import matplotlib.pyplot as plt
import numpy as np

from scripts.figure_plotters import ternary




def plt_ternary_save(data, tertitle='',  labelNames=('Species A','Species B','Species C'), scale=100,
                       sv=False, svpth=r"C:/Users/Travis W/Pictures/", svflnm='Unnamed',
                       cbl='Scale', vmin=None, vmax=None, cmap='viridis', cb=True, style='h', show_ticks=True):
    """
    Overview
    ----------
    This program makes use of the ternary package and creates a ternary colormap

    Parameters
    ----------
    data: 4-tup of (a,b,c,i) where a, b, and c are the ternary coordinates and i is the intensity
    tertitle: chart title
    labelNames: Names of a, b, and c for chart axes
    scale: scale of chart (if 0-100, then scale is 100)
    sv: Boolean, save chart when true, show chart when false
    svpth: path to save ternary image
    svflnm: file name for ternary diagram when saving
    cbl: colorbar label
    vmin: minimum value of colorbar (leave blank to set to min value in i)
    vmax: maximum value of colorbar (leave blank to set to max value in i)
    cmap: determines color map used
    cb: use colorbar if true
    style: h = hexagons, d = triangles for point shape
    show_ticks: plot ticks on the ternary (no ticks if False)

    Returns
    -------

    """
    if sv:
        font = {'size': 12}   # Set font size for **kwargs
        figsize = (4, 3)
        ticksize = 6
        lnwdth = 0.5
        lnsty = '--'
        alpha = 0.5
    else:
        font = {'size': 30}   # Set font size for **kwargs
        figsize = (30, 30)
        ticksize = 20
        lnwdth = 2
        lnsty = ':'
        alpha = 0.5

    d = dict()
    x = data[:, 1]
    y = data[:, 0]

    if cb:
        i = data[:, 3]

        for col in range(1, len(x)):
            d[(x[col], y[col])] = i[col]
    else:
        for col in range(1, len(x)):
            d[(x[col], y[col])] = 0.5

    # Turn off normal axis, set figure size
    figure, (ax, cax) = plt.subplots(ncols=2, figsize=figsize, gridspec_kw={"width_ratios":[1, 0.05]})
    ax.axis("off")

    # Create ternary axes (tax)
    figure, tax = ternary.figure(ax=ax, scale=scale)

    # Axis Labels (bottom corrisponds to x values, left corrisponds to y values)
    if show_ticks:
        tax.bottom_axis_label(labelNames[0], position=(-0.11, 1.22, 0), rotation=0, **font)
        tax.left_axis_label(labelNames[1], position=(1.05, 0.00, 0), rotation=0, **font)
        tax.right_axis_label(labelNames[2], position=(-0.08, 0.00, 0), rotation=0, **font)
    else:
        tax.bottom_axis_label(labelNames[0], position=(-0.07, 1.13, 0), rotation=0, **font)
        tax.left_axis_label(labelNames[1], position=(0.96, 0.05, 0.00), rotation=0, **font)
        tax.right_axis_label(labelNames[2], position=(-0.01, 0.05, 0), rotation=0, **font)

    # Plot data, boundary, gridlines, and ticks
    tax.heatmap(d, style=style, cmap=cmap, vmin=vmin, vmax=vmax, colorbar=False)

    if cb:
        cdat = ax.imshow([[0]], cmap=cmap, vmin=vmin, vmax=vmax)
        cbar = figure.colorbar(cdat, ax=ax, cax=cax)
        pos1 = cax.get_position()
        pos2 = [pos1.x0 - 0.05, pos1.y0 + 0.1, pos1.width, pos1.height * 0.85]
        cax.set_position(pos2)
        cbar.set_label(cbl)

    if show_ticks:
        tax.boundary(linewidth=1)
        tax.gridlines(multiple=25, linewidth=lnwdth, alpha=alpha, linestyle=lnsty)
        ticks = [round(i / float(scale), 2) for i in range(0, scale+1, 25)]
        tax.ticks(ticks=ticks, axis='rlb', linewidth=1, clockwise=False, offset=0.03, textsize=ticksize)
    else:
        tax.boundary(linewidth=1)
        tax.gridlines(multiple=25, linewidth=lnwdth, alpha=0.50, linestyle=lnsty)

    # Set chart title
    tax.set_title(tertitle)

    # Make chart pretty
    tax.clear_matplotlib_ticks()
    tax._redraw_labels()
    # plt.tight_layout()

    # Save or show
    if sv:
        plt.savefig(''.join([svpth, svflnm]), dpi=600)
    else:
        tax.show()

def plt_tern_scatter(data, tertitle='',  labelNames=('Species A','Species B','Species C'), scale=100,
                       sv=False, svpth=r"C:/Users/Travis W/Pictures/", svflnm='Unnamed',
                       clr='k'):
    font = {'size': 24}

    # Turn off normal axis, set figure size
    figsize = [10,10]
    figure, ax = plt.subplots(figsize=figsize)
    ax.axis("off")

    figure, tax = ternary.figure(scale=scale)
    tax.set_title(tertitle, fontsize=20)
    tax.boundary(linewidth=2.0)
    tax.gridlines(multiple=25, color="k")

    # Axis Labels (bottom corrisponds to x values, left corrisponds to y values)
    tax.bottom_axis_label(labelNames[1], offset=0, **font)
    tax.left_axis_label(labelNames[2], offset=0.12, **font)
    tax.right_axis_label(labelNames[0], offset=0.12, **font)

    points = np.array([data[:,1], data[:,0]]).T

    # for WAXS MG stuff

    color = data[:, 3]
    print(color.shape)
    clrs = list()

    for i, col in enumerate(color):
        if col == 0:
            clrs.append('aqua')
        elif col == 1:
            clrs.append('lawngreen')
        else:
            clrs.append('yellow')
    # print(points, clrs)

    # end wax MG stuff

    tax.scatter(points, marker='o', color=clrs, s=100)
    tax.ticks(axis='lbr', linewidth=1, multiple=25, textsize=14)

    # Set chart title
    tax.set_title(tertitle)

    # Make chart pretty
    tax.clear_matplotlib_ticks()
    tax._redraw_labels()
    plt.tight_layout()
    plt.axis('off')

    if sv:
        plt.savefig(''.join([svpth, svflnm]), dpi=600)
    else:
        tax.show()
        
#
#data = np.genfromtxt('test_data.csv', delimiter=',')
##plt_ternary_save(data, tertitle='',  labelNames=('Co','Fe','V'), scale=100,
##                       sv=False, svpth=r"C:/Users/Travis W/Pictures/", svflnm='Unnamed',
##                       cbl='Scale', vmin=1, vmax=5, cmap='viridis', cb=True, style='h')
#
