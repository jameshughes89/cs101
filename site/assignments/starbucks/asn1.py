# NAME:
# ST-NUMBER:
# StFX EMAIL:

STARBUCKS_FILE_NAME = "starbucks2018.csv"

# Average radius of the earth in km
EARTH_RADIUS = 6371


def load_starbucks_data(file_name: str) -> list:
    """
    Load a comma separated value (csv) file containing latitude and longitudes for Starbucks locations. This function
    reads the file one line ("row") at a time and puts the corresponding latitude and longitudes pair into a tuple
    that is then put into a list. This is done for each line in the file. The resulting list contains the lat/lon pairs
    for all Starbucks locations in the file.

    An example tuple for some arbitrary starbucks location is as follows:

        (starbucks_x_latitude, starbucks_x_longitude)

        Where `x` is some arbitrary line/row number.

    A visualization of the list containing the data as tuples is as follows:

        [(starbucks_1_latitude, starbucks_1_longitude),
         (starbucks_1_latitude, starbucks_1_longitude),
         (starbucks_2_latitude, starbucks_2_longitude),
         (starbucks_3_latitude, starbucks_3_longitude),
         (starbucks_4_latitude, starbucks_4_longitude),
         ...
         (starbucks_n_latitude, starbucks_n_longitude)]

        Where `n` is the number of Starbucks locations/lines in the file.

    :param file_name: Name of the file to be opened.
    :type file_name: string.
    :return: A list containing the latitude/longitude pairs of Starbucks locations.
    :rtype: list of tuples of lat/lon pairs.
    """
    import csv

    # Open the Starbucks file specified by `file_name`
    starbucks_file = open(file_name, "r")
    starbucks_file_reader = csv.reader(starbucks_file)

    # Create an empty list that the Starbucks location tuples will be added to
    starbucks_locations = []

    # For each row in the file, create a tuple of the lat/lon pair and add it to the list
    for row in starbucks_file_reader:
        location_tuple = (float(row[0]), float(row[1]))
        starbucks_locations.append(location_tuple)

    starbucks_file.close()
    return starbucks_locations


# Test load_starbucks_data
assert 25599 == len(load_starbucks_data(STARBUCKS_FILE_NAME))
assert isinstance(load_starbucks_data(STARBUCKS_FILE_NAME)[0][0], float)
assert (47.51, -92.55) == load_starbucks_data(STARBUCKS_FILE_NAME)[0]
assert (33.79, -118.33) == load_starbucks_data(STARBUCKS_FILE_NAME)[-1]


def convert_degrees_to_decimal(degrees: float, minutes: float, seconds: float) -> float:
    """
    Convert a latitude or longitude from a degrees, minutes, and seconds format to a decimal format. There are
    60 minutes/degree and 60 seconds/minute.

    :param degrees: Latitude or longitude degrees from **degrees**, minutes, seconds format.
    :type degrees: float
    :param minutes: Latitude or longitude minutes from degrees, **minutes**, seconds format.
    :type minutes: float
    :param seconds: Latitude or longitude seconds from degrees, minutes, **seconds** format.
    :type seconds: float
    :return: Latitude or longitude in decimal format.
    :rtype: float
    """


# Test convert_degrees_to_decimal
# assert 0 == convert_degrees_to_decimal(0, 0, 0)
# assert 10 == convert_degrees_to_decimal(10, 0, 0)
# assert 0.00001 > abs(convert_degrees_to_decimal(0, 10, 0) - 0.16666666666)
# assert 0.00001 > abs(convert_degrees_to_decimal(0, 0, 10) - 0.00277777777)
# assert 0.00001 > abs(convert_degrees_to_decimal(10, 10, 10) - 10.16944444444)
# assert 0.00001 > abs(convert_degrees_to_decimal(-10, -10, -10) - (-10.16944444444))


def subtended_area(
    latitude_line_1: float, latitude_line_2: float, longitude_line_1: float, longitude_line_2: float
) -> float:
    """
    Calculate the *subtended* area of the "rectangle" defined by the four latitude/longitude lines. The area defined by
    the "rectangle" is not calculated with your typical length * width calculation. This is because the "rectangle"
    in this case is not actually a rectangle since it is on the surface of a sphere. Long story short, the formula for
    calculating the *subtended* area is

        pi/180 * R^2 * |sin(lat_1) - sin(lat_2)| * |lon_1 - lon_2|,

    where R is the radius of the sphere. In this case, the sphere is the Earth, and the Earth has an average radius of
    6371km.

    **Warning:** Radians are typically a nicer unit to work with compared to degrees; humans tend to like degrees, but
    most other calculating devices/systems prefer radians. Python's angle related calculations (sin, cos, etc.) all
    expect the provided values to be in radians, not degrees. Fortunately the Python math library provides an
    easy-to-use function for a conversion to radians. Check out the Python documentation for more details. For our
    needs, simply use the function to convert a value to radians when calling sin in the above formula.

    :param latitude_line_1: One of the latitude (east-west) lines defining the "rectangle".
    :type latitude_line_1: Float
    :param latitude_line_2: One of the latitude (east-west) lines defining the "rectangle".
    :type latitude_line_2: Float
    :param longitude_line_1: One of the longitude (north-south) lines defining the "rectangle".
    :type longitude_line_1: Float
    :param longitude_line_2: One of the longitude (north-south) lines defining the "rectangle".
    :type longitude_line_2: Float
    :return: The *subtended* area defined by the four latitude/longitude lines in km^2.
    :rtype: Float (units are km^2)
    """
    import math


# Test convert_degsubtended_area
# assert 0 == subtended_area(10, 10, 10, 10)
# assert 0 == subtended_area(10, 10, -10, 10)
# assert abs(subtended_area(10, 20, 10, 20) - 1192785.52) < 0.01
# assert abs(subtended_area(-10, 20, -10, 20) - 10959337.08) < 0.01
# assert abs(subtended_area(90, -90, 180, -180) - 510064471.91) < 0.01


def number_starbucks_within_area(
    locations: list, latitude_line_1: float, latitude_line_2: float, longitude_line_1: float, longitude_line_2: float
) -> int:
    """
    Count the total number of Starbucks within the specified "rectangle" defined by the latitude and longitude lines.
    This function assumes that latitude_line_1 is less than or equal to latitude_line_2, and similarly with the
    longitude lines.

    Within this function you will find a *loop*, which is something we have yet discussed in lecture, but this should
    not be a significant issue. More details on this are provided within comments below.

                 y
      |              |
    --+--------------+--
      |  x           |
      |              |
      |              |
    --+--------------+--
      |              |

    In the above example, the two latitude lines represent the east-west lines and the two longitude lines represent
    the north-south lines. The point 'x' is within the "rectangle" defined by the latitude and longitude lines, which
    means it should get counted as one of the Starbucks locations within the specified area. The point 'y' falls outside
    the "rectangle", therefore it will not get counted.

    :param locations: List of latitude and longitude tuples representing Starbucks locations
    :type locations: List of tuples
    :param latitude_line_1: One of the latitude (east-west) lines defining the "rectangle".
    :type latitude_line_1: Float
    :param latitude_line_2: One of the latitude (east-west) lines defining the "rectangle".
    :type latitude_line_2: Float
    :param longitude_line_1: One of the longitude (north-south) lines defining the "rectangle".
    :type longitude_line_1: Float
    :param longitude_line_2: One of the longitude (north-south) lines defining the "rectangle".
    :type longitude_line_2: Float
    :return: The total number of Starbucks within the specified "rectangle"
    :rtype: int
    """

    # Add your code here --- you will want some variable to keep track of the running total of Starbucks within the
    # specified area

    # This is a *loop* --- the code within the loop (indented) will repeat multiple times. In this particular case, the
    # loop will run once for every location within the list locations.
    for starbucks in locations:
        latitude = starbucks[0]
        longitude = starbucks[1]

        # Add your code here --- you need to check if the current Starbucks location being looked at is within the
        # specified area. If it is within the specified area, it needs to be counted.

    # Return the final total number of Starbucks
    return


# Test number_starbucks_within_area
# assert 0 == number_starbucks_within_area([], 1, 10, 1, 10)
# assert 0 == number_starbucks_within_area([(1, 1), (1, 1)], 1, 1, 1, 1)
# assert 0 == number_starbucks_within_area([(1, 1), (1, 1)], 1, 2, 1, 1)
# assert 0 == number_starbucks_within_area([(1, 1), (1, 1)], 1, 1, 1, 2)
# assert 1 == number_starbucks_within_area([(1, -1), (1, 1)], 0, 10, 0, 10)
# assert 1 == number_starbucks_within_area([(-1, 1), (1, 1)], 0, 10, 0, 10)
# assert 0 == number_starbucks_within_area([(1, 1), (1, 1)], 10, 20, 10, 20)
# assert 2 == number_starbucks_within_area([(1, 1), (1, 1)], 0, 10, 0, 10)
# assert 2 == number_starbucks_within_area([(1, 1), (1, 1), (11, 11), (12, 12)], 0, 10, 0, 10)


def starbucks_per_square_kilometer(
    file_name: str, latitude_line_1: float, latitude_line_2: float, longitude_line_1: float, longitude_line_2: float
) -> float:
    """
    Calculate the Starbucks density in Starbucks/km^2. The density is calculated based on the number of Starbucks
    existing within a specified "rectangle" defined by latitude and longitude lines. This function should make use of
    the load_starbucks_data, subtended_area, and number_starbucks_within_area functions you already wrote. You will
    need to:

        - Load the locations
        - Count the number of starbucks within an area
        - Calculate the area
        - Calculate the density
        - Return the density

    :param file_name: name of the file containing the Starbucks locations
    :type file_name: String
    :param latitude_line_1: One of the latitude (east-west) lines defining the "rectangle".
    :type latitude_line_1: Float
    :param latitude_line_2: One of the latitude (east-west) lines defining the "rectangle".
    :type latitude_line_2: Float
    :param longitude_line_1: One of the longitude (north-south) lines defining the "rectangle".
    :type longitude_line_1: Float
    :param longitude_line_2: One of the longitude (north-south) lines defining the "rectangle".
    :type longitude_line_2: Float
    :return: The density of starbucks from the specified "rectangle"
    :rtype: Float
    """


# Test starbucks_per_square_kilometer
# assert 0 == starbucks_per_square_kilometer(STARBUCKS_FILE_NAME, 0, 1, 0, 1)
# assert abs(starbucks_per_square_kilometer(STARBUCKS_FILE_NAME, -90, 90, -180, 180) - 0.0000501877) < 0.0001
# assert abs(starbucks_per_square_kilometer(STARBUCKS_FILE_NAME, 30, 40, -120, -100) - 0.0014883245) < 0.0001
