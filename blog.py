#!/usr/bin/env python

import math
from gimpfu import *

def python_circulos(timg, tdrawable):
    
    #image = gimp.image_list()[0]
    if not pdb.gimp_selection_is_empty(timg):
		
		pdb.gimp_selection_border(timg, 2)
		layer = pdb.gimp_layer_new(timg, timg.width, timg.height, RGBA_IMAGE, "capa transparente", 100, NORMAL_MODE)
		timg.add_layer(layer, 0)
		
		fg_color = pdb.gimp_context_get_foreground()
		pdb.gimp_context_set_foreground((225,16,16))
		pdb.gimp_edit_fill(tdrawable, FOREGROUND_FILL)
		pdb.gimp_image_merge_visible_layers(timg, CLIP_TO_IMAGE)

		pdb.gimp_selection_none(timg) 
		pdb.gimp_context_set_foreground(fg_color)

register(
        "python_jasv_marcar_circulos",
        "Destaca cierta zona de una imagen rodeandola con circulos rojos",
        "Circulos rojos",
        "El Informatico de Guardia",
        "http://andalinux.wordpress.com",
        "2016",
        "<Image>/Filters/Blog/Circulos",
        "RGB*",
        [],
        [],
        python_circulos)

main()
