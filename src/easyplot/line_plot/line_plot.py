"""File used to create and export plots and tables directly into latex. Can be
used to automatically update your results each time you run latex.

For copy-pastable examples, see:     example_create_a_table()
example_create_multi_line_plot()     example_create_single_line_plot()
at the bottom of this file.
"""
from typing import List

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import lines
from typeguard import typechecked


@typechecked
def example_create_multi_line_plot() -> None:
    """Example that creates a plot with multiple lines.

    Copy paste it in your own code and modify the values accordingly.
    """

    multiple_y_series = np.zeros((2, 2), dtype=int)
    # actually fill with data
    multiple_y_series[0] = [1, 2]
    lineLabels = [
        "first-line",
        "second_line",
    ]  # add a label for each dataseries
    single_x_series = [3, 5]

    plot_multiple_lines(
        x=single_x_series,
        y_series=multiple_y_series,
        x_label="x-axis label [units]",
        y_label="y-axis label [units]",
        label=lineLabels,
        filename="3b",
        legendPosition=4,
    )


# plot graphs
@typechecked
def plot_multiple_lines(
    x: List,
    y_series: np.ndarray,
    x_label: str,
    y_label: str,
    label: List,
    filename: str,
    legendPosition: int,
) -> None:
    """

    :param x:
    :param y_series:
    :param x_label:
    :param y_label:
    :param label:
    :param filename:
    :param legendPosition:
    :param y_series:
    :param y_label:
    :param filename:
    :param y_label:
    :
    """
    # pylint: disable=R0913
    # TODO: reduce 9/5 arguments to at most 5/5 arguments.
    fig = plt.figure()
    ax = fig.add_subplot(111)

    # generate colours
    cmap = get_cmap(plt, len(y_series[:, 0]))

    # generate line types
    lineTypes = generateLineTypes(y_series)

    for i in range(0, len(y_series)):
        # overwrite linetypes to single type
        lineTypes[i] = "-"
        ax.plot(
            x,
            y_series[i, :],
            ls=lineTypes[i],
            label=label[i],
            fillstyle="none",
            c=cmap(i),
        )
        # color

    # configure plot layout
    plt.legend(loc=legendPosition)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.savefig(
        # os.path.dirname(__file__)
        "latex/"
        + "/Images/"
        + filename
        + ".png"
    )
    plt.clf()
    plt.close()


# Generate random line colours
# Source: https://stackoverflow.com/questions/14720331/
# how-to-generate-random-colors-in-matplotlib
@typechecked
def get_cmap(
    some_plt: matplotlib.pyplot,
    nr_of_colours: int,
    name: str = "hsv",
) -> matplotlib.colors.LinearSegmentedColormap:
    """Returns a function that maps each index in 0, 1, ..., n-1 to a distinct
    RGB color; the keyword argument name must be a standard mpl colormap name.

    :param n: param name:  (Default value = "hsv")
    :param name: Default value = "hsv")
    """
    return some_plt.cm.get_cmap(name, nr_of_colours)


@typechecked
def generateLineTypes(y_series: np.ndarray) -> List:
    """

    :param y_series:

    """
    # generate varying linetypes
    typeOfLines = list(lines.lineStyles.keys())

    while len(y_series) > len(typeOfLines):
        typeOfLines.append("-.")

    # remove void lines
    for i in range(0, len(y_series)):
        if typeOfLines[i] == "None":
            typeOfLines[i] = "-"
        if typeOfLines[i] == "":
            typeOfLines[i] = ":"
        if typeOfLines[i] == " ":
            typeOfLines[i] = "--"
    return typeOfLines
