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
import numpy
import cv2

import openalea.opencv.extension as ocv2

from openalea.infraphenogrid.binarization_algorithm import (
    mean_shift_binarization,
    hsv_binarization)

from openalea.infraphenogrid.binarization_processing import (
    clean_noise)
# ==============================================================================


def side_binarization_hsv(image, configuration):
    """
    Binarization of side image for Lemnatech  cabin based on hsv segmentation.

    Based on Michael pipeline
    :param image: BGR image
    :param configuration: Object BinarizationConfig
    :return: Binary image
    """

    # elementMorph = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))

    c = configuration.cubicle_domain
    image_cropped = image[c[0]:c[1], c[2]:c[3]]
    hsv_image = ocv2.bgr2hsv(image_cropped)

    # ==========================================================================
    # Main area segmentation
    main_area_seg = cv2.medianBlur(hsv_image, ksize=9)
    main_area_seg = cv2.inRange(main_area_seg,
                                configuration.roi_main.hsv_min,
                                configuration.roi_main.hsv_max)

    main_area_seg = ocv2.dilate(main_area_seg, iterations=2)
    main_area_seg = ocv2.erode(main_area_seg, iterations=2)

    mask_cropped = configuration.roi_main.mask[c[0]:c[1], c[2]:c[3]]
    main_area_seg = cv2.bitwise_and(main_area_seg,
                                    main_area_seg,
                                    mask=mask_cropped)

    # ==========================================================================
    # Band area segmentation
    background_cropped = configuration.background[c[0]:c[1], c[2]:c[3]]
    hsv_background = ocv2.bgr2hsv(background_cropped)
    grayscale_background = hsv_background[:, :, 0]

    grayscale_image = hsv_image[:, :, 0]

    band_area_seg = cv2.subtract(grayscale_image, grayscale_background)
    retval, band_area_seg = cv2.threshold(band_area_seg,
                                          122,
                                          255,
                                          cv2.THRESH_BINARY)

    mask_cropped = configuration.roi_orange_band.mask[c[0]:c[1], c[2]:c[3]]
    band_area_seg = cv2.bitwise_and(band_area_seg,
                                    band_area_seg,
                                    mask=mask_cropped)

    band_area_seg = ocv2.erode(band_area_seg, iterations=5)
    band_area_seg = ocv2.dilate(band_area_seg, iterations=5)

    # ==========================================================================
    # Pot area segmentation
    pot_area_seg = cv2.inRange(hsv_image,
                               configuration.roi_pot.hsv_min,
                               configuration.roi_pot.hsv_max)

    mask_cropped = configuration.roi_pot.mask[c[0]:c[1], c[2]:c[3]]
    pot_area_seg = cv2.bitwise_and(pot_area_seg,
                                   pot_area_seg,
                                   mask=mask_cropped)

    # ==========================================================================
    # Full segmented image
    image_seg = cv2.add(main_area_seg, band_area_seg)
    image_seg = cv2.add(image_seg, pot_area_seg)

    image_out = numpy.zeros([image.shape[0], image.shape[1]], 'uint8')
    image_out[c[0]:c[1], c[2]:c[3]] = image_seg

    return image_out


def side_binarization(image, mean_image, configuration):
    """
    Binarization of side image based on mean shift difference

    :param image: BGR image
    :param mean_image: Mean image
    :param configuration: Object BinarizeConfiguration
    :return: Binary image
    """
    roi_main = configuration.roi_main

    mask = cv2.add(roi_main.mask,
                   configuration.roi_orange_band.mask)

    mask = cv2.add(mask,
                   configuration.roi_panel.mask)

    binary_hsv_image = hsv_binarization(image,
                                        configuration.roi_main.hsv_min,
                                        configuration.roi_main.hsv_max,
                                        configuration.roi_main.mask)

    binary_meanshift_image = mean_shift_binarization(
        image,
        mean_image,
        configuration.meanshift_binarization_factor.threshold,
        configuration.meanshift_binarization_factor.dark_background,
        mask)

    result = cv2.add(binary_hsv_image, binary_meanshift_image * 255)

    mask_clean_noise = cv2.add(configuration.roi_orange_band.mask,
                               configuration.roi_panel.mask)

    result = clean_noise(result, mask_clean_noise)

    return result


def side_binarization_adaptive_thresh(image, configuration):
    """
    Binarization of side image based on adaptive threshold algorithm of cv2
    """
    # ==========================================================================
    # Check Parameters
    if not isinstance(image, numpy.ndarray):
        raise TypeError('image should be a numpy.ndarray')
    if image.ndim != 3:
        raise ValueError('image should be 3D array')

    mask = configuration.roi_main.mask
    if mask is not None:
        if not isinstance(mask, numpy.ndarray):
            raise TypeError('mask should be a numpy.ndarray')
        if mask.ndim != 2:
            raise ValueError('image should be 2D array')

        if image.shape[0:2] != mask.shape:
            raise ValueError('image and mask should have the same shape')
    # ==========================================================================

    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    if mask is not None:
        img = cv2.bitwise_and(img, img, mask=mask)

    block_size, c = (41, 20)
    result1 = cv2.adaptiveThreshold(img,
                                    255,
                                    cv2.ADAPTIVE_THRESH_MEAN_C,
                                    cv2.THRESH_BINARY_INV,
                                    block_size,
                                    c)

    block_size, c = (399, 45)
    result2 = cv2.adaptiveThreshold(img,
                                    255,
                                    cv2.ADAPTIVE_THRESH_MEAN_C,
                                    cv2.THRESH_BINARY_INV,
                                    block_size,
                                    c)

    block_size, c = (41, 20)
    result3 = cv2.adaptiveThreshold(img,
                                    255,
                                    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                    cv2.THRESH_BINARY_INV,
                                    block_size,
                                    c)

    result = cv2.add(result1, result2)
    result = cv2.add(result, result3)

    if mask is not None:
        result = cv2.bitwise_and(result, result, mask=mask)

    return result

