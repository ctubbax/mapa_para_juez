from fastkml import KML

def read_kml(fname='ss.kml'):
    kml = KML()
    kml.from_string(open(fname).read())
    points = dict()
    for feature in kml.features():
        for placemark in feature.features():
            if placemark.styleUrl.startswith('#hf'):
                points.update({placemark.name:
                                   (placemark.geometry.y, placemark.geometry.x, )})
    return points