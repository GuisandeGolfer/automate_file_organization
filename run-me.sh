#!/usr/bin/env bash

user=$(whoami)
current_directory=$(pwd)

echo "Welcome to the Python Watchdog Folder Automation Tool"

sleep 2

echo "Let's start by configuring a couple of file locations ..."

sleep 2 

echo "What path do you want this script to monitor changes? ('Desktop', 'Downloads', or full-path-name"

read source_dir

if [[ $source_dir -eq "Desktop" ]]; then  
    echo "Desktop is a nice location to de-clutter"
    source_dir="/Users/$user/Desktop"
    export source_dir

elif [[ $source_dir -eq "Downloads" ]]; then
    echo "Downloads folder works! keep it nice and organized"
    source_dir="/Users/$user/Downloads"
    export source_dir
else
    echo "CooL! went with your own custom path location"
    export source_dir
fi

# tip: make sure there is a space next to the colon for doing multi-line comments

#    Everything is operational above this multi-line comments
#    all I need to do next is 
#        1. [x] fill out the rest of the directory instantiating
#        2. [x] figure out how to add those variables into my python script automatically (exporting variable and then pulling them later into python script)
#        3. [x] and then run "main.py" (just write "python3 main.py" directly in the bash script)
#        4. add error-handling for when bash runs the commands "python3 main.py" 

echo "Where do you want to put images?"

read image_location

echo "gotcha, folder name recieved" 

export image_location

echo "...videos?"

read video_directory
export video_directory

echo "...customer documents?"

read customer_result
export customer_result 

echo "do you want to designate a location for one_drive?"

read one_drive_result
export one_drive_result

echo -e " Is this information correct?: \n $source_dir \n $image_location \n $video_directory \n $customer_result \n $one_drive_result"

python3 main.py
