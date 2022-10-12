#!/bin/bash
# Download, 20 processes at a time

xargs -I arg -P 20 <../urls.txt ../helper.sh arg

# Sort into directories

mkdir 0 1500 1630 1760

mv *1500* 1500
mv *1630* 1630
mv *1750* 1760
mv 2* 0
