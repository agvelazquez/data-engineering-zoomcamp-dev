### How to run the project 

1- Create an account on GCP
2- Create a new project
3- Create a VM in Google by enabling the Compute Engine API.*
	- Select region and zone. Example: "us-central1 (Iowa)" and zone "us-central1-a". 
	- Machine type: E2-standard-4 (4 vCPU, 16 GB memory)
	- Ubuntu 20.04 LTS. 60 GB boot disk.
	- Allow full access to all Cloud APIs.
	- Allow HTTP/HTTPS traffic.
4- Generate SSH key. You can follow the next link. 
5- Add the public generated ssh key to GCP -> Compute Engine -> Metadata
6- If you are using Windows locally, move the private and public keys to the ./.ssh folder.
7- Create a config file and put it in ./.ssh folder. You can use the config model in the repo. 
8- Connect using GitBash to the VM by writing "ssh HostName" 
9- Now you have a new working environment, install tools needed:
	- Anaconda. Get Linux installer from official website.
	- Docker. Use sudo apt-get update then sudo apt-get install docker.io. To include docker within sudo: -sudo groupadd docker
				 -sudo gpasswd -a $USER docker
				 -sudo service docker restart
				 -Restart the VM 
				 -Run docker run hello-world to verify everything is setup.
	- Docker compose 
				- Donwload latest version from Github using wget https://github.com/docker/compose/ -O docker-compose
				- chmod +x FileName to change file to executable
				- Edite the .bashrc file
	- Git repo. Clone this Github repo in the VM using HTTPS


*Is it possible to run Terraform locally using a service account to connect to GCP and create the VM using the same Terraform code. Current local access doesn't allow me to install most of the tools needed. 