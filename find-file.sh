#!/bin/bash

if ! grep -q "$1" "allturtles.txt";then

	echo "$1" >> "allturtles.txt" 
fi
