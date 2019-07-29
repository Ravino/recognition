Start for recognition image
Dependinces: docker and files of format .jpg
In Directory "scripts" are automaticly building and load image from hub docker
Commands:
1. git clone https://github.com/Ravino/recognition.git
cd ./recognition
sudo chmod +x scripts/start.sh
sudo ln -s ./scripts/start.sh /usr/bin/recognition-image


You can specify the path to the script to the bash interpreter,but you will have to do it all the time

For recognition image input command
Go to the directory with images of numbers
cd ./img

Running command for recognition
recognition-image 1.jpg

