#!/bin/bash

# create loop over each h5 file
#  make dir named datetime
#   create loop over dataset
#    parse each and write to csv

while read h5
do

    DATETIME=`echo $h5 | cut -d "_" -f5`
    mkdir "../csv/raw/${DATETIME}"
    mkdir "../csv/raw/${DATETIME}/meta"
    mkdir "../csv/rebuilt/${DATETIME}"
    mkdir "../csv/rebuilt/${DATETIME}/meta"
    
    while read dataset
    do
        h5dump -d "Geophysical_Data/${dataset}[0,0;1,1;151,160;1,1;]" -o ../csv/raw/${DATETIME}/${dataset}.csv -w 161 ../h5/${h5}
    done < <(cat dataset.txt)

    while read metadata
    do
        h5dump -d "${metadata}[0,0;1,1;151,160;1,1;]" -o ../csv/raw/${DATETIME}/meta/${metadata}.csv -w 161 ../h5/${h5}
    done < <(cat metadata.txt)

#for prod rm head pipe
done < <(ls ../h5/ | grep .h5 | head -n 2) 


