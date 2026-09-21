#!/bin/bash

# Buat file ringkasan baru
summary="bader_summary.txt"
echo "Ringkasan Bader Charge per Basin" > $summary
echo "================================" >> $summary

for f in *_bader.log; do
  echo "===== $f =====" >> $summary
  # Ambil tabel Basin (Integral dan Volume)
  awk '/#Basin/{flag=1;next}/Sum of above/{flag=0}flag' "$f" >> $summary
  # Ambil total elektron
  grep "Sum of above values" "$f" >> $summary
  echo "" >> $summary
done

echo "Selesai! Lihat hasil di $summary"
