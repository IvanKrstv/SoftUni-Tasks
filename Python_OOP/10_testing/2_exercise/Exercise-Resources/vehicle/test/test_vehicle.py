from unittest import TestCase, main
from project.vehicle import Vehicle

class VehicleTests(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(60, 100)

    def test_init(self):
        self.assertEqual(60, self.vehicle.fuel)
        self.assertEqual(60, self.vehicle.capacity)
        self.assertEqual(100, self.vehicle.horse_power)
        self.assertEqual(1.25,self.vehicle.fuel_consumption)

    def test_drive_without_enough_fuel_raises(self):
        self.assertEqual(60, self.vehicle.fuel)

        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)
        self.assertEqual("Not enough fuel", str(ex.exception))

        self.assertEqual(60, self.vehicle.fuel)

    def test_drive(self):
        self.assertEqual(60, self.vehicle.fuel)
        self.vehicle.drive(10)
        self.assertEqual(47.5, self.vehicle.fuel)

    def test_refuel_too_much_raises(self):
        self.assertEqual(60, self.vehicle.fuel)
        self.assertEqual(60, self.vehicle.capacity)

        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(10)
        self.assertEqual("Too much fuel", str(ex.exception))

        self.assertEqual(60, self.vehicle.fuel)

    def test_refuel(self):
        self.assertEqual(60, self.vehicle.fuel)
        self.assertEqual(60, self.vehicle.capacity)

        self.vehicle.drive(10)
        self.assertEqual(47.5, self.vehicle.fuel)

        self.vehicle.refuel(10)
        self.assertEqual(57.5, self.vehicle.fuel)

        self.vehicle.drive(10)
        self.assertEqual(45, self.vehicle.fuel)

        self.vehicle.refuel(15)
        self.assertEqual(60, self.vehicle.fuel)

    def test_str(self):
        self.assertEqual(f"The vehicle has {self.vehicle.horse_power} "
               f"horse power with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption", str(self.vehicle))


if __name__ == '__main__':
    main()