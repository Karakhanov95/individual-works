# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 23:20:18 2022

@author: Acer
"""

import phonenumbers
from phonenumbers import geocoder, carrier

phoneNumber = phonenumbers.parse("+998900000000")

Region = geocoder.description_for_number(phoneNumber, 'en')

print(Region)