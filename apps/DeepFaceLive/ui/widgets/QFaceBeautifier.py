from localization import L
from resources.fonts import QXFontDB
from xlib import qt as lib_qt
from xlib.mp.csw import Number, Bool, TimeNumber

from .QBackendPanel import QBackendPanel
from .QComboBoxCSWDynamicSingleSwitch import QComboBoxCSWDynamicSingleSwitch
from .QDoubleSpinBoxCSWNumber import QDoubleSpinBoxCSWNumber
from .QFrameCSWDynamicContent import QFrameCSWDynamicContent
from .QLabelPopupInfo import QLabelPopupInfo
from .QSliderCSWNumber import QSliderCSWNumber
from .QSpinBoxCSWNumber import QSpinBoxCSWNumber

class QFaceBeautifier(QBackendPanel):
    def __init__(self, backend):
        cs = backend.get_control_sheet()
        
        # Beauty params
        btn_beauty_group = lib_qt.QXCollapsibleSection(L('@FaceBeautifier.beauty_group'), is_opened=True)
        
        with btn_beauty_group.content_layout:
            with lib_qt.QXHBoxLayout():
                lib_qt.QXLabel(L('@FaceBeautifier.beauty_level'))
                beauty_level = QSliderCSWNumber(cs.beauty_level, reflect_state_widgets=[])
                
        # Face slim params
        btn_slim_group = lib_qt.QXCollapsibleSection(L('@FaceBeautifier.slim_group'), is_opened=True)
        
        with btn_slim_group.content_layout:
            with lib_qt.QXHBoxLayout():
                lib_qt.QXLabel(L('@FaceBeautifier.face_slim'))
                face_slim = QSliderCSWNumber(cs.face_slim_level, reflect_state_widgets=[])
            
            with lib_qt.QXHBoxLayout():
                lib_qt.QXLabel(L('@FaceBeautifier.chin_slim'))
                chin_slim = QSliderCSWNumber(cs.chin_slim_level, reflect_state_widgets=[])

        # Combine all widgets
        super().__init__(backend, 
                        L('@FaceBeautifier.module_title'),
                        layout=lib_qt.QXVBoxLayout([btn_beauty_group, 
                                                  btn_slim_group]))