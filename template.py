import os 
from pathlib import Path


list_of_files = [
   "src/__init__.py",
   "src/mongodb/__init__.py", 
   "src/mongodb/mongo_crud.py", 
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
   "src/logger/my_logging.py",
   "src/exception/exception.py",
   "tests/__init__.py",
   "tests/unit/__init__.py",
   "tests/integration/__init__.py",
   "init_setup.sh",
   "requirements.txt",
   "requirements.txt",
   "setup.py",
   "setup.cfg",
   "pyproject.toml",
   "tox.ini",
   "experiments/experiments.ipynb",
   "app.py",
   "templates/index.html",
   "templates/form.html",
   "templates/result.html",
]

for file in list_of_files:

    file =Path(file)
    filedir,filename =os.path.split(file)
    if filedir != '':
        os.makedirs(filedir,exist_ok=True)

    if not os.path.exists(file):
        with open(file,"w") as f:
            pass
