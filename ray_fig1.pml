set light_count,1
set spec_count,1
set shininess, 10
set specular, 0
set ambient,0.5
set direct,0
set cartoon_side_chain_helper, 1
set reflect,1.5
set ray_shadow_decay_factor, 0.1
set ray_shadow_decay_range, 2
#set ray_trace_mode, 1
set ray_shadow, on
set cartoon_loop_radius, 0.35
set cartoon_loop_radius, 0.35
set cartoon_oval_width, 0.5
#cartoon tube
set cartoon_tube_radius, 1.0
set cartoon_smooth_loops
set ray_trace_mode, 3
set ray_trace_gain, 0.1
set antialias, 3
set ray_trace_color, black
set ray_trace_disco_factor, 1.0
set ray_transparency_contrast, 2.0

#load mounts/rdd48/pdbs_worms/production_runs/fc_binders/t32/tetra_dhr_noHfuse/config_tetra_dhr_n4_1l6x-scad-renum-fuse_ex254_en14_EXT6-DHR70_ex129_en7_tj04C3_int5v2__ABAB_0.49_36_4_2_ASU.pdb
#remove resi 1-207 and config_tetra_dhr_n4_1l6x-scad-renum-fuse_ex254_en14_EXT6-DHR70_ex129_en7_tj04C3_int5v2__ABAB_0.49_36_4_2_ASU
#show sti, !hydr and resi 337+381+378+333
#color white, resi 1-254 and chain A
#color grey70, resi 255-370 and chain A
#color grey40, resi 371-999 and chain A
#set cartoon_tube_radius, 0.5 #for insert close-up
#set cartoon_tube_radius, 0.8 #for building block library