# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 16:47:22 2021

@author: sigve
"""

class Question:
    def __init__(self,ask="", alt=[], rikt=""):
        self.ask = ask
        self.alt = alt
        self.rikt = rikt


    def __str__(self):
        return(f"{self.ask},{self.alt}")
    
    
    def __repr__(self):
        return print(f"{self.ask},self.alt")