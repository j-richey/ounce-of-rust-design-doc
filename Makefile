# Makefile for building the documentation.
# This is a modified version of the Sphinx generated file. 

SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build
PDFNAME		  = "ounce_of_rust_project_design_document.pdf"

.PHONY: all html singlehtml latexpdf clean help

# All simply builds all the various outputs.
all: html singlehtml pdf


.PHONY: html
html:
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)"


# The single HTML page is copied into the HTML directory and renamed so it can
# use the same resources. Not how the internal links are fixed up.
singlehtml: html
	@$(SPHINXBUILD) -M singlehtml "$(SOURCEDIR)" "$(BUILDDIR)"
	sed -r 's/href="index.html/href="singlepage.html/g' "$(BUILDDIR)/singlehtml/index.html" > "$(BUILDDIR)/html/singlepage.html"


# The PDF is copied to the HTML directory so it can be downloaded from the main
# HTML pages.
# TODO: reduce the amount of output from this command.
pdf: html
	@$(SPHINXBUILD) -M latexpdf "$(SOURCEDIR)" "$(BUILDDIR)"
	@cp -v "$(BUILDDIR)/latex/$(PDFNAME)" "$(BUILDDIR)/html/"


clean:
	@$(SPHINXBUILD) -M clean "$(SOURCEDIR)" "$(BUILDDIR)"


help:
	@echo "Makefile for building the documentation."
	@echo ""
	@echo "Available commands:"
	@echo "  all         Builds all the different output types. (default)"
	@echo "  html        Builds standalone HTML files for the documentation."
	@echo "  singlehtml  Builds a single HTML file of the documentation."
	@echo "  latexpdf    Builds a PDF of the documentation."
	@echo "  clean       Cleans the output directory."
	@echo "  help        Shows this help message."

