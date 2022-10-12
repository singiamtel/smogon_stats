#!/bin/bash

arg=$1
filename=$(echo $arg | cut -d'/' -f 5- | awk -F'/' '{print $1 ":" $3}')

wget $arg -O $filename
