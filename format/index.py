from js import document
import sys
from unittest.mock import MagicMock
sys.modules['_multiprocessing'] = MagicMock()
import black
def blacken(evt=None):
    src_el = document.getElementById("source")
    src_el.value = black.format_str(src_el.value, mode=black.Mode())

document.getElementById("go").onclick = blacken