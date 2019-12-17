from pandas_flavor import register_dataframe_method
from ipywidgets import HBox
import qgrid


@register_dataframe_method
def display(df, width=800, *args, **kwargs):
    return HBox(
        [
            qgrid.show_grid(
                df,
                grid_options={"forceFitColumns": True, "defaultColumnWidth": 200},
                *args,
                **kwargs,
            )
        ],
        layout={"width": f"{width}px"},
    )
