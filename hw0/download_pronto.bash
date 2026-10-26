#!/bin/bash

mkdir -p pronto
cd pronto
echo "This dataset contains Pronto bike-sharing trip, station, status, and weather data from Seattle (Oct 2014 - Oct 2015)." > README.txt
mkdir -p data
cd data
curl -O https://s3.amazonaws.com/pronto-data/open_data_year_one.zip
unzip -o open_data_year_one.zip
head 2015_trip_data.csv
