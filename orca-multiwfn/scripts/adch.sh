#!/bin/bash

FILES=("") #.molden files

echo "=========================================="
echo "   CALCULATING ADCH CHARGES      "
echo "=========================================="

for f in "${FILES[@]}"; do
    if [ -f "$f" ]; then
        echo "Processing $f ..."
        printf "7\n11\n1\n0\nq\n" | Multiwfn "$f" > "${f%.molden}_adch.log"
        echo "Saved to ${f%.molden}_adch.log"
    else
        echo "File $f not found, skipping."
    fi
done

echo "Done!"
