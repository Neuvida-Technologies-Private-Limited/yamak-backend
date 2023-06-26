## yamak-llm-automation-backend

# Important commands

# Steps to create virtual environment
    * create a virtual environment ```python3 -m virtualenv venv```
    * acivate a virtual environment ```source ./venv/bin/activate```

# Backend server setup on ec2
* SSH into the server 
    dev  ```ssh -i yamak-dev.pem ubuntu@<server-ip>```
    prod ```ssh -i yamak-prod.pem ubuntu@<server-ip>```
    <br />
    > **_NOTE:_**  For error: Permission denied (publickey) use: ```chmod 400 <key-file.pem>``` 

* Update the system
    ```sudo apt-get update```
    <br />
* Generate a new SSH key and add it to the ssh-agent
    [Link](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

* Copy the ssh key
    ```cat < ~/.ssh/id_ed25519.pub```
* Add the key to github account
    [Link](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)    

# Steps to run the backend
* Create a .env file ```touch .env```
* Copy sample.env to .env ```cp sample.env .env```
* Paste the correct .env values in the file.
    > **_NOTE:_**  Take the values from another dev

