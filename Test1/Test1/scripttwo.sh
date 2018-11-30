#scripttwo

echo "How old is the child?"
read age

if [ "$age" = 3 ]
then
	echo "You get a pet potato"
elif [ "$age" = 10 ]
then
	echo "You get a pet rock"
else
	echo "You get a pet Chupacabra"
	exit 1
fi
exit 0
