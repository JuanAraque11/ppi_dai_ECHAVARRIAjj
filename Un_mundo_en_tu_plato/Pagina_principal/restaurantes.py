import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist

import geopandas as gpd

url = ""

datos = gpd.read_file(url)