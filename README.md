========================================================================================
Traditional way of running docker
========================================================================================
Building Image=
docker build -f Dockerfile -t my-dev-image .
#-f means from which file
#-t means what tag should we give our image (name)
#. tells where our Dockerfile is located
#this will only create the image not container


Check all the images we build
docker image


Inspect the image we build
docker inspect my-dev-image


Running the container
docker run -d --name dev-cont1 -p 8000:8000 my-dev-image
#run will not only run the container, it will also create the container
#-d (detach) will run everything in the background and leave the terminal free for us to use
#port laptop:host 
#the port for container is fixed and can not be changed


Check the logs
docker logs dev-cont1


Check the containers running
docker ps


Check all the containers created and running
docker ps -a


Test the container
docker run -it --rm my-dev-image /bin/bash -c "poetry run pytest"
#-it (interactive mode) we are telling the docker to take us inside the running container/connect with it
#--rm means that we are telling the docker to remove this container when you are done
#/bin/bash where to connect the Dockerfile with
#-c command to run i.e "poetry run pytest"


Stop the container
docker stop dev-cont1


Remove a container
docker rm dev-cont1


Exit from your container
exit

========================================================================================
Dev Container
========================================================================================
Install Dev Container Extension
Goto Remote Explorer
Open In folder
Select The dir where Dockerfile is placed
Click on Workspace
Select Dockerfile
Hit ok


The container and the image will start to build and a new window will open
We are now inside the docker container


in terminal run the command:
poetry run uvicorn docker_prac.main:app --reload


To exit from the container
right click on the running container in the remote explorer window
click on open window in local file

========================================================================================
DOCKER COMPOSE
========================================================================================
Run the container=
docker compose up -d
#this will automatically create the image and up the container


Read all the things mentioned and not mentioned in yml file=
docker compose config


Check the running containers
docker compose ps
#read the compose file first and then show


Stop the container
docker compose stop


Start the container
docker compose start


Remove the container
docker compose down


If we do some changes in the code we will need to rebuild the image
#docker compose down
#docker compose up -d --build

========================================================================================
docker compose + dev containers
========================================================================================
docker compose up -d
poetry run uvicorn docker_prac.main:app --reload
run remote explorer
new terminal
open explorer
open folder
enter the workdir we enetered in our dockerfile i.e /app/


While staying inside dev container it will be connected to our vs code and see the changes live