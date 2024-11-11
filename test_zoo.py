import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)
       
    # Add your additional test cases here.
    def test_ecp_case1(self):
        self.assertEqual(self.zoo.get_ticket_price(-5), "Invalid")

    def test_ecp_case2(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)

    def test_ecp_case3(self):
        self.assertEqual(self.zoo.get_ticket_price(15), 100)

    def test_ecp_case4(self):
        self.assertEqual(self.zoo.get_ticket_price(25), 150)

    def test_ecp_case5(self):
        self.assertEqual(self.zoo.get_ticket_price(65), 100) 




    def test_bva_case1(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), "Invalid")

    def test_bva_case2(self):
        self.assertEqual(self.zoo.get_ticket_price(0), 50)

    def test_bva_case3(self):
        self.assertEqual(self.zoo.get_ticket_price(12), 50)

    def test_bva_case4(self):
        self.assertEqual(self.zoo.get_ticket_price(13), 100)

    def test_bva_case5(self):
        self.assertEqual(self.zoo.get_ticket_price(20), 100)

    def test_bva_case6(self):
        self.assertEqual(self.zoo.get_ticket_price(21), 150)

    def test_bva_case7(self):
        self.assertEqual(self.zoo.get_ticket_price(60), 150)

    def test_bva_case8(self):
        self.assertEqual(self.zoo.get_ticket_price(61), 100)


if __name__ == '__main__':
    unittest.main()