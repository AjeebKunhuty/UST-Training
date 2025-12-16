sumOfN(){
	sum=0
	for ((i=1;i<=n;i++ ))
	do
		sum=$((sum+i))
	done
	echo "Sum upto $n = $sum"
}

read -p "Enter n: " n
sumOfN n
