#! /bin/bash
. env.sh
# abaqus viewer noGUI=track_point.py
 # /home/matt/PhD/abaqus/6.13-4/coating-plastic-kinematic-rough-high-2
odb=../coating-plastic-kinematic-rough-high-2.odb
odb=../coating-plastic-penalty-slip-low.odb
# odb=../coating-plastic-penalty-slip-low.odb
DIR=$(readlink -f $odb)
echo $DIR
export ROOTODB=$DIR
export OUTPATH=./test.out

abaqus viewer noGUI=process_energy.py
# abaqus viewer noGUI=process_profile.py
