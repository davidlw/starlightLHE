#!/bin/bash
#date

if [ $# != 1 ]; then
    echo "Please provide particle species name: \"LowMassGammaGamma\" OR \"CohJpsi\" OR \"CohJpsi_0n0n\" OR \"CohJpsi_0nXn\" OR \"CohJpsi_XnXn\" OR \"InCohJpsi\" OR \"CohPsi2S\" OR \"InCohPsi2S\" OR \"CohPhi\" OR \"CohPhi2KKinOOAt5p36TeV\" OR \"CohPhi2KKinpOAt9p9TeV\" OR \"CohPhi2KKinNeNeAt5p36TeV\" OR \"CohRho\" !!!"
    exit
fi

if [ $1 != "LowMassGammaGamma" -a $1 != "CohJpsi" -a $1 != "CohJpsi_0n0n" -a $1 != "CohJpsi_0nXn" -a $1 != "CohJpsi_XnXn" -a $1 != "InCohJpsi" -a $1 != "CohPsi2S" -a $1 != "InCohPsi2S" -a $1 != "CohPhi" -a $1 != "CohPhi2KKinOOAt5p36TeV" -a $1 != "CohPhi2KKinpOAt9p9TeV" -a $1 != "CohPhi2KKinNeNeAt5p36TeV" -a $1 != "CohRho" ]; then
    echo "The particle species name should be: \"LowMassGammaGamma\" OR \"CohJpsi\" OR \"CohJpsi_0n0n\" OR \"CohJpsi_0nXn\" OR \"InCohJpsi\" OR \"CohPsi2S\" OR \"InCohPsi2S\" OR \"CohPhi\" OR \"CohPhi2KKinOOAt5p36TeV\" OR \"CohPhi2KKinpOAt9p9TeV\" OR \"CohPhi2KKinNeNeAt5p36TeV\" OR \"CohRho\" !!!"
    exit
fi

dir=$1

lheFileDir="lheFiles"

if [ ! -d $dir/$lheFileDir ]; then
    mkdir -p $dir/$lheFileDir
fi

if [ "`ls -A $dir/$lheFileDir`" != "" ]; then
    rm -rf $dir/$lheFileDir/*
fi

cmsEnergyDiv2=4950
dauID=321

for inputFile in `ls $dir/splitFiles/slight*`
do
    echo $inputFile

    baseFileName=`basename $inputFile`

    #outputFile=${baseFileName/.out/.lhe}
    if [[ $baseFileName =~ ".out" ]]; then
        outputFile=${baseFileName%.out}  # remove `.out`
    fi

    if [[ $baseFileName =~ ".tx" ]]; then
        outputFile=${baseFileName%.tx}  # remove `.tx`
    fi

    idx=${outputFile:$strLen-4}

    modIdx=$(echo $idx | sed 's/^0*//')  # remove leading zeroes
    #modIdx=$((10#$idx))  # remove leading zeroes

    modOutputFile=${outputFile/$idx/$modIdx}

    echo $outputFile
    #echo $modOutputFile
    #echo ""

    root -l -b << EOF
    .x convert_SL2LHE.C+("$inputFile","$dir/$lheFileDir/$outputFile",$cmsEnergyDiv2,$cmsEnergyDiv2,$dauID)
    .q
EOF

done
