read -p "Enter number: " n
i=$n
rev=0
negative="False"
if [ $i -lt 0 ]; then
        i=$((i*-1))
        negative="True"
fi
while [ $i -gt 0 ]
do
        rev=$(((rev*10) + (i%10)))
        i=$((i/10))
done
if [ $negative == "True" ]; then
        rev=$((-1*rev))
        echo "Reverse of $n = $rev"
else
        echo "Reverse of $n = $rev"
fi