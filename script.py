# %%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import plotly.offline as py
import plotly.graph_objs as go
import plotly.express as px

# %% [markdown]
# # Participant#2: Age 40, Male 
# Medium Intensity Session

# %%
#Chest Breathing Interval
chest_bb_interval = pd.read_csv(r'C:\Users\wwwKa\OneDrive\Desktop\Digital Biomarkers\fatigueset\08\03\chest_bb_interval.csv')
chest_bb_interval['Datetime'] = pd.to_datetime(chest_bb_interval['timestamp'],unit='ms',origin='unix')
view = go.Scatter(x=chest_bb_interval['Datetime'], y=chest_bb_interval['duration'], name= 'Breathes')
py.iplot([view])

# %%
#Chest Raw acc Interval
chest_raw_acc = pd.read_csv(r'C:\Users\wwwKa\OneDrive\Desktop\Digital Biomarkers\fatigueset\08\03\chest_raw_acc.csv')
chest_raw_acc['Datetime'] = pd.to_datetime(chest_raw_acc['timestamp'],unit='ms',origin='unix')
vertical = go.Scatter(x=chest_raw_acc['Datetime'], y=chest_raw_acc['vertical'], name= 'vertical')
lateral = go.Scatter(x=chest_raw_acc['Datetime'], y=chest_raw_acc['lateral'], name= 'lateral')
sagittal = go.Scatter(x=chest_raw_acc['Datetime'], y=chest_raw_acc['sagittal'], name= 'sagittal')
py.iplot([vertical, lateral, sagittal])


# %%
#Chest Raw Breathing Interval
chest_raw_breathing = pd.read_csv(r'C:\Users\wwwKa\OneDrive\Desktop\Digital Biomarkers\fatigueset\08\03\chest_raw_breathing.csv')
chest_raw_breathing['Datetime'] = pd.to_datetime(chest_raw_breathing['timestamp'],unit='ms',origin='unix')
view = go.Scatter(x=chest_raw_breathing['Datetime'], y=chest_raw_breathing['breathing_waveform'], name= 'Breathes')
py.iplot([view])

# %%
chest_raw_ecg = pd.read_csv(r'C:\Users\wwwKa\OneDrive\Desktop\Digital Biomarkers\fatigueset\08\03\chest_raw_ecg.csv')
chest_raw_ecg['Datetime'] = pd.to_datetime(chest_raw_ecg['timestamp'],unit='ms',origin='unix')
view_chest_raw_ecg = go.Scatter(x=chest_raw_ecg['Datetime'], y=chest_raw_ecg['ecg_waveform'], name= 'ecg_waveform')
py.iplot([view_chest_raw_ecg])

# %%
chest_rr_interval = pd.read_csv(r'C:\Users\wwwKa\OneDrive\Desktop\Digital Biomarkers\fatigueset\08\03\chest_rr_interval.csv')
chest_rr_interval['Datetime'] = pd.to_datetime(chest_rr_interval['timestamp'],unit='ms',origin='unix')
view_chest_rr_interval = go.Scatter(x=chest_rr_interval['Datetime'], y=chest_rr_interval['duration'], name= 'duration')
py.iplot([view_chest_rr_interval])

# %%
ear_acc_left = pd.read_csv(r'C:\Users\wwwKa\OneDrive\Desktop\Digital Biomarkers\fatigueset\08\03\ear_acc_left.csv')
ear_acc_left['Datetime'] = pd.to_datetime(ear_acc_left['timestamp'],unit='ms',origin='unix')
ax = go.Scatter(x=ear_acc_left['Datetime'], y=ear_acc_left['ax'], name= 'ax')
ay = go.Scatter(x=ear_acc_left['Datetime'], y=ear_acc_left['ay'], name= 'ay')
az = go.Scatter(x=ear_acc_left['Datetime'], y=ear_acc_left['az'], name= 'az')
py.iplot([ax, ay, az])



# %%
ear_acc_right = pd.read_csv(r'C:\Users\wwwKa\OneDrive\Desktop\Digital Biomarkers\fatigueset\08\03\ear_acc_right.csv')
ear_acc_right['Datetime'] = pd.to_datetime(ear_acc_right['timestamp'],unit='ms',origin='unix')
ax = go.Scatter(x=ear_acc_right['Datetime'], y=ear_acc_right['ax'], name= 'ax')
ay = go.Scatter(x=ear_acc_right['Datetime'], y=ear_acc_right['ay'], name= 'ay')
az = go.Scatter(x=ear_acc_right['Datetime'], y=ear_acc_right['az'], name= 'az')
py.iplot([ax, ay, az])

# view_ear_acc_left_ax.show()
# view_ear_acc_left_ay.show()
# view_ear_acc_left_az.show()



# %%
ear_gyro_left = pd.read_csv(r'C:\Users\wwwKa\OneDrive\Desktop\Digital Biomarkers\fatigueset\08\03\ear_gyro_left.csv')
ear_gyro_left['Datetime'] = pd.to_datetime(ear_gyro_left['timestamp'],unit='ms',origin='unix')
gx = go.Scatter(x=ear_gyro_left['Datetime'], y=ear_gyro_left['gx'], name= 'gx')
gy = go.Scatter(x=ear_gyro_left['Datetime'], y=ear_gyro_left['gy'], name= 'gy')
gz = go.Scatter(x=ear_gyro_left['Datetime'], y=ear_gyro_left['gz'], name= 'gz')
py.iplot([gx, gy, gz])

# %%
ear_gyro_right = pd.read_csv(r'C:\Users\wwwKa\OneDrive\Desktop\Digital Biomarkers\fatigueset\08\03\ear_gyro_right.csv')
ear_gyro_right['Datetime'] = pd.to_datetime(ear_gyro_right['timestamp'],unit='ms',origin='unix')
gx = go.Scatter(x=ear_gyro_right['Datetime'], y=ear_gyro_right['gx'], name= 'gx')
gy = go.Scatter(x=ear_gyro_right['Datetime'], y=ear_gyro_right['gy'], name= 'gy')
gz = go.Scatter(x=ear_gyro_right['Datetime'], y=ear_gyro_right['gz'], name= 'gz')
py.iplot([gx, gy, gz])

# %%
ear_ppg_left = pd.read_csv(r'C:\Users\wwwKa\OneDrive\Desktop\Digital Biomarkers\fatigueset\08\03\ear_ppg_left.csv')
ear_ppg_left['Datetime'] = pd.to_datetime(ear_ppg_left['timestamp'],unit='ms',origin='unix')
green = go.Scatter(x=ear_ppg_left['Datetime'], y=ear_ppg_left['green'], name= 'green')
ir = go.Scatter(x=ear_ppg_left['Datetime'], y=ear_ppg_left['ir'], name= 'ir')
red = go.Scatter(x=ear_ppg_left['Datetime'], y=ear_ppg_left['red'], name= 'red')
py.iplot([green, ir, red])

# %%
ear_ppg_right = pd.read_csv(r'C:\Users\wwwKa\OneDrive\Desktop\Digital Biomarkers\fatigueset\08\03\ear_ppg_right.csv')
ear_ppg_right['Datetime'] = pd.to_datetime(ear_ppg_right['timestamp'],unit='ms',origin='unix')
green = go.Scatter(x=ear_ppg_right['Datetime'], y=ear_ppg_right['green'], name= 'green')
ir = go.Scatter(x=ear_ppg_right['Datetime'], y=ear_ppg_right['ir'], name= 'ir')
red = go.Scatter(x=ear_ppg_right['Datetime'], y=ear_ppg_right['red'], name= 'red')
py.iplot([green, ir, red])

# %%
forehead_acc = pd.read_csv(r'C:\Users\wwwKa\OneDrive\Desktop\Digital Biomarkers\fatigueset\08\03\forehead_acc.csv')
forehead_acc['Datetime'] = pd.to_datetime(forehead_acc['timestamp'],unit='ms',origin='unix')
ax = go.Scatter(x=forehead_acc['Datetime'], y=forehead_acc['ax'], name= 'ax')
ay = go.Scatter(x=forehead_acc['Datetime'], y=forehead_acc['ay'], name= 'ay')
az = go.Scatter(x=forehead_acc['Datetime'], y=forehead_acc['az'], name= 'az')
py.iplot([ax, ay, az])

# %%
forehead_eeg_alpha_abs = pd.read_csv(r'C:\Users\wwwKa\OneDrive\Desktop\Digital Biomarkers\fatigueset\08\03\forehead_eeg_alpha_abs.csv')
forehead_eeg_alpha_abs['Datetime'] = pd.to_datetime(forehead_eeg_alpha_abs['timestamp'],unit='ms',origin='unix')
TP9 = go.Scatter(x=forehead_eeg_alpha_abs['Datetime'], y=forehead_eeg_alpha_abs['TP9'], name= 'TP9')
AF7 = go.Scatter(x=forehead_eeg_alpha_abs['Datetime'], y=forehead_eeg_alpha_abs['AF7'], name= 'AF7')
AF8 = go.Scatter(x=forehead_eeg_alpha_abs['Datetime'], y=forehead_eeg_alpha_abs['AF8'], name= 'AF8')
TP10 = go.Scatter(x=forehead_eeg_alpha_abs['Datetime'], y=forehead_eeg_alpha_abs['TP10'], name= 'TP10')
py.iplot([TP9, AF7, AF8,TP10])

# %%
forehead_eeg_beta_abs = pd.read_csv(r'C:\Users\wwwKa\OneDrive\Desktop\Digital Biomarkers\fatigueset\08\03\forehead_eeg_beta_abs.csv')
forehead_eeg_beta_abs['Datetime'] = pd.to_datetime(forehead_eeg_beta_abs['timestamp'],unit='ms',origin='unix')
TP9 = go.Scatter(x=forehead_eeg_beta_abs['Datetime'], y=forehead_eeg_beta_abs['TP9'], name= 'TP9')
AF7 = go.Scatter(x=forehead_eeg_beta_abs['Datetime'], y=forehead_eeg_beta_abs['AF7'], name= 'AF7')
AF8 = go.Scatter(x=forehead_eeg_beta_abs['Datetime'], y=forehead_eeg_beta_abs['AF8'], name= 'AF8')
TP10 = go.Scatter(x=forehead_eeg_beta_abs['Datetime'], y=forehead_eeg_beta_abs['TP10'], name= 'TP10')
py.iplot([TP9, AF7, AF8,TP10])

# %%
forehead_eeg_delta_abs = pd.read_csv(r'C:\Users\wwwKa\OneDrive\Desktop\Digital Biomarkers\fatigueset\08\03\forehead_eeg_delta_abs.csv')
forehead_eeg_delta_abs['Datetime'] = pd.to_datetime(forehead_eeg_delta_abs['timestamp'],unit='ms',origin='unix')
TP9 = go.Scatter(x=forehead_eeg_delta_abs['Datetime'], y=forehead_eeg_delta_abs['TP9'], name= 'TP9')
AF7 = go.Scatter(x=forehead_eeg_delta_abs['Datetime'], y=forehead_eeg_delta_abs['AF7'], name= 'AF7')
AF8 = go.Scatter(x=forehead_eeg_delta_abs['Datetime'], y=forehead_eeg_delta_abs['AF8'], name= 'AF8')
TP10 = go.Scatter(x=forehead_eeg_delta_abs['Datetime'], y=forehead_eeg_delta_abs['TP10'], name= 'TP10')
py.iplot([TP9, AF7, AF8,TP10])

# %%
forehead_eeg_gamma_abs = pd.read_csv(r'C:\Users\wwwKa\OneDrive\Desktop\Digital Biomarkers\fatigueset\08\03\forehead_eeg_gamma_abs.csv')
forehead_eeg_gamma_abs['Datetime'] = pd.to_datetime(forehead_eeg_gamma_abs['timestamp'],unit='ms',origin='unix')
TP9 = go.Scatter(x=forehead_eeg_gamma_abs['Datetime'], y=forehead_eeg_gamma_abs['TP9'], name= 'TP9')
AF7 = go.Scatter(x=forehead_eeg_gamma_abs['Datetime'], y=forehead_eeg_gamma_abs['AF7'], name= 'AF7')
AF8 = go.Scatter(x=forehead_eeg_gamma_abs['Datetime'], y=forehead_eeg_gamma_abs['AF8'], name= 'AF8')
TP10 = go.Scatter(x=forehead_eeg_gamma_abs['Datetime'], y=forehead_eeg_gamma_abs['TP10'], name= 'TP10')
py.iplot([TP9, AF7, AF8,TP10])

# %%
forehead_eeg_raw = pd.read_csv(r'C:\Users\wwwKa\OneDrive\Desktop\Digital Biomarkers\fatigueset\08\03\forehead_eeg_raw.csv')
forehead_eeg_raw['Datetime'] = pd.to_datetime(forehead_eeg_raw['timestamp'],unit='ms',origin='unix')
TP9 = go.Scatter(x=forehead_eeg_raw['Datetime'], y=forehead_eeg_raw['TP9'], name= 'TP9')
AF7 = go.Scatter(x=forehead_eeg_raw['Datetime'], y=forehead_eeg_raw['AF7'], name= 'AF7')
AF8 = go.Scatter(x=forehead_eeg_raw['Datetime'], y=forehead_eeg_raw['AF8'], name= 'AF8')
TP10 = go.Scatter(x=forehead_eeg_raw['Datetime'], y=forehead_eeg_raw['TP10'], name= 'TP10')
py.iplot([TP9, AF7, AF8,TP10])

# %%
forehead_eeg_theta_abs = pd.read_csv(r'C:\Users\wwwKa\OneDrive\Desktop\Digital Biomarkers\fatigueset\08\03\forehead_eeg_theta_abs.csv')
forehead_eeg_theta_abs['Datetime'] = pd.to_datetime(forehead_eeg_theta_abs['timestamp'],unit='ms',origin='unix')
TP9 = go.Scatter(x=forehead_eeg_theta_abs['Datetime'], y=forehead_eeg_theta_abs['TP9'], name= 'TP9')
AF7 = go.Scatter(x=forehead_eeg_theta_abs['Datetime'], y=forehead_eeg_theta_abs['AF7'], name= 'AF7')
AF8 = go.Scatter(x=forehead_eeg_theta_abs['Datetime'], y=forehead_eeg_theta_abs['AF8'], name= 'AF8')
TP10 = go.Scatter(x=forehead_eeg_theta_abs['Datetime'], y=forehead_eeg_theta_abs['TP10'], name= 'TP10')
py.iplot([TP9, AF7, AF8,TP10])

# %%
forehead_gyro = pd.read_csv(r'C:\Users\wwwKa\OneDrive\Desktop\Digital Biomarkers\fatigueset\08\03\forehead_gyro.csv')
forehead_gyro['Datetime'] = pd.to_datetime(forehead_gyro['timestamp'],unit='ms',origin='unix')
gx = go.Scatter(x=forehead_gyro['Datetime'], y=forehead_gyro['gx'], name= 'gx')
gy = go.Scatter(x=forehead_gyro['Datetime'], y=forehead_gyro['gy'], name= 'gy')
gz = go.Scatter(x=forehead_gyro['Datetime'], y=forehead_gyro['gz'], name= 'gz')
py.iplot([gx, gy, gz])

# %%
wrist_acc = pd.read_csv(r'C:\Users\wwwKa\OneDrive\Desktop\Digital Biomarkers\fatigueset\08\03\wrist_acc.csv')
wrist_acc['Datetime'] = pd.to_datetime(wrist_acc['timestamp'],unit='ms',origin='unix')
ax = go.Scatter(x=wrist_acc['Datetime'], y=wrist_acc['ax'], name= 'ax')
ay = go.Scatter(x=wrist_acc['Datetime'], y=wrist_acc['ay'], name= 'ay')
az = go.Scatter(x=wrist_acc['Datetime'], y=wrist_acc['az'], name= 'az')
py.iplot([ax, ay, az])

# %%
wrist_bvp = pd.read_csv(r'C:\Users\wwwKa\OneDrive\Desktop\Digital Biomarkers\fatigueset\08\03\wrist_bvp.csv')
wrist_bvp['Datetime'] = pd.to_datetime(wrist_bvp['timestamp'],unit='ms',origin='unix')
c = go.Scatter(x=wrist_bvp['Datetime'], y=wrist_bvp['bvp'], name= 'bvp')
py.iplot([c])

# %%
wrist_eda = pd.read_csv(r'C:\Users\wwwKa\OneDrive\Desktop\Digital Biomarkers\fatigueset\08\03\wrist_eda.csv')
wrist_eda['Datetime'] = pd.to_datetime(wrist_eda['timestamp'],unit='ms',origin='unix')
c = go.Scatter(x=wrist_eda['Datetime'], y=wrist_eda['eda'], name= 'eda')
py.iplot([c])

# %%
wrist_hr = pd.read_csv(r'C:\Users\wwwKa\OneDrive\Desktop\Digital Biomarkers\fatigueset\08\03\wrist_hr.csv')
wrist_hr['Datetime'] = pd.to_datetime(wrist_hr['timestamp'],unit='ms',origin='unix')
c = go.Scatter(x=wrist_hr['Datetime'], y=wrist_hr['hr'], name= 'hr')
py.iplot([c])

# %%
wrist_ibi = pd.read_csv(r'C:\Users\wwwKa\OneDrive\Desktop\Digital Biomarkers\fatigueset\08\03\wrist_ibi.csv')
wrist_ibi['Datetime'] = pd.to_datetime(wrist_ibi['timestamp'],unit='ms',origin='unix')
c = go.Scatter(x=wrist_ibi['Datetime'], y=wrist_ibi['duration'], name= 'duration')
py.iplot([c])

# %%
wrist_skin_temperature = pd.read_csv(r'C:\Users\wwwKa\OneDrive\Desktop\Digital Biomarkers\fatigueset\08\03\wrist_skin_temperature.csv')
wrist_skin_temperature['Datetime'] = pd.to_datetime(wrist_skin_temperature['timestamp'],unit='ms',origin='unix')
c = go.Scatter(x=wrist_skin_temperature['Datetime'], y=wrist_skin_temperature['temp'], name= 'temp')
py.iplot([c])

# %%



