def points_with_equal_distance(center, distance):
    result = []
    for x in range(center[0] - distance, center[0] + distance + 1):
        y_range = distance - abs(x - center[0])
        # for y in range(center[1] - y_range, center[1] + y_range + 1):
        result.append((x, y))
    return result

center = (10, 10)
distance = 2
equal_distance_points = points_with_equal_distance(center, distance)
print(equal_distance_points)
