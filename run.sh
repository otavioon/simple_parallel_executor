#!/bin/bash

# Location where configuration files will be searched for"
CONFIGSDIR="configs"
# Maximum number of parallel processes 
POOLSIZE=2

# Find all *yaml folder at configs directory. The script_to_run.py will be called with each file located at configs dir
find $CONFIGSDIR -type f -name "*.yaml" | xargs -P $POOLSIZE -I{} sh -c 'python script_to_run.py --config-file {} --output-dir output'
