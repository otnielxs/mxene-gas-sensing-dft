#!/bin/bash

systems=("co2" "h2s" "nh3" "no2")

for sys in "${systems[@]}"; do
    echo "=========================================="
    echo " Memproses NCI/RDG untuk: $sys"
    echo "=========================================="

    if [ -f "${sys}.gbw" ] && [ ! -f "${sys}.molden" ]; then
        orca_2mkl "$sys" -molden
        if [ -f "${sys}.molden.input" ]; then
            mv "${sys}.molden.input" "${sys}.molden"
        fi
    fi

    Multiwfn "${sys}.molden" << EOF
20
1
2
3
2
0
0
q
EOF

    [ -f "func1.cub" ] && mv func1.cub "${sys}_sign_rho.cub"
    [ -f "func2.cub" ] && mv func2.cub "${sys}_RDG.cub"
    [ -f "output.txt" ] && mv output.txt "${sys}_scatter.txt"
done
