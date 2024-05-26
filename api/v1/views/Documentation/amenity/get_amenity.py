gets amenity by ID
---
tags:
    - Amenities
parameters:
    - name: amenity_id
    in: path
    type: string
    required: true
    description: The id of the amenity
responses:
    404:
        description: amenity not found.
    200:
        description: request executed successfully
        schema:
            properties:
                __class__:
                    type: string
                created_at:
                    type: string
                    description: time of creation of the instance
                updated_at:
                    type: string
                    description: time of last update of the instance
                id:
                    type: string
                    description: The uuid of the instance
                name:
                    type: string
                    description: amenity name
