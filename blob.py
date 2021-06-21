from pymol import cmd
import glob

'''
This script is used to create marshmallow-like blob objects for each unique protein chain in pymol. Usage: 
	1. load this script in pymol via load /path/to/blob.py
	2. blob my_designs # recognizes regex, so e.g. blob * will blob everything.

This is based off Will Sheffler's marshmallow.py blobbing approach, see https://github.com/willsheffler/pymol for more.
'''

def blob(designs):
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




cmd.extend( "blob", blob )


