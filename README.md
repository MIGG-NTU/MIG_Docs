# MIG Documentation

[![Deploy](https://github.com/MIGG-NTU/MIG_Docs/actions/workflows/deploy.yml/badge.svg)](https://github.com/MIGG-NTU/MIG_Docs/actions/workflows/deploy.yml)

This site is the [MIG Documentation](https://migg-ntu.github.io/MIG_Docs/) that contains most information and resources in Prof. Ping Tong's group.

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
