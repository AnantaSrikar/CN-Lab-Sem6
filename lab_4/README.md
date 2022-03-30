# Lab-4
Implement an Application Level file sharing protocol. 
Problem Setting: Two network clients listening for requests waiting to share files (FTP)

### Programming Tasks
1. Know list of files on each other's machines in designated shared folders
2. Upload a file to each other
3. Download a file to each other

## Execution
- First, head over to the right directory which will contain both the `server.py` and `client.py` files.
- Make a virutal environment to install the ftp server package by running `python3 -m venv env`.
- Activate virtual environment with the command `source env/bin/activate`.
- Its suggested to run `pip3 install --upgrade pip setuptools` to get the latest base packages.
- Install necessary packages by running `pip3 install -r requirements.txt`
- Run `python3 server.py` to start the server.
- Run `python3 client.py` to start the client.