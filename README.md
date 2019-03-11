# pyEPICSDocker
Docker container for running python scripts using the python EPICS API

To run, first build:
```bash
sudo docker build -t pyep .
```

Then initiate and instance with the docker run command:
```bash
sudo docker run  --name=testpyep -it pyep
```
This will launch an interactive bash env so you can see it spitting out value of the test channel C3:EXP-modbusDocker (the default). There is no need to expose ports as the docker is reaching out to the network for connections, outside containers are not requesting access into the container.

You can run this along side fincle/modbusEPICSDocker for testing.  

More to come.


---
Note: that the system architecture is hard coded to linux-x86_64 in at least two places in this Dockerfile.  If you are seeking to run this docker on an ARM (raspberry pi, etc) then you will need to probably change these to the relevant value for your system.
