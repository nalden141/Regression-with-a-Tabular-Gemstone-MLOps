<<<<<<< HEAD
import os
=======
import os 
>>>>>>> fbd1c785b1933ef6324c74028a3527cf51af7480
from pathlib import Path


list_of_files = [
<<<<<<< HEAD
   ".github/workflows/ci.yaml",
   "src/__init__.py",
   f"src/mongodb/__init__.py", 
   f"src/mongodb/mongo_crud.py", 
=======
   ".github/workflows/.gitkeep",
   "src/__init__.py",
   "src/components/__init__.py", 
   "src/components/data_ingestion.py",
   "src/components/data_transfromation.py",
   "src/components/model_trainer.py",
   "src/components/model_evaluation.py",
   "src/pipeline/__init__.py",
   "src/pipeline/training_pipeline.py",
   "src/pipeline/prediction_pipeline.py",
   "src/utils/__init__.py",
   "src/utils/utils.py",
   "src/logger/logging.py",
   "src/exception/exception.py",
>>>>>>> fbd1c785b1933ef6324c74028a3527cf51af7480
   "tests/__init__.py",
   "tests/unit/__init__.py",
   "tests/integration/__init__.py",
   "init_setup.sh",
<<<<<<< HEAD
   "requirements.txt", 
=======
   "requirements.txt",
   "setup.py",
   "setup.cfg",
>>>>>>> fbd1c785b1933ef6324c74028a3527cf51af7480
   "pyproject.toml",
   "tox.ini",
   "experiments/experiments.ipynb", 
]

<<<<<<< HEAD
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass

=======
for file in list_of_files:

    file =Path(file)
    filedir,filename =os.path.split(file)
    
    if filedir != '':
        os.makedirs(filedir,exist_ok=True)

    if not os.path.exists(file):
        with open(file,"w") as f:
            pass
>>>>>>> fbd1c785b1933ef6324c74028a3527cf51af7480
