import unittest

from utils import calculate_subnet_ipv4

class CalculateSubnetIpv4Test(unittest.TestCase):
    def test_should_return_proper_subnet(self):
        inputIpAddress = "192.168.244.3"
        inputSubnetMask = "255.255.0.0"

        output = calculate_subnet_ipv4(inputIpAddress, inputSubnetMask)

        self.assertEqual(output, "192.168.0.0")
