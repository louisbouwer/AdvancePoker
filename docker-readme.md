# Advance Poker
This is a simplified poker game where the Python code deal 5 cards to make a hand and then define the class or type of the hand.

## Python Source Code
The program was written in python.  
It make use of the "treys" library to identify the poker hand of 5 drawn cards.  

## Install Docker Engine on Your System
Download the Docker client from here: https://www.docker.com/products/docker-desktop  

## Download the Docker Container
Open a Shell Command Line Interface (CLI) and type: docker pull drlouis/advancepoker  

##  Command to Run the Container
It is important to run the Docker container in interactive mode as follows:  
docker run --rm -i -t advpoker20img:alpha  
with:  
  - -rm : removes the container after used.  
  - -i : this is important to ensure the container provides an interactive interface.
  - -t : is the tag to use.

