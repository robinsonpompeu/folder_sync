import os
import sys
from pathlib import Path
sys.path.insert(0, str(Path('../..', 'src/folder_sync').resolve()))

project = "Folder Sync"
author = "Robinson Pompeu"

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosummary',
    'myst_parser'
]

source_suffix = ['.rst', '.md']

html_theme = 'sphinx_rtd_theme'

autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'special-members': '__init__',
    'undoc-members': True,
    'exclude-members': '__weakref__'
}