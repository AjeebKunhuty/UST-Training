fileExistence(){
	if [ -f $1 ]; then
		echo "File exists"
		filePermissions $1
	else
		echo "File Not Found"
	fi
}

filePermissions(){
	if [ -r $1 ]; then
		echo "Readable"
	else
		echo "Not readable"
	fi
	if [ -w $1 ]; then
		echo "Writable"
	else
		echo "Not writable"
	fi
	if [ -x $1 ]; then
		echo "Executable"
	else
		echo "Not Executable"
	fi
}

fileExistence $1
