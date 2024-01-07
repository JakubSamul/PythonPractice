import unittest
from main import (
    SignalPoint,
    Transmiter,
    whether_the_transmitters_are_within_range,
    whether_the_point_is_within_the_range_of_the_transmitter,
    whether_the_signal_will_reach_its_destination,
)


class TestSignal(unittest.TestCase):
    def test_transmiters_are_in_the_same_range(self):
        t_1 = Transmiter(8, 17, 3)
        t_2 = Transmiter(12, 19, 4)
        result = whether_the_transmitters_are_within_range(t_1, t_2)
        self.assertTrue(result)

    def test_transmiters_are_not_in_the_same_range(self):
        t_2 = Transmiter(8, 17, 3)
        t_3 = Transmiter(19, 19, 2)
        result = whether_the_transmitters_are_within_range(t_2, t_3)
        self.assertFalse(result)

    def test_point_is_not_within_the_range_of_the_transmiter(self):
        p_start = SignalPoint(10, 19)
        t_1 = Transmiter(6, 11, 4)
        result = whether_the_point_is_within_the_range_of_the_transmitter(t_1, p_start)
        self.assertFalse(result)

    def test_point_is_within_the_range_of_the_transmiter(self):
        p_start = SignalPoint(10, 19)
        t_6 = Transmiter(12, 19, 4)
        result = whether_the_point_is_within_the_range_of_the_transmitter(t_6, p_start)
        self.assertTrue(result)

    def the_start_point_is_within_the_range_of_the_end_point(self):
        p_start = SignalPoint(10, 19)
        p_end = SignalPoint(19, 14)
        t_1 = Transmiter(6, 11, 4)
        t_2 = Transmiter(8, 17, 3)
        t_3 = Transmiter(19, 19, 2)
        t_4 = Transmiter(19, 11, 4)
        t_5 = Transmiter(15, 7, 6)
        t_6 = Transmiter(12, 19, 4)
        all_transmiters = [t_1, t_2, t_3, t_4, t_5, t_6]
        result = whether_the_signal_will_reach_its_destination(
            p_start, p_end, all_transmiters
        )
        self.assertTrue(result)

    def the_start_point_is_not_within_the_range_of_the_end_point(self):
        p_start = SignalPoint(10, 19)
        p_end = SignalPoint(19, 14)
        t_1 = Transmiter(60, 11, 4)
        t_2 = Transmiter(80, 17, 3)
        t_3 = Transmiter(190, 19, 2)
        t_4 = Transmiter(190, 11, 4)
        t_5 = Transmiter(150, 7, 6)
        t_6 = Transmiter(120, 19, 4)
        all_transmiters = [t_1, t_2, t_3, t_4, t_5, t_6]
        result = whether_the_signal_will_reach_its_destination(
            p_start, p_end, all_transmiters
        )
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
