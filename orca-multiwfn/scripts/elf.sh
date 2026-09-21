#!/bin/bash
molden_file=$1
output_prefix=${molden_file%.molden}

cat << EOF | Multiwfn $molden_file
5        # Output property in spatial region
9        # ELF
100      # Grid size (misalnya 100, bisa disesuaikan)
0        # Use default box size
5        # Output to cube file
${output_prefix}_ELF.cube
q        # Quit
EOF

echo "ELF cube file saved as ${output_prefix}_ELF.cube"

! run with bash
