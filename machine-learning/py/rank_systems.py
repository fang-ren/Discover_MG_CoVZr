# Author: Logan Ward
from __future__ import print_function
from collections import OrderedDict
import json
import pandas as pd
import gzip
import sys
import numpy
import re
import numpy as np

# Get arguments
if len(sys.argv) != 4:
    print("Usage: <data file> <prob threshold> <dist threshold>")
    exit(1)
data_file = sys.argv[1][:-8]
prob_threshold = float(sys.argv[2])
dist_threshold = float(sys.argv[3])

# Read in the JSON file
if sys.version_info >= (3,):
    json_out = json.load(gzip.open(sys.argv[1], "rt"))
else:
    json_out = json.load(gzip.open(sys.argv[1]))
entries = json_out['entries']
dist_prop = [x['name'] for x in json_out['properties']].index('compdistance')
am_class = json_out['class-names'].index('AM')
del json_out
data = pd.DataFrame()
data['composition'] = [ x['composition'] for x in entries ]
data['probability'] = [ x['class']['probabilities'][am_class] for x in entries ]
data['distance'] = [ x['properties'][dist_prop]['measured'] for x in entries ]
del entries
#print("[Status] Loaded %d entries"%len(data))
#print("[Result] %d are above %.2f%% probability"%(sum(data['probability'] > prob_threshold), prob_threshold * 100))

# Get the elements
elem_regex = re.compile('[A-Z][a-z]?')
data['elems'] = data['composition'].apply(lambda x: elem_regex.findall(x))
#print("[Status] Parsed elements for all entries")

# Group by each system, get the name and number above prob and dist thresholds
data['system'] = data['elems'].apply(lambda x: "-".join(sorted(x)))
systems = []
for gid, group in data.groupby('system'):
    number_evals = len(group)
    above_prob = len(group.query('probability >= %f'%prob_threshold))
    above_dist = len(group.query('distance >= %f'%dist_threshold))
    above_both = len(group.query('distance >= %f and probability >= %f'%(dist_threshold, prob_threshold)))
    best_gfl = group['probability'].max()
    best_gfl_composition = group['composition'][group['probability'].idxmax()]
    systems.append(OrderedDict(
        system=gid,
        nelems=gid.count("-") + 1,
        number_alloys=number_evals,
        fraction_glassy=float(above_prob) / number_evals,
        predicted_glassy=above_prob,
        unexplored=above_dist,
        unexplored_glassy=above_both,
        highest_GFL=best_gfl,
        highest_GFL_composition=best_gfl_composition
    ))
    

# Make into data frame, sort by above both, and save
output = pd.DataFrame(systems)

# Save the ternary systems
output.sort_values(by='unexplored_glassy', ascending=False, inplace=True)
output.query('nelems == 3').to_csv(open('%s_P%.2f_dist%.2f.csv'%(data_file, prob_threshold, dist_threshold), 'w'), index=False)

# Print out some summary data
print('Number of ternary systems scanned:', sum(output['nelems'] == 3))
print('Number of ternary systems with glasses:', len(output.query('nelems == 3 and predicted_glassy > 0')))
print('Number of ternary systems with new glasses:', len(output.query('nelems == 3 and unexplored_glassy > 0')))
print('Number of ternary systems with >2% glassy alloys:', len(output.query('nelems == 3 and fraction_glassy > 0.02')))
print('Number of alloys scanned:', output['number_alloys'].sum())
print('Number of alloys predicted to be glassy:', output['predicted_glassy'].sum())
print('Number of new alloys predicted to be glassy:', output['unexplored_glassy'].sum())
