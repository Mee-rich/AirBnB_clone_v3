#!/usr/bin/python3

from api.v1.views import app_views

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    '''Status of API'''
    return jsonify({"status": "OK"}
            )

@app_viwews.route('/stats', methods=['GET'], strict_slashes=False)
def number_objects():
    '''Retrieves the number of each objects by type'''
    classes = [Amenity, City, Place, Review, State, User]
    names = ["amenities", "cities", "places", "reviews", "states", "users"]

    num_objs = {name:storage.count(cls) for name, cls in zip(names, classes)}
    return jsonify(num_objs)
