# SCTE 55-1 Terminal Address Converters
[SCTE 55-1](http://scte.org/documents/pdf/Standards/ANSI_SCTE-55-1-2009.pdf) terminals (e.g. Motorola cable boxes and CableCARDs) are assigned a unique 40-bit identifier. This identifier is represented in one of two forms:

1. The "MAC address" format - a string of 12 hexadecimal digits, sometimes with colons (e.g. `00:00:00:00:00:00`)
2. The "Unit Address" - a string of 16 decimal digits with four dash-separated sections (e.g. `000-0000-0000-000`)

This module provides two functions, `mac_to_ua` and `ua_to_mac` that will convert between the two forms. See below for usage instructions

A suite of unit tests is also provided. The tests use known MAC / UA pairs to validate the functions and also test randomly-generated UAs and MACs.

# Explanation
To compute the MAC address from the unit address:

1. Drop the dashes from the string (e.g. `000-00004-47363-215` becomes `0000000447363215`)
2. Drop the last three digits, which are the checksum (`0000000447363`)
3. Interpret this string as a base-10 integer (`447363`)
4. Convert the base-10 integer to a base-16 integer with 12 digits (`00000006d383`)

Computing the Unit address from the MAC address is more difficult - the first 13 digits of the Unit address are given by converting the MAC address from hex to decimal. However, the last 3 digits are a [CRC](http://en.wikipedia.org/wiki/Cyclic_redundancy_check). The details of the computation are shown in the source for [terminal_address.py](terminal_address/scte_55_1_address.py)

## Installation and usage
Download the source package and run `setup.py install`. Then you can do:

```python
>>> import terminal_address
>>> terminal_address.ua_to_mac("000-00004-47363-215")
'00000006d383'
>>> terminal_address.mac_to_ua("00000006d383")
'000-00004-47363-215'
```

## Contact the author
I wrote this tool to save myself time - the Arris/Motorola DAC, NC1500, and NC2000 require a UA to locate a terminal, but the SeaChange Axiom VOD back office requires a MAC address. It's very difficult to compute the UA from the MAC by hand.

E-mail Bo Bayles (bbayles@gmail.com) with questions and feature suggestions.
