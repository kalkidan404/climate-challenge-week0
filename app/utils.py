import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

ethiopia = pd.read_csv(os.path.join(BASE_DIR, "data", "ethiopia_clean.csv"))
kenya = pd.read_csv(os.path.join(BASE_DIR, "data", "kenya_clean.csv"))
tanzania = pd.read_csv(os.path.join(BASE_DIR, "data", "tanzania_clean.csv"))
nigeria = pd.read_csv(os.path.join(BASE_DIR, "data", "nigeria_clean.csv"))
sudan= pd.read_csv(os.path.join(BASE_DIR, "data", "sudan_clean.csv"))
