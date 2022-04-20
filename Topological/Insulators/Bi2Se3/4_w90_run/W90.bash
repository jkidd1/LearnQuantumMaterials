#!/bin/bash
#SBATCH -J Bi2Se3     
#SBATCH -o output   
#SBATCH -e error  
#SBATCH -N 1          
#SBATCH -n 12
#SBATCH -t 01:00:00 

w90=/home/SOFTWARE/wannier90-3.1.0/wannier90.x

date
mpirun -np 12 $w90 wannier90
date
