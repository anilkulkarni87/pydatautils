"""Sphinx configuration."""
project = "PyDataAssist"
author = "Anil Kulkarni"
copyright = "2023, Anil Kulkarni"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.imgconverter",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
