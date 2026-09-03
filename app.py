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

        
        # self.submit_test = submit_test
        # self.test_file_input = test_file_input
        # self.tabs = tabs

        pn.config.theme = "dark"
        pn.extension("plotly", "vega", "tabulator")

        # submit button
        submit_test = pn.widgets.Button(name="Load CSV", button_type="primary")

        # test file input component
        test_file_input = pn.widgets.FileInput(accept=".csv", multiple=False)

        table = pn.Column(
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
        

        test = pn.Column(test_file_input,submit_test, table, tabs,  sizing_mode="stretch_both",
        styles={
        "width": "100vw",     # full viewport width
        "height": "100vh",    # full viewport height
        "overflow": "hidden"  # prevents spillover
        })

        test.servable() # displays component in server app



def main():
        # create an instance of the EDA_webapp class
        print("webapp instance creating")

        web_app = eda_app()
        print("created")


if __name__ == "__main__":
    main()``