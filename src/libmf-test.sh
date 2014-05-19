#!/bin/sh

set -e

libmf=../lib/libmf-1.1/libmf
subtrain=../data/libmf/subtrain
val=../data/libmf/val
test=../data/libmf/test

${libmf} convert ${subtrain} subtrain.bin
${libmf} convert ${val} val.bin
${libmf} convert ${test} test.bin
${libmf} train --tr-rmse --obj -k 40 -s 4 -p 0.05 -q 0.05 -g 0.003 -ub -1 -ib -1 --no-use-avg --rand-shuffle -v val.bin subtrain.bin model
${libmf} predict test.bin model output
