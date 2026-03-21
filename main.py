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

# test alert types
text = (
    "This is a **{alert_type}** alert with [an example link]"
    "(https://panel.holoviz.org/). Give it a click if you like."
)

test_alert = pn.Column(*[
    pn.pane.Alert(text.format(alert_type=at), alert_type=at)
    for at in pn.pane.Alert.param.alert_type.objects],
    sizing_mode="stretch_width"
)

# test file input component
test_file_input = pn.widgets.FileInput(accept=".csv", multiple=False)

# label displayable panel component
test = pn.Column(test_alert, test_file_input)







test.servable() # displays component in server app

# if __name__ == "__main__":

