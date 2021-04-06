# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
from datetime import datetime


# -- Project information -----------------------------------------------------
project = 'MIG Documentation'
author = "MIGG-NTU"
copyright = f"2020–{datetime.today().year}, {author}"
github_user = "MIGG-NTU"
github_repo = "MIG_Docs"
github_url = f"https://github.com/{github_user}/{github_repo}"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.githubpages'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output ----------------------------------------------
import sphinx_rtd_theme

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_extra_path = []
html_last_updated_fmt = "%Y-%m-%d"
html_title = project
html_css_files = ["custom.css"]

html_context = {
    "favicon": "favicon.ico",
    "display_github": True,
    "github_user": github_user,
    "github_repo": github_repo,
    "github_version": "main",
    "conf_py_path": "/source/",
    "theme_vcs_pageview_mode": "blob",
    "menu_links": [
        (   '<i class="fa fa-home"></i> MIG Homopage',
            "https://personal.ntu.edu.sg/tongping/",
        ),
        (
            '<i class="fa fa-github fa-fw"></i> Source Code',
            github_url,
        ),
        (
            '<i class="fa fa-comments fa-fw"></i> Contact',
            f"{github_url}/discussions",
        ),
    ],
}
