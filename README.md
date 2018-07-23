# WaMDaM Controlled Vocabularies
A Python/Django web application and REST API for managing the WaMDaM Controlled Vocabularies. This repository contains the source code for the master controlled vocabulary registry for the Water Management Data Model (WaMDaM).  
The configuration and deployment of the original repository have been significantly changed to be much simplified and automated using Ansible and Docker. A developer now can configure and deploy the app many times if they wish much easier than before.     

The production Controlled Vocabulary website for WaMDaM (which uses this code) can be accessed at: http://vocabulary.wamdam.org/
This online moderated registry aims to promote consistent terminology (i.e., Controlled Vocabularies-(CVs)) to describe water system components and their attributes across datasets, models, and users, while still retaining the native terms. Registering your model's native terms against these CVs will allow you to relate, query, and compare all of your water management data within a single database. 


## Required hardware and software 
* Linux or windows local machine 	
* A Web server to host this controlled vocabulary server. Here we use an Amazon Elastic Compute Cloud instance (Amazon EC2) at the Amazon Web Services (AWS). Ubuntu Server 16.04
*	Excel 2007 and on (.xlsx) to organize the CV terms and load them dynamically to the web-server in one command line 
*	MySQL to host the CV database in the server  
*	Python/Jango  
*	Docker to install software containers   
*	Ansible to deploy the repository from a local machine into the server
* Simple Mail Transfer Protocol (SMTP) server to send emails from the CV server to the moderator and the people who submit new terms. Here we use a Gmail smpt server   
*	reCAPTCHA service that protects the CV website from spam and abuse as far as submitting new CV terms  
* WinSCP which is a secure file transfer between a local Windows computer and a remote computer (server). It also helps navigate the content of the Linux machine in like windows. 
** PuTTY SSH terminal to connect from Windows to the emulator, serial console and network file transfer application.


# Steps to deploy the WaMDaM CV system 
This section provides step by step instructions on how to deploy the WaMDaM Django based application into an Amazon EC2 instance, using Ansible and Docker without previous knowledge of the app code. The instructions are meant for a programmer with background in Linux, Python, Django, cloud services, GitHub, MySql, and Domain Name System (DNS). However, the deployment and configuration has been simplified and automated to which can be reused many times easily.   


## 1.Create an Amazon Web Services account and an Amazon EC2 Instance  
First thing you will need is an account on Amazon Web Services (AWS) if you dont have any. Head to this link and follow the instructions to sign up: http://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/AboutAWSAccounts.html  
A Step by step details with screenshots to create an EC2 instance and get to know how to access it are provided here @
The third below assumes you already have an EC2 instance and you're connected to it.  

## 2. Set up the environment on your local machine (install Python and Ansible)  
To use this instructions you just need some basic knowledge on Linux Commands. Python, Django MySQL and Docker skills are desirable but not mandatory to deploy this application. 
You are going to deploy this application on remote hosts from a local machine that you have access to. To do so, you need to install some software on this local machine. These instructions are valid for any Debian based distributions (Ubuntu, Linux Mint, etc). Specific instructions for Windows systems are not provided here but these links might be useful:
* http://python-guide-pt-br.readthedocs.io/en/latest/starting/install/win/
* https://www.howtogeek.com/197947/how-to-install-python-on-windows/
* http://docs.ansible.com/ansible/intro_windows.html

Now, on your local machine with a Debian derivative system, the only requirement is Ansible itself, but first you need to install (as root) __pip__ if you don't have it already, using this command:

`apt install python-pip`

Now, install ansible using this command (again as root):

`pip install ansible`


## 3. Set up the server machine and deploy the application 
There are two ways to connect and transfer files to the EC2 Ubuntu Server. The first is PuTTY to type commands to the server and the seocnmd is WinSCP to trasnfer files. Instructions and screenshots on how you can use them are available here @ 

Before you deploy any application on this instance you need to install python on the EC2 instance. So, login to the instance using the __key pair__ previously provided when you created the EC2 instance. Once you login on the instance, run this command:

```
sudo apt install python
```

With this you will be ready to deploy applications into this instance using Ansible

To deploy the apps using Ansible you need the __key pair__ that you use to connect to the EC2 instance, for this example is named `WATER.pem`

Now, clone this repository in your local machine, if not, run this command: 

`git clone https://github.com/WamdamProject/WaMDaM_ControlledVocabularies`  

Now that you have the key pair and the cloned project, open a terminal on your local machine and change directory to the Ansible folder of the cloned repository. You may want to check the Ansible documentation on the README.md file on this folder, to learn about the parameters you can change to customize the deployment. 

https://github.com/WamdamProject/WaMDaM_ControlledVocabularies/tree/master/ansible#ansible-playbooks

When you are done customizing, run this command to deploy:

```
ansible-playbook -i hosts deploy.yml --private-key /<path-to-the-ec2-key>/<key-name>.pem
```

e. g:

```
ansible-playbook -i hosts deploy.yml --private-key /home/user/my-aws-keys/WATER.pem
```

Then you will see some output on your screen, pointing the steps that are being executed and its outcome. After a few minutes the deployment should be sucessful (if you don't see any messages in red color), meaning that your apps are up and running. Congratulations!
### Useful System Commands

The following commands are meant to be run in the EC2 instance once the applications are successfully deployed and running

* Create superuser
A superuser account is created during the deployment process with the credentials provided in `vars.yml`, but you can create another superuser account running this command: 
`sudo docker exec <appname> python manage.py createsu <user> <email> <password>`

* Reset tables on database
To clean the database to its original state run this command:

`sudo docker exec <appname> python manage.py reset_db`
If everything goes well you should not see any output

* Check logs

To check the logs of a given container run `docker logs -f <app_container>`

To close the logs hit `Ctrl + c`

* Backup and restore the database containers

To get a dump database directly from the containers you can use this command:

`sudo docker exec <app_container> /usr/bin/mysqldump -u root --password=<root-passwd> <db_name> > backup.sql`

To restore a dump into the container database use:

`cat backup.sql | sudo docker exec -i <db_container> /usr/bin/mysql -u root --password=<root-passwd> <db_name>`

You can find the <root-passwd> variable on the `vars.yml` file, in the `mysql_root_passwd` variable


### How to uninstall the application   
If you want to uninstall the WaMDaM application run the following commands from the EC2 instance, to remove the nginx virtualhost

```
# It is assumed that the 'clone_location' variable is set to "/home/ubuntu/env"
# if not, you need to change the code below to reflect its actual value
sudo rm -f /home/ubuntu/env/conf.d/wamdam1.conf
```

and then to remove the container

```
# Same as above, if you changed the 'wamdam_container' variable value then you have
# to reflect the changes in the code below
sudo docker rm -f wamdam1
```

lastly restart the nginx container

```
sudo docker restart nginx
```

## 4. Populate the application database from Excel  
To initially populate the application with controlled vocabulary terms and their definitions to all some or all of the tables, you can use this generic Excel (.xlsx) template. Fill out the data into Excel, then use the Terminal CMD.EXE

First you need to place the spreadsheets on the `spreadsheets` folder as it's set in the `vars.yml` file. This location is shared with the apps containers, that means that any file you place here would be accesible for both apps in the `spreadsheets` directory. 
 
First use the WinScp to upload the Excel file from Windows int othe Linux machine root dir, then move the Excel file into the spreadsheet dir. Note, permissions, do not allow uploading Excel file directly from Windows into the spreadsheet dir   
 `sudo mv WaMDaM_CVs_July2018.xlsx spreadsheets`

Then run:

`sudo docker exec <appname> python manage.py populate_db /spreadsheets/<excel-file-full-path>`

e. g:

`sudo docker exec wamdam1 python manage.py populate_db /spreadsheets/WaMDaM_CVs_June20.xlsx`

Same as the previous step, if everything goes well you should not see any output. After this all the data should be correctly loaded to the server. 

* Considerations about the spreadsheet format
* Sheet names should match table names
* Sheet column titles must also match table fields
* The content of the `term` column must not contain spaces anywhere. Also you must avoid symbols. Numbers are ok


## 5. Set up the EC2 URL to a domain of your choice (e.g., GoDaddy)
Once deployed, the application will have a URL like this one: ec2-35-162-109-121.us-west-2.compute.amazonaws.com. We provide instructions if you want to set it up to a specific domain. 

Login to your account in GoDaddy. Domains -> My Account -> Domain Management (e.g., wamdam.org)-> DNS Manager. Click "Edit Zone" when it appears. Associate domain with Elastic IP. In the Zone Editor, you will see several tables. In the table where it says "A (Host)", find the entry where Host = "@". Click on that entry to edit the field for "Points to". Add the elastic IP you just got from Amazon. Click "Save Zone File" when you are done. Then we save this record configuration, this is likely to take some minutes until it takes effect.

Check on the current state of DNS propagation after having made changes to your domains records @ 
https://www.whatsmydns.net

See how the site appears to the rest of the world @ https://geopeeker.com/


### Licensing  
WaMDaM and materials in this GitHub repository are disturbed under a BSD 3-Clause [LICENSE](/LICENSE). 
For alternative licensing arrangements, contact Adel M. Abdallah or David E. Rosenberg directly.    


### Sponsors and Credit 
We adapted the design of this registry from the source code of the ODM2 ControlledVocabularies available on GitHub @ https://github.com/ODM2/ODM2ControlledVocabularies. Thanks to Dr. Jeff Horsburgh and the ODM2 team for promoting #OpenScience by publishing their source code.   

This server of the WaMDaM registry is deployed on Amazon Web Services (AWS) thanks to AWS Educate for their support. Thanks to Jose Guerrero, the configuration and deployment of the original repository have been significantly changed to be much simplified and automated using Ansible and Docker. A developer now can reconfigure and deploy the app many times if they wish much easier than before.   
 
WaMDaM and related software development have been developed under funding from several different sources. It was primarily supported by the National Science Foundation <a href="http://www.nsf.gov/awardsearch/showAward?AWD_ID=1135482" target="_blank">CI-Water Project</a> and later from the <a href="https://www.nsf.gov/awardsearch/showAward?AWD_ID=1208732" target="_blank">iUtah Project</a>. 
Any opinions, findings, and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the National Science Foundation.    

WaMDaM has been developed at and also additionally funded by the Utah Water Research Lab at Utah State University, Logan Utah during the period of August, 2012-2017. Thanks to Dr. Steven Burian at the University of Utah, Salt Lake City Utah for hosting Adel Abdallah as a visiting scholar 2014-2017.
