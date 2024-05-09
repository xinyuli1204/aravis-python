import os
import ctypes
import platform
pre_built_path = os.path.dirname(__file__)
if platform.system() == 'Windows':
    aravis_module = os.path.join(pre_built_path, "bin/aravis-0.8-0.dll")
elif platform.system() == 'Darwin':
    pass
    # aravis_module = os.path.join(pre_built_path, 'libaravis-0.8.so')
elif platform.system() == 'Linux':
    aravis_module = os.path.join(pre_built_path, "lib/libaravis-0.8.so")

ctypes.cdll.LoadLibrary(aravis_module)

gi_typelib = os.path.join(os.path.dirname(__file__), 'lib')
os.environ['GI_TYPELIB_PATH'] = gi_typelib
import gi
gi.require_version("Aravis", "0.8")
from gi.repository import Aravis
