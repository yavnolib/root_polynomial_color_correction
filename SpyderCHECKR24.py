# This defines the SpyderCHECKR 24 color calibration chart colors
# as defined https://www.datacolor.com/wp-content/uploads/2018/01/SpyderCheckr_Color_Data_V2.pdf
import colour
import numpy
from collections import OrderedDict

checker_swatches_sRGB = numpy.array([
    [43, 41, 43],
    [80, 80, 78],
    [122, 118, 116],
    [161, 157, 154],
    [202, 198, 195],
    [249, 242, 238],
    [25, 55, 135],
    [57, 146, 64],
    [186, 26, 51],
    [245, 250, 0],
    [192, 75, 145],
    [0, 127, 159],
    [238, 158, 25],
    [157, 188, 54],
    [83, 58, 106],
    [195, 79, 95],
    [58, 88, 159],
    [222, 118, 32],
    [112, 76, 60],
    [197, 145, 125],
    [87, 120, 155],
    [82, 106, 60],
    [126, 125, 174],
    [98, 187, 166]
])/255

names = [
    'card black',
    '80% gray',
    '60% gray',
    '40% gray',
    '20% gray',
    'card white',
    'primary blue',
    'primary green',
    'primary red',
    'primary yellow',
    'primary magenta',
    'primary cyan',
    'sunflower',
    'apple green',
    'violet', 'pink',
    'blueprint',
    'primary orange',
    'classic dark skin',
    'classic light skin',
    'steel blue',
    'evergreen',
    'lavender',
    'aqua'
]

data = OrderedDict(zip(names, colour.XYZ_to_xyY(
    colour.sRGB_to_XYZ(checker_swatches_sRGB))))

D65 = colour.CCS_ILLUMINANTS['CIE 1931 2 Degree Standard Observer']['D65']
colour_checker = colour.characterisation.ColourChecker(
    'SpyderCHECKR 24', data, D65)
