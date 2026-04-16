import numpy as np
import mymodule

signal = np.random.randn(1000)
smoothed = mymodule.gaussian_smooth(signal, sigma=3.0)