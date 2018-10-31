import math

def get_dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 )

def crush_check_line(x1, y1, x2, y2, box_x1, box_y1, box_x2, box_y2):
    points = [[box_x1, box_y1], [box_x2, box_y1], [box_x2, box_y2], [box_x1, box_y2]]

    i = -1

    while i < 3:
        x3, x4 = points[i][0], points[i+1][0]
        y3, y4 = points[i][1], points[i + 1][1]
        denom = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1)

        if denom != 0:
            t = (x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)
            s = (x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)
            t = t / denom
            s = s / denom
            if t >= 0 and t <= 1 and s >= 0 and s <= 1:
                return True

        i = i + 1
    return False



def crush_check_box(box1_x1, box1_y1, box1_x2, box1_y2, box2_x1, box2_y1, box2_x2, box2_y2):
    pass