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

# Base name (with out the extension) of the PDF file.
_pdf_base_name = "{project} Rev {release}".format(
    project=project, release=release).lower().replace(' ', '_')

# Create a reStructuredText macro for downloading the PDF that includes the
# correct filename based on revision.
rst_epilog = '.. |pdf_download| replace:: `Download PDF <{}.pdf>`__'.format(_pdf_base_name)

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

# Number figures, tables, and code listings.
numfig = True
numfig_format = {
    'figure': "Figure %s",
    'table': "Table %s",
    'code-block': "Listing %s",
    'section': "Section",
}


# -- Options for HTML output -------------------------------------------------

html_title = project + " Rev. " + release

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# For alabaster optoins see https://alabaster.readthedocs.io/en/latest/customization.html
html_theme_options = {
    'sidebar_collapse': True,
    'code_font_size': "0.8em",
    'extra_nav_links': {
        "Download PDF": _pdf_base_name + ".pdf",
        "View Single Page": "singlepage.html",
        "GitHub Source": "https://github.com/j-richey/ounce-of-rust-design-doc",
    },
}


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Options for LaTeX output -------------------------------------------------

latex_documents = [(
    master_doc,                         # startdocname
    # targetname, e.g. the name of the PDF file.
    _pdf_base_name + '.tex',
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
