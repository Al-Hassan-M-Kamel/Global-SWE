

# commands

# Delete all containers...

-> docker container rm -f $(docker container ls -q)

# Delete all images...

-> docker image rm -f $(docker image ls -q)

-> go to troubleshooting and clean purge data and restart the engine...