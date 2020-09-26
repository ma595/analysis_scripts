#! /bin/bash
# env.sh
# abaqus viewer noGUI=track_point.py
# /home/matt/PhD/abaqus/6.13-4/coating-plastic-kinematic-rough-high-2
odb=../coating-plastic-kinematic-rough-high-2.odb
odb=../coating-plastic-penalty-slip-low.odb
# odb=../coating-plastic-penalty-slip-low.odb
odb=../abaqus_output/Job-8.odb
odb=$(readlink -f $odb)
out_name=$(basename $odb)
echo $out_name
out_dir=./out/$out_name/

mkdir -p $out_dir

export ROOTODB=$odb
export OUTDIR=$out_dir
readlink -f $odb

script=profile
/home/m/abaqus_install/Commands/abaqus viewer noGUI=process_$script.py
