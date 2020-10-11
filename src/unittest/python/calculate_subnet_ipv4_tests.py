import unittest

from utils import calculate_subnet_ipv4

class CalculateSubnetIpv4Test(unittest.TestCase):
    def test_should_return_proper_subnet_class_a(self):
        inputIpAddress = "127.255.255.255"
        inputSubnetMask = "255.0.0.0"

        output = calculate_subnet_ipv4(inputIpAddress, inputSubnetMask)

        self.assertEqual(output, "127.0.0.0")

    def test_should_return_proper_subnet_class_b(self):
        inputIpAddress = "191.255.255.255"
        inputSubnetMask = "255.255.0.0"

        output = calculate_subnet_ipv4(inputIpAddress, inputSubnetMask)

        self.assertEqual(output, "191.255.0.0")

    def test_should_return_proper_subnet_class_c(self):
        inputIpAddress = "223.255.255.255"
        inputSubnetMask = "255.255.255.0"

        output = calculate_subnet_ipv4(inputIpAddress, inputSubnetMask)

        self.assertEqual(output, "223.255.255.0")
