# -*- python -*-
#
#       Copyright 2015 INRIA - CIRAD - INRA
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
#
#       OpenAlea WebSite : http://openalea.gforge.inria.fr
#
# ==============================================================================

__revision__ = ""

import cv2


from openalea.deploy.shared_data import shared_data
import alinea.phenomenal
# ==============================================================================


def side_blob_test_1():
    shared_directory = shared_data(alinea.phenomenal)
    return cv2.imread(shared_directory + '/images/' + 'side_blob_test_1.png')


def top_blob_test():
    shared_directory = shared_data(alinea.phenomenal)
    return cv2.imread(shared_directory + '/images/' + 'top_blob_test.png')

