import pymol
from random import random
# import sys

# first_frame = sys.argv[3]
# last_frame = sys.argv[4]

cmd.do('reinitialize')
cmd.do('set matrix_mode, 1')
cmd.do('set movie_panel, 0')
cmd.do('set cache_frames, 0')
cmd.do('set movie_auto_interpolate, 1')

cmd.do('load ~/Desktop/manuscript/fig1_all/ray_fig1.pml')
cmd.do('set ray_trace_mode, 1')
cmd.do('set ray_trace_gain, 0.1')

cmd.do('load ~/Desktop/baker_lab/pymol_movies/tools_hold.py')
cmd.do('load ~/Desktop/baker_lab/pymol_movies/blob.py')
cmd.do('load ~/Desktop/baker_lab/pymol_movies/fc_tools.py')
cmd.do('load ~/Desktop/pdbs/d2.4.pdb')

for i in range(1,6):
	cmd.do(f'create c{i}, d2.4')

rotations = [
['60', '60', '60'], 
['30', '30', '30'],
['90', '120', '30'],
['45', '45', '45'],
['120', '120', '150']
]

translations = [
[-450, 50, 100],
[450, 100, -30],
[10, -400, 250],
[-10, 450, -20],
[90, -90, -400],
]

axes = 'xyz'

cmd.do('create c0, d2.4')
cmd.do('delete d2.4')

for i in range(6):
	cmd.do(f'create fc_ab_c{i}, c{i} and resi 1-207 and chain A+B')
	cmd.do(f'create fc_cd_c{i}, c{i} and resi 1-207 and chain C+D')
	cmd.do(f'create design_ad_c{i}, c{i} and resi 208-999 and chain A+D')
	cmd.do(f'create design_bc_c{i}, c{i} and resi 208-999 and chain B+C')
	cmd.do(f'delete c{i}')

cmd.do('blob_tester *')

design_names = ['blob_*_fc_ab_c', 'blob_*_fc_cd_c', 'blob_*_design_ad_c', 'blob_*_design_bc_c']

for i in range(5):
	for j in range(3):
		for k in range(4):
			cmd.do(f'rotate {axes[j]}, {rotations[i][j]}, object={design_names[k]}{i+1}, camera=0, origin=[0,0,0]')
			cmd.do(f'translate {translations[i]}, object={design_names[k]}{i+1}, camera=0')

cmd.do('color purpleblue, blob_*_fc*')
cmd.do('color grey70, blob_*_design*')
cmd.do('bg_color white')

cmd.do('hide car')
# cmd.do('color slate, fc*')
# cmd.do('color grey80, design*')
# cmd.do('bg_color white')

cmd.do('set_view (\
     0.978465617,   -0.030679079,   -0.204117626,\
    -0.201946869,    0.062263336,   -0.977414191,\
     0.042695265,    0.997585535,    0.054726265,\
     0.000003539,    0.000040770, -5081.196777344,\
    33.189281464,   -6.090503216,   10.941041946,\
  -197887.734375000, 208050.078125000,  -20.000000000 )')

# cmd.do('show surf, blob_*_fc_*')


cmd.do('mset 1 x 10')
cmd.do('frame 1')
# cmd.do('show surf, blob_*_fc_*')
cmd.do('mview store, object=*')

cmd.do('frame 9')
cmd.do('mview store, object=*')

last_frame = 140

for x in range(10, last_frame+1):
	cmd.madd("1 x1")
	cmd.frame(x)
	cmd.do('mview store, object=*')

	if x < 20:
		step = 2
	elif x < 40:
		step = 3
	elif x < 60:
		step = 4
	elif x < 80:
		step = 5
	elif x < 100:
		step = 6

	for j in range(3):
		for k in range(4):
			translations = [((random() - 0.5) * 30) for t in range(3)]
			cmd.do(f'translate {translations}, object={design_names[k]}0, camera=0')

			for i in range(step):
				xyz_rot = [((random() - 0.5) * 5) for y in range(3)]
				#xyz_trans = [(random() * 10) for i in range(3)]

				cmd.do(f'rotate {axes[j]}, {xyz_rot[j]}, object={design_names[k]}{i}, camera=0, origin=[0,0,0]')
				#cmd.do(f'translate {xyz_trans[j]}, object={design_names[k]}{i+1}, camera=0')
	# if  x == last_frame - 21:
	# 	cmd.do('show surf, blob_*_fc_*')
	# elif x > last_frame - 20:
	# 	cmd.do('hide surf, blob_*_fc_*')
	
cmd.mplay()

# cmd.do(f'mpng /Users/robbydivine/Desktop/baker_lab/pymol_movies/png_out/assemble_d2_, mode=1, modal=-1, first={first_frame}, last={last_frame}')