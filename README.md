# Ounce of Rust Project Design Document
This repository contains the design document for the Ounce of Rust project. This
document describes the objectives of the Ounce of Rust project is details how
the objectives are achieved.


## Building
This documentation is rendered using [Sphinx](https://www.sphinx-doc.org/en/master/).
The following applications are required to build this documentation:

* Python 3.5 or newer
* inkscape
* plantuml
* A LaTeX toolchain
* Sphinx

On Ununtu / Debian system the required packages can be installed and 
documentation built with: 

```
$ sudo apt install texlive-full inkscape plantuml
$ python3 -m venv ounce-of-rust-docs-venv
$ source ounce-of-rust-docs-venv/bin/activate
$ pip install -r requirements.txt
$ make
``` 

The output will be in the `build` directory, specifically, the `build/html`
directory contains the complete documentation including the PDF and single page
versions and is suitable for copying to a web server for hosting the document.


## Editing
The document is written in reStructuredText. The following characters are used
for headings:

* `#` with  overline for the page title
* `=` with overline for page sections
* `-` with overline for subsections
* Single `=` then `-` if additional levels are needed.

For details on reStructuredText as understood by Sphinx see
[Sphinx's reStructuredText Primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html).

When editing specific versions of the documentation can be built with `make html`
or `make pdf` allowing one to quickly look at modifications.  See `make help` 
for a complete list of output types.
