#!/bin/bash

cd hw0
mkdir pronto_data
cd pronto_data
curl -O https://s3.amazonaws.com/pronto-data/open_data_year_one.zip
ls
unzip open_data_year_one.zip
ls   
head 2015_trip_data.csv