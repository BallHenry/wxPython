# Name:         wxlib.py
# Purpose:      Component plugins for wx.lib classes
# Author:       Roman Rolinsky <rolinsky@femagsoft.com>
# Created:      05.09.2007
# RCS-ID:       $Id$

from xh_wxlib import *
from component import *

TRACE('*** creating wx.lib components')

# FoldPanelBar

### wxWizard

c = SmartContainer('FoldPanelBar', ['book', 'window'], ['pos', 'size'],
                   implicit_klass='foldpanel', 
                   implicit_page='FoldPanel', 
                   implicit_attributes=['label'])
c.addStyles('FPB_DEFAULT_STYLE', 'FPB_SINGLE_FOLD', 'FPB_COLLAPSE_TO_BOTTOM',
            'FPB_EXCLUSIVE_FOLD', 'FPB_HORIZONTAL', 'FPB_VERTICAL')
Manager.register(c)
Manager.addXmlHandler(FoldPanelBarXmlHandler)
Manager.setMenu(c, 'bar', 'fold panel bar', 'FoldPanelBar')
