![netmonastery](https://user-images.githubusercontent.com/2355314/40475725-e345a632-5f5f-11e8-9b08-3495caefbd32.jpg)
# AWS-Digi
****
### Project Description
Our main objective is to identify a dynamic dataset suitable for analysis through the platform, understand the key parameters of the dataset,parsing of the dataset,create a dashboard and generate alerts upon any anomalies recorded in the dataset.This project is all about how to analyze data real-time inside DNIF with the help of inbuilt function.  

# Table Of Content

* <a href="https://github.com/dnif/AWS-Digi/blob/master/README.md#introduction-to-dnif"> Introduction to DNIF</a>
* <a href="https://github.com/dnif/AWS-Digi/blob/master/README.md#dnif-installation"> DNIF Installation</a>
    * <a href="https://github.com/dnif/AWS-Digi/blob/master/README.md#tools"> Tools used for project</a>
    * <a href="https://github.com/dnif/AWS-Digi/blob/master/README.md#pre-requisites"> Pre-Requisite</a>
    * <a href="https://github.com/dnif/AWS-Digi/blob/master/README.md#docker-installation"> Docker Installation</a>
    * <a href="https://github.com/dnif/AWS-Digi/blob/master/README.md#configuring-dnif"> DNIF configuration</a>
    * <a href="https://github.com/dnif/AWS-Digi/blob/master/README.md#web-console"> Web Console</a>
* <a href="https://github.com/dnif/AWS-Digi/blob/master/README.md#webiron"> About Webiron</a>
    * <a href="https://github.com/dnif/AWS-Digi/blob/master/README.md#key-metrics"> Key Metrics</a>
    * <a href="https://github.com/dnif/AWS-Digi/blob/master/README.md#interacting-with-dnif"> Interacting with DNIF </a>
	* <a href="https://github.com/dnif/AWS-Digi/blob/master/README.md#dnif-interaction-through-postman"> DNIF interaction through Postman </a>
        * <a href="https://github.com/dnif/AWS-Digi/blob/master/README.md#dnif-interaction-through-http-api"> DNIF interaction through HTTP API </a>
* <a href="https://github.com/dnif/AWS-Digi/blob/master/README.md#analysis-and-dashboard"> Analysis and Dashboard</a>


# Introduction to DNIF
DNIF is a data platform that can collect, parse, enrich, index, balance, and analyse data in a continuously changing environment, helping enterprises take precautionary measures for cyber defence. It allows users to partition one data infrastructure and enable multiple teams to solve many challenges.

Apart from cybersecurity analytics, DNIF can also be used for any Big Data analytics use case, transaction analytics, fraud detection, analytics on IoT data, and financial risk analysis.

The platform offers consumers three types of deployment — on-premises (installed and runs on computers in the premises), on cloud, and virtual.

It offers four plans, including free, community, standard and enterprise, to suit the need and pocket of consumers. Consumers can subscribe as per usage and install DNIF on commodity servers. The software will then stream log data from servers, network devices, and security devices. Once downloaded, DNIF will ingest this data and identify threats using techniques like thresholding, lookups, profilers/baseliners, and machine learning.

# DNIF Installation
****
## Tools

	- Virtual Box
	- JetBrains: PyCharm Community Edition
	- Ubuntu 16.04 or above
	- Docker
   
## Pre-requisites
* VirtualBox
* Ubuntu ISO
* DNIF Account

## System Requirement
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

# Webiron

Webiron provides a comprehensive managed security service that will keep your web servers safe from harm. Webiron's intelligent technology is designed to immediately detect, block and prevent automated bot and malware attacks.

## Key Metrics
Abuse e-mail feed contains a log of our abuse reports and status of the issue reported. This feed is filterable by e-mail address, IP address, or ASN number. This is the master feed for the Twitter “bad abuse” feed and is pulled from live data.

<table>
   <tr>
      <td>Field</td>
      <td>Description</td>
   </tr>
   <tr>
      <td>Log Entry Type</td>
      <td>ontains the action. This is either, report sent, report opened, report or if the host has replied with a resolved statement.</td>
   </tr>
   <tr>
      <td>Log Time</td>
      <td>Time action was done.</td>
   </tr>   
   <tr>
      <td>Attacker IP</td>
      <td>The IP reported for issues (lookup link forwards to IP lookup page). The “IP” link filters the feed by the IP while the “lookup” provides more detailed information on the IP.</td>
   </tr>     
   <tr>
      <td>Logged E-Mails</td>
      <td>These are either a list of e-mail addresses reported to for the attacker IP or the address that responded to a resolved or opened event. Clicking on an e-mail will filter the feed by that e-mail address.</td>
   </tr>      
   <tr>
      <td>Log Message</td>
      <td>The list of issues reported or an action message.</td>
   </tr>      
   <tr>
      <td>Deliverable</td>
      <td>Was the e-mail accepted by the host?</td>
   </tr>      
   <tr>
      <td>Days Unresolved</td>
      <td>The number of days the issue since the issue was reported to the host.</td>
   </tr>      
   <tr>
      <td>Incidents Reported</td>
      <td>The number of incidents reported. Some bots use thousands of nodes rather than heavier concentrations from fewer hosts. The damages are the same however.</td>
   </tr>
</table>

## Interacting with DNIF

You can interact with DNIF in two ways
1. Through Event Store.
To read more about event store ,click [here](https://dnif.it/docs/guides/tutorials/using-eventstore.html)
2. Through live dataset using connectors.
3. Using in built DNIF data models,to know about these data model click [here](https://dnif.it/docs/explore/index.html)

### DNIF interaction through Postman
Please refer to wiki , click [here](https://github.com/dnif/AWS-Digi/wiki/Dynamic-dataset-handle-with-Postman)
### DNIF interaction through HTTP API
Please refer to wiki , click [here](https://github.com/dnif/AWS-Digi/wiki/Dynamic-dataset-handle-with-HTTP-API)

# Analysis and Dashboard
* List of event message:<br>
Query:<br>
` _fetch * from event limit 100 >>_agg count_unique $event_msg`
 
![2 event msg](https://user-images.githubusercontent.com/2355314/40480212-69a5ecfe-5f6b-11e8-8aff-e63dc6a9b0c7.png) 
![2 event msg output](https://user-images.githubusercontent.com/2355314/40480211-691f8178-5f6b-11e8-883c-e2500ff50e7f.png)
![2 event msg_op](https://user-images.githubusercontent.com/2355314/40480213-6a6c0cfe-5f6b-11e8-8585-6013be9743e4.png)


* List of entry type <br>
Query:<br>
`_fetch * from event limit 100 >>_agg count_unique $entry_type`

![3 listentrytype](https://user-images.githubusercontent.com/2355314/40480217-6b58a582-5f6b-11e8-85f8-a88398ad4ee3.png)
![3 list entry type output](https://user-images.githubusercontent.com/2355314/40480215-6afc40d0-5f6b-11e8-99bd-7deb5fbec2ed.png)
![3 listentrytype_op](https://user-images.githubusercontent.com/2355314/40480220-6bd7b2a0-5f6b-11e8-8212-2f2ae1232f10.png)

* Days Unresolved <br>
Query:<br>

`_fetch * from event limit 100 >>_agg count_unique $days_unresolved`

![4 daysunresolved](https://user-images.githubusercontent.com/2355314/40480948-8fb82612-5f6d-11e8-9c4f-5b82d773bde6.png)
![4 days unresolved output](https://user-images.githubusercontent.com/2355314/40480947-8f74c8b8-5f6d-11e8-9be9-33118210455b.png)
![4 daysunresolved_op](https://user-images.githubusercontent.com/2355314/40480949-9024b87c-5f6d-11e8-8627-2fc45f8e9443.png)

 * IP which is reported more than 4 times <br>
 Query: <br>
 
 `_fetch * from event where $entry_type= report group count_unique $attacker_ip >>_checkif int_compare count_unique >4 include`
 
![5 repeatattack](https://user-images.githubusercontent.com/2355314/40480227-6e2157f0-5f6b-11e8-9158-2ca4a886c3c5.png)
![5 repeatattackoutput](https://user-images.githubusercontent.com/2355314/40480231-6f659a18-5f6b-11e8-8db7-0785ff6d052f.png)
![5 repeatattack_op](https://user-images.githubusercontent.com/2355314/40480229-6eb663f4-5f6b-11e8-9f3e-5ee00c262cdc.png)

 
* List of event emails <br>
Query: <br>

`_fetch * from event limit 100 >>_agg count_unique $event_emails`

![6 event spam](https://user-images.githubusercontent.com/2355314/40480233-70863e5c-5f6b-11e8-98f2-31a75c5bee31.png)
![6 spam email output](https://user-images.githubusercontent.com/2355314/40480238-71f3cee4-5f6b-11e8-8a30-8cba4310a07a.png)
![6 email spam op](https://user-images.githubusercontent.com/2355314/40480235-71123e66-5f6b-11e8-8259-652aaf58f69d.png)

## Dashboard
 Dashboard is DNIF function where you can do threat analysis visually. But to do that you need to create different widgets and then add those widget to dashboard
 
![dashboard1](https://user-images.githubusercontent.com/2355314/40480242-732350fa-5f6b-11e8-82ae-148a8486e9e4.png)
![dashboard2](https://user-images.githubusercontent.com/2355314/40480243-74389f0e-5f6b-11e8-9e3a-d7a66939f7ef.png)
