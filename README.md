## Introduction

This project use pandas library to display the relevant numbers and ratio from financial statement. To enable the search by stock symbol capability, Finanicial Modelling prep are used as the source of data, so the FMP API key is required. 



## setting up enviornment
Note that this set-up took place in WSL.

```shell
# set up the conda environment
sudo apt-get update
sudo apt-get install wget
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
sh ./Miniconda3-latest-Linux-x86_64.sh

# create seperate environment
conda create -y -n fmp_valuation python=3.12
conda activate fmp_valuation

# install necessary package
pip install pandas
pip install fmpsdk
conda install Jinja2


```

> Note: remember to create `.env` file in the root directory, and specify `apikey=your_fmp_apikey`.
