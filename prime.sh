prime(){
	isPrime="True"
	if [ $1 -lt 0 ]; then
		echo "Negative number cannot be computed"
	elif [ $1 -le 1 ]; then
		echo "Neither Prime nor Composite"
	elif [ $1 -le 3 ]; then
		echo "Prime"
	elif [ $(($1 % 2)) -eq 0 ]; then
		echo "Composite"
	else
		i=3
		while [ $i -lt $1 ]
		do
			if [ $(($1 % $i)) -eq 0 ]; then
				echo "Composite"
				exit 0
			else
				i=$((i+2))
			fi
		done
		echo "Prime"
	fi
}

prime $1
