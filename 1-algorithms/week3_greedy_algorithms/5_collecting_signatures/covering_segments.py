# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments: list):
    segments.sort(key=lambda s: (s.end, s.end - s.start))
    points = []
    while segments:
        segment = segments.pop(0)
        point = segment.end
        points.append(point)
        for s in segments[:]:
            if s.start <= point <= s.end:
                segments.remove(s)
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)

