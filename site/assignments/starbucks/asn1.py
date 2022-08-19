# NAME:
# ST-NUMBER:
# EMAIL:


def load_asn1_data():
    """
    This function loads the file `starbucks.csv` and returns a LIST of
    latitudes and longitudes for North American Starbucks'.
    We'll talk about LISTs formally in class in a few lectures, but maybe
    you can start guessing how they work based on what you see here...
    """

    import csv

    reader = csv.reader(
        open("starbucks.csv", "r")
    )  # starbucks.csv MUST be in the same directory as this script for this to work!
    locations = []

    for r in reader:
        locations.append((r[0], r[1]))

    return locations


def convert_to_decimal(degrees, minutes, seconds):
    """
    You fill in this one yourself!

    :returns: a (single) decimal lat/long
    """

    # INSERT YOUR CODE HERE!

    return 0  # replace this with your real return statement (0 is just placeholder)


def subtended_area(lat1, lon1, lat2, lon2):
    """
    You fill in this one yourself!
    :returns : the area of the lat-long rectangle between the given points (in km^2)
    """

    # INSERT YOUR CODE HERE!
    return 0  # replace this with your real return statement (0 is just placeholder)


def num_starbucks(locations, lat1, lon1, lat2, lon2):
    """
    Function to compute the number of Starbucks in the lat-long rectangle with
    corners lat1,lon1 and lat2,lon2.

    There's new stuff in here, too. We haven't formally discussed `for` loops, so
    the loop is already done... but have a look at it. What do you think it's doing?

    :param locations: a list of Starbucks locations as (lon,lat) pairs
    :param lat1: Latitude for bottom left corner (in decimal degrees)
    :param lon1: Longitude for bottom left corner (in decimal degrees)
    :param lat2: Latitude for upper right corner (in decimal degrees)
    :param lon2: Longitude for upper right corner (in decimal degrees)

    :returns: An integer with the number of Starbucks locations in the given rectangle
    """

    # HINT: You should probably initialize some kind of 'Starbucks counter' variable here,
    # before the loop

    # This is an instruction to Python: Do the body (the indented code) following
    # `for` statement, for _every_ location in our list of locations.
    # This is a loop. It's already written for you... you just have to fill in the body
    # Really what this means is: Go through each location (line in the input file) and do....... (whatever we're writing below)
    for loc in locations:
        loc_lat = float(loc[1])  # Values will be strings, so let's make them floats
        loc_lon = float(loc[0])

        # print(loc_lat, loc_lon,  (lat1 < loc_lat), ( loc_lat < lat2), (lon1 < loc_lon), (loc_lon < lon2))

        # INSERT YOUR CODE HERE!

    # RETURN the value in your counter variable


def starbucks_per_kmsq(lat1, lon1, lat2, lon2):
    # INSERT YOUR CODE HERE!
    return 0  # replace this with your real return statement (0 is just placeholder)


# This line will test the density of Starbucks in the area bounded by San Diego and Boston
# Should be in the neighborhood of 0.00120 sb/km^2
# >>> starbucks_per_kmsq(32.72,-117.16,42.35,-71.06)
