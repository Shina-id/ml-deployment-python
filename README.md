# ml-deployment-python
Tensorflow model deployment to cloud and the API to call prediction

## Step by Step deployment using VM (IaaS)

- Config your VM that allow traffic from port 5000

- in the VM, create your virtual environment using command:
  sudo apt-get update
  wget https://repo.anaconda.com/miniconda/Miniconda3-4.7.10-Linux-x86_64.sh
  bash Miniconda3-4.7.10-Linux-x86_64.sh
  export PATH=/home/<your name here>/miniconda3/bin:$PATH
  conda create -n <your-virtual-environment-here> python=3.7
  conda activate <your-virtual-environment-here>
  
- Clone the project repository
  git clone https://github.com/Shina-id/ml-deployment-python.git
  
- Run the app:
  cd ml-deployment-python
  python3 app.py
  ### note: dont forget to change the saved_model directory in paddy.py with your saved_model directory
