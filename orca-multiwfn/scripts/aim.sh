#!/bin/bash

summary="aim_summary.txt"
echo "AIM Charges per Atom" > $summary
echo "================================" >> $summary

for f in *_bader.log; do
  echo "===== $f =====" >> $summary
  awk '/The atomic charges after normalization/{flag=1;next}/Integrating basins/{flag=0}flag' "$f" >> $summary
  echo "" >> $summary
done

echo "Done, check the result on $summary"
