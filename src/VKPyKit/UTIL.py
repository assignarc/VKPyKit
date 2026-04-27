import os
import matplotlib.pyplot as plt
import numpy as np
from VKPyKit.VKPy import *
from IPython.display import display, HTML
import cv2  
try:
    from cv2.typing import MatLike
except (ImportError, AttributeError):
    from typing import Any
    MatLike = Any
import tensorflow as tf
import warnings
warnings.filterwarnings("ignore")
import torch
import keras



class UTIL(VKPy):
    
    def __init__(self): 
        super().__init__()
        pass

  
    """
    Display Images
    """ 

    @staticmethod
    def display_image(img: MatLike) -> None:
        """
        Display an image with OpenCV
        """
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)) 
        plt.axis('off')
        plt.show()

    """
    Print Line
    """
    @staticmethod
    def printline(length: int = 0) -> None:
        """
        Print a line of dashes
        length: length of the line (default is 100)
        return: None
        """
        if length == 0:
            print("-" * UTIL.NUMBER_OF_DASHES)
        else:
            print("-" * length)

    # END OF PRINT LINE FUNCTION

    @staticmethod
    def setseed(seed: int = VKPy.RANDOM_STATE):
        """ Set seeds for common libraries
        Many machine learning algorithms and data processing steps 
        (like train-test splits or neural network weight initialization) 
        rely on random number generators. If the seed is not set, 
        every run will produce slightly different results, 
        making debugging and comparison difficult

        seed: int = 42
        """
        UTIL.RANDOM_STATE = seed
        UTIL.printline()
        print(f"Setting seed to {seed} - RANDOM, np.random")        
        random.seed(UTIL.RANDOM_STATE)
        np.random.seed(UTIL.RANDOM_STATE)

        UTIL.printline()
        print("Setting seed for TensorFlow/Keras")
        # For TensorFlow/Keras (if available)
        try:
            import tensorflow as tf
            print(f"Setting seed to {seed} - tf.random")   
            tf.random.set_seed(UTIL.RANDOM_STATE)

            print(f"Setting seed to {seed} - tf.keras.utils")   
            tf.keras.utils.set_random_seed(UTIL.RANDOM_STATE)

            print(f"Enabling - tf.config.experimental.enable_op_determinism")   
            tf.config.experimental.enable_op_determinism()  
            
        except ImportError:
            pass  # TensorFlow not installed

        # For PyTorch (if available)
        try:
            import torch
            torch.manual_seed(UTIL.RANDOM_STATE)
            if torch.cuda.is_available():
                print(f"Setting seed to {seed} - torch.cuda")   
                torch.cuda.manual_seed(UTIL.RANDOM_STATE)
            if torch.backends.mps.is_available():
                print(f"Setting seed to {seed} - torch.mps")   
                torch.mps.manual_seed(UTIL.RANDOM_STATE)
        except ImportError:
            pass  # PyTorch not installed
        
        UTIL.printline()

    # END OF DISPLAY IMAGE FUNCTION
    @staticmethod
    def check_gpu_availability() -> None:
        """
        Check GPU availability
        """
        UTIL.printline()
        print("Checking GPU Availability")
        UTIL.printline()
        
        # Set Keras backend to torch
        os.environ["KERAS_BACKEND"] = "torch"
      

        name = ""
        device_count = 0
        # Identify primary device
        if torch.cuda.is_available():
            device = torch.device("cuda")
            name = torch.cuda.get_device_name(0)
            device_count = torch.cuda.device_count()
        elif torch.backends.mps.is_available():
            device = torch.device("mps")
            name = "Apple Silicon - MPS"
            device_count = torch.mps.device_count()
        else:
            device = torch.device("cpu")
            name = "CPU"
            device_count = torch.cpu.device_count()

        print(f"Active Keras/Torch Device: {name} - {device}")
        print(f"Active Device Count: {device_count}")
        print(f"TensorFlow Version: {tf.__version__}")
        UTIL.printline()
        
