# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 19:33:54 2018

@author: edup_
"""

from Product import * 

def test_recalculate_potato():
    potato = Product("potato",3)
    recalculate_quality(potato)
    assert potato.quality == 2.5
    
def test_recalculate_cheese():
    cheese = Product("cheese",5)
    recalculate_quality(cheese)
    assert cheese.quality == 3
    
def test_recalculate_other_product():
    watermelon = Product("watermelon",9000)
    recalculate_quality(watermelon)
    assert watermelon.quality == 9000

def test_recalculate_whatever():
    whatever = Product("nothing",0)
    recalculate_quality(whatever)
    assert watever.quality == 0
    