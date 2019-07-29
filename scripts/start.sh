#!/bin/bash



docker run --rm -v $PWD:/src/img ravino/ins:recognition-image $1
