import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
st.title("Climate Dashboard")

# Load data
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

ethiopia = pd.read_csv(os.path.join(BASE_DIR, "data", "ethiopia_clean.csv"))
kenya = pd.read_csv(os.path.join(BASE_DIR, "data", "kenya_clean.csv"))
tanzania = pd.read_csv(os.path.join(BASE_DIR, "data", "tanzania_clean.csv"))
sudan= pd.read_csv(os.path.join(BASE_DIR, "data", "sudan_clean.csv"))
nigeria = pd.read_csv(os.path.join(BASE_DIR, "data", "nigeria_clean.csv"))

df = pd.concat([ethiopia, kenya, tanzania, sudan, nigeria])

# Country selector
countries = st.multiselect(
    "Select Countries",
    df["Country"].unique(),
    default=df["Country"].unique()
)

filtered = df[df["Country"].isin(countries)]

# Variable selector
var = st.selectbox("Select Variable", ["T2M", "PRECTOTCORR", "RH2M"])

# Year filter (optional simple version)
year_range = st.slider("Year range", 2015, 2026, (2015, 2026))
filtered = filtered[(filtered["YEAR"] >= year_range[0]) & (filtered["YEAR"] <= year_range[1])]

# Plot
st.subheader("Trend Over Time")

fig, ax = plt.subplots()

for c in countries:
    temp = filtered[filtered["Country"] == c].groupby("MONTH")[var].mean()
    ax.plot(temp, label=c)

ax.legend()
st.pyplot(fig)