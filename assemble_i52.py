import pymol

cmd.do('set matrix_mode, 1')
cmd.do('set movie_panel, 0')
cmd.do('set cache_frames, 0')
cmd.do('set movie_auto_interpolate, 1')

cmd.do('load /Users/robbydivine/Desktop/baker_lab/pymol_movies/tools_hold.py')
cmd.do('load /Users/robbydivine/Desktop/baker_lab/pymol_movies/blob.py')
cmd.do('load /Users/robbydivine/Desktop/baker_lab/pymol_movies/fc_tools.py')

cmd.do('load ~/Desktop/pdbs/i52.3.pdb')

cmd.do('load ~/Desktop/manuscript/fig1_all/ray_fig1.pml')
cmd.do('set ray_trace_mode, 1')
cmd.do('set specular, 0')

cmd.do('i52_axes')

cmd.do('separate_i52')

cmd.do('blob_tester pentamer*')
cmd.do('blob_tester dimer*')

cmd.do('blow_up_i52 pentamer*, intensity=250, blob=1')
cmd.do('blow_up_i52 dimer*, intensity=250, blob=1')
cmd.do('blow_up_i52 pentamer*, intensity=250')
cmd.do('blow_up_i52 dimer*, intensity=250')

cmd.do('hide car')

cmd.do('color 0x4e0aad, blob_*_dimer*')
cmd.do('color grey70, blob_*_pentamer*')

cmd.do("set dash_gap, 5")
cmd.do('bg_color white')

cmd.do('set cartoon_cylindrical_helices, 1')
cmd.do('color 0x82fff7, resi 1-326')
cmd.do('color 0x1dcf63, resi 327-497')
cmd.do('color grey70, resi 498-999')

cmd.do('set_view (\
    -0.131515414,   -0.257548779,    0.957274497,\
     0.989961624,    0.016287819,    0.140387312,\
    -0.051747192,    0.966126144,    0.252819508,\
    -0.000130195,   -0.000194728, -1470.225341797,\
    81.474494934,   30.998931885,   17.546806335,\
  1055.401611328, 1885.044921875,  -20.000000000 )')

cmd.do('hide surf, blob*')


cmd.do('mset 1 x 120')
cmd.do('frame 1')
cmd.do('hide surf, blob*')
cmd.do('mview store, object=*')
cmd.do('scene 001, store')
cmd.do('mview store, scene=001')

cmd.do('frame 30')
cmd.do('hide cgo, *')
cmd.do('show cgo, axes_ABCDE_i52.3')
# cmd.do('show surf, blob_A_pentamer_ABCDE_i52.3')
# cmd.do('show surf, blob_B_pentamer_ABCDE_i52.3')
# cmd.do('show surf, blob_C_pentamer_ABCDE_i52.3')
# cmd.do('show surf, blob_E_pentamer_ABCDE_i52.3')
cmd.do('show surf, blob_*_pentamer_ABCDE_i52.3')
cmd.do('set transparency, 0.67, blob_D_pentamer_ABCDE_i52.3')
cmd.do('show car, chain D and pentamer_ABCDE_i52.3 and resi 208-999')
cmd.do('blow_up_i52 pentamer_ABCDE_i52.3, intensity=-250, blob=1')
cmd.do('blow_up_i52 pentamer_ABCDE_i52.3, intensity=-250')
cmd.do('show cgo, axes_DM_i52.3')
cmd.do('show surf, blob_*_dimer_DM_i52.3')
cmd.do('blow_up_i52 dimer_DM_i52.3, intensity=-250, blob=1')
cmd.do('mview store, object=*')
cmd.do('scene 002, store')
cmd.do('mview store, scene=002')

cmd.do('frame 45')
cmd.do('show car, chain D and pentamer_ABCDE_i52.3 and resi 208-999')
# cmd.do('show surf, blob_D_pentamer_ABCDE_i52.3')
# cmd.do('set transparency, 0.75, blob_D_pentamer_ABCDE_i52.3')
cmd.do('mview store, object=*')
cmd.do('scene 003, store')
cmd.do('mview store, scene=003')

cmd.do('frame 90')
cmd.do('show cgo, axes_*')
cmd.do('show surf, blob*')
# cmd.do('hide surf, blob_L_dimer*')
# cmd.do('hide surf, blob_R_dimer*')
cmd.do('show car, chain D and pentamer_ABCDE_i52.3 and resi 208-999')

c5_list = ['Z0123', 'FGHIJ', 'KLMNO', 'PQRST', 'UVWXY']
for i in c5_list:
    cmd.do(f'blow_up_i52 pentamer_{i}_i52.3, intensity=-250, blob=1')
    cmd.do(f'blow_up_i52 pentamer_{i}_i52.3_copy, intensity=-250, blob=1')
cmd.do('blow_up_i52 pentamer_ABCDE_i52.3_copy, intensity=-250, blob=1')

c2_list = ['A3', 'BT', 'CI', 'EX', 'GY', 'HO', 'N1', 'Q2', 'SU', 'LL', 'JK', 'KJ', 'FZ', 'ZF', '0W', 'PV', 'RR', 'VP', 'W0']
for i in c2_list:
    cmd.do(f'blow_up_i52 dimer_{i}_i52.3, intensity=-250, blob=1')
    cmd.do(f'blow_up_i52 dimer_{i}_i52.3_copy, intensity=-250, blob=1')
cmd.do('blow_up_i52 dimer_DM_i52.3_copy, intensity=-250, blob=1')

cmd.do('mview store, object=*')
cmd.do('scene 004, store')
cmd.do('mview store, scene=004')

cmd.do('frame 120')
cmd.do('show cgo, axes_*')
cmd.do('show surf, blob*')
cmd.do('show car, chain D and pentamer_ABCDE_i52.3 and resi 208-999')
cmd.do('set transparency, 0.67, blob_D_pentamer_ABCDE_i52.3')
cmd.do('set_view (\
     0.147241771,    0.266855001,   -0.952422738,\
    -0.988714516,    0.012798435,   -0.149264723,\
    -0.027643824,    0.963650227,    0.265727371,\
     0.000132066,    0.000054598, -1638.755615234,\
    59.473110199,   -4.465154171,  -21.272539139,\
  1132.746948242, 2144.753417969,  -20.000000000 )')
cmd.do('mview store, object=*')
cmd.do('scene 005, store')
cmd.do('mview store, scene=005')

cmd.do('mview reinterpolate')

cmd.do('mplay')