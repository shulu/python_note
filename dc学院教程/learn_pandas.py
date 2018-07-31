# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.rand(6,3))
print(df.head())

df.to_csv('numppy.csv')