import z2pack
import matplotlib.pyplot as plt 

kx = [0, 0.5]

for k in kx:
    result = z2pack.io.load('data/result_kx_{}.p'.format(k)) 
    plt.figure()
    z2pack.plot.wcc(
        result, 
        wcc_settings = {'s': 12.5,'alpha': 0.1, 'color': 'black'}
    )
    plt.title(r'$k_x={}$'.format(k))
    plt.ylabel('HWCC')
    plt.xlabel(r'$k$')
    plt.savefig('hwcc_kx={}.png'.format(k), bbox_inches = 'tight', dpi = 250)
    plt.close()
