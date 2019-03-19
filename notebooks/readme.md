# Setup

To set up your environment, you need `conda` installed, and run:
```sh
conda env create -f fair-recommendation.yml
```

Then activate the environment:
```sh
conda activate fair-recommendation
```

If you have several python environments installed in your system, then run the following command to give a reasonable name to your current environment:
```sh
python3 -m ipykernel install --user --name fair-recommendation --display-name fair-recommendation
```

Then start `jupyter` and select `fair-recommentdation` as your kernel when opening a notebook:
```sh
jupyter lab
```

### Update the environment
To add a new library, update [fair-recommendation.yml](fair-recommendation.yml) with the library and then run
```sh
conda env update -f fair-recommendation.yml
```
to refresh your local environment.

# Content

This folder contains 3 notebooks that run experiments and showcase the use of the fairness metrics.

## [Test2.ipynb](Test2.ipynb)
This is an example notebook to get you started. And this is a very important sentence explaining why this notebook is very important.
