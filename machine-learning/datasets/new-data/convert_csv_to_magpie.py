from __future__ import print_function
import pandas as pd
import sys

def parse_file(filename):
    # Read in the data
    data = pd.read_csv(filename, sep='[, ]+')

    # Figure out the elements
    elems = data.columns[:3]
    print('Reading data from %s. Elements: %s'%(filename, ' '.join(elems)))

    # Compute composition as a string
    def make_composition(x):
        return ''.join('%s%f'%(e,x[e]) for e in elems)
    data['composition'] = data.apply(make_composition, axis=1)

    # Compute "Glassy or Amorphous"
    data['is_glass_label'] = data['is_glass'].apply(lambda x: 'AM' if x >= 1 else 'CR')

    # Save it in Magpie format
    with open('sputtering_%s.data'%''.join(elems), 'w') as fp:
        print('composition', 'gfa{AM,CR}', 'processing{melting,sputtering}', file=fp)

        for rid,row in data.iterrows():
            print(row['composition'], row['is_glass_label'], 'sputtering', file=fp)

for f in sys.argv[1:]:
    parse_file(f)
