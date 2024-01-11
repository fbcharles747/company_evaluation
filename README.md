## Introduction

This project use pandas library to calculate some ratios that value investor is looking at. With the financial data coming from FMP (financial modeling prep), the jupyter notebook program help investor to identify company with competitive advantages. The bias list in `longterm_analysis.ipynb` come from the book <b><i>Warren Buffett and the Interpretation of Financial Statements: The Search for the Company with a Durable Competitive Advantage
by Mary Buffett</i></b>.

## Major issue

I also try to integrate the discounted cashflow formula mentioned in the book <b><i>The Little Book of Valuation: How to Value a Company, Pick a Stock and Profit (Little Books. Big Profits)
by Aswath Damodaran</i></b>. There is some issue relating to calculating the reinvestment rate.

As presented in the book:
$reinvestment \quad rate = \dfrac {(net \quad Capital \quad expenditure + change \quad in \quad working \quad capital)} {operating \quad income \quad after \quad tax}$

Sometimes, the sum of net capital expenditure and change in working capital is negative number, which yield negative reinvestment rate. I have not yet figure out how to handle this case accurately. At this point, the best thing I can do is wrap the logic of reinvestment calculation into a function `reinvestment_rate` in `helper.py`, so it is easier to change in the future.

> Note that intrinsic value calculation of table 2 will require FMP standard subscription

## setting up enviornment

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
