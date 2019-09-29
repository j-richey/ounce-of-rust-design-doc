# Ounce of Rust Project Design Document
This repository contains the design document for the Ounce of Rust project. This
document describes the objectives of the Ounce of Rust project is details how
the objectives are achieved.


## Building
The documentation is rendered using [Sphinx](https://www.sphinx-doc.org/en/master/).
To install Sphinx create a Python virtual environment then use `pip` to install
the required packages.

```
$ python3 -m venv ounce-of-rust-docs
$ source ounce-of-rust-docs/bin/activate
$ pip install -r requirements.txt
```

Once Sphinx is installed, use `make` to build the documentation. 
```
$ make html
```

The output will be in the `build` directory.


## Editing
The document is written in reStructuredText. The following characters are used
for headings:

* `#` with  overline for the page title
* `=` with overline for page sections
* `-` with overline for subsections
* Single `=` then `-` if additional levels are needed.

For details on reStructuredText as understood by Sphinx see
[Sphinx's reStructuredText Primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html).
