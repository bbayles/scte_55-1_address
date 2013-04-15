# Unit Address / MAC Address converters for SCTE 55-1 terminals
# Unit tests module
from scte_55_1_address import mac_to_ua, ua_to_mac
import unittest
import random

class known_ua(unittest.TestCase):
  def test_known_ua(self):
    """mac_to_ua should give known result with known input"""
    for ua, mac in A_ua_mac:
      self.assertEqual(ua, mac_to_ua(mac))

class known_mac(unittest.TestCase):
  def test_known_mac(self):
    """ua_to_mac should give known result with known input"""
    for ua, mac in A_ua_mac:
      self.assertEqual(mac, ua_to_mac(ua))

class known_ua_roundtrip(unittest.TestCase):
  def test_known_ua_roundtrip(self):
    """mac_to_ua(ua_to_mac(ua)) should equal ua for known ua"""
    for ua, mac in A_ua_mac:
      self.assertEqual(ua, mac_to_ua(ua_to_mac(ua)))

class known_mac_roundtrip(unittest.TestCase):
  def test_known_mac_roundtrip(self):
    """ua_to_mac(mac_to_ua(mac)) should equal mac for known mac"""
    for ua, mac in A_ua_mac:
      self.assertEqual(mac, ua_to_mac(mac_to_ua(mac)))

class random_mac_roundtrip(unittest.TestCase):
  def test_random_mac_roundtrip(self):
    """ua_to_mac(mac_to_ua(mac)) should equal mac for random mac"""
    for _ in range(test_count):
      n = random.randrange(0, pow(2, 40))
      mac = format(n, "012x")
      self.assertEqual(mac, ua_to_mac(mac_to_ua(mac)))

class invalid_mac(unittest.TestCase):
  def test_invalid_mac(self):
    for _ in range(test_count):
      n = random.randrange(pow(2, 40), pow(2, 48))
      mac = format(n, "012x")
      self.assertRaises(ValueError, mac_to_ua, mac)

class invalid_ua(unittest.TestCase):
  def test_invalid_mac(self):
    for _ in range(test_count):
      n = random.randrange(pow(2, 40), pow(10, 13))
      s = format(n, "013")
      ua = "{}-{}-{}-{}".format(s[0: 3], s[3: 8], s[8: 13], "000")
      self.assertRaises(ValueError, ua_to_mac, ua)

if __name__ == "__main__":
  test_count = 1000
  # Load known values
  A_ua_mac = []
  with open("mac_ua_tests.csv") as infile:
    headers = next(infile)
    for line in infile:
      line = line.strip()
      ua, mac = line.split(',')
      A_ua_mac.append((ua, mac))
  
  unittest.main()