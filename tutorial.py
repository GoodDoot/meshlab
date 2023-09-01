import pymeshlab



    # create a new MeshSet
ms = pymeshlab.MeshSet()

ms.load_new_mesh('5_17.ply')

# applying some filters...
# ms.generate_simplified_point_cloud()
ms.generate_surface_reconstruction_ball_pivoting()
ms.compute_texcoord_parametrization_triangle_trivial_per_wedge(textdim=1024)
ms.compute_texmap_from_color(textname='chameleon_simplified.png')

ms.save_current_mesh('5_17_output.ply')
