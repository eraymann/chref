# -*- coding: utf-8 -*-

# MIT License
#
# Copyright (c) 2020 Elias Raymann
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


# TODO: fix paths and mention of the source
# WGS84 <-> LV03 converter based on the scripts of swisstopo written for python2.7
# Aaron Schmocker [aaron@duckpond.ch]

# Source: http://www.swisstopo.admin.ch/internet/swisstopo/en/home/topics/survey/sys/refsys/projections.html (see PDFs under "Documentation")
# Updated 9 dec 2014
# Please validate your results with NAVREF on-line service: http://www.swisstopo.admin.ch/internet/swisstopo/en/home/apps/calc/navref.html (difference ~ 1-2m)

import math


def lv03_to_wgs84(east, north, height=None):
    """
    Convert LV03 to WGS84.

    :param float height: altitude
    :param float east:
    :param float north:
    :rtype: float
    """
    # Axiliary values (Bern)
    e_aux = (east - 600000) / 1000000
    n_aux = (north - 200000) / 1000000

    lat = 16.9023892 + 3.238272 * n_aux - 0.270978 * pow(e_aux, 2) - 0.002528 * pow(n_aux, 2) - 0.0447 * n_aux * pow(e_aux, 2) - 0.0140 * pow(n_aux, 3)
    lon = 2.6779094 + 4.728982 * e_aux + 0.791484 * e_aux * n_aux + 0.1306 * e_aux * pow(n_aux, 2) - 0.0436 * pow(e_aux, 3)
    alt = height + 49.55 - 12.60 * e_aux - 22.64 * n_aux if height else None

    # convert seconds to degrees (dec)
    return lat / 0.36, lon / 0.36, alt


def _dec_to_sex_angle(dec_deg):
    """
    Convert decimal angle (° dec) to sexagesimal angle (dd.mmss,ss).

    :param dec_deg:
    :return:
    """
    degree = int(dec_deg)
    minute = int((dec_deg - degree) * 60)
    second = (((dec_deg - degree) * 60) - minute) * 60
    return degree + (minute / 100.0 * 60) + (second / 10000.0 * 3600)


def _sex_angle_to_seconds(dms):
    """
    Convert sexagesimal angle (dd.mmss,ss) to seconds.

    :param dms:
    :return:
    """
    degree = math.floor(dms)
    minute = math.floor((dms - degree) * 100)
    second = (((dms - degree) * 100) - minute) * 100
    result = second + (minute * 60) + (degree * 3600)
    return second + (minute * 60) + (degree * 3600)


def wgs84_to_lv03(latitude, longitude, altitude=None):
    """
    Convert WGS84 to LV03 Return an array of double that contaign east,
    north, and height

    :param float latitude: latitude
    :param float longitude: longitude
    :param float altitude: altitude
    :return:
    """
    lat = _dec_to_sex_angle(dec_deg=latitude)
    lng = _dec_to_sex_angle(dec_deg=longitude)
    lat = _sex_angle_to_seconds(dms=lat)
    lng = _sex_angle_to_seconds(dms=lng)
    #
    # print((divmod(latitude, int(latitude))[1] / 10) * 6)

    # Axiliary values (% Bern)
    lat_aux = (latitude * 3600 - 169028.66) / 10000
    lon_aux = (longitude * 3600 - 26782.5) / 10000

    east = 600072.37 + 211455.93 * lon_aux - 10938.51 * lon_aux * lat_aux - 0.36 * lon_aux * pow(lat_aux, 2) - 44.54 * pow(lon_aux, 3)
    north = 200147.07 + 308807.95 * lat_aux + 3745.25 * pow(lon_aux, 2) + 76.63 * pow(lat_aux, 2) - 194.56 * pow(lon_aux, 2) * lat_aux + 119.79 * pow(lat_aux, 3)
    height = altitude - 49.55 + 2.73 * lon_aux + 6.94 * lat_aux if altitude else None

    return east, north, height


print(lv03_to_wgs84(east=751257.13, north=252777.7))
print(wgs84_to_lv03(47.40843067781613, 9.442845024413383))
