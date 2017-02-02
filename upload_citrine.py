"""
Created on 12/13/16

@author: fangren
"""

from pypif import pif
from pypif.obj import *
from citrination_client import CitrinationClient
import numpy as np


def file_index(index):
    """
    formatting the index of each file
    """
    if len(str(index)) == 1:
        return '000' + str(index)
    elif len(str(index)) == 2:
        return '00' + str(index)
    elif len(str(index)) == 3:
        return '0' + str(index)
    elif len(str(index)) == 4:
        return str(index)


master_file_path = 'C:\\Research_FangRen\\Data\\July2016\\CoVZr_ternary\\masterfiles\\high\\'
master_file_name = 'CLEANED_Sample14_master_metadata_high.csv'
master_file = master_file_path + master_file_name

data = np.genfromtxt(master_file, delimiter=',', skip_header = 1)

Co = data[:,57]*100
V = data[:,58]*100
Zr = data[:,59]*100
peak_position = data[:,60]
peak_width = data[:,61]
scan_num = data[:,52].astype(int)

spectra_file_path = 'C:\\Research_FangRen\Data\\July2016\\CoVZr_ternary\\1Dfiles\\high_power_8_14_17\\'
spectra_basename = 'Sample14_7thin_24x24_t30_'

ID = 902
IDs = []

for i in range(len(Co)):
    alloy = Alloy()
    spectrum_file = spectra_file_path + spectra_basename + file_index(scan_num[i]) + '_1D.csv'
    # print scan_num[i]
    spectrum = np.genfromtxt(spectrum_file, delimiter=',')
    IntAve = spectrum[:950,1]
    Qlist = spectrum[:950,0]
    IntAve = IntAve.astype(float)
    Qlist = Qlist.astype(float)
    IntAve = list(IntAve)
    Qlist = list(Qlist)
    # print IntAve, Qlist
    alloy.chemical_formula = 'Co'+str(round(Co[i],2))+'V'+str(round(V[i],2))+'Zr'+str(round(Zr[i],2))
    alloy.composition = [Composition(element='Co',ideal_atomic_percent=Co[i]),
                                   Composition(element='V',ideal_atomic_percent=V[i]),
                                   Composition(element='Zr',ideal_atomic_percent=Zr[i])]

    alloy.preparation = [ProcessStep(name = 'sputtering (power < 30W)')]

    alloy.source = Source(producer='Hattrick-Simplers Group (The University of South Carolina)')

    alloy.properties = [Property(name = 'XRD Intensity', scalars = IntAve,
                                 conditions=[Value(name = 'Q', scalars = Qlist),
                                             Value(name='Temperature', scalars='25', units='$^\\circ$C'),
                                             Value(name='Exposure time', scalars='30', units='seconds')],
                                 method = Method(instruments=(Instrument(name = 'MARCCD')))),
                        Property(name='Maximum intensity/average intensity', scalars=np.nanmax(IntAve)/np.nanmean(IntAve)),
                        Property(name = 'Full width half maximum (FWHM) of FSDP', scalars = peak_width[i]),
                        Property(name = 'First sharp diffraction peak (FSDP) position', scalars = peak_position[i]),
                        Property(name = 'Textured', scalars = 0)]

    alloy.uid = 'CoVZr_high_power'

    # print pif.dumps(alloy, indent=4)

    pif.dump(alloy, open('temp.json','w'))
    client = CitrinationClient(api_key = 'CXvOe54ijESoSqEtZtnG7Att', site = 'https://slac.citrination.com')

    # # to let the system assign an ID automatically
    # response = client.create_data_set()
    # client.upload_file('temp.json',data_set_id = response.json()['id'])  # id is the folder id
    # ID = response.json()['id']
    # IDs.append(ID)
    # print ID


    # to specify an ID to the sample:
    client.upload_file('temp.json',data_set_id = ID)  # id is the folder id, each folder for 1 sample
    IDs.append(ID)
    print ID
    ID = ID + 1
np.savetxt(master_file_path+'Citrine_ID.csv', IDs)


    # to delete a record
    # C:\Python27\Scripts>citrination create_dataset_version -k CXvOe54ijESoSqEtZtnG7Att -p slac -d ID

