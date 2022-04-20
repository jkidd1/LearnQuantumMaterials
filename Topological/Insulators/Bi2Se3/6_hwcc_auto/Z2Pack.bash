#!/bin/bash
#SBATCH -J Bi2Se3    
#SBATCH -o output   
#SBATCH -e error   
#SBATCH -N 1          
#SBATCH -n 12    
#SBATCH -t 01:00:00 

date
python hwcc.py
date
