from abc import ABC, abstractmethod
import numpy as np
import random
class VKPy:

    def __init__(self):
        pass

    RANDOM_STATE = 42
    NUMBER_OF_DASHES = 100
    

    def __str__(self):
        return (f"VKPy : RANDOM_STATE = {VKPy.RANDOM_STATE} | DASHES ={VKPy.NUMBER_OF_DASHES}")
    
    