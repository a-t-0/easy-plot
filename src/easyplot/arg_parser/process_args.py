"""Completes the tasks specified in the arg_parser."""
import argparse

from typeguard import typechecked

from src.easyplot.export_plot import create_target_dir_if_not_exists
from src.easyplot.line_plot.latex_table import example_create_a_table
from src.easyplot.line_plot.line_plot import example_create_multi_line_plot


@typechecked
def process_args(args: argparse.Namespace, default_output_path: str) -> None:
    """Processes the arguments and ensures the accompanying tasks are
    executed."""
    # Create output path.
    create_target_dir_if_not_exists(default_output_path)
    print(f"TODO: create: {default_output_path}")

    # Delete output images if desired.
    if args.delete_images:
        print("TODO: delete images.")

    if args.box_plot:
        print("TODO: Create box plot.")

    if args.line_plot:
        example_create_multi_line_plot(
            extensions=[
                ".png",
            ],
            filename="example",
            output_dir=default_output_path,
        )

    if args.latex_table:
        print("TODO: Create LaTex table.")
        example_create_a_table(
            filename="example", output_dir=default_output_path
        )
