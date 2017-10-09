# Author: Logan Ward
import matplotlib.figure as f
import matplotlib.pyplot as plt
from matplotlib import gridspec
import matplotlib.cm as cm
import numpy as np
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})
import sys
import pandas as pd
import json
import ternary
import os
import shutil
import re
import gzip

# Important things to change
labelSize = 12
tickSize = 10
titleSize = 22
plotWidth = 89 / 25.4 # Full width
plotHeight = plotWidth * 0.7
width = 0.8
markerSize = 1
plotDPI = 320
bbox = {'edgecolor':'black', 'facecolor':'white'}

# Get the elems from the user
if len(sys.argv) != 5:
    print("Usage: <filename> <elemA> <elemB> <elemC>")
    exit()
datafile = sys.argv[1]
file_name = datafile[:-8]
elems = sys.argv[2:]

# Load in the results
def parse_json_data(filename):
    json_out = json.load(gzip.open(filename, 'r'))
    entries = json_out['entries']
    #gfa_prop = [x['name'] for x in json_out['properties']].index('gfa')
    try:
        proc_prop = [x['name'] for x in json_out['properties']].index('processing')
    except:
        proc_prop = None
    
    am_class = json_out['class-names'].index('AM')
    del json_out
    data = pd.DataFrame()
    data['composition'] = [ x['composition'] for x in entries ]
    data['probability'] = [ x['class']['probabilities'][am_class] for x in entries ]
    data['measured'] = [ x['class']['measured'] if 'measured' in x['class'] else np.nan for x in entries ]
    if proc_prop is not None:
        data['processing'] = [x['properties'][proc_prop]['measured'] for x in entries ]
    del entries
    print("[Status] Loaded %d entries"%len(data))
    
    # If processing data available, filter out only those made using sputtering (== 1)
    if 'processing' in data.columns:
        data = data.query('processing == 1').copy()

    # Get the elements
    elem_regex = re.compile('(?P<elem>[A-Z][a-z]?)(?P<frac>[0-9.]*)')
    
    data['elems'] = data['composition'].apply(lambda x: dict(elem_regex.findall(x)))
    total_elems = set()
    data['elems'].apply(lambda x: total_elems.update(x.keys()))
    print("[Status] %d known elements"%len(total_elems))
        
    # Parse the compositions of each element
    def get_frac(comp, elem):
        if elem in comp:
            frac = comp[elem]
            return 1 if len(frac) == 0 else float(frac)
        return 0
    for elem in total_elems:
        data['X_%s'%elem] = data['elems'].apply(lambda x: get_frac(x, elem))
    data['total'] = np.sum(data[['X_%s'%e for e in total_elems]].as_matrix(), axis=1)
    for elem in total_elems:
        data['X_%s'%elem] = data['X_%s'%elem] / data['total']
    print("[Status] Parsed element fractions")
        
    # Get only those with a fraction equal to 1
    data['my_elems_comp'] = np.sum(data[['X_%s'%e for e in elems]], axis=1)
    data = data.query('%s > 0.999'%' + '.join(['X_%s'%e for e in elems]))
    print("[Status] Got %d entries in the %s system"%(len(data), "-".join(elems)))
    
    # Get only the desired columns
    cols = ['composition', 'probability', 'measured']
    cols.extend(['X_%s'%e for e in elems])
    data = data[cols]
    return data
data = parse_json_data(datafile)

def prettify(ax, label):
        # Make it pretty
        #   Add in labels
        plt.axis('off')
        ax.set_xlim([-5, 110])
        ax.set_ylim([-5, 110 * 3 ** 0.5 / 2])
        ax.text(110, -10, elems[0], ha='right', fontsize=labelSize) # 1st elem
        ax.text(50, 90, elems[1], ha='center', fontsize=labelSize) # 2nd elem
        ax.text(-10, -10, elems[2], ha='left', fontsize=labelSize) # 3rd elem
        ax.text(-10, ax.get_ylim()[1]-10, label, fontsize=titleSize)

# Make the figure 
def plot_ternary(ax, data, val, train_data=None, diff=False):
    fig, tax = ternary.figure(scale=100, ax=ax)
    
    tax.gridlines(color="black", multiple=10)
    
    # Get the coordinates
    def get_coords(data, elems):
        data_list = []
        for a,c,m in zip(data['X_' + elems[0]], data['X_' + elems[1]], data['X_' + elems[2]]):
            data_list.append((a*100,c*100,m*100))
            
        # Transform
        xs, ys = ternary.helpers.project_sequence(data_list)
        return xs, ys
    xs, ys = get_coords(data, elems)

    #   Make boundary
    from matplotlib.colors import SymLogNorm, PowerNorm
    tax.boundary(linewidth=1.0)
    if diff:
        sc = ax.scatter(xs, ys, s=3.9, c=val,
                        cmap='seismic', vmin=-0.5, vmax=0.5, edgecolor='face')
    else:
        sc = ax.scatter(xs, ys, s=3.9, c=val,
                        cmap='viridis_r', vmin=0.5, vmax=1, edgecolor='face')
                        
    # Output training data
    if train_data is not None:
        if len(train_data) > 0:
            xs, ys = get_coords(train_data, elems)
            sc_train = ax.scatter(xs, ys, s=4,
                    marker = 's',
                    color=['r' if v == 1 else 'b' for v in train_data['measured']],
                    edgecolor='k',
                    alpha=0.5,
                    lw=0.2)
        
    # Add colorbar
    cb = plt.colorbar(sc, ax=ax)
    
    cb.ax.set_ylabel('P(GFA = True)' if not diff else 'Change', fontsize=tickSize)
    
    for x in cb.ax.get_yticklabels():
        x.set_size(tickSize)
    
    if not diff:
        cb_ticks = [x.get_text() if i > 5 else '' for i,x in enumerate(cb.ax.get_yticklabels())]
        cb.ax.set_yticklabels(cb_ticks)
  
# Make the plot of predictions w/o the training data
fig, ax = plt.subplots()
plot_ternary(ax, data, data['probability'])#, train_data=training_data)
prettify(ax, '')

if not os.path.isdir('plots'):
    os.mkdir('plots')

fig = plt.gcf()
fig.set_size_inches(plotWidth, plotHeight)
plt.tight_layout()
fig.savefig(os.path.join('plots', '%s.png'%(''.join(elems))), dpi=320)

# Save the data
data.to_csv(os.path.join('plots', '%s.csv'%(''.join(elems))), index=False)
