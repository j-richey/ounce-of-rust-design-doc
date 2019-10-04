# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------

project = 'Ounce of Rust Project Design Document'
copyright = '2019, James Richey'
author = 'James Richey'

# The full version, including alpha/beta/rc tags
release = 'A draft 1'


# -- General configuration ---------------------------------------------------

master_doc = 'index'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinxcontrib.plantuml',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

nitpicky = True

numfig = True


# -- Options for HTML output -------------------------------------------------

html_title = project + " Rev. " + release

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# For alabaster optoins see https://alabaster.readthedocs.io/en/latest/customization.html


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Options for LaTeX output -------------------------------------------------

latex_documents = [(
    master_doc,                         # startdocname
    # targetname, e.g. the name of the PDF file.
    project.lower().replace(' ', '_') + '.tex',
    project,                            # title
    author,                             # author
    'manual',                           # documentclass
    True)]                              # toctree_only

latex_show_urls = 'footnote'

latex_elements = {
    'releasename': 'Rev.',
}


# -- Options for Plant UML -------------------------------------------------

plantuml_output_format = 'svg_img'
plantuml_latex_output_format = 'pdf'

# Ensure problematic diagrams are indicated.
plantuml_syntax_error_image = True
