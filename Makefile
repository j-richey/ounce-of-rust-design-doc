# Makefile for building the documentation.
# This is a modified version of the Sphinx generated file. 

SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build
PDFNAME		  = "ounce_of_rust_project_design_document.pdf"

.PHONY: all html singlehtml latexpdf clean help

# All simply builds all the various outputs then ensures a copy of the PDF and
# single page HTML is in the HTML output directory so these other varients can 
# be downloaded. 
# sed is used to fix the internal links and copy the single page HTML so
# they point to the correct location.
all: html singlehtml pdf
	@sed -r 's/href="index.html/href="singlepage.html/g' "$(BUILDDIR)/singlehtml/index.html" > "$(BUILDDIR)/html/singlepage.html"
	@cp -v "$(BUILDDIR)/latex/$(PDFNAME)" "$(BUILDDIR)/html/"


html:
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)"


# The single HTML page is copied into the HTML directory and renamed so it can
# use the same resources. Not how the internal links are fixed up.
singlehtml:
	@$(SPHINXBUILD) -M singlehtml "$(SOURCEDIR)" "$(BUILDDIR)"


# TODO: reduce the amount of output from this command.
pdf:
	@$(SPHINXBUILD) -M latexpdf "$(SOURCEDIR)" "$(BUILDDIR)"


clean:
	@$(SPHINXBUILD) -M clean "$(SOURCEDIR)" "$(BUILDDIR)"


help:
	@echo "Makefile for building the documentation."
	@echo ""
	@echo "Available commands:"
	@echo "  all         Builds all the different output types. (default)"
	@echo "  html        Builds standalone HTML files for the documentation."
	@echo "  singlehtml  Builds a single HTML file of the documentation."
	@echo "  pdf         Builds a PDF of the documentation."
	@echo "  clean       Cleans the output directory."
	@echo "  help        Shows this help message."
	@echo ""
	@echo "For details on how to build the documentation see the README."

