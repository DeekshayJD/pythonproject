# Define a tuple to represent geographic coordinates: (latitude, longitude)
# For example, (latitude, longitude) = (37.7749, -122.4194) represents the coordinates of San Francisco, CA.

coordinates = {
    "San Francisco": (37.7749, -122.4194),
    "New York City": (40.7128, -74.0060),
    "London": (51.5074, -0.1278),
    "Tokyo": (35.6895, 139.6917)
}

# Accessing coordinates for a specific location
print("Coordinates of San Francisco:", coordinates["San Francisco"])

# Iterating through the coordinates
for location, coords in coordinates.items():
    print("Coordinates of", location + ":", coords)
