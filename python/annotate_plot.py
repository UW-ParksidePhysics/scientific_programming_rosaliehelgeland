"""
Annotate a plot using Pyplot's textLinks to an external site. function

Module name:
annotate_plot

Parameters:
annotations: dict

Dictionary whose keys are the labels, as strings, to be annotated and whose values are dictionaries 
with the following key-value pairs:
'position': ndarray, shape (2,)
x, y coordinates for the position of the textbox.
'alignment': list or tuple of str, shape (2,)
Horizontal alignment and vertical alignment values for the text function.
'fontsize': float
Value of the font size in points.

Returns:
annotation_objects: list
List of text annotation objects returned by Pyplot's text function.

Raises:
KeyError
When a required key is missing from the annotation dictionary.

Test:
Sign and timestamp a test graph with the string "Created by (Your first name) (Your last name) 
(Today's date in ISO 8601 format)" in the bottom left of the plot below the axes labels and tickmarks.
 Use Python's datetime module to get the date from the system.
"""
__author__ = "rosie"
import numpy as np
import matplotlib.pyplot as plt
from datetime import date

def annotate_plot(annotations: dict) -> list:
    annotate_objects = []
    try:
        for label, value in annotations.items():
            position = value["position"]
            alignment= value["alignment"]
            fontsize = value["fontsize"]

            annotation = plt.text(
                position[0],
                position[1],
                label,
                ha = alignment[0],
                va = alignment[1],
                fontsize = fontsize
            )

            annotate_objects.append(annotation)

        return annotate_objects
    except KeyError as error:
        print(f"required key missing from annotation dictionary!")

if __name__ == "__main__":
    x_values = np.arange(1,10)
    y_values = (x_values**2)
    
    plt.plot(x_values, y_values)

    today = date.today().isoformat()
    
    
    annotations = {
        f"Created by Rosie Helgeland on {today}": {
            "position": np.array([1, -10]),
            "alignment": ("left", "top"),
            "fontsize": 10
        }
        
    }

    annotate_plot(annotations)

    plt.savefig("annotate_plot.png")