import z2pack

vasp = '/home/SOFTWARE/vasp.6.2_w90.3.1/vasp_ncl'

system = z2pack.fp.System(
    input_files=['input/INCAR', 'input/POSCAR', 'input/POTCAR', 'input/CHGCAR'],
    kpt_fct=z2pack.fp.kpoint.vasp,
    kpt_path='KPOINTS',
    command='mpirun {} > result.vasp'.format(vasp)
)

kx = [0, 0.5]
inv = dict()

for k in kx:
    result = z2pack.surface.run(
        system = system,
        surface = lambda s, t: [k, s/2, t], 
        save_file = './data/result_kx_{}.p'.format(k)
    )
    inv[k] = z2pack.invariant.z2(result)

with open('invariant', 'w') as f:
    f.write('\n'.join(['Z2 topological invariant at kx = {}: {}'.format(k, inv[k]) for k in kx]))
