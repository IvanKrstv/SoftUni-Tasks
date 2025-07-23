class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'

import unittest

class WorkerTests(unittest.TestCase):
    def test_init(self):
        worker = Worker(name="Tosho", salary=1000, energy=100)
        self.assertEqual("Tosho", worker.name)
        self.assertEqual(1000, worker.salary)
        self.assertEqual(100, worker.energy)
        self.assertEqual(0, worker.money)

    def test_work_negative_energy(self):
        worker = Worker(name="Tosho", salary=1000, energy=-1)

        self.assertEqual(-1, worker.energy)
        self.assertEqual(0, worker.money)

        with self.assertRaises(Exception) as ex:
            self.assertEqual('Not enough energy.', str(ex.exception))

        self.assertEqual(-1, worker.energy)
        self.assertEqual(0, worker.money)

    def test_work_zero_energy(self):
        worker = Worker(name="Tosho", salary=1000, energy=0)

        self.assertEqual(0, worker.energy)
        self.assertEqual(0, worker.money)

        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

        self.assertEqual(0, worker.energy)
        self.assertEqual(0, worker.money)

    def test_work(self):
        worker = Worker(name="Tosho", salary=1000, energy=100)

        worker.work()
        worker.work()

        self.assertEqual(2000, worker.money)
        self.assertEqual(98, worker.energy)

    def test_rest(self):
        worker = Worker(name="Tosho", salary=1000, energy=100)

        worker.rest()

        self.assertEqual(101, worker.energy)

    def test_get_info(self):
        worker = Worker(name="Tosho", salary=1000, energy=100)

        worker.work()
        worker.work()

        self.assertEqual(f'Tosho has saved 2000 money.', worker.get_info())



if __name__ == '__main__':
    unittest.main()