from openalea.core import *

# This file has been generated at Tue Feb 02 11:32:17 2016


__name__ = 'openalea.infraphenogrid.algorithm.binarization'

__editable__ = True
__description__ = ''
__license__ = 'CeCILL-C'
__url__ = 'http://openalea.gforge.inria.fr'
__alias__ = []
__version__ = '0.0.6'
__authors__ = 'C. Fournier'
__institutes__ = None
__icon__ = ''
__all__ = []

infraphenogrid_side_binarization_hsv = Factory(
    name='side_binarization_hsv',
    authors='Michael',
    description='',
    category='Binarization',
    nodemodule='openalea.infraphenogrid.binarization',
    nodeclass='side_binarization_hsv',
    inputs=[{'interface': None, 'name': 'image'},
            {'interface': None, 'name': 'configuration'}],
    outputs=[{'interface': None, 'name': 'Binary image'}],
    widgetmodule=None,
    widgetclass=None)

__all__.append('infraphenogrid_side_binarization_hsv')

Infraphenogrid_side_binarization = Factory(
    name='side_binarization',
    authors='(C.Fournier)',
    description='',
    category='Binarization',
    nodemodule='openalea.infraphenogrid.binarization',
    nodeclass='side_binarization',
    inputs=[{'interface': None, 'name': 'image'},
            {'interface': None, 'name': 'mean_image'},
            {'interface': None, 'name': 'configuration'}],
    outputs=[{'interface': None, 'name': 'Binary image'}],
    widgetmodule=None,
    widgetclass=None,
)

__all__.append('Infraphenogrid_side_binarization')

Infraphenogrid_side_binarization_adaptive_thresh = Factory(
    name='side_binarization_adaptive_thresh',
    authors='Simon',
    description='',
    category='Binarization',
    nodemodule='openalea.infraphenogrid.binarization',
    nodeclass='side_binarization_adaptive_thresh',
    inputs=[{'interface': None, 'name': 'image'},
            {'interface': None, 'name': 'configuration'}],
    outputs=[{'interface': None, 'name': 'Binary image'}],
    widgetmodule=None,
    widgetclass=None,
)

__all__.append('Infraphenogrid_side_binarization_adaptive_thresh')
