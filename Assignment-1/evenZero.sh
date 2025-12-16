oddEvenZero(){
        if [ $n -eq 0 ]; then
                echo "$n is Zero"
        else if [ $(($n%2)) -eq 0 ]; then
                        echo "$n is Even"
                else
                        echo "$n is Odd"
                fi
        fi
}

read -p "Enter number: " n
oddEvenZero n