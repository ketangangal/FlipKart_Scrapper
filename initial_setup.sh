#!/bin/bash

echo [$(date)] : "STARTING INITIAL SETUP"
export _VERSION_=3.8

echo [$(date)] : "PROJECT DIRECTORY NAME"
read project_name
export project_name_=$project_name

echo [$(date)] : "CREATING PROJECT STRUCTURE"

echo [$(date)] : "CREATING UTILITY LAYER"
mkdir ${project_name_}_utils_layer
touch ${project_name_}_utils_layer/__init__.py ${project_name_}_utils_layer/utils.py

echo [$(date)] : "CREATING LOGGING LAYER"
mkdir ${project_name_}_logging_layer
touch ${project_name_}_logging_layer/__init__.py ${project_name_}_logging_layer/logging.py

echo [$(date)] : "CREATING DATA ACCESS LAYER"
mkdir ${project_name_}_data_access_layer
touch ${project_name_}_data_access_layer/__init__.py ${project_name_}_data_access_layer/data_access.py

echo [$(date)] : "CREATING EXCEPTION LAYER"
mkdir ${project_name_}_exception_layer
touch ${project_name_}_exception_layer/__init__.py ${project_name_}_exception_layer/exception.py

echo [$(date)] : "CREATING ENTITY LAYER"
mkdir ${project_name_}_entity_layer
touch ${project_name_}_entity_layer/__init__.py ${project_name_}_entity_layer/entity.py

echo [$(date)] : "CREATING TESTING LAYER"
mkdir ${project_name_}_testing
touch ${project_name_}_testing/__init__.py ${project_name_}_testing/tests.py

echo [$(date)] : "CREATING CONDA ENVIRONMENT"
conda create --prefix ./env python=${_VERSION_} -y
source activate ./env

echo [$(date)] : "CREATE REQUIREMENTS TEXT FILE"
touch requirements.txt

echo [$(date)]: "CREATING DOCKER FILE"
touch dockerfile

echo [$(date)]: "CREATING ADDITIONAL FILES"
touch config.yaml
touch app.py


echo [$(date)] : "END"