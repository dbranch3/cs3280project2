import unittest

from utils import calculate_subnet_ipv6

class CalculateSubnetIpv6Test(unittest.TestCase):
    def test_should_have_64_bit_network_portion(self):
        inputIpAddress = "2601:00cb:0000:d9e0:a5fe:b1a7:dab9:cdb1"
        inputPrefix = 64

        output = calculate_subnet_ipv6(inputIpAddress, inputPrefix)

        self.assertEqual(output, "2601:00cb:0000:d9e0:0000:0000:0000:0000")
