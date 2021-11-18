# variables
containername = hotline
imagename = sannae/hotline

# build image
buildhotline:
	sudo docker build -t $(imagename) .

# run container
runhotline:
	sudo docker run --name hotline -d -p 8000:8000 $(imagename)

# remove container
removehotline:
	sudo docker stop $(containername)
	sudo docker rm $(containername)