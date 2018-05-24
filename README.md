![netmonastery](https://user-images.githubusercontent.com/2355314/40475725-e345a632-5f5f-11e8-9b08-3495caefbd32.jpg)
# AWS-Digi
****
### Project Description
Our main objective is to identify a dynamic dataset suitable for analysis through the platform, understand the key parameters of the dataset,parsing of the dataset,create a dashboard and generate alerts upon any anomalies recorded in the dataset.This project is all about how to analyze data real-time inside DNIF with the help of inbuilt function.  

# Table Of Content

* <a href="https://github.com/dnif/AWS-Digi/blob/master/README.md#introduction-to-dnif"> Introduction to DNIF</a>
* <a href="https://github.com/dnif/AWS-Digi/blob/master/README.md#dnif-installation"> DNIF Installation</a>
    * [Tools used for project]()
    * [Pre-Requisite]()
    * [Docker Installation]()
    * [DNIF configuration]()
    * [Web Console]()
* [About Webiron]()
    * [Key Metrics]()
    * [Interacting with DNIF]()
        * [DNIF interaction through Postman]()
        * [DNIF interaction through HTTP API]()
* [Analysis and Dashboard]()


# Introduction to DNIF
DNIF is a data platform that can collect, parse, enrich, index, balance, and analyse data in a continuously changing environment, helping enterprises take precautionary measures for cyber defence. It allows users to partition one data infrastructure and enable multiple teams to solve many challenges.

Apart from cybersecurity analytics, DNIF can also be used for any Big Data analytics use case, transaction analytics, fraud detection, analytics on IoT data, and financial risk analysis.

The platform offers consumers three types of deployment — on-premises (installed and runs on computers in the premises), on cloud, and virtual.

It offers four plans, including free, community, standard and enterprise, to suit the need and pocket of consumers. Consumers can subscribe as per usage and install DNIF on commodity servers. The software will then stream log data from servers, network devices, and security devices. Once downloaded, DNIF will ingest this data and identify threats using techniques like thresholding, lookups, profilers/baseliners, and machine learning.

# DNIF Installation
****
## Pre-requisites
* VirtualBox
* Ubuntu ISO
* DNIF Account

### System Requirement
* Minimum configuration required is 4 Cores
* 16GB RAM
* 200GB Disk Space

DNIF can be installed in any physical/virtual machine.[Check All the Pre-Requisites](https://dnif.it/docs/guides/getting-started/prerequisites.html)

> Note - The hardware ready reckoner only provides an indicative stack required to run DNIF. 
> You are free to start slow and upgrade your hardware as your usage builds up. 
> DNIF is built on a big data framework and therefore it can scale in phases.

## Virtual Box setting

Download Virtual Box [Download from here](https://www.virtualbox.org/wiki/Downloads) <br>
Set Minimum 4 GB Ram in System setting <br>
Go to Network setting, Under Attached Network Select Bridge Adapter

## Ubuntu

Download Latest version of Ubuntu from [here](https://www.ubuntu.com/download/desktop) <br>
Configure your Ubuntu and install in Virtual Box

## Docker Installation
Open terminal and copy paste following command in the terminal

1. Update the apt package index <br>
`sudo apt-get update`
1. Install packages to allow apt to use a repository over HTTPS<br>
 ` sudo apt-get install \ 
    apt-transport-https \ 
    ca-certificates \ 
    curl \ 
    software-properties-common`
1. Add Docker’s official GPG key
`curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -` <br>
1. Verify 
`sudo apt-key fingerprint 0EBFCD88` <br>
1. Set up the stable repository <br>
`sudo add-apt-repository \ 
"deb [arch=amd64] https://download.docker.com/linux/ubuntu \ 
   $(lsb_release -cs) \ 
   stable"`
1. Update the apt package index <br>
`sudo apt-get update`
1. Check For release <br>
`apt-cache madison docker-ce` or `apt-cache policy docker-ce`
1. Install Docker <br>
`sudo apt-get install docker-ce=17.06.2~ce-0~ubuntu`
You can replace after **=** for different release

1. Verify that Docker is installed correctly <br>
`sudo docker run hello-world`
1. Install python-pip <br>
`sudo apt-get install python-pip`
1. Install Docker-Compose <br>
`sudo pip install docker-compose`

> Note: If facing any difficulties with the above commands, please visit the Docker website where these
> steps are mentioned. Visit that webpage, and copy the command (that isn’t working from this list) and
> paste it as it is.

Docker Installation official Link:[Click here](https://docs.docker.com/install/linux/docker-ce/ubuntu/#set-up-the-repository)

## Configuring DNIF

1. Register Yourself [Sign Up](https://dnif.it/signup.html?plan=freeforever)
1. Download All in One File – Named as A10.[Click here to download A10 file](https://dnif.it/docs/guides/getting-started/installing-dnif.html)
1. Create folder on desktop (a10 folder) and paste a10 file inside this folder.
1. Open docker-compose.yml file and change following parameter/field
   1. `/path/to/volume:` Replace this text with the path where you would like to install the files (for example, /home/test/).
   1. `DKEY` : Put your own deployment key. Check email title: **DNIF: Getting Started**
   1. `CRIP` : Replace this value with the IP address of the machine on which the installation is being done.
In case you don't know IP address open terminal and type ifconfig and run command. 
> Try to keep localhost IP static. If it's dynamic. Check [this](https://github.com/dnif/AWS-Digi/wiki/How-to-make-Static-Ip#static-ip)
5. run `sudo docker-compose up` inside a10 directory. This command successfully performs a “pull” operation , which gets the latest code from the online repository and runs the same.

> Do not close the “Terminal” window after the above command has been executed, otherwise the application will cease  
>  to operate and terminate itself. However, you can minimize it.
6. Once the folder is created in the path specified in Volumes field, download license and
signature.bin files attached in mail **Title =DNIF - Getting Started**
7. Move both files in your_deployment_key_folder/LICENSE (the folder which got created in the Volumes
path specified).

> if not able to move file open new terminal and write this command `sudo chown -R $USER: $HOME`

## Web Console
1. Visit https://go.dnif.it/
1. Login. 

> You need Google Authenticator to generate OTP, your secret Auth key is specified in Email **Title:Sign In to Web Console** and visit [here](https://dnif.it/docs/guides/getting-started/signing-in.html)
> **Account Name**: DNIF
> **Key**: Provided in mail. Named as GAuth Key
> **DropDown**: Time Based
3. Once logged in, Go to Management Tab -> Connection -> Change Source Address Field (same as the one provided in CRIP. This is the Ubuntu IP address) and click on link and add SSL certificate.
4. Save and Update field.
5. Enjoy your DNIF installation and configuration is done.


If any doubt please wiki. Click [here](https://github.com/dnif/AWS-Digi/wiki/DNIF-Installation-Step-By-Step)
To get overview about installation check out our infographics, click [here](https://github.com/dnif/AWS-Digi/wiki/Installation-of-DNIF)

****

## Webiron
