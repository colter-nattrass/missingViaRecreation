import math
import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return math.sqrt(self.x**2 + self.y**2)

    def rotate_90_degrees(self):
        new_x = -self.y
        new_y = self.x
        return Point(new_x, new_y)

    def rotate_by_radians(self, angle_radians):
        cos_angle = math.cos(angle_radians)
        sin_angle = math.sin(angle_radians)

        new_x = self.x * cos_angle - self.y * sin_angle
        new_y = self.x * sin_angle + self.y * cos_angle
        return Point(new_x, new_y)

    def draw_box_around_point(self, length, height):
        half_length = length / 2
        half_height = height / 2

        top_left = Point(self.x - half_length, self.y + half_height)
        top_right = Point(self.x + half_length, self.y + half_height)
        bottom_left = Point(self.x - half_length, self.y - half_height)
        bottom_right = Point(self.x + half_length, self.y - half_height)

        return top_left, top_right, bottom_left, bottom_right

    @staticmethod
    def generate_random_point(max_distance=150):
        x = random.uniform(-max_distance, max_distance)
        y_range = math.sqrt(max_distance**2 - x**2)
        y = random.uniform(-y_range, y_range)
        return Point(x, y)


class SimulatedThicknessValue:
    def __init__(self, mean=20, deviation=5, outlier_probability=0.2):
        self.mean = mean
        self.deviation = deviation
        self.outlier_probability = outlier_probability

    def generate_value(self):
        if random.random() < self.outlier_probability:
            return random.uniform(self.mean - 2 * self.deviation, self.mean + 2 * self.deviation)
        else:
            return random.uniform(self.mean - self.deviation, self.mean + self.deviation)

