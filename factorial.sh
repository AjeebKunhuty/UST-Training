factorial(){
	fact=1
	i=$n
	while [ $i -ge 2 ]
	do
		fact=$((fact*i))
		i=$((i-1))
	done
	echo "Factorial of $n = $fact"
}

read -p "Enter number to check factorial of: " n
factorial n
