#!/bin/sh

#Copy all templates into a single file

for i in ??; do
    echo "-${i}-------------------------------------"
    cat $i/solution/*.template.py
done > all_assignments.txt
