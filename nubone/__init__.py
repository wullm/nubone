import numpy as np
from matplotlib import cm
from matplotlib.colors import LinearSegmentedColormap
import colorsys

def saturate(r, g, b, factor):
	h,l,s = colorsys.rgb_to_hls(r, g, b)
	r,g,b = colorsys.hls_to_rgb(h, l, s * factor)
	return (r,g,b)

def create_nubone(N = 1024, saturate_factor = 3):
	bone = cm.get_cmap("bone", N+1)
	bone_colors = bone(np.linspace(0, 1, N + 1))
	nubone_saturated = np.zeros((3, N+1))
	nubone_segments = np.linspace(0, 1, N)

	for i in range(N+1):
		r,g,b = saturate(bone_colors[i,0], bone_colors[i,1], bone_colors[i,2], saturate_factor)		
		nubone_saturated[:,i] = [r, g, b]

	nubone_red_segments = np.array([nubone_segments, nubone_saturated[0,:-1], nubone_saturated[0,1:]]).T
	nubone_green_segments = np.array([nubone_segments, nubone_saturated[1,:-1], nubone_saturated[1,1:]]).T
	nubone_blue_segments = np.array([nubone_segments, nubone_saturated[2,:-1], nubone_saturated[2,1:]]).T

	nubone_dict = {
			"red": nubone_red_segments,
			"green": nubone_green_segments,
			"blue": nubone_blue_segments}

	return LinearSegmentedColormap("nubone", segmentdata = nubone_dict, N = N)
	
nubone = create_nubone()
