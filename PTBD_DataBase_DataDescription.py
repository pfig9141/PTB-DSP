# -*- coding: utf-8 -*-
# https://www.physionet.org/content/ptbdb/1.0.0/
# https://github.com/MIT-LCP/wfdb-python

import numpy as np
import wfdb
import matplotlib.pyplot as plt

directory = 'F:/Foldery/Nauka/Python/ekg/patient1/s0010_re'
ecg_record = wfdb.io.rdheader('F:/Foldery/Nauka/Python/ekg/patient1/s0010_re')

ecg_record.file_name[0]     # file name
ecg_record.fmt[0]           # format
ecg_record.adc_gain[0]      # ADV GAIN
ecg_record.adc_res[0]       # ADC RESOL
ecg_record.adc_zero[0]      # ADC ZERO
ecg_record.init_value[0]    # init value
ecg_record.checksum[0]      # cheksum
ecg_record.block_size[0]    # block size
ecg_record.sig_name[0]      # description

print(ecg_record.record_name + str(ecg_record.n_sig) + ' ' + str(int(ecg_record.fs)) + ' ' 
      + str(ecg_record.sig_len))
for k in range(ecg_record.n_sig):
    print(ecg_record.file_name[k] + ' ' + ecg_record.fmt[k] + ' ' + str(int(ecg_record.adc_gain[k])) +
      ' ' + str(ecg_record.adc_res[k]) + ' ' + str(ecg_record.adc_zero[k]) +
      ' ' + str(ecg_record.init_value[k]) + ' ' + str(ecg_record.checksum[k]) +
      ' ' + str(ecg_record.block_size[k]) + ' ' + ecg_record.sig_name[k])
    

    
signals, fields = wfdb.rdsamp(directory,sampfrom=0,sampto=2000,channels=[0,1])
N = len(signals)
plt.plot(np.arange(N),signals)
