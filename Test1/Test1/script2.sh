#script2

echo "What is your birthday month number?"
read monthofyear

if [ "$monthofyear" = 1 ]
then
        echo "January"

elif [ "$monthofyear" = 2 ]
then
        echo "February"

elif [ "$monthofyear" = 3 ] 
then
        echo "March"

elif [ "$monthofyear" = 4 ] 
then
        echo "April"

elif [ "$monthofyear" = 5 ] 
then
        echo "May"

elif [ "$monthofyear" = 6 ] 
then
        echo "June"

elif [ "$monthofyear" = 7 ] 
then
        echo "July"

elif [ "$monthofyear" = 8 ] 
then
        echo "August"

elif [ "$monthofyear" = 9 ] 
then
        echo "September"

elif [ "$monthofyear" = 10 ] 
then
        echo "October"

elif [ "$monthofyear" = 11 ] 
then
        echo "November"

elif [ "$monthofyear" = 12 ] 
then
        echo "December"

else
        echo "Sorry, $monthofyear not recognized. Now exiting the program"
        exit 1
fi

exit 0

