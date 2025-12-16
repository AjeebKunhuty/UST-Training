add(){
	echo "$1 + $2 = $(( $1 + $2 ))"
}
subtract(){
	echo "$1 - $2 = $(( $1 - $2 ))"
}
multiply(){
	echo "$1 * $2 = $(( $1 * $2 ))"
}
divide(){
	if [ $2 -eq 0 ]; then
		echo "Divisor cannot be zero"
	else
		echo "$1 / $2 = $(( $1 / $2 ))"
	fi
}

while :
do
	read -p "Enter numbers: " a b
	echo "1.Add   2.Subtract   3.Multiply   4.Divide   5.Exit"
	read choice
	case $choice in
		1) 	add $a $b ;;
		2) 	subtract $a $b ;;
		3) 	multiply $a $b ;;
		4) 	divide $a $b ;;
		5) 	echo "Exiting..."
		   	exit 0 ;;
		*) 	echo "Invalid choice" ;;
	esac
done
