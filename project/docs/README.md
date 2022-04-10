# How to run the project 

Follow step-by-step to setup the initial infrastructure in Google Cloud Platform (GCP)

* Create an account on GCP
* Create a new project
* Create a VM in Google by enabling the Compute Engine API.*
	* Select region and zone. Example: "us-central1 (Iowa)" and zone "us-central1-a". 
	* Machine type: E2-standard-4 (4 vCPU, 16 GB memory)
	* Ubuntu 20.04 LTS. 60 GB boot disk.
	* Allow full access to all Cloud APIs.
	* Allow HTTP/HTTPS traffic. 
* Generate SSH key. You can follow the next link. 
* Add the public generated ssh key to GCP -> Compute Engine -> Metadata
* If you are using Windows locally, move the private and public keys to the ./.ssh folder.
* Create a config file and put it in ./.ssh folder. You can use the config model in the repo. 
* Connect using GitBash to the VM by writing "ssh HostName" 
* Now you have a new working environment, install tools needed:
	- Anaconda. Get Linux installer from official website.
	- Docker

		```shell
		apt-get update 
		sudo apt-get install docker.io
		sudo groupadd docker
		sudo gpasswd -a $USER docker
		sudo service docker restart
		```
		- Restart the VM 
		- Run docker run hello-world to verify everything is setup.
		- Also, you can check if it was installed correctly by 
		```shell
			docker-composer --version
		```

	- Docker compose 
		- Donwload latest version from Github. 

		```shell
			wget https://github.com/docker/compose/ -O docker-compose
			chmod +x FileName #change file to executable
			export PATH="${HOME}/bin:${PATH}" #Edit the .bashrc file with the path for docker compose like 
			source .bashrc
		```
		- Check if it was installed correctly using
		```shell
			docker-composer --version
		```
	- Terraform
		- Download the latest Linux binary version for Amd64 using wget 
		- unzip the file
		- Create a service account to be used by terraform
	- Git repo 
		- Clone this Github repo in the VM using HTTPS


*Is it possible to run Terraform locally using a service account to connect to GCP and create the VM using the same Terraform code. Current local access doesn't allow me to install most of the tools needed. 


## Set-up infrastructure

For this purpose we are going to use terraform. 

* First you need to create a service account in GCP to allow Terraform make changes.
* Donwload the key and put it to some location and then set:
	```shell 
		export GOOGLE_APPLICATION_CREDENTIALS=~/credentials_path.json
	```
* Authenticate the account
	```shell
		gcloud auth activate-service-account --key-file $GOOGLE_APPLICATION_CREDENTIALS
	```

* Update the variables.tf file with your project_id, region, zone and credentials. 
* Run docker compose in the docker-compose directory
	```shell
		docker-compose build
	```
* Then run:
	```shell
		docker-compose -f ./docker-compose.yaml run --rm terraform init
		docker-compose -f ./docker-compose.yaml run --rm terraform apply
	```
* You should see all the changes applied. 

## Set-up airflow 

	```shell
	mkdir -p ./dags ./logs ./plugins
	echo -e "AIRFLOW_UID=$(id -u)" > .env
	```



## Useful links: 

### Docker
* https://londonappdeveloper.com/how-to-use-terraform-via-docker-compose-for-professional-developers/

* https://docs.divio.com/en/latest/reference/docker-docker-compose/

* https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/week_2_data_ingestion/airflow

* https://adamtheautomator.com/docker-compose-environment-variables/

### Bash 

* https://www.howtogeek.com/439199/15-special-characters-you-need-to-know-for-bash/


To run bash in docker container 

docker exec -it <container-ID> bash