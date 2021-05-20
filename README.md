# MIG Documentation

[![Deploy](https://github.com/MIGG-NTU/MIG_Docs/actions/workflows/deploy.yml/badge.svg)](https://github.com/MIGG-NTU/MIG_Docs/actions/workflows/deploy.yml)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-blue.svg)](https://creativecommons.org/licenses/by-nc/4.0/deed.en)

This repository contains the source codes of the [MIG Documenation](https://migg-ntu.github.io/MIG_Docs/),
which collects useful resources and links for the [Mathematical Imaging and Geophysics Group (MIGG) at NTU](https://personal.ntu.edu.sg/tongping/index.html):

- Source codes: https://github.com/MIGG-NTU/MIG_Docs
- Website: https://migg-ntu.github.io/MIG_Docs/

## Build the documentation

The documentation is built by [Sphinx](http://www.sphinx-doc.org/).
We can follow the steps below to build the documenation on our own computers.

1.  Clone the repository

    ```
    # Assume that the repository is downloaded to ~/Downloads/
    $ cd ~/Downloads/

    # Clone the repository and then switch to the directory
    $ git clone https://github.com/MIGG-NTU/MIG_Docs.git
    $ cd MIG_Docs
    ```

2.  Install requirements

    ```
    # Install requirements including Sphinx
    $ pip install -r requirements.txt
    ```

3.  Compile and generate documentation in HTML format

    ```
    $ make html
    ```

4.  The generated documentation is located in the ``build/html/`` directory
    and can be previewed locally by directly opening ``build/html/index.html``
    with a browser.

## License

This material uses [Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/deed.en).
You are free to share and adapt the material as long as you follow the following
license terms:

- Attribution: You must give appropriate credit, provide a link to the license, and indicate if changes were made.
- NonCommercial: You may not use the material for commercial purposes.
