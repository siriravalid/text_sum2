import os
from pathlib import Path # object oriented way to work with path files 
import logging # to log information during runtime as well

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "textSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep", # to do the cicd deployment, it we give commit github will automatically deploy in cloud
    f"src/{project_name}/__init__.py",# if we commit in github, empty folder cannot be uploaded, so thats why
    f"src/{project_name}/conponents/__init__.py",#constructor file, imports from one one to another, we need lccal package, in order to use locally, we need constructor file
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile", #deploying using docker
    "requirements.txt",
    "setup.py", #local package setup
    "research/trials.ipynb", #notebook experiments

]


for filepath in list_of_files: # looping through the list
    #filepath is being passed to the PATH Function
    # each one of the path is being passed and based on the operating system, path is detected
    filepath = Path(filepath) #converting path to our operating system format, in linus forward slash, linux backward slash etc..thats why we imported pathlib
    filedir, filename = os.path.split(filepath)#we want to create folder first and file next, so we separate them first, function returns 2 things, file directory and file name

    if filedir != "": #folder creating
        os.makedirs(filedir, exist_ok=True) # if we dont have folder it will not create, 
        logging.info(f"Creating directory:{filedir} for the file {filename}")# to see log in terminal

    # file creation, checking that the file does not exist, checking the size, is size of file is 0, then only create the file, in write mode
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f: #creating file in write mode
            pass
            logging.info(f"Creating empty file: {filepath}")# logging the info


    
    else:
        logging.info(f"{filename} is already exists")