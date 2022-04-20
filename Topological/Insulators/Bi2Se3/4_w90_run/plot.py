import pandas as pd
from pymatgen.io.vasp.outputs import Vasprun
import matplotlib.pyplot as plt

def plot_wannier_fitting(dft,w90,E_Fermi,labels,gap=0,title=None):
    plt.figure()
    plt.scatter(dft['#k-distance'], dft['eigenvalue[eV]'], s = 10, label = 'DFT')
    plt.scatter(w90[0], w90[1] - E_Fermi + 0.5*gap, s = 1, label = 'Wannier', color = 'orange')
    plt.ylim(min(w90[1]-E_Fermi+0.5*gap), max(w90[1]-E_Fermi+ 0.5*gap))
    plt.xlim(min(dft['#k-distance']),max(dft['#k-distance']))
    leg = plt.legend()
    leg.legendHandles[0]._sizes = [30]
    leg.legendHandles[1]._sizes = [30]
    plt.axhline(color = 'black')
    plt.ylabel('Energy (eV)')
    if title:
        plt.title(title)
    plt.xticks(labels[0], labels[1])
    for pos in labels[0]:
        plt.axvline(pos, color = 'black', ls = '--', alpha = 0.5)
    plt.savefig('wannier.png', dpi = 300)

band_data = Vasprun('../2_bands/vasprun.xml').get_band_structure()
dft_bands = pd.read_table('../2_bands/band.dat', sep = '\s+')
wannier_bands = pd.read_table('wannier90_band.dat', sep = '\s+', header = None)
k_labels = pd.read_table('../2_bands/sumo-bandplot.log', sep = ':', header = None, skiprows=[0,1])

plot_wannier_fitting(dft_bands,wannier_bands,band_data.efermi,k_labels,band_data.get_band_gap()['energy'],title=r'Bi$_2$Se$_3$')
