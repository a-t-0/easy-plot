"""File used to create and export plots and tables directly into latex. Can be
used to automatically update your results each time you run latex.

For copy-pastable examples, see:     example_create_a_table()
example_create_multi_line_plot()     example_create_single_line_plot()
at the bottom of this file.
"""

import os

import numpy as np
from typeguard import typechecked


# replace this with your own table creation and then pass it to
# put_table_in_tex(..)
@typechecked
def example_create_a_table() -> None:
    """Example on how to create a latex table from Python."""

    table_name = "example_table_name"
    rows = 2
    columns = 4
    table_matrix = np.zeros((rows, columns), dtype=object)
    table_matrix[:, :] = ""  # replace the standard zeros with empty cell
    for column in range(0, columns):
        for row in range(0, rows):
            table_matrix[row, column] = row + column
    table_matrix[1, 0] = "example"
    table_matrix[0, 1] = "grid sizes"

    put_table_in_tex(table_matrix=table_matrix, filename=table_name)


# Create a table with: table_matrix = np.zeros((4,4),dtype=object) and pass
# it to this object
@typechecked
def put_table_in_tex(table_matrix: np.ndarray, filename: str) -> None:
    """This table can be directly plotted into latex by putting the commented
    code below into your latex file at the position where you want your
    table:"""
    # \begin{table}[H]
    #     \\centering
    #     \\caption{Results some computation.}\\label{tab:some_computation}
    #     \begin{tabular}{|c|c|} % remember to update this to show all
    #     %columns of table
    #         \\hline
    #         \\input{latex/project3/tables/q2.txt}
    #     \\end{tabular}
    # \\end{table}

    # You should update the number of columns in that latex code.

    cols = np.shape(table_matrix)[1]
    some_format = "%s"
    for _ in range(1, cols):
        some_format = some_format + " & %s"
    some_format = some_format + ""
    print(f"format={format}")
    # TODO: Change to something else to save as txt.
    os.mkdir("latex/tables/")
    np.savetxt(
        "latex/" + "tables/" + filename + ".txt",
        table_matrix,
        delimiter=" & ",
        # fmt=format,  # type: ignore[arg-type]
        fmt=some_format,  # type: ignore[arg-type]
        newline="  \\\\ \\hline \n",
    )
