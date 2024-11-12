## Create a ssh key and add to windows
ssh-keygen -t ed25519 -C "YOUR_MAIL@MAIL.com"

## Display your keys in finder
%USERPROFILE%\.ssh

Copy the key and save it in the github ssh keys


## Create a environment
python -m venv myenv 

## Activate environment
.\myenv\Scripts\activate.bat  

## Install Required Packages
.\pip install -r ..\..\requirements.txt 


## Run streamlit app
cd to chittimvp folder and run the below command

..\myenv\Scripts\streamlit run app.py

