#!/bin/bash

for i in {1..10}; do
	touch "test${i}.txt"
done

j=1
while [ $j -le 10  ]; do
	rm "test${j}.txt"
	((j++))

done
