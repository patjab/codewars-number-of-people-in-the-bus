def number(bus_stops):
    bus_stops.insert(0, 0)
    return reduce(lambda acc, curr: acc + curr[0] - curr[1], bus_stops)
