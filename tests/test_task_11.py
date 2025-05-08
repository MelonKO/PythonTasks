import unittest
from src.task_11 import Dessert


class TastyTest(unittest.TestCase):
    def test(self):
        # Default constructed
        unknow_dessert = Dessert()
        unknow_dessert.name = "Cockerel on a stick"
        self.assertEqual(unknow_dessert.name, "Cockerel on a stick")
        unknow_dessert.calories = 300
        self.assertEqual(unknow_dessert.calories, 300)
        self.assertFalse(unknow_dessert.is_healthy())
        unknow_dessert.calories = 200
        self.assertFalse(unknow_dessert.is_healthy())
        unknow_dessert.calories = 199
        self.assertTrue(unknow_dessert.is_healthy())

        # Cheesecake
        cheesecake = Dessert("Cheesecake", 321)
        self.assertEqual(cheesecake.name, "Cheesecake")
        self.assertEqual(cheesecake.calories, 321)
        self.assertFalse(cheesecake.is_healthy())

        # Anyway, both are delicious
        self.assertTrue(unknow_dessert.is_delicious()
                        and cheesecake.is_delicious())

        with self.assertRaises(TypeError):
            bad_dessert = Dessert(5, -5)

        with self.assertRaises(TypeError):
            bad_dessert = Dessert("abba", -5.0)

        bad_dessert = Dessert("Some new bad desert", -5)
        self.assertEqual(bad_dessert.name, "Some new bad desert")
        self.assertEqual(bad_dessert.calories, 0)


if __name__ == "__main__":
    unittest.main()
