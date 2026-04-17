import panel as pn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import io
print(sys.executable)

# make sure its a dark theme
pn.config.theme = "dark"


# cli to start panel server: `panel serve main.py`

# cli for dev mode | panel serve app.py --dev --show --autoreload 
# reloads app on file changes and opens in browser automatically

# configures panel en preloads the specified extensions and widget support
pn.extension("plotly", "vega", "tabulator")

# test alert types
# text = (
#     "This is a **{alert_type}** alert with [an example link]"
#     "(https://panel.holoviz.org/). Give it a click if you like."
# )

# test_alert = pn.Column(*[
#     pn.pane.Alert(text.format(alert_type=at), alert_type=at)
#     for at in pn.pane.Alert.param.alert_type.objects],
#     sizing_mode="stretch_width"
# )

# submit button test
submit_test = pn.widgets.Button(name="Load CSV", button_type="primary")

# test file input component
test_file_input = pn.widgets.FileInput(accept=".csv", multiple=False)


# binding file input to test print
# pn.bind(test_file_input, print(test_file_input.value))


table = pn.Column(
    pn.pane.Markdown(
        "### No data loaded yet. Please select a CSV file and click 'Load CSV' to display the data."
        )
)

def load_csv(event):
    if test_file_input.value is not None:
        df = pd.read_csv(io.BytesIO(test_file_input.value))
        global table
        table.clear()
        table.append(pn.widgets.Tabulator(df, pagination="remote",theme="midnight",sizing_mode="stretch_both",layout="fit_columns"))
        print("data loading complete")
submit_test.on_click(load_csv)

p1 = pn.Column(pn.pane.Markdown("### This is a test panel app"), sizing_mode="stretch_both")

#add tabs
tabs= pn.Tabs(
    ("Tab 1", p1),
    ("Tab 2", pn.pane.Markdown("### This is tab 2 content")),
    ("Tab 3", pn.pane.Markdown("### This is tab 3 content")),
    sizing_mode="stretch_both", dynamic=True
)

# label displayable panel components
test = pn.Column(test_file_input,submit_test, table, tabs,  sizing_mode="stretch_both",
    styles={
        "width": "100vw",     # full viewport width
        "height": "100vh",    # full viewport height
        "overflow": "hidden"  # prevents spillover
    })



test.servable() # displays component in server app

# if __name__ == "__main__":

