import panel as pn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys
print(sys.executable)

# cli to start panel server: `panel serve main.py`

# configures panel en preloads the specified extensions and widget support
pn.extension("plotly", "vega", "tabulator")

# create displayable panel component
test = pn.panel("Hello, Panel!")

if __name__ == "__main__":
    test.servable() # displays component in server app

