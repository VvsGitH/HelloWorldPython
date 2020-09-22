# 1. [First Time Only] Create a Virtual Environment (VENV):
#       python -m venv .venv
#       In .venv/pyvenv.cfg set include-system-site-packages = true
# 2. Activate the VENV:
#       .venv\Scripts\Activate
# 2.1. [First Time Only] Update pip: 
#       python -m pip install -U pip
# 3. [First Time Only] Install matplotlib:
#       python -m pip install matplotlib
# 4. Deactivate VENV:
#       deactivate

# NOTE: VSCode automaticly run the code with the venv, without the need to activate it

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
plt.plot(x, np.sin(x))       # Plot the sine of each x point
plt.show()                   # Display the plot