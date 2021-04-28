# -*- coding: utf-8 -*-

"""
Buggy function
==============
A module that used to contain a buggy function.

"""


# %% FUNCTION DEFINITIONS
# Define function that converts a given angle to its sexigesimal format
def angle_to_sexigesimal(angle_in_degrees, decimals=3):
    """
    Convert the given angle to a sexigesimal string of hours of RA.

    Parameters
    ----------
    angle_in_degrees : float
        A scalar angle, expressed in degrees.

    Optional
    --------
    decimals : int. Default: 3
        The number of decimals that the returned seconds string must have.

    Returns
    -------
    hms_str : str
        The sexigesimal string giving the hours, minutes, and seconds of RA for
        the given `angle_in_degrees`.

    """

    # Check if given decimals is an integer
    if not isinstance(decimals, int):
        # If not, raise a ValueError
        raise ValueError("Input argument 'decimals' should be an integer!")

    # Check the value of decimals and act accordingly
    n_digits = decimals+3 if decimals else 2

    # Calculate the number of full hours in the provided number of degrees
    hours_num = angle_in_degrees*24/360
    hours = int(hours_num)

    # Calculate the number of full minutes in the remaining number of hours
    min_num = (hours_num-hours)*60
    minutes = int(min_num)

    # Calculate the number of seconds in the remaining number of minutes
    seconds = (min_num-minutes)*60

    # Determine the format of the sexigesimal string and use it
    format_string = "{0:02.0f}:{1:02.0f}:{2:0{3}.{4}f}"
    hms_str = format_string.format(hours, minutes, seconds, n_digits, decimals)

    # Return hms_str
    return(hms_str)
