#!/bin/sh

set -e

# Define library folder location.
LIBMF=../lib/libmf-1.1/libmf

# Define data set location.
SUBTRAIN=../data/libmf/subtrain
VAL=../data/libmf/val
TEST=../data/libmf/test

# Build (make) libmf executable if it does not exist.
if [ ! -f $LIBMF ];
then
  echo "File $LIBMF does not exist. Building it first..."
  cd ../lib/libmf-1.1/
  make
  cd -
fi

# Convert data sets to binary files.
${LIBMF} convert ${SUBTRAIN} subtrain.bin
${LIBMF} convert ${VAL} val.bin
${LIBMF} convert ${TEST} test.bin

# Train.
${LIBMF} train --tr-rmse --obj -k 40 -s 4 -p 0.05 -q 0.05 -g 0.003 -ub -1 -ib -1 --no-use-avg --rand-shuffle -v val.bin subtrain.bin model

# Predict.
${LIBMF} predict test.bin model output
