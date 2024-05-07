import os
import ctypes

pre_built_path = os.path.join(os.path.dirname(__file__), 'bin')

os.add_dll_directory(pre_built_path)

aravis_module = os.path.join(pre_built_path, 'aravis-0.8-0.dll')
ctypes.cdll.LoadLibrary(aravis_module)

gi_typelib = os.path.join(os.path.dirname(__file__), 'lib')
os.environ['GI_TYPELIB_PATH'] = gi_typelib
import gi
gi.require_version("Aravis", "0.8")
from gi.repository import Aravis
