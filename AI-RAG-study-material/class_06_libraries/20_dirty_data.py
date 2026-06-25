import pandas as pd
import numpy as np

# Create a DataFrame that includes a missing value (NaN).
dirty_df = pd.DataFrame({"Data": [10, np.nan, 10, 40]})
print("Raw Dirty Data Example:")
print(dirty_df)
