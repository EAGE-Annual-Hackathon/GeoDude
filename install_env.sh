#!/bin/bash
# 
# Installer for package
# 
# Run: ./install.sh
# 


echo 'Creating geodude environment'

# create conda env
conda env create -f environment.yml
source ~/miniconda3/etc/profile.d/conda.sh
conda activate geodude
conda env list
echo 'Created and activated environment:' $(which python)

# check cupy works as expected
echo 'Checking numpy version and running a command...'
python -c 'import numpy as np; np.ones(10)'

echo 'Done!'

