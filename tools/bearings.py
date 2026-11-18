#!/usr/bin/env python3
"""The map check for the one checkable remote-viewing session in the Buckley file.

On 2 April 1984 (CENTER LANE interview HU-1074/8404/63, CIA-RDP96-00788R001900590001-8) the viewer,
working outward from a site the CIA already suspected (Baalbek, Lebanon), reported three things at
three bearings:

    "approximately 21 miles north-northwest ... rugged mountain peaks"
    "approximately 47 miles north-northeast ... an airfield and a lake"
    "approximately 35 miles south-southeast ... a flat area with many white buildings, perhaps a city"

This script measures, from Baalbek, the great-circle distance and the initial true bearing to the
three real places that fit those descriptions, and names the 16-point compass sector each bearing
falls in.  Coordinates were read from each place's English Wikipedia entry on 18 November 2026 and
are written here so nothing is hidden in a lookup.  Run it:  python3 tools/bearings.py

What the check can and cannot say is written in 03_THE_REST_OF_THE_RECORD.md: the three bearings
match the map, and the session was not sealed (the viewer had been shown overhead imagery of the
suspected site first), so the match proves the protocol's weakness, not the faculty.
"""
import math

# name, latitude (deg N), longitude (deg E), source
PLACES = [
    ("Baalbek, Lebanon (the sponsor's suspected site)", 34.00633611, 36.20732222, "en.wikipedia.org/wiki/Baalbek"),
    ("Qurnat as Sawda' (Lebanon's highest peak)",      34.30000000, 36.11666667, "en.wikipedia.org/wiki/Qurnat_as_Sawda'"),
    ("Lake Homs (Qattinah), Syria",                     34.64340000, 36.57280000, "en.wikipedia.org/wiki/Lake_Homs"),
    ("Damascus, Syria",                                 33.51305556, 36.30944444, "en.wikipedia.org/wiki/Damascus"),
]

CLAIMS = [  # (distance in miles, sector) as the viewer gave them
    (21, "NNW"),
    (47, "NNE"),
    (35, "SSE"),
]

EARTH_RADIUS_MI = 3958.7613   # mean Earth radius, 6371.0088 km, in statute miles
SECTORS = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
           "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]


def great_circle_miles(lat1, lon1, lat2, lon2):
    """Haversine distance between two points given in degrees."""
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dp = p2 - p1
    dl = math.radians(lon2 - lon1)
    a = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * EARTH_RADIUS_MI * math.asin(math.sqrt(a))


def initial_bearing_deg(lat1, lon1, lat2, lon2):
    """Initial bearing from point 1 to point 2, clockwise from true north, in degrees."""
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dl = math.radians(lon2 - lon1)
    x = math.sin(dl) * math.cos(p2)
    y = math.cos(p1) * math.sin(p2) - math.sin(p1) * math.cos(p2) * math.cos(dl)
    return (math.degrees(math.atan2(x, y)) + 360.0) % 360.0


def sector(bearing):
    """The 16-point compass sector a bearing falls in; each sector is 22.5 degrees wide, N centred on 0."""
    return SECTORS[int(((bearing + 11.25) % 360) // 22.5)]


def degrees_outside(bearing, name):
    """How far (degrees) a bearing lies outside the named sector; 0.0 when it is inside."""
    centre = SECTORS.index(name) * 22.5
    off = abs(((bearing - centre) + 180) % 360 - 180)   # angular distance from the sector's centre
    return max(0.0, off - 11.25)


def main():
    origin = PLACES[0]
    print(f"From {origin[0]} ({origin[1]:.5f} N, {origin[2]:.5f} E)")
    print(f"{'place':46s} {'miles':>6s} {'bearing':>8s} {'sector':>6s}   viewer said")
    for (name, lat, lon, _), (claim_mi, claim_sec) in zip(PLACES[1:], CLAIMS):
        d = great_circle_miles(origin[1], origin[2], lat, lon)
        b = initial_bearing_deg(origin[1], origin[2], lat, lon)
        s = sector(b)
        out = degrees_outside(b, claim_sec)
        where = "inside the sector the viewer named" if out == 0.0 else f"{out:.1f} deg outside the sector the viewer named"
        print(f"{name:46s} {d:6.1f} {b:8.1f} {s:>6s}   {claim_mi} mi {claim_sec}"
              f"  (distance off by {abs(d - claim_mi):.1f} mi; {where})")
    print()
    print("Sources: coordinates from the Wikipedia entries named in PLACES (read 18 Nov 2026);")
    print("the viewer's words from CIA-RDP96-00788R001900590001-8 (documents/INDEX.md).")


if __name__ == "__main__":
    main()
