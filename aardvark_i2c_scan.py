# -*- coding: utf-8 -*-
"""
Created on Fri May 12 15:50:13 2017

@author: Srinivas N

Description: This program scans for all I2C slaves (7bit address) connected to Aardvark and
prints them.

Dependency:
OS:Windows
Others: Aardvark Drivers should be intalled.
"""

import pyaardvark

try:
    #a = pyaardvark.open(serial_number='2237-988786')
    print "Aardvark Info below:"    
    print str(pyaardvark.find_devices())+'\n'
    
    a = pyaardvark.open(0)
    print "Scanning for I2C devices.."
    for i in range(0x00,0x7f): #0 t0 127
        data = a.i2c_master_write_read(i, '\x00',1)
        if data != '':
            print str(hex(i))+', '
        
    a.close()
    
    print "Scanning Completed"


except Exception as e:
    print "Exception occured"
    print str(e)
    raw_input()
    a.close()

