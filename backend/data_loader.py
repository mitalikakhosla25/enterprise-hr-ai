from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "processed" / "hr_cleaned.csv"

hr_data = pd.read_csv(DATA_PATH)

print(f"HR data loaded: {hr_data.shape}")