#!/usr/bin/env bash

df -H / | grep -v "Avail" |  awk '{ print  $4 }'
