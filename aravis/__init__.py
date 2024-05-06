import os

os.add_dll_directory(os.path.join(os.path.dirname(__file__), 'bin'))
gi_typelib = os.path.join(os.path.dirname(__file__), 'lib/girepository-1.0')
os.environ['GI_TYPELIB_PATH'] = gi_typelib
import gi
gi.require_version("Aravis", "0.8")
from gi.repository import Aravis


