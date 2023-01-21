"""Exports a plot/image to a file."""
import os
from typing import List

import matplotlib
from typeguard import typechecked


@typechecked
def export_plot(
    some_plt: matplotlib.pyplot, filename: str, extensions: List[str]
) -> None:
    """

    :param plt:
    :param filename:

    """
    create_target_dir_if_not_exists("latex/Images/", "graphs")
    for extension in extensions:
        some_plt.savefig(
            "latex/Images/" + "graphs/" + filename + f".{extension}",
            dpi=200,
        )


@typechecked
def create_target_dir_if_not_exists(path: str, new_dir_name: str) -> None:
    """

    :param path:
    :param new_dir_name:

    """
    if os.path.exists(path):
        if not os.path.exists(f"{path}/{new_dir_name}"):
            os.makedirs(f"{path}/{new_dir_name}")
    else:
        raise Exception(f"Error, path={path} did not exist.")
