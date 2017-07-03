__author__ = "Travis Williams. :pgam Ward"
# University of South Carolina
# Jason Hattrick-Simpers group
# Starting Date: June, 2016

from matplotlib import pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap
from scipy import interpolate
import numpy as np
import os

import ternary

def interpolate_probabilities(a,b,c,p):
    """Prepare probabilities for plotting with ternary's heatmap
    
    Inputs:
        a,b,c - Fractions of metal A,B,C
        p - Probability function to be interpolated
    Output:
        Probabilities at a finer spacing all over the ternary, in a form that 
    """
        
    probability_func = interpolate.Rbf(a,b,c,p, function='multiquadric',
                                           smooth=0.3)

    metal1_range = np.linspace(0, 100, 63, endpoint=False) # Makes the nicest plots
    metal2_range = metal1_range[:] # Copy

    metal1 = []
    metal2 = []
    metal3 = []

    probability_interpolate = []

    for i in metal1_range:
        for j in metal2_range:
            if i + j <= 100 and i+j >= 0:
                try:
                    metal1.append(i)
                    metal2.append(j)
                    metal3.append(100-i-j)
                    probability_interpolate.append(float(probability_func(i, j, (100-i-j))))
                except(ValueError):
                    continue

    ternary_data = np.concatenate(([metal1],[metal2],[metal3],[probability_interpolate]), axis = 0)
    return np.transpose(ternary_data)

def make_cmap(base='viridis_r', scale_factor=1.5, cutoff=0.9, adjust_factor=0.1):
    """Make a colormap that this scaled to emphasize the top of the range.
    
    Two kinds of emphasis:
        1) Scaling the colormap to have a stronger gradient at the top
        2) Making the colors below a treshold lighter
        
    Inputs:
        base - str, base color map name
        scale_factor - float, how much to exaggerate the range at the top (larger value -> larger scaling)
        cutoff - float, treshold below which to lighten colors (0-1)
        adjust_factor - float, how much to dampen colors (0-1)
    Returns:
        Colormap
    """
    
    # Get the base colormap
    v = cm.get_cmap('viridis_r')
    
    # Scale it
    new_list = v(np.linspace(0,1,300) ** scale_factor)

    # Apply cutoff
    new_list[:int(len(new_list)*cutoff),:3] += (1 - new_list[:int(len(new_list)*0.9),:3]) * adjust_factor
    return ListedColormap(new_list, name='%s_scaled'%base)

def interpolation_ternary(data, tertitle='',  labelNames=('Species A','Species B','Species C'), scale=100,
                       sv=False, svpth=".", svflnm='Unnamed',
                       cbl='Scale', vmin=None, vmax=None, cmap='viridis', cb=True, style='h'):
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

    Returns
    -------

    """
    if sv:
        font = {'size': 12}   # Set font size for **kwargs
        figsize = (3.4, 2.5)
        ticksize = 6
        lnwdth = 0.5
        lnsty = '--'
        alpha = 0.15
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
    figure, ax = plt.subplots(figsize=figsize)
    ax.axis("off")

    # Create ternary axes (tax)
    figure, tax = ternary.figure(ax=ax, scale=scale)

    # Axis Labels (bottom corrisponds to x values, left corrisponds to y values)
    tax.bottom_axis_label(labelNames[1], offset=-0.1, **font)
    tax.left_axis_label(labelNames[2], offset=0.17, **font)
    tax.right_axis_label(labelNames[0], offset=0.17, **font)

    # Plot data, boundary, gridlines, and ticks
    tax.heatmap(d, style=style, cmap=cmap, vmin=vmin, vmax=vmax, colorbar=False)
    tax.boundary(linewidth=1)
    tax.gridlines(multiple=10, linewidth=lnwdth, alpha=alpha, linestyle=lnsty)
    ticks = [round(i / float(scale), 1) for i in range(0, scale+1, 10)]
    tax.ticks(ticks=ticks, axis='rlb', linewidth=1, clockwise=False, offset=0.03, fsize=ticksize)

    # Set chart title
    tax.set_title(tertitle)
    
    # Make a colorbar
    i = ax.imshow([[5]], cmap=cmap, vmin=vmin, vmax=vmax)
    cb = plt.colorbar(i)
    
    cb.set_label(cbl)
    
    ticks = np.arange(0.5, 1.01, 0.05)
    cb.set_ticks(ticks)
    tick_labels = np.array(['%.1f'%t for t in ticks])
    tick_labels[1::2] = ''
    cb.set_ticklabels(tick_labels)
    
    cb.update_ticks()

    # Make chart pretty
    #tax.clear_matplotlib_ticks()
    tax._redraw_labels()
    plt.tight_layout()

    # Save or show
    if sv:
        plt.savefig(os.path.join(svpth, svflnm), dpi=600)
    else:
        tax.show()
