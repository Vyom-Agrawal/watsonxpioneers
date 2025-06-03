import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest

def load_poaching_data(filepath):
    df = pd.read_csv(filepath)
    # Basic cleaning
    df = df.dropna(subset=['species', 'location', 'date', 'latitude', 'longitude'])
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df = df.dropna(subset=['date'])
    return df

def load_nasa_hls_data(filepath):
    df = pd.read_csv(filepath)
    if 'acquisition_date' in df.columns:
        df['acquisition_date'] = pd.to_datetime(df['acquisition_date'], errors='coerce')
    return df

def merge_datasets(poaching_df, satellite_df, spatial_tolerance=0.01, temporal_tolerance=pd.Timedelta('7 days')):
    merged_records = []
    for idx, p_row in poaching_df.iterrows():
        sat_subset = satellite_df[
            (np.abs(satellite_df['latitude'] - p_row['latitude']) <= spatial_tolerance) &
            (np.abs(satellite_df['longitude'] - p_row['longitude']) <= spatial_tolerance)
        ]
        sat_subset = sat_subset[
            (sat_subset['acquisition_date'] >= p_row['date'] - temporal_tolerance) &
            (sat_subset['acquisition_date'] <= p_row['date'] + temporal_tolerance)
        ]
        for _, s_row in sat_subset.iterrows():
            merged_records.append({
                'species': p_row['species'],
                'location': p_row['location'],
                'poaching_date': p_row['date'],
                'latitude': p_row['latitude'],
                'longitude': p_row['longitude'],
                'satellite_date': s_row['acquisition_date'],
                'ndvi': s_row.get('ndvi', np.nan),
                'deforestation_index': s_row.get('deforestation_index', np.nan)
            })
    merged_df = pd.DataFrame(merged_records)
    return merged_df

def bias_correction(df, features):
    clf = IsolationForest(contamination=0.05, random_state=42)
    df['bias_flag'] = clf.fit_predict(df[features])
    corrected_df = df[df['bias_flag'] == 1].copy()
    corrected_df.drop(columns=['bias_flag'], inplace=True)
    return corrected_df

# Example usage (uncomment for actual use):
# poaching_df = load_poaching_data('data/raw/lemis_poaching.csv')
# satellite_df = load_nasa_hls_data('data/raw/nasa_hls.csv')
# merged_df = merge_datasets(poaching_df, satellite_df)
# corrected_df = bias_correction(merged_df, ['ndvi', 'deforestation_index'])
# corrected_df.to_csv('data/processed/merged_corrected.csv', index=False)
