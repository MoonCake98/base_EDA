from main import load_csv
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
        self.submit_button = pn.widgets.Button(name="Load CSV", button_type="primary")

        # object file input component
        self.input = pn.widgets.FileInput(accept=".csv", multiple=False)

        self.df = None

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
        # complete servable answer
        self.complete_serving = pn.Column(
            self.input,self.submit_button, self.table,
                   tabs,  sizing_mode="stretch_both",
        styles={
        "width": "100vw",     # full viewport width
        "height": "100vh",    # full viewport height
        "overflow": "hidden"  # prevents spillover
        })

        # attach the update of the table to the button click event
        self.submit_button.on_click(self.load_csv)

        self.complete_serving.servable() # displays component in server app

    def load_csv(self,event):
        if self.input.value is not None:
            self.df = pd.read_csv(io.BytesIO(self.input.value))
            self.table.clear()
            self.table.append(pn.widgets.Tabulator(self.df, pagination="remote",theme="midnight",sizing_mode="stretch_both",layout="fit_columns"))
            print("data loading complete")
            





app = eda_app()