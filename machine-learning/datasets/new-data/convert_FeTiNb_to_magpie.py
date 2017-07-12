import pandas as pd

# Read in the data
data = pd.read_csv('GFA_FeTiNb.csv', sep='[, ]+')

# Compute composition as a string
def make_composition(x):
    return ''.join('%s%f'%(e,x[e]) for e in ['Fe','Nb','Ti'])
data['composition'] = data.apply(make_composition, axis=1)

# Compute "Glassy or Amorphous"
data['is_glass_label'] = data['is_glass'].apply(lambda x: 'AM' if x >= 1 else 'CR')

# Save it in Magpie format
with open('sputtering_FeTiNb.data', 'w') as fp:
    print('composition', 'gfa{AM,CR}', 'processing{melting,sputtering}', file=fp)

    for rid,row in data.iterrows():
        print(row['composition'], row['is_glass_label'], 'sputtering', file=fp)