#!/usr/bin/env python3

# -- Path configuration ------------------------------------------------

import os
import sys
from trojanzoo_sphinx_theme.linkcode import linkcode_helper

sys.path.insert(0, os.path.abspath('./'))
sys.path.insert(0, os.path.abspath('../../'))

import alpsplot as package  # noqa

# -- General configuration ------------------------------------------------

project = 'AlpsPlot'
author = 'ain-soph'
copyright = f'2021, {author}'

github_user = author
github_repo = package.__name__
github_version = 'main'

github_url = f'https://github.com/{github_user}/{github_repo}/'
gh_page_url = f'https://{github_user}.github.io/{github_repo}/'

html_baseurl = gh_page_url
html_context = {
    'display_github': True,
    'github_user': github_user,
    'github_repo': github_repo,
    'github_version': github_version,
    "conf_py_path": "/docs/source/",  # Path in the checkout to the docs root
}
html_theme_options = {
    'github_url': github_url,

    'doc_items': {
        'AlpsPlot': '/alpsplot',
        'TrojanZoo': '/trojanzoo',
        'trojanzoo_sphinx_theme': '/trojanzoo_sphinx_theme',
        'base': 'https://github.com/ain-soph/base',
    },

    'logo': 'images/logo/trojanzoo-logo.svg',
    'logo_dark': 'images/logo/trojanzoo-logo-dark.svg',
    'logo_icon': 'images/logo/trojanzoo-logo-icon.svg',
}

# -- Extension configuration ----------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.githubpages',
    'sphinx.ext.intersphinx',
    'sphinx.ext.linkcode',  # viewcode
    'sphinx.ext.napoleon',
    'sphinxcontrib.katex',
]


def linkcode_resolve(domain, info):
    return linkcode_helper(
        domain, info,
        package=package,
        github_url=github_url,
        github_version=github_version)


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'matplotlib': ('https://matplotlib.org/stable', None),
    'numpy': ('https://numpy.org/doc/stable', None),
    'scipy': ('https://docs.scipy.org/doc/scipy/reference', None),
}

# -- General default configuration ----------------------------------------

needs_sphinx = '4.0.2'
templates_path = ['_templates']
source_suffix = '.rst'  # ['.rst', '.md']
root_doc = 'index'

release = str(package.__version__)
version = release if release.find('a') == -1 else release[:release.find('a')]

language = None
exclude_patterns = []

# -- General default extension configuration ------------------------------

# autodoc options
autodoc_docstring_signature = True
autodoc_inherit_docstrings = False
autodoc_typehints = 'none'

# autosectionlabel options
# autosectionlabel throws warnings if section names are duplicated.
# The following tells autosectionlabel to not throw a warning for
# duplicated section names that are in different documents.
autosectionlabel_prefix_document = True

# katex options
katex_prerender = True

# napoleon options
napoleon_use_ivar = True
napoleon_use_rtype = False

# todo options
# If true, `todo` and `todoList` produce output, else they produce nothing.
# todo_include_todos = True

# -- Options for HTML output ----------------------------------------------

html_theme = 'trojanzoo_sphinx_theme'
html_permalinks_icon = '\uf08e'  # '\uf0c1'  font-family = FontAwesome
html_favicon = 'images/favicon.ico'
html_title = " ".join((project, version, "documentation"))

# -- Options for HTMLHelp output ------------------------------------------
htmlhelp_basename = f'{project}doc'

# -- Options for LaTeX output ---------------------------------------------
latex_elements = {}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (root_doc, f'{package.__name__}.tex', f'{project} Documentation',
     author, 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (root_doc, project, f'{project} Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (root_doc, project, f'{project} Documentation',
     author, project, 'One line description of project.',
     'Miscellaneous'),
]
