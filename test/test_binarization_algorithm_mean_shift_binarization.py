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

from openalea.infraphenogrid.binarization_algorithm import (
    mean_shift_binarization,
    get_mean_image)
# ==============================================================================


def test_wrong_parameters_1():
    mean_image = numpy.zeros((25, 25, 3), dtype=numpy.uint8)
    try:
        mean_shift_binarization(None, mean_image)
    except Exception, e:
        assert e.message == 'image should be a numpy.ndarray'
        assert type(e) == TypeError
    else:
        assert False


def test_wrong_parameters_2():
    image = numpy.zeros((25, 25, 3), dtype=numpy.uint8)
    try:
        mean_shift_binarization(image, None)
    except Exception, e:
        assert e.message == 'mean should be a numpy.ndarray'
        assert type(e) == TypeError
    else:
        assert False


def test_wrong_parameters_3():

    image = numpy.zeros((25, 25), dtype=numpy.uint8)
    mean_image = numpy.zeros((25, 25, 3), dtype=numpy.uint8)

    try:
        mean_shift_binarization(image, mean_image)
    except Exception, e:
        assert e.message == 'image should be 3D array'
        assert type(e) == ValueError
    else:
        assert False


def test_wrong_parameters_4():

    image = numpy.zeros((25, 25), dtype=numpy.uint8)
    mean_image = numpy.zeros((25, 25, 3), dtype=numpy.uint8)

    try:
        mean_shift_binarization(image, mean_image)
    except Exception, e:
        assert e.message == 'image should be 3D array'
        assert type(e) == ValueError
    else:
        assert False


def test_wrong_parameters_5():

    image = numpy.zeros((25, 25, 3), dtype=numpy.uint8)
    mean_image = numpy.zeros((25, 25), dtype=numpy.uint8)

    try:
        mean_shift_binarization(image, mean_image)
    except Exception, e:
        assert e.message == 'mean should be 3D array'
        assert type(e) == ValueError
    else:
        assert False


def test_wrong_parameters_6():
    image = numpy.zeros((25, 25, 3), dtype=numpy.uint8)
    mean_image = numpy.zeros((10, 10, 3), dtype=numpy.uint8)

    try:
        mean_shift_binarization(image, mean_image)
    except Exception, e:
        assert e.message == 'image and mean must have equal sizes'
        assert type(e) == ValueError
    else:
        assert False


def test_simply_working_1():
    images = list()
    img_1 = numpy.ones((25, 25, 3), numpy.uint8)
    images.append(img_1)
    images.append(numpy.zeros((25, 25, 3), numpy.uint8))
    mean_image = get_mean_image(images)

    image = mean_shift_binarization(img_1, mean_image)
    assert numpy.count_nonzero(image) == 0
    assert mean_image.shape == (25, 25, 3)
    assert mean_image.ndim == 3
    assert numpy.count_nonzero(mean_image) == 0



# ==============================================================================

if __name__ == "__main__":
    test_wrong_parameters_1()
    test_wrong_parameters_2()
    test_wrong_parameters_3()
    test_wrong_parameters_4()
    test_wrong_parameters_5()
    test_wrong_parameters_6()

    test_simply_working_1()


