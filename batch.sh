#!/usr/bin/env bash
python dataset_batch.py 0 12500 1 &
python dataset_batch.py 12500 25000 2 &
python dataset_batch.py 25000 37500 3 &
python dataset_batch.py 37500 50000 4 &
python dataset_batch.py 50000 62500 5 &
python dataset_batch.py 62500 75000 6 &
python dataset_batch.py 75000 87500 7 &
python dataset_batch.py 87500 100000 8 &
