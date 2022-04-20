#!/bin/bash
#SBATCH -J Bi2Se3     
#SBATCH -o output   
#SBATCH -e error  
#SBATCH -N 1          
#SBATCH -n 12         
#SBATCH -t 01:00:00 

vasp=/home/SOFTWARE/vasp.6.2_w90.3.1/vasp_ncl

date
mpirun $vasp > result.vasp
date
