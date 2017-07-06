# -*- coding: utf-8 -*-
"""
Created on Wed July 6 2017

@author: T Williams, F Ren
"""

import numpy as np
import pandas as pd
import imp
plotTernary = imp.load_source("plt_ternary_save", "plotTernary.py")

# Set up paths
path = '..//..//data//master_data//'
save_path = '..//..//figures//'

s8_flnm = 'CLEANED_Sample8_master_metadata_high_WDS.csv'
s17_flnm = 'CLEANED_Sample17_master_metadata_high_WDS.csv'

s8_pth = path + s8_flnm
s17_pth = path + s17_flnm

# Load in data
s8df = pd.read_csv(s8_pth, usecols=['Co_adjusted', 'V_adjusted', ' Zr_adjusted', 'Co_WDS', 'V_WDS', 'Zr_WDS'])
s17df = pd.read_csv(s17_pth, usecols=['Co_adjusted', 'V_adjusted', ' Zr_adjusted', 'Co_WDS', 'V_WDS', 'Zr_WDS'])

# Change scale of model data to 0-100
s8df.loc[:, ['Co_adjusted', 'V_adjusted', ' Zr_adjusted']] = s8df.loc[:, ['Co_adjusted', 'V_adjusted', ' Zr_adjusted']] * 100
s17df.loc[:, ['Co_adjusted', 'V_adjusted', ' Zr_adjusted']] = s17df.loc[:, ['Co_adjusted', 'V_adjusted', ' Zr_adjusted']] * 100

# Calculate atomic difference (error)
s8df['Co_error'] = s8df.loc[:, 'Co_adjusted'] - s8df.loc[:, 'Co_WDS']
s8df['V_error'] = s8df.loc[:, 'V_adjusted'] - s8df.loc[:, 'V_WDS']
s8df['Zr_error'] = s8df.loc[:, ' Zr_adjusted'] - s8df.loc[:, 'Zr_WDS']

s17df['Co_error'] = s17df.loc[:, 'Co_adjusted'] - s17df.loc[:, 'Co_WDS']
s17df['V_error'] = s17df.loc[:, 'V_adjusted'] - s17df.loc[:, 'V_WDS']
s17df['Zr_error'] = s17df.loc[:, ' Zr_adjusted'] - s17df.loc[:, 'Zr_WDS']

print(s17df)

# Create dataframes for plotting
s8_co_data = pd.concat([s8df.loc[:, ['Co_adjusted', 'V_adjusted', ' Zr_adjusted']], np.abs(s8df.loc[:, 'Co_error'])], axis=1)
s8_v_data = pd.concat([s8df.loc[:, ['Co_adjusted', 'V_adjusted', ' Zr_adjusted']], np.abs(s8df.loc[:, 'V_error'])], axis=1)
s8_zr_data = pd.concat([s8df.loc[:, ['Co_adjusted', 'V_adjusted', ' Zr_adjusted']], np.abs(s8df.loc[:, 'Zr_error'])], axis=1)

s17_co_data = pd.concat([s17df.loc[:, ['Co_adjusted', 'V_adjusted', ' Zr_adjusted']], np.abs(s17df.loc[:, 'Co_error'])], axis=1)
s17_v_data = pd.concat([s17df.loc[:, ['Co_adjusted', 'V_adjusted', ' Zr_adjusted']], np.abs(s17df.loc[:, 'V_error'])], axis=1)
s17_zr_data = pd.concat([s17df.loc[:, ['Co_adjusted', 'V_adjusted', ' Zr_adjusted']], np.abs(s17df.loc[:, 'Zr_error'])], axis=1)

# Format dataframes for ease of viewing
s8_co_data.columns = ['Co','V','Zr','Co_error']
s8_v_data.columns = ['Co','V','Zr','V_error']
s8_zr_data.columns = ['Co','V','Zr','Zr_error']

s17_co_data.columns = ['Co','V','Zr','Co_error']
s17_v_data.columns = ['Co','V','Zr','V_error']
s17_zr_data.columns = ['Co','V','Zr','Zr_error']

# Plot data
plotTernary.plt_ternary_save(s8_co_data.values, sv=True, labelNames=['Co','V','Zr'], tertitle='', cbl='',
                             vmin=0, vmax=5, svpth=save_path, svflnm='FigureS7_8Co')
plotTernary.plt_ternary_save(s8_v_data.values, sv=True, labelNames=['Co','V','Zr'], tertitle='', cbl='',
                             vmin=0, vmax=5, svpth=save_path, svflnm='FigureS7_8V')
plotTernary.plt_ternary_save(s8_zr_data.values, sv=True, labelNames=['Co','V','Zr'], tertitle='', cbl='',
                             vmin=0, vmax=5, svpth=save_path, svflnm='FigureS7_8Zr')

plotTernary.plt_ternary_save(s17_co_data.values, sv=True, labelNames=['Co','V','Zr'], tertitle='', cbl='',
                             vmin=0, vmax=5, svpth=save_path, svflnm='FigureS7_17Co')
plotTernary.plt_ternary_save(s17_v_data.values, sv=True, labelNames=['Co','V','Zr'], tertitle='', cbl='',
                             vmin=0, vmax=5, svpth=save_path, svflnm='FigureS7_17V')
plotTernary.plt_ternary_save(s17_zr_data.values, sv=True, labelNames=['Co','V','Zr'], tertitle='', cbl='',
                             vmin=0, vmax=5, svpth=save_path, svflnm='FigureS7_17Zr')