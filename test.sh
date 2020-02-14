#!/bin/bash

revid=$(git log -n 1 --grep=merge -i --pretty=format:"%h")
echo $revid
#git checkout $revid
