import pandas as pd
from terratorch.datasets import HLS2Dataset

# Load LEMIS poaching data
poaching_df = pd.read_csv("lemis_2000_2014_cleaned.csv")

# Load NASA HLS-2 satellite data (convert to CSV-friendly format)
nasa_data = HLS2Dataset(root="nasa_hls/", split="train")
nasa_df = nasa_data.to_pandas()  # Export to DataFrame

# Merge datasets
merged_df = pd.merge(
    poaching_df, 
    nasa_df, 
    left_on=["latitude", "longitude"], 
    right_on=["lat", "lon"]
)

# Bias correction for citizen data (e.g., TARTLE)
from sklearn.ensemble import IsolationForest
clf = IsolationForest(contamination=0.01)
merged_df["is_valid"] = clf.fit_predict(merged_df[["poaching_count", "deforestation_rate"]])
clean_df = merged_df[merged_df["is_valid"] == 1]
