"""
author: Shunqiang Xu
date: 20/04/2025
"""
import os
import time
import math
import pickle
import shapefile
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def get_distance(point1, point2):
    """ calculate the distance between two global coordinates using haversine formula
    :param:
        point1: (lonitude, latitude)
        point2: (longitude, latitude)
    :return:
        distance: in meter
    """
    rad_lat1 = math.radians(point1[1])
    rad_lat2 = math.radians(point2[1])
    delta_lon = math.radians(point1[0] - point2[0])
    top_1 = math.cos(rad_lat2) * math.sin(delta_lon)
    top_2 = math.cos(rad_lat2) * math.sin(rad_lat2) - math.sin(rad_lat1) * math.cos(rad_lat2) * math.cos(delta_lon)
    top = math.sqrt(top_1 * top_1 + top_2 * top_2)
    bottom = math.sin(rad_lat1) * math.sin(rad_lat2) + math.cos(rad_lat1) * math.cos(rad_lat2) * math.cos(delta_lon)
    delta_sigma = math.atan2(top, bottom)
    distance = delta_sigma * 6378137.0
    return round(distance, 3)


class AisPoint(object):
    def __init__(self, mmsi: int, timestamp: int, lon: float, lat: float, sog: float, cog: float):
        self.mmsi = mmsi
        self.timestamp = timestamp
        self.lon = lon
        self.lat = lat
        self.sog = sog
        self.cog = cog

    def set_timestamp(self, time: int):
        self.timestamp = time

    def get_timestamp(self):
        return self.timestamp

    def get_mmsi(self):
        return self.mmsi

    def get_lon(self):
        return self.lon

    def get_lat(self):
        return self.lat

    def get_sog(self):
        return self.sog

    def get_cog(self):
        return self.cog


def detect_stay(ais_seg: list) -> list:
    """
    detect stay behavior in a single trajectory
    :param ais_seg: list of ais point objects
    :return: stays: list of list of stay trajectory segments
    """
    DISTANCE = 400  # maximum distance in the stay segment
    TIME = 1800  # minimal stay duration
    POINT_NUM = 5  # minimal number of stay points
    stays = []  # save stay segments

    m = 0  # start point of stay segment
    n = 0  # end index of stay segment
    while m + 1 < len(ais_seg):
        while get_distance((ais_seg[m].get_lon(), ais_seg[m].get_lat()),
                           (ais_seg[n].get_lon(),
                            ais_seg[n].get_lat())) < DISTANCE and n + 1 < len(ais_seg):
            n = n + 1
        if ais_seg[n].get_timestamp() - ais_seg[m].get_timestamp() > TIME and n - m > POINT_NUM:
            behavior = ais_seg[m:n]
            stays.append(behavior)
        m = n
    return stays


def detect_stays(ais_segs: list) -> list:
    stays = []  # save segment of stay behavior
    for ais_seg in ais_segs:
        stay = detect_stay(ais_seg)
        if stay:
            stays.append(stay)
    return stays


def visualize(stays):
    fig, ax = plt.subplots(1, 1)
    fig_config = {
        "font.size": 15,
        "font.style": 'normal',
        "axes.labelsize": 15,
        "xtick.labelsize": 15,
        "ytick.labelsize": 15,
        "figure.figsize": (4, 4),
        "figure.dpi": 600
    }
    plt.rcParams.update(fig_config)

    cwd = os.getcwd()  # current working directory
    pwd = os.path.dirname(cwd)  # parent working directory

    # add geospatial background
    dmk_shp_file = os.path.join(pwd, 'data', 'Denmark-shapfile', 'DNK_adm0.shp')
    sf_dmk = shapefile.Reader(dmk_shp_file)
    dmk_records = sf_dmk.shapeRecords()
    dmk_sep_idx = sf_dmk.shapes()[0].parts

    for i in range(1, len(dmk_sep_idx)):
        for shape in dmk_records:
            xy = [i for i in shape.shape.points[dmk_sep_idx[i-1]:dmk_sep_idx[i]]]
            x, y = zip(*[(j[0], j[1]) for j in xy])
            polygon = Polygon(xy,
                              closed=True,
                              facecolor='lightgrey',
                              edgecolor='black',
                              zorder=2)
            ax.add_patch(polygon)
            ax.plot(x, y, color='black', linewidth=1, zorder=2)

    # plot stay points
    stay_segments = [item for stay in stays for item in stay]
    for stay_seg in stay_segments:
        lon = [stay_seg[i].get_lon() for i in range(len(stay_seg))]
        lat = [stay_seg[i].get_lat() for i in range(len(stay_seg))]
        ax.scatter(lon, lat, c='r', s=10, zorder=3)
    ax.scatter(stay_segments[0][0].get_lon(),
               stay_segments[0][0].get_lat(),
               c='r',
               s=10,
               label='Stay point',
               zorder=3)
    
    # additional figure configuration
    ax.grid(alpha=0.2, zorder=1)
    ax.set_xlim(8.5, 13)
    ax.set_ylim(54.5, 56.5)
    ax.set_xlabel(r'Longitude($^\circ$)', fontsize=15)
    ax.set_ylabel(r'Latitude($^\circ$)', fontsize=15)
    ax.legend(loc=1)
    outputs = os.path.join(pwd, 'outputs.png')
    plt.savefig(outputs, dpi=600)


def load_ais_data(name):
    """ load data based on its name
    :param name:            the name of the data to be used
    :return: ais_data:      list of point objects
    """
    cwd = os.getcwd()  # current working directory
    pwd = os.path.dirname(cwd)  # parent working directory
    target_folder = os.path.join(pwd, "data")
    data = os.path.join(target_folder, name)
    return pickle.load(open(data, 'rb'))


def main():
    print('Loading data...')
    cleaned_ais = load_ais_data('cleaned_ais.pkl')
    print('Number of ships: {}'.format(len(cleaned_ais)))
    start_time = time.time() * 1000
    stays = detect_stays(cleaned_ais)
    end_time = time.time() * 1000
    print('Execution time:{} ms'.format(round(end_time-start_time)))
    print('Visualizing results....')
    visualize(stays)
    print('Done!')
    return 0


if __name__ == '__main__':
    main()
