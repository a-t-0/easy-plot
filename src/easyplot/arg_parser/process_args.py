"""Completes the tasks specified in the arg_parser."""
import argparse

from typeguard import typechecked


@typechecked
def process_args(args: argparse.Namespace, default_output_path: str) -> None:
    """Processes the arguments and ensures the accompanying tasks are
    executed."""
    # Create output path.
    print(f"TODO: create: {default_output_path}")

    # Delete output images if desired.
    if args.delete_images:
        print("TODO: delete images.")

    if args.box_plot:
        print("TODO: Create box plot.")

    if args.line_plot:
        print("TODO: Create line plot.")

    if args.latex_table:
        print("TODO: Create LaTex table.")
