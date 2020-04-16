#! /bin/bash
sed '/#/d' $1 | sort -k1 -g &> "$1".out
