#script3

echo "How many classes are you taking?"
read classes

foo=1
while [ "$foo" -le "$classes" ]
do
	echo "How many credits is this class worth?"
	read credit
	foo=$(($foo+1))
done

exit 0

