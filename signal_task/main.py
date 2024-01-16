from dataclasses import dataclass


@dataclass
class Transmiter:
    coordinate_x: int
    coordinate_y: int
    radius: int


@dataclass
class SignalPoint:
    coordinate_x: int
    coordinate_y: int


t_1 = Transmiter(6, 11, 4)
t_2 = Transmiter(8, 17, 3)
t_3 = Transmiter(19, 19, 2)
t_4 = Transmiter(19, 11, 4)
t_5 = Transmiter(15, 7, 6)
t_6 = Transmiter(12, 19, 4)
all_transmiters = [t_1, t_2, t_3, t_4, t_5, t_6]

p_start = SignalPoint(10, 19)
p_end = SignalPoint(19, 14)


def whether_the_transmitters_are_within_range(
    transmiter1: Transmiter, transmiter2: Transmiter
) -> bool:
    length_centre = (
        (transmiter2.coordinate_x - transmiter1.coordinate_x) ** 2
        + (transmiter2.coordinate_y - transmiter1.coordinate_y) ** 2
    ) ** (1 / 2)
    length_r = transmiter1.radius + transmiter2.radius
    return length_centre <= length_r


def whether_the_point_is_within_the_range_of_the_transmitter(
    transmiter: Transmiter, point: SignalPoint
) -> bool:
    length_centre = (
        (transmiter.coordinate_x - point.coordinate_x) ** 2
        + (transmiter.coordinate_y - point.coordinate_y) ** 2
    ) ** (1 / 2)
    return length_centre <= transmiter.radius


def whether_the_signal_will_reach_its_destination(
    start_point: SignalPoint, end_point: SignalPoint, transmiters: list
) -> bool:
    p_end_transmiters = []
    connection_transmiters = []

    for i in transmiters:
        if whether_the_point_is_within_the_range_of_the_transmitter(i, start_point):
            connection_transmiters.append(i)

    for i in transmiters:
        if whether_the_point_is_within_the_range_of_the_transmitter(i, end_point):
            p_end_transmiters.append(i)

    for z in connection_transmiters:
        for i in all_transmiters:
            if i in connection_transmiters:
                continue
            elif whether_the_transmitters_are_within_range(z, i):
                connection_transmiters.append(i)

    for i in p_end_transmiters:
        return i in connection_transmiters

    return False


# print(signal_path(t_6, all_transmiters, []))
print(whether_the_signal_will_reach_its_destination(p_start, p_end, all_transmiters))
# print(whether_the_point_is_within_the_range_of_the_transmitter(t_1,p_start))
# print(whether_the_transmitters_are_within_range(t_1,t_5))
