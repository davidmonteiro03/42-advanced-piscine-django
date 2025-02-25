#!/usr/bin/python3
import sys
from antigravity import geohash


def main():
    argc = len(sys.argv)
    try:
        assert argc == 4, \
            f"Usage: python3 {sys.argv[0]} <latitude> <longitude> <datedow>"
        try:
            latitude = float(sys.argv[1])
        except Exception:
            raise Exception("Error reading latitude.")
        try:
            longitude = float(sys.argv[2])
        except Exception:
            raise Exception("Error reading longitude.")
        try:
            datedow = str(sys.argv[3]).encode()
        except Exception:
            raise Exception("Error reading datedow.")
        try:
            geohash(latitude, longitude, datedow)
        except Exception:
            raise Exception("Error doing geohash.")
    except Exception as e:
        print(e, file=sys.stderr)
        exit(1)


if __name__ == '__main__':
    main()
