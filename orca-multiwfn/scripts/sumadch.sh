#!/bin/bash

summary="adch_summary.txt"
echo "Ringkasan ADCH Charges per Atom" > $summary
echo "================================" >> $summary

for f in *_adch.log; do
  echo "===== $f =====" >> $summary
  # Ambil hanya baris setelah "Final atomic charges" yang berisi tabel Atom
  awk '/Final atomic charges/{flag=1;next}/^$/{flag=0}flag' "$f" >> $summary
  echo "" >> $summary
done

echo "Selesai! Lihat hasil di $summary"
