import logging
logger = logging.getLogger(__name__)

from geopy.distance import geodesic, great_circle


def calculate_distance(point_a, point_b, method=great_circle):
    """Calulcate distance between two locations.

    Parameters
    ----------
    point_a : tuple
        (lat, long)
    point_b : tuple
        (lat, long)
    method : func
        Valid values: geodesic, great_circle.
        from geopy.distance import geodesic, great_circle

    Returns
    -------
    distance : float
        Distance two points in miles.

    """
    distance = method(point_a, point_b).miles
    return distance


def categorize_location(point, categories):
    """Get nearest category for one specific location.

    Parameters
    ----------
    point : tuple
        (lat, long)
    categories : dict
        config.CATEGORIES

    Returns
    -------
    category : str
        Nearest category.

    """
    categories_distances = {}
    try:
        for cat in categories.keys():
            cat_distances = []
            central_points = categories[cat]['central']
            for central_point in central_points:
                point_c = (central_point['lat'], central_point['long'])
                distance = calculate_distance(point, point_c)
                cat_distances.append(distance)
            categories_distances[cat] = min(cat_distances)

        categories_distances_sorted = sorted(categories_distances.items(),
                                             key=lambda kv: kv[1])
        category = categories_distances_sorted[0][0]
        return category

    except (KeyError, IndexError) as e:
        logger.exception(e)
        return None
