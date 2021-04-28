import math

def angle_to_sexigesimal(angle_in_degrees:float, decimals:int=3) -> str:
    """
    Convert the given angle to a sexigesimal string of hours of RA.

    Parameters
    ----------
    angle_in_degrees : float
        A scalar angle, expressed in degrees

    Returns
    -------
    hms_str : str
        The sexigesimal string giving the hours, minutes, and seconds of RA for
        the given `angle_in_degrees`

    Example
    -------
    angle_to_sexigesimal(48.311167,3) returns 48d 18' 40.201"

    """
    if math.floor(decimals) != decimals:
        raise OSError('decimals should be an integer!')

    degrees = math.floor(angle_in_degrees)
    min_num = (angle_in_degrees - degrees)*60
    minutes = math.floor(min_num)

    seconds = (min_num - minutes)*60

    format_string = "{}d {}' {:." + str(decimals) + "f}\""
    return format_string.format(degrees, minutes, seconds)
