import math

AB = int(input())
BC = int(input())

theta = math.degrees(math.atan2(AB, BC))
print(str(round(theta)) + chr(176))
