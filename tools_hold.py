from pymol import cmd
from pymol.cgo import *

def fancy_helices():
	cmd.do("set cartoon_fancy_helices, 1")
	cmd.do("set cartoon_highlight_color, grey70")
	cmd.do("set specular, 0")
	cmd.do("set ray_trace_mode, 3")
	cmd.do("set ray_trace_color, black")
	cmd.do("set ray_trace_gain, 0.1")
	cmd.do("bg_color white")

def d2_dist(protein_name="all"):

	c2a_list = ['AD', 'BC']
	c2b_list = ['AB', 'CD']

	c2a_stretch = 1.25
	c2b_stretch = 1.25

	c2a_centroids = []
	c2b_centroids = []

	for design_name in cmd.get_names(protein_name):

		for c2 in c2a_list:
			xa,ya,za = cmd.centerofmass("{design_name} and chain {chain} and name OXT".format(design_name=design_name, chain=c2[0]))
			xb,yb,zb = cmd.centerofmass("{design_name} and chain {chain} and name OXT".format(design_name=design_name, chain=c2[1]))
			centroid = [float((xa + xb) / 2), float((ya + yb) / 2), float((za + zb) / 2)]
			c2a_centroids.append(centroid)

		for c2 in c2b_list:
			xa,ya,za = cmd.centerofmass("{design_name} and chain {chain} and resi 1 and name CA".format(design_name=design_name, chain=c2[0]))
			xb,yb,zb = cmd.centerofmass("{design_name} and chain {chain} and resi 1 and name CA".format(design_name=design_name, chain=c2[1]))
			centroid = [float((xa + xb) / 2), float((ya + yb) / 2), float((za + zb) / 2)]
			c2b_centroids.append(centroid)

		for i in range(len(c2a_centroids)):
			for k in range(len(c2a_centroids)):
				psuedo_1 = cmd.do("pseudoatom tmp1, pos={vertices}".format(vertices=c2a_centroids[i]))
				psuedo_2 = cmd.do("pseudoatom tmp2, pos={vertices}".format(vertices=c2b_centroids[k]))
				cmd.do("distance dist_{i}_{k}, tmp1, tmp2".format(i=i, k=k))
				cmd.do("delete tmp1; delete tmp2")

		cmd.do("hide labels")
		cmd.do("color black, dist*")
		cmd.do("set dash_gap, 3")
		cmd.do("bg_color white")


def t32_axes(protein_name="all"):

	c3_list = ['ABC', 'DEF', 'GHI', 'JKL']
	c2_list = ['AK', 'BE', 'CI', 'DH', 'FJ', 'GL']

	c3_stretch = 1.25
	c2_stretch = 1.25

	c3_centroids = []

	for design_name in cmd.get_names(protein_name):

		for c3 in c3_list:
			xa,ya,za = cmd.centerofmass("{design_name} and chain {chain} and name OXT".format(design_name=design_name, chain=c3[0]))
			xb,yb,zb = cmd.centerofmass("{design_name} and chain {chain} and name OXT".format(design_name=design_name, chain=c3[1]))
			xc,yc,zc = cmd.centerofmass("{design_name} and chain {chain} and name OXT".format(design_name=design_name, chain=c3[2]))
			centroid = [float((xa + xb + xc) / 3), float((ya + yb + yc) / 3), float((za + zb + zc) / 3)]
			obj = [CYLINDER, 0., 0., 0., c3_stretch * centroid[0], c3_stretch * centroid[1], c3_stretch * centroid[2], 1.0, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7,]
			cmd.load_cgo(obj, 'axes_{c3}'.format(c3=c3))

			c3_centroids.append(centroid)

		for c2 in c2_list:
			xa,ya,za = cmd.centerofmass("{design_name} and chain {chain} and resi 1 and name CA".format(design_name=design_name, chain=c2[0]))
			xb,yb,zb = cmd.centerofmass("{design_name} and chain {chain} and resi 1 and name CA".format(design_name=design_name, chain=c2[1]))
			midpoint = [float(c2_stretch * (xa + xb) / 2), float(c2_stretch * (ya + yb) / 2), float(c2_stretch * (za + zb) / 2)]
			obj = [CYLINDER, 0., 0., 0., midpoint[0], midpoint[1], midpoint[2], 1.0, 0.5, 0.5, 1.0, 0.5, 0.5, 1.0,]
			cmd.load_cgo(obj, 'axes_{c2}'.format(c2=c2))

		for i in range(len(c3_centroids)):
			for k in range(i+1, len(c3_centroids)):
				psuedo_1 = cmd.do("pseudoatom tmp1, pos={vertices}".format(vertices=c3_centroids[i]))
				psuedo_2 = cmd.do("pseudoatom tmp2, pos={vertices}".format(vertices=c3_centroids[k]))
				cmd.do("distance dist_{i}_{k}, tmp1, tmp2".format(i=i, k=k))
				cmd.do("delete tmp1; delete tmp2")

		cmd.do("hide labels")
		cmd.do("color black, dist*")
		cmd.do("set dash_gap, 3")
		cmd.do("bg_color white")

def calc_t32_axes_intersect(protein_name="all"):

	#c3_list = ['ABC', 'DEF', 'GHI', 'JKL']
	c2_list = ['AK', 'BE', 'CI', 'DH', 'FJ', 'GL']

	for design_name in cmd.get_names(protein_name):

		for c3 in ['ABC']:
			xa,ya,za = cmd.centerofmass("{design_name} and chain {chain} and name OXT".format(design_name=design_name, chain=c3[0]))
			xb,yb,zb = cmd.centerofmass("{design_name} and chain {chain} and name OXT".format(design_name=design_name, chain=c3[1]))
			xc,yc,zc = cmd.centerofmass("{design_name} and chain {chain} and name OXT".format(design_name=design_name, chain=c3[2]))
			centroid_c3 = [float((xa + xb + xc) / 3), float((ya + yb + yc) / 3), float((za + zb + zc) / 3)]

		for c2 in c2_list:
			xa,ya,za = cmd.centerofmass("{design_name} and chain {chain} and resi 1 and name CA".format(design_name=design_name, chain=c2[0]))
			xb,yb,zb = cmd.centerofmass("{design_name} and chain {chain} and resi 1 and name CA".format(design_name=design_name, chain=c2[1]))
			midpoint = [float((xa + xb) / 2), float((ya + yb) / 2), float((za + zb) / 2)]

		print(centroid_c3, midpoint)

		


def o42_axes(protein_name="all"):
	c4_list = ['ADHI', 'BEMP', 'CTRX', 'FKSU', 'GLNQ', 'JOVW']
	c2_list = ['AB', 'CD', 'EF', 'GH', 'IJ', 'KL', 'MN', 'OP', 'QR', 'ST', 'UV', 'WX']

	c4_stretch = 1.5
	c2_stretch = 1.25

	c4_centroids = []

	for design_name in cmd.get_names(protein_name):
		for c4 in c4_list:
			xa,ya,za = cmd.centerofmass("{design_name} and chain {chain} and name OXT".format(design_name=design_name, chain=c4[0]))
			xb,yb,zb = cmd.centerofmass("{design_name} and chain {chain} and name OXT".format(design_name=design_name, chain=c4[1]))
			xc,yc,zc = cmd.centerofmass("{design_name} and chain {chain} and name OXT".format(design_name=design_name, chain=c4[2]))
			xd,yd,zd = cmd.centerofmass("{design_name} and chain {chain} and name OXT".format(design_name=design_name, chain=c4[2]))
			centroid = [float((xa + xb + xc + xd) / 4), float((ya + yb + yc + yd) / 4), float((za + zb + zc + zd) / 4)]
			obj = [CYLINDER, 0., 0., 0., c4_stretch * centroid[0], c4_stretch * centroid[1], c4_stretch * centroid[2], 1.0, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7,]
			cmd.load_cgo(obj, 'axes_{c4}'.format(c4=c4))

			c4_centroids.append(centroid)

		for c2 in c2_list:
			xa,ya,za = cmd.centerofmass("{design_name} and chain {chain} and resi 1 and name CA".format(design_name=design_name, chain=c2[0]))
			xb,yb,zb = cmd.centerofmass("{design_name} and chain {chain} and resi 1 and name CA".format(design_name=design_name, chain=c2[1]))
			midpoint = [float(c2_stretch * (xa + xb) / 2), float(c2_stretch * (ya + yb) / 2), float(c2_stretch * (za + zb) / 2)]
			obj = [CYLINDER, 0., 0., 0., midpoint[0], midpoint[1], midpoint[2], 1.0, 0.5, 0.5, 1.0, 0.5, 0.5, 1.0,]
			cmd.load_cgo(obj, 'axes_{c2}'.format(c2=c2))

		for i in range(len(c4_centroids)):
			for k in range(i+1, len(c4_centroids)):
				if not (i == 0 and k == 3) or (i == 1 and k == 2) or (i == 4 and k == 5):
					psuedo_1 = cmd.do("pseudoatom tmp1, pos={vertices}".format(vertices=c4_centroids[i]))
					psuedo_2 = cmd.do("pseudoatom tmp2, pos={vertices}".format(vertices=c4_centroids[k]))
					cmd.do("distance dist_{i}_{k}, tmp1, tmp2".format(i=i, k=k))
					cmd.do("delete tmp1; delete tmp2")

		cmd.do("hide labels")
		cmd.do("color black, dist*")
		cmd.do("set dash_gap, 3")
		cmd.do("bg_color white")


def i52_axes(protein_name="all"):
	cmd.do("create i52.3_copy, i52.3")
	cmd.do("rotate z, 180, i52.3_copy, origin=[0,0,0], camera=0")
	c5_list = ['Z0123', 'ABCDE', 'FGHIJ', 'KLMNO', 'PQRST', 'UVWXY']
	c2_list_within = ['A3', 'BT', 'CI', 'DM', 'EX', 'GY', 'HO', 'N1', 'Q2', 'SU']
	c2_list_between = ['LL', 'JK', 'KJ', 'FZ', 'ZF', '0W', 'PV', 'RR', 'VP', 'W0']

	c5_stretch = 1.5
	c2_stretch = 1.25

	c5_centroids = []
	design_names = []

	for design_name in cmd.get_object_list(protein_name):
		design_names.append(design_name)

		for c5 in c5_list:
			xa,ya,za = cmd.centerofmass("{design_name} and chain {chain} and name OXT".format(design_name=design_name, chain=c5[0]))
			xb,yb,zb = cmd.centerofmass("{design_name} and chain {chain} and name OXT".format(design_name=design_name, chain=c5[1]))
			xc,yc,zc = cmd.centerofmass("{design_name} and chain {chain} and name OXT".format(design_name=design_name, chain=c5[2]))
			xd,yd,zd = cmd.centerofmass("{design_name} and chain {chain} and name OXT".format(design_name=design_name, chain=c5[2]))
			xe,ye,ze = cmd.centerofmass("{design_name} and chain {chain} and name OXT".format(design_name=design_name, chain=c5[2]))
			centroid = [float((xa + xb + xc + xd + xe) / 5), float((ya + yb + yc + yd + ye) / 5), float((za + zb + zc + zd + ze) / 5)]
			obj = [CYLINDER, 0., 0., 0., c5_stretch * centroid[0], c5_stretch * centroid[1], c5_stretch * centroid[2], 1.0, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7,]
			cmd.load_cgo(obj, 'axes_{c5}_{design_name}'.format(c5=c5, design_name=design_name))

			c5_centroids.append(centroid)

		for c2 in c2_list_within:
			xa,ya,za = cmd.centerofmass("{design_name} and chain {chain} and resi 1 and name CA".format(design_name=design_name, chain=c2[0]))
			xb,yb,zb = cmd.centerofmass("{design_name} and chain {chain} and resi 1 and name CA".format(design_name=design_name, chain=c2[1]))
			midpoint = [float(c2_stretch * (xa + xb) / 2), float(c2_stretch * (ya + yb) / 2), float(c2_stretch * (za + zb) / 2)]
			obj = [CYLINDER, 0., 0., 0., midpoint[0], midpoint[1], midpoint[2], 1.0, 0.5, 0.5, 1.0, 0.5, 0.5, 1.0,]
			cmd.load_cgo(obj, 'axes_{c2}_{design_name}'.format(c2=c2, design_name=design_name))

	for c2 in c2_list_between:
		xa,ya,za = cmd.centerofmass("{design_name} and chain {chain} and resi 1 and name CA".format(design_name=design_names[0], chain=c2[0]))
		xb,yb,zb = cmd.centerofmass("{design_name} and chain {chain} and resi 1 and name CA".format(design_name=design_names[1], chain=c2[1]))
		midpoint = [float(c2_stretch * (xa + xb) / 2), float(c2_stretch * (ya + yb) / 2), float(c2_stretch * (za + zb) / 2)]
		obj = [CYLINDER, 0., 0., 0., midpoint[0], midpoint[1], midpoint[2], 1.0, 0.5, 0.5, 1.0, 0.5, 0.5, 1.0,]
		cmd.load_cgo(obj, 'axes_{c2}_{design_name1}_{design_name2}'.format(c2=c2, design_name1=design_names[0], design_name2=design_names[1]))

	good_ik_pairs = {
		0: [1,3,4,8,11],
		1: [2,3,4,5],
		2: [3,5,6,9],
		3: [8,9],
		4: [5,10,11],
		5: [6,10],
		6: [7,9,10],
		7: [8,9,10,11],
		8: [9,11],
		9: [],
		10: [11]
	}

	for i in range(len(c5_centroids)):
		for k in range(i+1, len(c5_centroids)):
			if k in good_ik_pairs[i]:
				psuedo_1 = cmd.do("pseudoatom tmp1, pos={vertices}".format(vertices=c5_centroids[i]))
				psuedo_2 = cmd.do("pseudoatom tmp2, pos={vertices}".format(vertices=c5_centroids[k]))
				cmd.do("distance dist_{i}_{k}, tmp1, tmp2".format(i=i, k=k))
				cmd.do("delete tmp1; delete tmp2")

	cmd.do("hide labels")
	cmd.do("color black, dist*")
	cmd.do("set dash_gap, 3")
	cmd.do("bg_color white")

def t32_spheres(protein_name="all"):

	c3_list = ['ABC', 'DEF', 'GHI', 'JKL']
	c2_list = ['AK', 'BE', 'CI', 'DH', 'FJ', 'GL']

	c3_centroids = []

	for design_name in cmd.get_names(protein_name):

		for c3 in c3_list:
			xa,ya,za = cmd.centerofmass("{design_name} and chain {chain} and resi 537 and name CA".format(design_name=design_name, chain=c3[0]))
			xb,yb,zb = cmd.centerofmass("{design_name} and chain {chain} and resi 537 and name CA".format(design_name=design_name, chain=c3[1]))
			xc,yc,zc = cmd.centerofmass("{design_name} and chain {chain} and resi 537 and name CA".format(design_name=design_name, chain=c3[2]))

			obj1 = [COLOR, 0.7, 0.7, 0.7, SPHERE, xa, ya, za, 15.0]
			obj2 = [COLOR, 0.7, 0.7, 0.7, SPHERE, xb, yb, zb, 15.0]
			obj3 = [COLOR, 0.7, 0.7, 0.7, SPHERE, xc, yc, zc, 15.0]

			cmd.load_cgo(obj1, 'c3_sphere1_{c3}'.format(c3=c3))
			cmd.load_cgo(obj2, 'c3_sphere2_{c3}'.format(c3=c3))
			cmd.load_cgo(obj3, 'c3_sphere3_{c3}'.format(c3=c3))

		for c2 in c2_list:
			xa,ya,za = cmd.centerofmass("{design_name} and chain {chain} and resi 101 and name CA".format(design_name=design_name, chain=c2[0]))
			xb,yb,zb = cmd.centerofmass("{design_name} and chain {chain} and resi 101 and name CA".format(design_name=design_name, chain=c2[1]))

			obj1 = [COLOR, 0.5, 0.5, 1.0, SPHERE, xa * 0.8, ya * 0.8, za * 0.8, 15.0]
			obj2 = [COLOR, 0.5, 0.5, 1.0, SPHERE, xb * 0.8, yb * 0.8, zb * 0.8, 15.0]

			cmd.load_cgo(obj1, 'c2_sphere1_{c2}'.format(c2=c2))
			cmd.load_cgo(obj2, 'c2_sphere2_{c2}'.format(c2=c2))

def o42_spheres(protein_name="all"):

	c4_list = ['ADHI', 'BEMP', 'CTRX', 'FKSU', 'GLNQ', 'JOVW']
	c2_list = ['AB', 'CD', 'EF', 'GH', 'IJ', 'KL', 'MN', 'OP', 'QR', 'ST', 'UV', 'WX']

	for design_name in cmd.get_names(protein_name):

		for c4 in c4_list:
			xa,ya,za = cmd.centerofmass("{design_name} and chain {chain} and resi 537 and name CA".format(design_name=design_name, chain=c4[0]))
			xb,yb,zb = cmd.centerofmass("{design_name} and chain {chain} and resi 537 and name CA".format(design_name=design_name, chain=c4[1]))
			xc,yc,zc = cmd.centerofmass("{design_name} and chain {chain} and resi 537 and name CA".format(design_name=design_name, chain=c4[2]))
			xd,yd,zd = cmd.centerofmass("{design_name} and chain {chain} and resi 537 and name CA".format(design_name=design_name, chain=c4[3]))

			obj1 = [COLOR, 0.8, 0.8, 0.8, SPHERE, xa, ya, za, 15.0]
			obj2 = [COLOR, 0.8, 0.8, 0.8, SPHERE, xb, yb, zb, 15.0]
			obj3 = [COLOR, 0.8, 0.8, 0.8, SPHERE, xc, yc, zc, 15.0]
			obj4 = [COLOR, 0.8, 0.8, 0.8, SPHERE, xd, yd, zd, 15.0]

			cmd.load_cgo(obj1, 'c3_sphere1_{c4}'.format(c4=c4))
			cmd.load_cgo(obj2, 'c3_sphere2_{c4}'.format(c4=c4))
			cmd.load_cgo(obj3, 'c3_sphere3_{c4}'.format(c4=c4))
			cmd.load_cgo(obj4, 'c3_sphere4_{c4}'.format(c4=c4))

		for c2 in c2_list:
			xa,ya,za = cmd.centerofmass("{design_name} and chain {chain} and resi 101 and name CA".format(design_name=design_name, chain=c2[0]))
			xb,yb,zb = cmd.centerofmass("{design_name} and chain {chain} and resi 101 and name CA".format(design_name=design_name, chain=c2[1]))

			obj1 = [COLOR, 0.5, 0.5, 1.0, SPHERE, xa * 0.8, ya * 0.8, za * 0.8, 15.0]
			obj2 = [COLOR, 0.5, 0.5, 1.0, SPHERE, xb * 0.8, yb * 0.8, zb * 0.8, 15.0]

			cmd.load_cgo(obj1, 'c2_sphere1_{c2}'.format(c2=c2))
			cmd.load_cgo(obj2, 'c2_sphere2_{c2}'.format(c2=c2))

def separate_t32(designs='*'):

	c3_list = ['ABC', 'DEF', 'GHI', 'JKL']
	c2_list = ['AK', 'BE', 'CI', 'DH', 'FJ', 'GL']

	designs = cmd.get_object_list(designs)
	for design_name in designs:
		for i in c3_list:
			chain_plusses = i[0] + '+' + i[1] + '+' + i[2]
			cmd.create(f'trimer_{i}', f'{design_name} and chain {chain_plusses} and resi 208-999')
		for j in c2_list:
			chain_plusses = j[0] + '+' + j[1]
			cmd.create(f'dimer_{j}', f'{design_name} and chain {chain_plusses} and resi 1-207')

def blow_up_t32(designs='*', intensity=200, blob=0):
	designs = cmd.get_object_list(designs)
	intensity = float(intensity)

	for design in designs:
		if design.startswith('trimer'):
			c3 = design[-3:]
			xa,ya,za = cmd.centerofmass(f'{design} and chain {c3[0]} and name OXT')
			xb,yb,zb = cmd.centerofmass(f'{design} and chain {c3[1]} and name OXT')
			xc,yc,zc = cmd.centerofmass(f'{design} and chain {c3[2]} and name OXT')
			centroid = [float((xa + xb + xc) / 3), float((ya + yb + yc) / 3), float((za + zb + zc) / 3)]
			translate_vector = []
			for j in centroid:
				if j > 0.0000:
					translate_vector.append(intensity)
				elif j < 0.0000:
					translate_vector.append(intensity * -1)
				else:
					translate_vector.append(j)

			if blob == 0:
				cmd.do(f'translate {translate_vector}, object={design}, camera=0')

			elif blob == '1':
				for k in c3:
					cmd.do(f'translate {translate_vector}, object=blob_{k}_{design}, camera=0')
					cmd.do(f'translate {translate_vector}, object=blob_{k}_{design}, camera=0')
					cmd.do(f'translate {translate_vector}, object=blob_{k}_{design}, camera=0')


		elif design.startswith('dimer'):
			c2 = design[-2:]
			xa,ya,za = cmd.centerofmass(f'{design} and chain {c2[0]} and resi 1 and name CA')
			xb,yb,zb = cmd.centerofmass(f'{design} and chain {c2[1]} and resi 1 and name CA')
			centroid = [float((xa + xb) / 2), float((ya + yb) / 2), float((za + zb) / 2)]
			translate_vector = []
			for j in centroid:
				if j > 0.0000:
					translate_vector.append(intensity)
				elif j < 0.0000:
					translate_vector.append(intensity * -1)
				else:
					translate_vector.append(j)

			if blob == 0:
				cmd.do(f'translate {translate_vector}, object={design}, camera=0')

			elif blob == '1':
				for k in c2:
					cmd.do(f'translate {translate_vector}, object=blob_{k}_{design}, camera=0')
					cmd.do(f'translate {translate_vector}, object=blob_{k}_{design}, camera=0')




cmd.extend( "fancy_helices", fancy_helices)
cmd.extend( "d2_dist", d2_dist)
cmd.extend( "t32_axes", t32_axes)
cmd.extend( "o42_axes", o42_axes)
cmd.extend( "i52_axes", i52_axes)
cmd.extend( "t32_spheres", t32_spheres)
cmd.extend( "o42_spheres", o42_spheres)
cmd.extend( 'calc_t32_axes_intersect', calc_t32_axes_intersect)
cmd.extend( 'separate_t32', separate_t32)
cmd.extend( 'blow_up_t32', blow_up_t32)
