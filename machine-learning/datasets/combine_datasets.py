"""Combines two LB datasets, adding a column to acconut for processing technique"""

# Create the header
fo = open('landolt-combined.txt', 'w')
print("composition gfa{AM,AC,CR} processing{meltspin,sputtering}", file=fo)

# Read in other datafiles
def append_data(filename, processing):
    fi = open(filename, 'r')
    fi.readline() # header
    for line in fi:
        print("%s %s"%(line.strip(), processing), file=fo)
    fi.close()
    
append_data('landolt.txt', 'meltspin')
append_data('landolt-sputtering.txt', 'sputtering')

# Save data
fo.close()
