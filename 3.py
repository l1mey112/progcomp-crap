import math
import fileinput

kmdeglat0 = 110.567
kmdeglat90 = 111.699
kmdeglong0 = 111.321

def calc_dist(lat1: float, long1: float, lat2: float, long2: float):
	L = (lat1 + lat2) / 2
	LL = (long1 + long2) / 2

	long_scale = lambda x: x * math.cos(math.radians(L)) * kmdeglong0
	lat_scale = lambda x: x * ((90 - abs(LL)) * kmdeglat0 + abs(LL) * kmdeglat90) / 90

	return math.sqrt((lat_scale(lat2) - lat_scale(lat1)) ** 2 + (long_scale(long2) - long_scale(long1)) ** 2)

the_iter = fileinput.input()
next(the_iter) # Version,212
next(the_iter) #
next(the_iter) # WGS 1984 (GPS),217, 6378137, 298.257223563, 0, 0, 0
next(the_iter) # USER GRID,0,0,0,0,0
next(the_iter)

waypoints = [] # (name, lat, long, desc)

# w,d,jnS,-34.301117,150.999496,south junction,06-07-2024,05:58:15,0,0,48,0,13
# (2: NAME, 3: LAT, 4: LONG, 5: DESC)

# t,d,-34.299149,150.994003,00/00/00,00:00:00,0,1
# (2: LAT, 3: LONG)

# get waypoints
for line in the_iter:
	line: str = line.strip()

	if line == '':
		break

	_, _, name, lat, long, desc, *_ = line.split(',')

	i = len(waypoints)
	waypoints.append({
		'name': name,
		'lat': float(lat),
		'long': float(long),
		'desc': desc,
		'visited': False,
	})

total_dist = 0

lat_before, long_before = None, None

i = 0
# get routes
for line in the_iter:
	line: str = line.strip()

	if line == '':
		break

	_, _, lat, long, *_ = line.split(',')
	lat = float(lat)
	long = float(long)

	if not lat_before:
		lat_before, long_before = lat, long

	dist_between = calc_dist(lat_before, long_before, lat, long)
	lat_before, long_before = lat, long

	closest = None # (dist, obj)
	for waypoint in waypoints:
		dist = calc_dist(waypoint['lat'], waypoint['long'], lat, long)
		if not closest:
			closest = (dist, waypoint)
			continue
			
		if dist < closest[0]:
			closest = (dist, waypoint)

	if closest[0] < 0.03:
		name = closest[1]['name']

		if closest[1]['visited']:
			name = name + '*'

		print(f"{round(total_dist, 2)} {name.ljust(11)} {closest[1]['desc']}")

		closest[1]['visited'] = True

	total_dist += dist_between

	i += 1
