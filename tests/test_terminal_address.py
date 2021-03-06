# Unit Address / MAC Address converters for SCTE 55-1 terminals
# Unit tests module
from terminal_address.scte_55_1_address import mac_to_ua, ua_to_mac
import pkgutil
import random
import unittest

test_count = 1000

# Load known values
A_ua_mac = []
data = pkgutil.get_data(__package__, "mac_ua_tests.csv")
data = data.decode("utf-8").splitlines()[1:]
for line in data:
    line = line.strip()
    ua, mac = line.split(',')
    A_ua_mac.append((ua, mac))


class ConverterTests(unittest.TestCase):
    def test_known_ua(self):
        """mac_to_ua should give known result with known input"""
        for ua, mac in A_ua_mac:
            self.assertEqual(ua, mac_to_ua(mac))

    def test_known_mac(self):
        """ua_to_mac should give known result with known input"""
        for ua, mac in A_ua_mac:
            self.assertEqual(mac, ua_to_mac(ua))

    def test_known_ua_roundtrip(self):
        """mac_to_ua(ua_to_mac(ua)) should equal ua for known ua"""
        for ua, mac in A_ua_mac:
            self.assertEqual(ua, mac_to_ua(ua_to_mac(ua)))

    def test_known_mac_roundtrip(self):
        """ua_to_mac(mac_to_ua(mac)) should equal mac for known mac"""
        for ua, mac in A_ua_mac:
            self.assertEqual(mac, ua_to_mac(mac_to_ua(mac)))

    def test_random_mac_roundtrip(self):
        """ua_to_mac(mac_to_ua(mac)) should equal mac for random mac"""
        for _ in range(test_count):
            n = random.randrange(0, pow(2, 40))
            mac = format(n, "012x")
            self.assertEqual(mac, ua_to_mac(mac_to_ua(mac)))

    def test_invalid_mac(self):
        for _ in range(test_count):
            n = random.randrange(pow(2, 40), pow(2, 48))
            mac = format(n, "012x")
            self.assertRaises(ValueError, mac_to_ua, mac)

    def test_invalid_ua(self):
        for _ in range(test_count):
            n = random.randrange(pow(2, 40), pow(10, 13))
            s = format(n, "013")
            ua = "{}-{}-{}-{}".format(s[0: 3], s[3: 8], s[8: 13], "000")
            self.assertRaises(ValueError, ua_to_mac, ua)