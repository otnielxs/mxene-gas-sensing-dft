#!/bin/bash

FILES=("") #.gbw files

echo "=========================================="
echo "    CALCULATING BADER CHARGES (AIM)      "
echo "=========================================="

for f in "${FILES[@]}"; do
    if [ -f "$f" ]; then
        base="${f%.gbw}"
        echo "=== Running Bader Integration for $base ==="

        {
          echo 17; sleep 1
          echo 1;  sleep 1
          echo 1;  sleep 1
          echo 1;  sleep 1
          echo 7;  sleep 1
          echo 2;  sleep 1
          echo 1;  sleep 1
          echo q;  sleep 1
        } | Multiwfn "$f" > "${base}_bader.log"

        echo "===== Bader Charge Result: $base ====="
        grep -A 10 "Integrated value" "${base}_bader.log" || \
        grep -A 15 "Summary of basin integration" "${base}_bader.log"
    else
        echo "File $f not found!"
    fi
done

echo "Done! Check *_bader.log files."
