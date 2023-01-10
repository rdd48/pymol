from pymol import cmd

count = 0
t32_chains = "ABCDFG"
i52_1_chains = "FJKLPRWVZ0"
i52_all_chains = "ABCDEGOUQ1"
odd_chains = "ACEGIKMOQSUW"

def fc_separate(designs):
	designs = cmd.get_object_list(designs)
	for design_name in designs:
		cmd.do('create {design_name}_fcs, {design_name} and resi 1-207'.format(design_name=design_name))
		cmd.do('remove resi 1-207 and {design_name}'.format(design_name=design_name))

def align_igg(design_name, igg='1igt'):
	#may need to pre-fetch 1igt

	#cmd.do("fetch 1igt")
	#cmd.do("color slate, 1igt")
	cmd.do("hide lin")
	if design_name.startswith('t'):
		for i in t32_chains:
			cmd.do("create igg{i}_{design_name}, {igg}".format(i=i, design_name=design_name, igg=igg))
			cmd.do("align igg{i}_{design_name}, {design_name} and chain {i} and resi 1-207".format(i=i, design_name=design_name))
	elif design_name.startswith('i'):
		cmd.do("create i52_copy, " + design_name)
		cmd.do("rotate z, 180, i52_copy, camera=0, origin=[0,0,0]")
		for i in i52_1_chains:
			cmd.do("create igg" + i + ", {igg}".format(igg=igg))
			cmd.do("align igg" + i + ", " + design_name + " and chain " + i + " and resi 1-207")
		for i in i52_all_chains:
			cmd.do("create igg" + i + ", {igg}".format(igg=igg))
			cmd.do("align igg" + i + ", " + design_name + " and chain " + i + " and resi 1-207")
			cmd.do("create igg_dupl" + i + ", {igg}".format(igg=igg))
			cmd.do("align igg_dupl" + i + ", i52_copy and chain " + i + " and resi 1-207")
		cmd.do("color grey90, i52_copy")
	else:
		for i in cmd.get_chains(design_name):
			if i in odd_chains:
				cmd.do("create igg{i}_{design_name}, {igg}".format(i=i, design_name=design_name, igg=igg))
				cmd.do("align igg{i}_{design_name}, {design_name} and chain {i} and resi 1-207".format(i=i, design_name=design_name))
	cmd.do("delete {igg}".format(igg=igg))
	cmd.do("remove resi 1-207 and " + design_name)
	cmd.do("color grey70, " + design_name)
	cmd.do("show all")

def align_ang1(design_name):

	if design_name.startswith('t'):
		for i in t32_chains:
			cmd.do("create igg{i}_{design_name}, ang1f-fc".format(i=i, design_name=design_name))
			cmd.do("align igg{i}_{design_name}, {design_name} and chain {i} and resi 1-207".format(i=i, design_name=design_name))
	elif design_name.startswith('i'):
		cmd.do("create i52_copy, " + design_name)
		cmd.do("rotate z, 180, i52_copy, camera=0, origin=[0,0,0]")
		for i in i52_1_chains:
			cmd.do("create igg" + i + ", ang1f-fc")
			cmd.do("align igg" + i + ", " + design_name + " and chain " + i + " and resi 1-207")
		for i in i52_all_chains:
			cmd.do("create igg" + i + ", ang1f-fc")
			cmd.do("align igg" + i + ", " + design_name + " and chain " + i + " and resi 1-207")
			cmd.do("create igg_dupl" + i + ", ang1f-fc")
			cmd.do("align igg_dupl" + i + ", i52_copy and chain " + i + " and resi 1-207")
		cmd.do("color grey90, i52_copy")
	else:
		for i in cmd.get_chains(design_name):
			if i in odd_chains:
				cmd.do("create igg{i}_{design_name}, ang1f-fc".format(i=i, design_name=design_name))
				cmd.do("align igg{i}_{design_name}, {design_name} and chain {i} and resi 1-207".format(i=i, design_name=design_name))

def align_i5350(design_name, trimer_ligand):
	#cmd.do("create I53-50_c1, " + design_name)
	#cmd.do("rotate z, 180, I53-50_c1, camera=0, origin=[0,0,0]")
	i53_trimers = ['jXP', 'Lth', 'FrN', 'bn>', 'Jld', 'D$7', '@.5', 'v1f', 'BZz', 'RH3']
	
	for i in i53_trimers:
		if i[0] == '@':
			decoy = 'at'
		elif i[1] == '$':
			decoy = 'dollars'
		elif i[1] == '.':
			decoy = 'dot'
		elif i[2] == '>':
			decoy = 'goat'
		else:
			decoy = i
		cmd.do("create {design_name}_{trimer_ligand}_{i}, {trimer_ligand}".format(design_name=design_name, trimer_ligand=trimer_ligand, i=decoy))
		cmd.do("align {design_name}_{trimer_ligand}_{i}, {design_name} and chain {i1}".format(trimer_ligand=trimer_ligand, design_name=design_name, i=decoy, i1 = i[0]))
			#cmd.do("create {trimer_ligand}_{i}_2, {trimer_ligand}".format(trimer_ligand=trimer_ligand, i=i))
			#cmd.do("align {trimer_ligand}_{i}_2, I53-50_c1 and chain {i1}+{i2}+{i3}".format(trimer_ligand=trimer_ligand, design_name=design_name, i=i, i1 = i[0], i2 = i[1], i3 = i[2]))
	#cmd.do("delete {trimer_ligand}".format(trimer_ligand=trimer_ligand))

def abc(design_nickname):
	name_dict = {'d2': 'd2.4.pdb', 'd24': 'd2.4.pdb', 't4': 't4_r1.pdb', 't8': 't.8.pdb', \
	'o4': 'o42.1.pdb', 'o': 'o42.1.pdb', 'o421': 'o42.1.pdb', \
	'i5': 'i52.3.pdb', 'i': 'i52.3.pdb', 'i523': 'i52.3.pdb'}
	cmd.do("load ~/Desktop/pdbs/" + name_dict[design_nickname])

def d24():
	cmd.do("load ~/Desktop/pdbs/d2.4.pdb")
def t4():
	cmd.do("load ~/Desktop/pdbs/t4_r1.pdb")
def t8():
	cmd.do("load ~/Desktop/pdbs/t.8.pdb")
def o4():
	cmd.do("load ~/Desktop/pdbs/o42.1.pdb")
def i5():
	cmd.do("load ~/Desktop/pdbs/i52.3.pdb")
def igg():
	cmd.do("fetch 1igt")

cmd.extend("align_igg", align_igg)
cmd.extend("align_ang1", align_ang1)
cmd.extend("fc_separate", fc_separate)
cmd.extend("abc", abc)
cmd.extend("d24", d24)
cmd.extend("d2.4", d24)
cmd.extend("t4", t4)
cmd.extend("t.4", t4)
cmd.extend("t4_r1", t4)
cmd.extend("t8", t8)
cmd.extend("t.8", t8)
cmd.extend("o4", o4)
cmd.extend("o42.1", o4)
cmd.extend("o421", o4)
cmd.extend("o42", o4)
cmd.extend("i5", i5)
cmd.extend("i52.3", i5)
cmd.extend("i523", i5)
cmd.extend("i52", i5)
cmd.extend("igg", igg)
cmd.extend("align_i5350", align_i5350)
