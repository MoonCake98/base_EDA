import panel as pn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import io

# start command:
# panel serve app.py --dev --show --autoreload
class eda_app():
    """"base eda web app based on panel architecture"""
    def __init__(self):
        self.input = None
        
        self.table = pn.Column(
            pn.pane.Markdown(
                "### No data loaded yet. Please select a CSV file and click 'Load CSV' to display the data."
                )
                )

        
        # self.test_file_input = test_file_input
        # self.tabs = tabs

        pn.config.theme = "dark"
        pn.extension("plotly", "vega", "tabulator")

        # submit button
        submit_test = pn.widgets.Button(name="Load CSV", button_type="primary")

        # object file input component
        self.input = pn.widgets.FileInput(accept=".csv", multiple=False)

        self.table = pn.Column(
            pn.pane.Markdown(
                "### No data loaded yet. Please select a CSV file and click 'Load CSV' to display the data."
                )
                )

        p1 = pn.Column(pn.pane.Markdown("### This is a test panel app"), sizing_mode="stretch_both")

        #add tabs
        tabs= pn.Tabs(
            ("Tab 1", p1),
            ("Tab 2", pn.pane.Markdown("### This is tab 2 content")),
            ("Tab 3", pn.pane.Markdown("### This is tab 3 content")),
            sizing_mode="stretch_both", dynamic=True
        )

    # def load_csv(event):
    #     if test_file_input.value is not None:
    #     df = pd.read_csv(io.BytesIO(test_file_input.value))
    #     global table
    #     table.clear()
    #     table.append(pn.widgets.Tabulator(df, pagination="remote",theme="midnight",sizing_mode="stretch_both",layout="fit_columns"))
    #     print("data loading complete")
    #     submit_test.on_click(load_csv)

        
        # complete servable answer
        self.complete_serving = pn.Column(
            self.input,submit_test, self.table,
                   tabs,  sizing_mode="stretch_both",
        styles={
        "width": "100vw",     # full viewport width
        "height": "100vh",    # full viewport height
        "overflow": "hidden"  # prevents spillover
        })

        self.complete_serving.servable() # displays component in server app


app = eda_app()