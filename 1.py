import pandas as pd
import numpy as np
import glob

# Step 1: Load all CSVs
csv_files = glob.glob('path/to/your/csvs/*.csv')  # Replace with your path
df = pd.concat([pd.read_csv(file) for file in csv_files])
df.reset_index(drop=True, inplace=True)

# Step 2: Create timestamp
df['Timestamp'] = pd.to_datetime(df[['Year', 'Month', 'Day', 'Hour']])
df.set_index('Timestamp', inplace=True)

# Step 3: Feature engineering
df['hour'] = df.index.hour
df['dayofyear'] = df.index.dayofyear

# Step 4: Select features and target
features = ['GHI', 'DHI', 'DNI', 'Temperature', 'Relative Humidity', 'hour', 'dayofyear']
target = 'GHI'
