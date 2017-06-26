import pandas as pd
from glob import glob 

elems = ['Co', 'V', 'Zr']
"""List of elements in library"""

def extract_data(filename, sheet):
    """Given dataset, extract alloy composition and peak width
    
    :param filename: string, path to file holding data
    :param sheet: sheet name
    :return: DataFrame, with keys "composition" and "gfa"
    """
    
    data = pd.read_excel(filename, sheetname=sheet, header=1)
    
    output = pd.DataFrame()
    print data.head()
    output['composition'] = data.apply(lambda x: "".join(["%s%f"%(e, x[e]) for e in elems]), axis=1)
    for e in elems:
        output[e] = data[e]
    output['gfa'] = data['Label']
    return output
    
# Get the data 
data = pd.DataFrame()
for sheet in ["Experimental_low_power"]:
    this_set = extract_data("All_Data_Theories.xlsx", sheet)
    data = data.append(this_set)
    
data['is_amorphous'] = data['gfa'] == 1

# Print it out
fp = open('sputtering_CoVZr.data', 'w')

print >>fp, "composition", "gfa{AM,CR}", "processing{meltspin,sputtering}"

for c,i in zip(data['composition'], data['is_amorphous']):
    print >>fp, c, "AM" if i else "CR", "sputtering"
    
fp.close()