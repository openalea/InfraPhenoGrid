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
"""
Post processing algorithms to improve binarization of a image
"""
# ==============================================================================
import cv2
import numpy

import openalea.opencv.extension as ocv2
# ==============================================================================


def clean_noise(binary_image, mask=None):
    """
    Goal: Cleaning orange band noise with mask

    Applied mask on image then erode and dilate on 3 iteration.
    Applied subtract image and mask and add to image modify before
    And finally, erode and dilate again

    Parameters
    ----------
    binary_image : numpy.ndarray
        2-D array

    mask : numpy.ndarray, optional
        Array of same shape as `image`. Only points at which mask == True
        will be processed.

    Returns
    -------
    out : numpy.ndarray
        Binary Image
    """
    # ==========================================================================
    # Check Parameters
    if not isinstance(binary_image, numpy.ndarray):
        raise TypeError('binary_image must be a numpy.ndarray')

    if binary_image.ndim != 2:
        raise ValueError('binary_image must be 2D array')

    if mask is not None:
        if not isinstance(mask, numpy.ndarray):
            raise TypeError('mask must be a numpy.ndarray')
        if mask.ndim != 2:
            raise ValueError('mask must be 2D array')
    # ==========================================================================
    if mask is not None:
        out = cv2.bitwise_and(binary_image, mask)
    else:
        out = binary_image.copy()

    element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    out = cv2.erode(out, element, iterations=3)
    out = cv2.dilate(out, element, iterations=3)

    if mask is not None:
        res = cv2.subtract(binary_image, mask)
        out = cv2.add(res, out)

    out = ocv2.erode(out)
    out = ocv2.dilate(out)

    return out
