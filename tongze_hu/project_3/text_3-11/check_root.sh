#!/bin/bash

check_root() {
	local TYPE=$1
	if [ $TYPE -eq 0 ]; then
		echo "You are admin"
	else
		echo "Error! You are not admin!"
	fi
}


check_root $EUID
