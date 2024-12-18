import unittest
from unittest import TestCase

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers
#
# class TournamentTest(TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.all_results = {}
#
#     def setUp(self):
#         self.runner_1 = Runner("Усейн", 10)
#         self.runner_2 = Runner("Андрей", 9)
#         self.runner_3 = Runner("Ник", 3)
#
#     def test_1(self):
#         tournament = Tournament(90, self.runner_1, self.runner_3)
#         results = tournament.start()
#         self.all_results['test_1'] = results
#         self.assertTrue(results[list(results.keys())[-1]] == 'Ник')
#
#     def test_2(self):
#         tournament = Tournament(90, self.runner_2, self.runner_3)
#         results = tournament.start()
#         self.all_results['test_2'] = results
#         self.assertTrue(results[list(results.keys())[-1]] == 'Ник')
#
#     def test_t3(self):
#         tournament = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
#         results = tournament.start()
#         self.all_results['test_3'] = results
#         self.assertTrue(results[list(results.keys())[-1]] == 'Ник')
#
#     @classmethod
#     def tearDownClass(cls):
#         for test_key, test_value in cls.all_results.items():
#             formatted_result = {key: value.name for key, value in sorted(test_value.items())}
#             print(formatted_result)
#
#
# if __name__ == '__main__':
#     unittest.main()