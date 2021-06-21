import pymol

cmd.do('set matrix_mode, 1')
cmd.do('set movie_panel, 0')
cmd.do('set cache_frames, 0')
cmd.do('set movie_auto_interpolate, 1')

cmd.do('load /Users/robbydivine/Desktop/baker_lab/pymol_movies/tools_hold.py')
cmd.do('load /Users/robbydivine/Desktop/baker_lab/pymol_movies/blob.py')
cmd.do('load /Users/robbydivine/Desktop/baker_lab/pymol_movies/fc_tools.py')

cmd.do('load ~/Desktop/pdbs/t4_r1.pdb')

cmd.do('load ~/Desktop/manuscript/fig1_all/ray_fig1.pml')
cmd.do('set ray_trace_mode, 1')
cmd.do('set specular, 0')

cmd.do('t32_axes_movie')
cmd.do('separate_t32 t4_r1')

cmd.do('blob_tester trimer*')
cmd.do('blob_tester dimer*')

cmd.do('blow_up_t32 intensity=250, blob=1')
cmd.do('blow_up_t32 intensity=250')

cmd.do('hide car')

cmd.do('color 0x4e0aad, blob_*_dimer*')
cmd.do('color grey70, blob_*_trimer*')

cmd.do("set dash_gap, 5")
cmd.do('bg_color white')

cmd.do('set cartoon_cylindrical_helices, 1')
cmd.do('color 0x82fff7, resi 1-254')
cmd.do('color 0x1dcf63, resi 255-370')
cmd.do('color grey70, resi 371-999')

cmd.do('set_view (\
    -0.641666770,   -0.650284350,    0.406679451,\
     0.070790149,    0.477757126,    0.875635326,\
    -0.763705671,    0.590655327,   -0.260525882,\
     0.000047386,    0.000019491, -973.463623047,\
     7.212645531,   25.489572525,   14.876826286,\
  -43939.527343750, 45886.457031250,  -20.000000000 )')

cmd.do('hide surf, blob*')


cmd.do('mset 1 x 120')
cmd.do('frame 1')
cmd.do('hide surf, blob*')
cmd.do('mview store, object=*')
cmd.do('scene 001, store')
cmd.do('mview store, scene=001')

cmd.do('frame 30')
cmd.do('hide cgo, *')
cmd.do('show cgo, axes_DEF')
cmd.do('show surf, blob_*_trimer_DEF')
cmd.do('set transparency, 0.67, blob_F_trimer*,')
cmd.do('show car, chain F and trimer_DEF and resi 208-999')
cmd.do('blow_up_t32 trimer_DEF, intensity=-250, blob=1')
cmd.do('blow_up_t32 trimer_DEF, intensity=-250')
cmd.do('show cgo, axes_FJ')
cmd.do('show surf, blob_*_dimer_FJ')
cmd.do('blow_up_t32 dimer_FJ, intensity=-250, blob=1')
cmd.do('mview store, object=*')
cmd.do('scene 002, store')
cmd.do('mview store, scene=002')

cmd.do('frame 45')
cmd.do('show car, chain F and trimer_DEF and resi 208-999')
cmd.do('mview store, object=*')
cmd.do('scene 003, store')
cmd.do('mview store, scene=003')

cmd.do('frame 90')
cmd.do('show cgo, axes_*')
cmd.do('show surf, blob*')
cmd.do('show car, chain F and trimer_DEF and resi 208-999')
cmd.do('blow_up_t32 trimer_ABC, intensity=-250, blob=1')
cmd.do('blow_up_t32 trimer_GHI, intensity=-250, blob=1')
cmd.do('blow_up_t32 trimer_JKL, intensity=-250, blob=1')
cmd.do('blow_up_t32 dimer_AK, intensity=-250, blob=1')
cmd.do('blow_up_t32 dimer_BE, intensity=-250, blob=1')
cmd.do('blow_up_t32 dimer_CI, intensity=-250, blob=1')
cmd.do('blow_up_t32 dimer_DH, intensity=-250, blob=1')
cmd.do('blow_up_t32 dimer_GL, intensity=-250, blob=1')
cmd.do('mview store, object=*')
cmd.do('scene 004, store')
cmd.do('mview store, scene=004')

cmd.do('frame 120')
cmd.do('show cgo, axes_*')
cmd.do('show surf, blob*')
cmd.do('show car, chain F and trimer_DEF and resi 208-999')
cmd.do('set transparency, 0.67, blob_F_trimer*,')
cmd.do('set_view (\
    -0.498390347,   -0.435399890,   -0.749685526,\
    -0.812705696,    0.535724759,    0.229149461,\
     0.301852107,    0.723479450,   -0.620852470,\
     0.000047386,    0.000019491, -973.463623047,\
     7.212645531,   25.489572525,   14.876826286,\
  -8365.519531250, 10312.447265625,  -20.000000000 )')
cmd.do('mview store, object=*')
cmd.do('scene 005, store')
cmd.do('mview store, scene=005')

cmd.do('mview reinterpolate')

cmd.do('mplay')