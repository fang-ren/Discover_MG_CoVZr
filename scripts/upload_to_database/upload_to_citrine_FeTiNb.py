"""
Created on 12/13/16

@author: fangren
"""

from pypif import pif
from pypif.obj import *
#from citrination_client import CitrinationClient
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


master_file_path = '..//..//data//master_data//'
master_file_name = 'CLEANED_SampleB2_21_master_metadata.csv'
master_file = master_file_path + master_file_name

data = np.genfromtxt(master_file, delimiter=',', skip_header = 1)

Fe = data[:,58]*100
Ti = data[:,60]*100
Nb = data[:,59]*100
peak_position = data[:,52]
peak_width = data[:,53]
scan_num = data[:,50].astype(int)

spectra_file_path = '..//..//data//1D_spectra//raw_1D//SampleB2_21//'
spectra_basename = 'SampleB2_21_24x24_t30_'

# one dataset
ID = 0

alloys = []
for i in range(len(Fe)):
# for i in range(1):
    alloy = ChemicalSystem()
    spectrum_file = spectra_file_path + spectra_basename + file_index(scan_num[i]) + '_1D.csv'
    print('Importing', spectrum_file)
    spectrum = np.genfromtxt(spectrum_file, delimiter=',')
    IntAve = spectrum[:950,1]
    Qlist = spectrum[:950,0]
    IntAve = IntAve.astype(float)
    Qlist = Qlist.astype(float)
    IntAve = list(IntAve)
    Qlist = list(Qlist)
    # print IntAve, Qlist
    alloy.chemical_formula = 'Fe'+str(round(Fe[i],2))+'Ti'+str(round(Ti[i],2))+'Nb'+str(round(Nb[i],2))
    alloy.composition = [Composition(element='Fe',ideal_atomic_percent=Fe[i]),
                                   Composition(element='Ti',ideal_atomic_percent=Ti[i]),
                                   Composition(element='Nb',ideal_atomic_percent=Nb[i])]

    #alloy.preparation = [ProcessStep(name = 'high power sputtering (>0.25 Angstrom/s)')]
    alloy.preparation = [ProcessStep(name='low power sputtering (<0.07 Angstrom/s)')]

    alloy.source = Source(producer='Hattrick-Simplers Group (The University of South Carolina)')

    alloy.properties = [Property(name = 'Qchi', files = FileReference(relative_path= '/Qchi_thumbnails/' + spectra_basename + file_index(scan_num[i]) + '_Qchi.png')),
                        Property(name = 'XRD Intensity', scalars = IntAve,
                                 conditions=[Value(name = 'Q, (Angstrom$^{-1}$)', scalars = Qlist),
                                             Value(name='Temperature', scalars='25', units='$^\\circ$C'),
                                             Value(name='Exposure time', scalars='30', units='seconds')],
                                 methods = Method(instruments=(Instrument(name = 'MARCCD, 2048 pixels x 2048 pixels, 79 microns')))),
                        Property(name='Maximum intensity/average intensity', scalars= round(np.nanmax(IntAve)/np.nanmean(IntAve),2)),
                        Property(name = 'Full width half maximum (FWHM) of FSDP', scalars = round(peak_width[i],2)),
                        Property(name = 'First sharp diffraction peak (FSDP) position', scalars = round(peak_position[i],2)),
                        Property(name = 'Textured', scalars = 0)]

    # specify a unique uid for each sample
    alloy.uid = 'Fe'+str(int(Fe[i]))+'Ti'+str(int(Ti[i]))+'Nb'+str(int(Nb[i])) + 'low_power' + str(scan_num[i])

    # print pif.dumps(alloy)
    alloys += [alloy]

pif.dump(alloys, open('..//..//data//Json_files_Citrine//SampleB2_21.json','w'))