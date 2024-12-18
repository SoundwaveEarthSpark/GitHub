import unittest
from tests_12_3 import RunnerTest, TournamentTest

runnerTS = unittest.TestSuite()
runnerTS.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
runnerTS.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runer = unittest.TextTestRunner(verbosity=2)
runer.run(runnerTS)
