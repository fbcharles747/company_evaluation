## Introduction

This project use pandas library to calculate some ratios that Warren Buffet is looking at. With the financial data coming from FMP (financial modeling prep), the jupyter notebook guide investor to identify company with competitive advantages. The bias list in `longterm_analysis.ipynb` come from the book <b><i>Warren Buffett and the Interpretation of Financial Statements: The Search for the Company with a Durable Competitive Advantage
by Mary Buffett</i></b>.

## Major issue

I also try to integrate the discounted cashflow formula mentioned in the book <b><i>The Little Book of Valuation: How to Value a Company, Pick a Stock and Profit (Little Books. Big Profits)
by Aswath Damodaran</i></b>. There is some issue relating to calculating the reinvestment rate.

As present in the book:
$reinvestment rate = \dfrac {(net \quad Capital \quad expenditure + change \quad in \quad working \quad capital)} {operating \quad after \quad tax}$

Sometimes, the sum of net capital expenditure and change in working capital is negative number, which yield negative reinvestment rate. I have not yet figure out how to handle that case. At this point, the best thing I can do is wrap the logic of reinvestment calculation into a function `reinvestment_rate` in `helper.py`, so it is easier to change in the future.

## setting up enviornment

```shell
# set up the conda environment
sudo apt-get update
sudo apt-get install wget
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

# create seperate environment
conda create -y -n fmp_valuation python=3.12
conda activate fmp_valuation

# install necessary package
pip install pandas
pip install fmpsdk
conda install Jinja2


```

> Note: remember to include `.env` file, and specify `apikey=your_fmp_apikey`.