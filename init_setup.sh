set -e
echo  "START"
echo "creating env with python = 3.8 "

conda create --prefix ./env python=3.8 -y

echo "activating the env"

source activate ./env

echo "installing the requirements"

pip install -r requirements.txt

echo "END"