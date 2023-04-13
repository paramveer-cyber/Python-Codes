import pandas as pd
import numpy as np

some_values = {
    "Names": ["someone", "something", "somehow", "somewhere"],
    "Length": [7, 9, 7, 9], 
    "Vowels": [4, 3, 3, 4]
}
data_frame = pd.DataFrame(some_values)
data_frame.to_csv("some_csv.csv", index=False)