# Muat berkas cube
mol new nh3_RDG.cube type cube
mol addfile nh3_sign_rho.cube type cube

mol representation CPK 1.0 0.3 30.0 30.0
mol color Name
mol selection {all}
mol material Opaque
mol addrep 0

mol representation Isosurface 0.5 0 0 0 1 1
mol color Volume 1
mol selection {all}
mol material Transparent
mol addrep 0

mol scaleminmax 0 1 -0.035 0.035
color scale method BWR

display background white

display shadows on
display ambientocclusion on
display depthcue off
