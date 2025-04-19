import math

def extract_ais_fields(row: list) -> list:
    """extract specific data fields: ID, timestamp, longitude, latitude, speed, course
    args:
        row: list of values of all data fields
    return:
        new_row: list values of specific data fields
    """
    # id, timestamp, longitude, latitude, speed, course
    new_row = [row[2], row[0], row[4], row[3], row[6], row[7]]
    return new_row


def detect_none(row):
    """detect none value in each row
    """
    if all(ele for ele in row):
        return True
    else:
        return False


def drop_duplicated_time(ais_points: list) -> list:
    """ drop duplicated time of each ship
    """
    new_ais_points = []
    for ais in ais_points:
        if any(data.get_timestamp() == ais.get_timestamp()
               for data in new_ais_points):
            pass
        else:
            new_ais_points.append(ais)
    return new_ais_points
