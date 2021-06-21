from pymol import cmd
import glob

def blob():
	cmd.do("remove hydro")
	cmd.do("hide lines")
	cmd.do("set surface_quality, 1")
	cmd.do("alter all, b=50")
	cmd.do("alter all, q=1")
	cmd.do("set gaussian_resolution,15")
	cmd.do("create c1, resi 1-207")
	cmd.do("create c2, resi 208-999")

	cmd.do("map_new map_fc, gaussian, 1, (c1 and name CA), 10")
	cmd.do("isosurface fc_blob, map_fc")
	cmd.do("color slate, fc_blob")

	cmd.do("map_new map_design, gaussian, 1, (c2 and name CA), 10")
	cmd.do("isosurface design_blob, map_design")
	cmd.do("color grey90, design_blob")

	cmd.do("set antialias, 2")
	cmd.do("set ray_trace_gain, 0.4")
	cmd.do("set ray_shadows, 0")
	cmd.do("set specular, 0")


def blob_each(design_name):
	#chain_names = cmd.do("get_chains " + design_name)
	#for ch in cmd.get_chains(design_name):
	#	print(ch)
	cmd.do("remove hydro")
	cmd.do("hide lines")
	cmd.do("set surface_quality, 1")
	cmd.do("alter all, b=50")
	cmd.do("alter all, q=1")
	cmd.do("set gaussian_resolution,15")
	for chain_id in cmd.get_chains(design_name):
		#cmd.do("create copy_" + chain_id + ", " + design_name + " and chain " + chain_id)
		cmd.do("map_new map_" + chain_id + "_" + design_name + ", gaussian, 1, (" + design_name + " and chain " + chain_id + " and name CA), 10")
		cmd.do("isosurface blob_" + chain_id + "_" + design_name + ", map_" + chain_id + "_" + design_name)

	cmd.do("set ray_trace_mode, 3")
	cmd.do("set antialias, 2")
	cmd.do("set ray_trace_color, black")
	cmd.do("set ray_trace_gain, 0.1")
	cmd.do("set ray_shadows, 0")
	cmd.do("set specular, 0")

def blob_everything():
	#chain_names = cmd.do("get_chains " + design_name)
	#for ch in cmd.get_chains(design_name):
	#	print(ch)
	cmd.do("remove hydro")
	cmd.do("hide lines")
	cmd.do("set surface_quality, 1")
	cmd.do("alter all, b=50")
	cmd.do("alter all, q=1")
	cmd.do("set gaussian_resolution,15")
	for design_name in cmd.get_names("all"):
		for chain_id in cmd.get_chains(design_name):
			#cmd.do("create copy_" + chain_id + ", " + design_name + " and chain " + chain_id)
			cmd.do("map_new map_" + chain_id + "_" + design_name + ", gaussian, 1, (" + design_name + " and chain " + chain_id + " and name CA), 10")
			cmd.do("isosurface blob_" + chain_id + "_" + design_name + ", map_" + chain_id + "_" + design_name)

	cmd.do("set ray_trace_mode, 3")
	cmd.do("set antialias, 2")
	cmd.do("set ray_trace_color, black")
	cmd.do("set ray_trace_gain, 0.1")
	cmd.do("set ray_shadows, 0")
	cmd.do("set specular, 0")

def blob_abc_2(abc_name):
	#chain_names = cmd.do("get_chains " + design_name)
	#for ch in cmd.get_chains(design_name):
	#	print(ch)
	cutoff_dict = {"d2.4": 307, "t4_r1": 254, "t.8": 246, "o42.1": 253, "i52.3": 326}
	cmd.do("remove hydro")
	cmd.do("hide lines")
	cmd.do("set surface_quality, 1")
	cmd.do("alter all, b=50")
	cmd.do("alter all, q=1")
	cmd.do("set gaussian_resolution,15")
	for design_name in cmd.get_names("all"):
		if abc_name in design_name:
			cutoff = cutoff_dict[abc_name]
			cutoff_plus_one = str(int(cutoff) + 1)
			for chain_id in cmd.get_chains(design_name):
				#cmd.do("create " + chain_id + "_" + abc_name + "_bind, resi 208-" + cutoff + " and " + abc_name + " and chain " + chain_id)
				cmd.do("create {chain_id}_{abc_name}_fc, resi 1-207 and {abc_name} and chain {chain_id}".format(chain_id=chain_id, abc_name=abc_name))
				cmd.do("create {chain_id}_{abc_name}_bind, resi 208-{cutoff} and {abc_name} and chain {chain_id}".format(chain_id=chain_id, abc_name=abc_name, cutoff=cutoff))
				cmd.do("create {chain_id}_{abc_name}_nobind, resi {cutoff_plus_one}-999 and {abc_name} and chain {chain_id}".format(chain_id=chain_id, abc_name=abc_name, cutoff_plus_one=cutoff_plus_one))
				cmd.do("map_new map_{chain_id}_{abc_name}_bind, gaussian, 1, ({chain_id}_{abc_name}_bind and chain {chain_id} and name CA), 10".format(chain_id=chain_id, abc_name=abc_name))
				cmd.do("isosurface blob_{chain_id}_{abc_name}_bind, map_{chain_id}_{abc_name}_bind".format(chain_id=chain_id, abc_name=abc_name))
				cmd.do("map_new map_{chain_id}_{abc_name}_nobind, gaussian, 1, ({chain_id}_{abc_name}_nobind and chain {chain_id} and name CA), 10".format(chain_id=chain_id, abc_name=abc_name))
				cmd.do("isosurface blob_{chain_id}_{abc_name}_nobind, map_{chain_id}_{abc_name}_nobind".format(chain_id=chain_id, abc_name=abc_name))
				cmd.do("map_new map_{chain_id}_{abc_name}_fc, gaussian, 1, ({chain_id}_{abc_name}_fc and chain {chain_id} and name CA), 10".format(chain_id=chain_id, abc_name=abc_name))
				cmd.do("isosurface blob_{chain_id}_{abc_name}_fc, map_{chain_id}_{abc_name}_fc".format(chain_id=chain_id, abc_name=abc_name))

		else:
			for chain_id in cmd.get_chains(design_name):
				#cmd.do("create copy_" + chain_id + ", " + design_name + " and chain " + chain_id)
				cmd.do("map_new map_{chain_id}_{design_name}, gaussian, 1, ({design_name} and chain {chain_id} and name CA), 10".format(chain_id=chain_id, design_name=design_name))
				cmd.do("isosurface blob_{chain_id}_{design_name}, map_{chain_id}_{design_name}".format(chain_id=chain_id, design_name=design_name))


def blob_abc_3(abc_name):
	#chain_names = cmd.do("get_chains " + design_name)
	#for ch in cmd.get_chains(design_name):
	#	print(ch)
	cutoff_dict = {"d2.4": 307, "t4_r1": [254, 369], "t.8": 246, "o42.1": 253, "i52.3": 326}
	cmd.do("remove hydro")
	cmd.do("hide lines")
	cmd.do("set surface_quality, 1")
	cmd.do("alter all, b=50")
	cmd.do("alter all, q=1")
	cmd.do("set gaussian_resolution,15")
	for design_name in cmd.get_names("all"):
		if abc_name in design_name:
			cutoff = cutoff_dict[abc_name][0]
			cutoff_plus_one = str(int(cutoff) + 1)
			cutoff_2 = cutoff_dict[abc_name][1]
			cutoff_2_plus_one = str(int(cutoff_2) + 1)
			for chain_id in cmd.get_chains(design_name):
				#cmd.do("create " + chain_id + "_" + abc_name + "_bind, resi 208-" + cutoff + " and " + abc_name + " and chain " + chain_id)
				cmd.do("create {chain_id}_{abc_name}_bind, resi 208-{cutoff} and {abc_name} and chain {chain_id}".format(chain_id=chain_id, abc_name=abc_name, cutoff=cutoff))
				cmd.do("create {chain_id}_{abc_name}_nobind1, resi {cutoff_plus_one}-{cutoff_2} and {abc_name} and chain {chain_id}".format(chain_id=chain_id, abc_name=abc_name, cutoff_plus_one=cutoff_plus_one, cutoff_2=cutoff_2))
				cmd.do("create {chain_id}_{abc_name}_nobind2, resi {cutoff_2_plus_one}-999 and {abc_name} and chain {chain_id}".format(chain_id=chain_id, abc_name=abc_name, cutoff_2_plus_one=cutoff_2_plus_one))
				cmd.do("map_new map_{chain_id}_{abc_name}_bind, gaussian, 1, ({chain_id}_{abc_name}_bind and chain {chain_id} and name CA), 10".format(chain_id=chain_id, abc_name=abc_name))
				cmd.do("isosurface blob_{chain_id}_{abc_name}_bind, map_{chain_id}_{abc_name}_bind".format(chain_id=chain_id, abc_name=abc_name))
				cmd.do("map_new map_{chain_id}_{abc_name}_nobind1, gaussian, 1, ({chain_id}_{abc_name}_nobind1 and chain {chain_id} and name CA), 10".format(chain_id=chain_id, abc_name=abc_name))
				cmd.do("isosurface blob_{chain_id}_{abc_name}_nobind1, map_{chain_id}_{abc_name}_nobind1".format(chain_id=chain_id, abc_name=abc_name))
				cmd.do("map_new map_{chain_id}_{abc_name}_nobind2, gaussian, 1, ({chain_id}_{abc_name}_nobind2 and chain {chain_id} and name CA), 10".format(chain_id=chain_id, abc_name=abc_name))
				cmd.do("isosurface blob_{chain_id}_{abc_name}_nobind2, map_{chain_id}_{abc_name}_nobind2".format(chain_id=chain_id, abc_name=abc_name))

		else:
			for chain_id in cmd.get_chains(design_name):
				#cmd.do("create copy_" + chain_id + ", " + design_name + " and chain " + chain_id)
				cmd.do("map_new map_{chain_id}_{design_name}, gaussian, 1, ({design_name} and chain {chain_id} and name CA), 10".format(chain_id=chain_id, design_name=design_name))
				cmd.do("isosurface blob_{chain_id}_{design_name}, map_{chain_id}_{design_name}".format(chain_id=chain_id, design_name=design_name))

	cmd.do("set ray_trace_mode, 3")
	cmd.do("set antialias, 2")
	cmd.do("set ray_trace_color, black")
	cmd.do("set ray_trace_gain, 0.1")
	cmd.do("set ray_shadows, 0")
	cmd.do("set specular, 0")

def blob_fc(abc_name):

	cmd.do("remove hydro")
	cmd.do("hide lines")
	cmd.do("set surface_quality, 1")
	cmd.do("alter all, b=50")
	cmd.do("alter all, q=1")
	cmd.do("set gaussian_resolution,15")
	for chain_id in cmd.get_chains(abc_name):
		cmd.do("create {chain_id}_{abc_name}_fc, resi 1-207 and {abc_name} and chain {chain_id}".format(chain_id=chain_id, abc_name=abc_name))
		cmd.do("map_new map_{chain_id}_{abc_name}_fc, gaussian, 1, ({chain_id}_{abc_name}_fc and chain {chain_id} and name CA), 10".format(chain_id=chain_id, abc_name=abc_name))
		cmd.do("isosurface blob_{chain_id}_{abc_name}_fc, map_{chain_id}_{abc_name}_fc".format(chain_id=chain_id, abc_name=abc_name))
		cmd.do("create {chain_id}_{abc_name}_bind, resi 208-999 and {abc_name} and chain {chain_id}".format(chain_id=chain_id, abc_name=abc_name))
		cmd.do("map_new map_{chain_id}_{abc_name}_bind, gaussian, 1, ({chain_id}_{abc_name}_bind and chain {chain_id} and name CA), 10".format(chain_id=chain_id, abc_name=abc_name))
		cmd.do("isosurface blob_{chain_id}_{abc_name}_bind, map_{chain_id}_{abc_name}_bind".format(chain_id=chain_id, abc_name=abc_name))
	cmd.do("set ray_trace_mode, 3")
	cmd.do("set antialias, 2")
	cmd.do("set ray_trace_color, black")
	cmd.do("set ray_trace_gain, 0.1")
	cmd.do("set ray_shadows, 0")
	cmd.do("set specular, 0")

def igg_color():
	cmd.do("color grey70, blob_*")
	cmd.do("color slate, *_B_igg*")
	cmd.do("color slate, *_D_igg*")
	cmd.do("color lightblue, *_A_igg*")
	cmd.do("color lightblue, *_C_igg*")
	cmd.do("color magenta, *_bind*")

def blob_tester(designs):
	cmd.do("remove hydro")
	cmd.do("hide lines")
	cmd.do("set surface_quality, 1")
	cmd.do("alter all, b=50")
	cmd.do("alter all, q=1")
	cmd.do("set gaussian_resolution,15")

	designs = cmd.get_object_list(designs)
	for design_name in designs:
		print(design_name)
		for chain_id in cmd.get_chains(design_name):
			#cmd.do("create copy_" + chain_id + ", " + design_name + " and chain " + chain_id)
			cmd.do("map_new map_{chain_id}_{design_name}, gaussian, 1, ({design_name} and chain {chain_id} and name CA), 10".format(chain_id=chain_id, design_name=design_name))
			cmd.do("isosurface blob_{chain_id}_{design_name}, map_{chain_id}_{design_name}".format(chain_id=chain_id, design_name=design_name))

	# cmd.do("set ray_trace_mode, 3")
	# cmd.do("set antialias, 2")
	# cmd.do("set ray_trace_color, black")
	# cmd.do("set ray_trace_gain, 0.1")
	# cmd.do("set ray_shadows, 0")
	# cmd.do("set specular, 0")
	#cmd.do('hide car')
	#cmd.do('color grey70, *.*')
	#cmd.do('color slate, *_fcs')



cmd.extend( "blob", blob )
cmd.extend( "blob_each", blob_each )
cmd.extend( "blob_everything", blob_everything )
cmd.extend( "blob_abc_2", blob_abc_2 )
cmd.extend( "blob_abc_3", blob_abc_3)
cmd.extend( "blob_fc", blob_fc)
cmd.extend("igg_color", igg_color)
cmd.extend("blob_tester", blob_tester)

