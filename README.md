# Model Maker Object Detection.

## VSCode integration
VS Code is capable of connecting to an existing Remote Jupyter Server. For that open the `Model_Maker_Object_Detection.ipynb` or any other `.ipynb` file and look for the Jupyter add-on on the bottom of vscode. 
  1. Click on the Jupyter add-on on the bottom of vscode
  2. Give the IP-Address of the server (http://192.168.209.26:8081/)
  3. Enter the Password

![alt text](res/documentation_pics/jupyterconnect.jpeg)

  4. Select the remote Virtual Environment called `venv38` for Running the Jupyter Server. 

![alt text](res/documentation_pics/venvSelect.jpeg)


## Jupyter Server
### Usage
The Jupyter server is located at:  

<b>host:</b> http://192.168.209.26:8081/  
<b>pw:</b> cetibar  

<details>
  <summary><big><b>Admin:</b> Instructions to start the Jupyter server</big></summary>


  #### 1. Change to the working Dir 
```
  cd  ~/Projects/
```

  #### 2. Set a Password
```  
  jupyter notebook password 
```  

  #### 3. Start the Server 
```
  jupyter notebook --ip 192.168.209.26 --port 8081
```


</details>


## CVAT Server
### Usage

The CVAT Server for the labels is located at:  

<b>host:</b> http://192.168.209.26:8080/  
<b>user:</b> comnets  
<b>pw:</b> ComNets1

<details>
  <summary><big><b>Admin:</b> Instructions to start the CVAT server</big></summary>

  #### 1. Change to the cvat tool Dir 
```
  cd  ~/Projects/tools/cvat/cvat
```

  #### 2. Start the container:
```  
  sudo CVAT_HOST=192.168.209.26 docker-compose up -d
```  
</details>

## Workflow

### CVAT
Once you have labeld all your images in a Projects Job export the Training and Validation Datasets separatelly. 
  1. Go to your Project (e.g. food classification)
  2. On the Jobs `Actions` click on `Export task dataset` 
  3. Select `PASCAL VOC 1.1` as your export format
  4. Select `Save images`
  5. Name your Dataset (e.g `train_food_pvoc.zip`/`val_food_pvoc.zip`)
  6. Click `OK`
  7. Save your Dataset in the `{Project}/res` folder as a zip file.
  8. Repeat from Step 2. for your validation Set

### Model Maker
Read the ModelMaker jupyter Script.
# TODO
