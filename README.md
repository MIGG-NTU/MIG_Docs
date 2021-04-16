# MIG Documentation

[![Deploy](https://github.com/MIGG-NTU/MIG_Docs/actions/workflows/deploy.yml/badge.svg)](https://github.com/MIGG-NTU/MIG_Docs/actions/workflows/deploy.yml)

This site is the [MIG Documentation](https://migg-ntu.github.io/MIG_Docs/) that contains most information and resources in Prof. Ping Tong's group.

## Build the documentation

The documentation is built by [Sphinx](http://www.sphinx-doc.org/).
We can follow the steps below to build the documenation on our own computers.

1.  Download the source codes

    ::

        # Go to ~/Downloads/ (Assume that the codes are downloaded this directory)
        $ cd ~/Downloads/

        # Clone the source codes
        $ git clone --depth=50 https://github.com/MIGG-NTU/MIG_Docs.git

2.  Install Sphinx

    ::

        # We can use pip (Python's own tool) to install Sphinx
        $ pip install sphinx

3.  Install requirements

    ::

        # Enter the downloaded source code directory
        $ cd ~/Downloads/seismology101/

        # Install requirements
        $ pip install -r requirements.txt

4.  Compile and generate documentation in HTML format

    ::

        $ make html

5.  The generated documentation is located in the :file:`build/html/` directory
    and can be previewed locally by directly opening :file:`build/html/index.html`
    with a browser.
