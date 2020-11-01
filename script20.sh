#!/bin/bash

while [[ true ]]
	do
	echo "Enter workout_duration (sec):"
	read wk_dur
	if [[ -z $wk_dur || $wk_dur -eq 0 ]]
	then echo "Тraining parameters cannot be calculated"
	break
	else echo "Workout duration is $wk_dur sec."
	fi

	echo "Therapeutic cardio zone (sec):"
	read zone1
	echo "Low cardio zone (sec):"
	read zone2
	echo "Aerobic cardio zone (sec):"
	read zone3
	echo "Anaerobic cardio zone (sec.):"
	read zone4
	echo "Red line cardio zone (sec.):"
	read zone5
	if [[ $zone1 -eq 0 && $zone2 -eq 0 && $zone3 -eq 0
	       && $zone4 -eq 0 && $zone5 -eq 0 ]]
	then echo "Тraining parameters cannot be calculated"
	break
	else 
		let w_pts="($zone1+$zone2*6/5 + $zone3*2+$zone4*5/2+$zone5*6)/60"
	echo "Workout points:"
       	echo "scale=2;$w_pts" |bc
	fi
done
