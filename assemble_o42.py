import pymol

cmd.do('set matrix_mode, 1')
cmd.do('set movie_panel, 0')
cmd.do('set cache_frames, 0')
cmd.do('set movie_auto_interpolate, 1')

cmd.do('load /Users/robbydivine/Desktop/baker_lab/pymol_movies/tools_hold.py')
cmd.do('load /Users/robbydivine/Desktop/baker_lab/pymol_movies/blob.py')
cmd.do('load /Users/robbydivine/Desktop/baker_lab/pymol_movies/fc_tools.py')

cmd.do('load ~/Desktop/pdbs/o42.1.pdb')

cmd.do('load ~/Desktop/manuscript/fig1_all/ray_fig1.pml')
cmd.do('set ray_trace_mode, 1')
cmd.do('set specular, 0')

cmd.do('o42_axes')

cmd.do('separate_o42')

cmd.do('blob_tester tetramer*')
cmd.do('blob_tester dimer*')

cmd.do('blow_up_o42 intensity=250, blob=1')
cmd.do('blow_up_o42 intensity=250')

cmd.do('hide car')

cmd.do('color 0x4e0aad, blob_*_dimer*')
cmd.do('color grey70, blob_*_tetramer*')

cmd.do("set dash_gap, 5")
cmd.do('bg_color white')

cmd.do('delete dist_1_2')
cmd.do('delete dist_4_5')

cmd.do('set cartoon_cylindrical_helices, 1')
cmd.do('color 0x82fff7, resi 1-253')
cmd.do('color 0x1dcf63, resi 254-464')
cmd.do('color grey70, resi 465-999')

cmd.do('set_view (\
     0.306149542,   -0.217816353,    0.926728010,\
     0.003380827,    0.973710716,    0.227743894,\
    -0.951977074,   -0.066589564,    0.298838854,\
     0.000026464,   -0.000099063, -1364.569335938,\
   -40.643161774,   -6.943825722,  -40.796363831,\
   916.553894043, 1812.603515625,  -20.000000000 )')

cmd.do('hide surf, blob*')


cmd.do('mset 1 x 120')
cmd.do('frame 1')
cmd.do('hide surf, blob*')
cmd.do('mview store, object=*')
cmd.do('scene 001, store')
cmd.do('mview store, scene=001')

cmd.do('frame 30')
cmd.do('hide cgo, *')
cmd.do('show cgo, axes_ADHI')
cmd.do('show surf, blob_*_tetramer_ADHI')
cmd.do('set transparency, 0.67, blob_A_tetramer_ADHI')
cmd.do('show car, chain A and tetramer_ADHI and resi 208-999')
cmd.do('blow_up_o42 tetramer_ADHI, intensity=-250, blob=1')
cmd.do('blow_up_o42 tetramer_ADHI, intensity=-250')
cmd.do('show cgo, axes_AB')
cmd.do('show surf, blob_*_dimer_AB')
cmd.do('blow_up_o42 dimer_AB, intensity=-250, blob=1')
cmd.do('mview store, object=*')
cmd.do('scene 002, store')
cmd.do('mview store, scene=002')

cmd.do('frame 45')
# cmd.do('show cgo, axes_FJ')
# cmd.do('show surf, blob_*_dimer_FJ')
# cmd.do('blow_up_t32 dimer_FJ, intensity=-250, blob=1')
cmd.do('show car, chain A and tetramer_ADHI and resi 208-999')
cmd.do('mview store, object=*')
cmd.do('scene 003, store')
cmd.do('mview store, scene=003')

cmd.do('frame 90')
cmd.do('show cgo, axes_*')
cmd.do('show surf, blob*')
cmd.do('show car, chain A and tetramer_ADHI and resi 208-999')

c4_list = ['BEMP', 'CTRX', 'FKSU', 'GLNQ', 'JOVW']
for i in c4_list:
    cmd.do(f'blow_up_o42 tetramer_{i}, intensity=-250, blob=1')

c2_list = ['CD', 'EF', 'GH', 'IJ', 'KL', 'MN', 'OP', 'QR', 'ST', 'UV', 'WX']
for i in c2_list:
    cmd.do(f'blow_up_o42 dimer_{i}, intensity=-250, blob=1')

# cmd.do('blow_up_t32 tetramer_ABC, intensity=-250, blob=1')
# cmd.do('blow_up_t32 tetramer_GHI, intensity=-250, blob=1')
# cmd.do('blow_up_t32 tetramer_JKL, intensity=-250, blob=1')
# cmd.do('blow_up_t32 dimer_AK, intensity=-250, blob=1')
# cmd.do('blow_up_t32 dimer_BE, intensity=-250, blob=1')
# cmd.do('blow_up_t32 dimer_CI, intensity=-250, blob=1')
# cmd.do('blow_up_t32 dimer_DH, intensity=-250, blob=1')
# cmd.do('blow_up_t32 dimer_GL, intensity=-250, blob=1')
cmd.do('mview store, object=*')
cmd.do('scene 004, store')
cmd.do('mview store, scene=004')

cmd.do('frame 120')
cmd.do('show cgo, axes_*')
cmd.do('show surf, blob*')
cmd.do('show car, chain A and tetramer_ADHI and resi 208-999')
cmd.do('set transparency, 0.67, blob_A_tetramer_ADHI')
cmd.do('set_view (\
    -0.640276968,    0.171000034,   -0.748865306,\
    -0.009806752,    0.973003566,    0.230562642,\
     0.768079102,    0.154970258,   -0.621317685,\
    -0.000223279,   -0.000260368, -1288.383056641,\
   -59.361164093,   22.213443756,    2.795000076,\
   149.449874878, 2427.321044922,  -20.000000000 )')
cmd.do('mview store, object=*')
cmd.do('scene 005, store')
cmd.do('mview store, scene=005')

cmd.do('mview reinterpolate')

cmd.do('mplay')