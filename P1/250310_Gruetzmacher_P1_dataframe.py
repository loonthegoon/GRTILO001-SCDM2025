#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 14:46:06 2025

@author: ilo
"""

import pandas as pd
ctd_file = pd.read_csv('./Assignment_P1/250309_CTD_data_with_units.dat',delimiter="\t")
ctd_dataframe = pd.DataFrame(ctd_file)
print(ctd_dataframe)