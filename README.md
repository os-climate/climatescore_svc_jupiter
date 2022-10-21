# OS-C ClimateScore API Service

## Description

This repo contains data, code, and documentation developed by Jupiter Intelligence for use by OS-Climate to set up a OS-C ClimateScore API Service (“ClimateScore Service”). Data contained in this repo is an upscaled version of Jupiter Intelligence's commercial product.

# Data Classification & Permissions
This repo, including all data, code, and documentation is currently **restricted** and cannot be shared with, used by, or accessed by anybody who is not part of the OS-Climate organization.

Data contained in this repo cannot be made available to OSC platform users until a formal licensing agreement is in place.

# Repo Contents
**OS-C-DOCS** contains documentation to guide a Cloud Engineer in installing the ClimateScore Service into the AWS Cloud Platform.

**OS-C-DATA** contains all the Jupiter contributed data in CSV format. The data is delivered as seven CSV files, each containing data for one peril (combined flood, drought, fire, hail, heat, precipitation, and wind).

**OS-C-RDS** contains the Python scripts necessary to create tables for each of the Perils as well as corresponding indexes.

**OS-C-API-SERVER** contains the Python Source Code of the Flask Application Server that provides the business logic of the ClimateScore Service.

**OS-C-FE-APPS** contains examples and documentation in Postman collections, Jupyter Notebooks, and Open API/Swagger format that is intended to help Developers and Data Scientists develop applications that utilize the ClimateScore Service.

## Release 
   - https://gitlab.com/jupiterintel/osc/-/releases/1.0.1 

## License

## Project status
   - Active
