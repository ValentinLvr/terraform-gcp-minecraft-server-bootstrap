# Minecraft server bootstrap with terraform & GCP

This repo contains components to create a minecraft server.

## prerequisites
- Have `gcloud` & `terraform` cli installed on your shell
- Have a GCP account & a GCP project with a billing account linked to it

## steps
### Initialization
1. Run init script with your GCP project & region
```shell
chmod +x init.sh
./init.sh --project GCP_PROJECT --region GCP_REGION --zone GCP_ZONE
```

2. Run terraform initialization
```shell
terraform init
```

### Infrastructure Installation
Run terraform apply
```shell
terraform apply
```

this will install all infrastucture components to run the minecraft server

### Download & install minecraft
1. connect to your newly created virtual machine via the GCP console
2. upgrade packages
```shell
sudo apt update && sudo apt upgrade
```
3. install java & screen
```shell
sudo apt install openjdk-17-jre-headless && sudo apt install screen
```
4. download minecraft server (1.20.4)
```shell
wget https://piston-data.mojang.com/v1/objects/8dd1a28015f51b1803213892b50b7b4fc76e594d/server.jar && \
mkdir /home/minecraft/ && \
mv server.jar /home/minecraft/minecraft_server.1.20.4.jar
```
5. Setup minecraft server
    1. 
    ```shell
    screen && \
    java -Xms1G -Xmx3G -jar minecraft_server.1.20.4.jar nogui
    ```
    It will prompt an error. It is normal ! do not worry.
    2. change the `eula.txt`
    ```shell
    vim /home/minecraft/eula.txt
    ```
    change `eula=false` to `eula=true`
6. (Optional) Update your server properties
```shell
vim /home/minecraft/server.properties
```
7. Add the backup script
```shell
touch /home/minecraft/backup.sh
```
copy the script below and add it to the newly created `backup.sh` file
```shell
#!/bin/bash
screen -r mcs -X stuff '/save-all\n/save-off\n'  # -> save the worlds, désactivate the auto saving
/usr/bin/gsutil -m cp -R /home/minecraft/world gs://minecraft-backup/$(date "+%Y%m%d-%H%M%S")-world # -> copy the saved data to our bucket
screen -r mcs -X stuff '/save-on\n' # -> re-activate the auto saving
```
8. Everything is setup ! :tada: close your VM

### Run the server & enjoy
1. go to your start cloud function http address. It will start your VM and give you its IP ! it should be https://GCP_REGION-GCP_PROJECT.cloudfunctions.net/start-minecraft-server
2. when you finish, do not forget to stop the VM by clicking the shutdown button on the cloud function url. it should be https://GCP_REGION-GCP_PROJECT.cloudfunctions.net/stop-minecraft-server

## Nota Bene
- We use Ephemeral IP for cost saving. Thus, the IP will change at each VM start.
- We also use SPOT VM for cost saving. Thus the VM will necessarly stop within 24h. You have to start it again when it appears

## Script used
### Startup script
```
#!/bin/bash
cd /home/minecraft
screen -d -m -S mcs java -Xms1G -Xmx3G -jar /home/minecraft/minecraft_server.1.19.3.jar nogui
```
We use screen to run the server on the background
NB: we use the flags -d -m because there is no terminal on the startup script

### Shutdown script
```
#!/bin/bash
/home/minecraft/backup.sh
screen -r mcs -X stuff '/stop\n'
```

### Backup script:
```
#!/bin/bash
screen -r mcs -X stuff '/save-all\n/save-off\n'  # -> save the worlds, désactivate the auto saving
/usr/bin/gsutil -m cp -R /home/minecraft/world gs://minecraft-backup/$(date "+%Y%m%d-%H%M%S")-world # -> copy the saved data to our bucket
screen -r mcs -X stuff '/save-on\n' # -> re-activate the auto saving
```

