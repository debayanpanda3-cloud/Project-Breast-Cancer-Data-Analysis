"""Plot pairwise relationships between selected breast-cancer features.

Examples
--------
List the available columns::

    python plot_breast_cancer_pairs.py --list-features

Plot selected features::

    python plot_breast_cancer_pairs.py \
        --features "mean radius" "mean texture" "mean perimeter"

The plot is displayed by default. Save it instead with ``--output``.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import pandas as pd
import seaborn as sns


DEFAULT_DATASET = Path(__file__).with_name("breast_cancer.csv")
DEFAULT_HUE_COLUMN = "diagnosis_label"


def load_data(dataset: Path) -> pd.DataFrame:
    """Load the dataset and report a useful error when it is unavailable."""
    if not dataset.is_file():
        raise FileNotFoundError(f"Dataset not found: {dataset}")
    return pd.read_csv(dataset)


def available_features(data: pd.DataFrame, hue_column: str) -> list[str]:
    """Return numeric mean columns that can be used as scatterplot features."""
    return [
        column
        for column in data.select_dtypes(include="number").columns
        if column != hue_column and column.startswith("mean ")
    ]


def plot_pairwise(
    data: pd.DataFrame,
    features: Sequence[str],
    hue_column: str | None = DEFAULT_HUE_COLUMN,
):
    """Create and return a seaborn pairwise scatterplot for ``features``."""
    if len(features) < 2:
        raise ValueError("Select at least two features to compare.")

    unavailable_features = [
        feature for feature in features if feature not in data or not feature.startswith("mean ")
    ]
    if unavailable_features:
        raise ValueError(
            "Only mean features are supported. Unavailable feature(s): "
            + ", ".join(repr(feature) for feature in unavailable_features)
        )

    non_numeric = [
        feature for feature in features if not pd.api.types.is_numeric_dtype(data[feature])
    ]
    if non_numeric:
        raise ValueError(
            "Features must be numeric: " + ", ".join(repr(feature) for feature in non_numeric)
        )

    if hue_column is not None and hue_column not in data:
        raise ValueError(f"Unknown hue column: {hue_column!r}")

    plot_data = data[list(features)].copy()
    if hue_column is not None:
        plot_data[hue_column] = data[hue_column]

    plot = sns.pairplot(
        plot_data,
        vars=list(features),
        hue=hue_column,
        diag_kind="hist",
        corner=True,
        plot_kws={"alpha": 0.7, "s": 35},
    )
    for axis in plot.axes.flat:
        if axis is not None:
            axis.grid(True, alpha=0.3)
    return plot


def add_feature_legend(
    plot,
    all_features: Sequence[str],
    active_features: Sequence[str],
) -> None:
    """Add a legend showing every available feature and its active state."""
    active = set(active_features)
    handles = [
        Patch(
            facecolor="green" if feature in active else "red",
            label=feature,
        )
        for feature in all_features
    ]
    plot.figure.legend(
        handles=handles,
        title=f"Features ({len(all_features)} total)",
        loc="center left",
        bbox_to_anchor=(1.02, 0.5),
        frameon=True,
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Plot pairwise scatterplots for selected breast-cancer features."
    )
    parser.add_argument(
        "--dataset",
        type=Path,
        default=DEFAULT_DATASET,
        help=f"CSV file to read (default: {DEFAULT_DATASET.name})",
    )
    parser.add_argument(
        "--features",
        nargs="+",
        metavar="FEATURE",
        help="Feature names to compare. Quote names containing spaces.",
    )
    parser.add_argument(
        "--hue",
        default=DEFAULT_HUE_COLUMN,
        help=(
            "Column used to color points (default: diagnosis_label). "
            "Use 'none' to disable coloring."
        ),
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Save the plot to this file instead of displaying it.",
    )
    parser.add_argument(
        "--list-features",
        action="store_true",
        help="List numeric feature columns and exit.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    data = load_data(args.dataset)
    features = available_features(data, args.hue)

    if args.list_features:
        print("\n".join(features))
        return

    selected_features = args.features or features[:4]
    hue_column = None if args.hue.lower() == "none" else args.hue
    plot = plot_pairwise(data, selected_features, hue_column)
    add_feature_legend(plot, features, selected_features)
    plot.figure.suptitle("Breast Cancer Feature Pairwise Scatterplot", y=1.02)
    plot.figure.tight_layout(rect=(0, 0, 0.8, 1))

    if args.output:
        plot.figure.savefig(args.output, dpi=300, bbox_inches="tight")
        print(f"Saved plot to {args.output}")
    else:
        plt.show()


if __name__ == "__main__":
    main()
