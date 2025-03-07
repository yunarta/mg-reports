# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from generate import render_templates
from facts import context

project = 'Reports'
copyright = '2025, Yunarta Kartawahyudi'
author = 'Yunarta Kartawahyudi'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

extensions = [
    'sphinx_rtd_theme',
    'sphinxcontrib.confluencebuilder',
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

render_templates(context)

# -- Confluence configuration ------------------------------------------------
confluence_publish = True
confluence_space_key = os.getenv('CONFLUENCE_SPACE_KEY')
confluence_server_url = os.getenv('CONFLUENCE_URL')
confluence_server_user = os.getenv('CONFLUENCE_USERNAME')
confluence_server_pass = os.getenv('CONFLUENCE_API_TOKEN')

# Optional: Set a parent page for the documentation
confluence_root_homepage = True
confluence_editor = 'v2'
confluence_page_generation_notice = True

