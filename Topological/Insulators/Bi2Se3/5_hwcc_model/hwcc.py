import tbmodels
import z2pack

model = tbmodels.Model.from_wannier_files(
    hr_file='../4_w90_run/wannier90_hr.dat',
    wsvec_file='../4_w90_run/wannier90_wsvec.dat',
    xyz_file='../4_w90_run/wannier90_centres.xyz',
    win_file='../4_w90_run/wannier90.win',
    occ = 18
)
system = z2pack.tb.System(model)

lines = 101
dist = 0.001
kx = [0, 0.5]
inv = dict()

for k in kx:
    result = z2pack.surface.run(
        system = system,
        surface = lambda s, t: [k, s/2, t], 
        num_lines = lines,
        min_neighbour_dist = dist,
        save_file = './data/result_kx_{}.p'.format(k),
    )
    inv[k] = z2pack.invariant.z2(result)

with open('invariant', 'w') as f:
    f.write('\n'.join(['Z2 topological invariant at kx = {}: {}'.format(k, inv[k]) for k in kx]))
