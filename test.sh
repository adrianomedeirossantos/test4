#!/bin/bash

set -e

if [[ $CI_MESSAGE != *"--skip-test"* ]]
then
	make ci
else
	echo "Instructed to Skip tests during this build"
fi
