{{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}

Project Organization
------------


├── LICENSE
├── Makefile           <- Makefile
├── fabfile.py         <- Fabfile with commands like `fab launch_train` or `fab launch_scoring`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── deps           <- Frozen unique dependencies
│   ├── gen            <- Generated data for deliverables
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── test           <- The original, immutable data dump.
│
├── docs               <- A default Sphinx project; see sphinx-doc.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│   │                     the creator's initials, and a short `-` delimited description, e.g.
│   │                     `1.0-jqp-initial-data-exploration`.
│   ├── explo          <-
│   ├── gen            <-
│   ├── loaders        <-
│   └── viz            <-
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── data           <- Scripts to download or generate data, & do basic preprocessing
│   │   └── TODO
│   │
│   ├── features       <- Scripts to turn raw data into features for modeling,
│   │   │                 comment some lines here if you want to speed up generation
│   │   │                 of features and you don't need those.
│   │   └── TODO
│   │
│   ├── models         <- Scripts to train models and then use trained models to make
│   │   │                 predictions
│   │   └── TODO
│   │
│   └── visualization  <- Scripts to create exploratory and results oriented visualizations
│       └── TODO
│
├── cnf.py             <- Shared constants
│
├── env.py             <- Imports tools & set global settings
│
├── paths.py           <- Provides absolute paths for diverse dependencies
│
└── tox.ini            <- tox file with settings for running tox; see tox.testrun.org
