#!/bin/bash

for py_file in $(find ../script -script *.py)
do
    python $py_file
done
