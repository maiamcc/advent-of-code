#! /usr/bin/env bash

echo $1 | entr /bin/sh -c "clear; python $1"
