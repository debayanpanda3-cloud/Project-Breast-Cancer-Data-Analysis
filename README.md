# Breast cancer feature plots

`plot_breast_cancer_pairs.py` creates a pairwise scatterplot from
`breast_cancer.csv`. Install the dependencies with:

```bash
python3 -m pip install -r requirements.txt
```

List the available mean features:

```bash
python3 plot_breast_cancer_pairs.py --list-features
```

Select the mean features to compare by passing their exact CSV column names.
Error and worst features are intentionally excluded:

```bash
python3 plot_breast_cancer_pairs.py \
  --features "mean radius" "mean texture" "mean perimeter" "mean area"
```

The points are colored by `diagnosis_label` by default. Save the result
instead of opening a window with `--output`:

```bash
python3 plot_breast_cancer_pairs.py \
  --features "mean radius" "mean texture" \
  --output breast-cancer-pairs.png
```

Use `--hue none` to disable diagnosis coloring. If `--features` is omitted,
the first four mean features are plotted. Grid lines are enabled on the
plot axes, and the legend lists all available mean features: active
features are green and inactive features are red.
