# Stock Market Forecaster

This is a program that uses data science to predict the stock market from a ticker of your choice!

## How It Works

This program grabs stock data from a givin depth back in time and calcualtes a liniar regreshion for those data values. The data it gets goes back in time in increments of months and ruterns days in those months (This means that the data you get back is in days)
Then, to compensate for big crops or rises in stock price, we have 3 workers, 1 that runs calculations on the bottom half of the data,
a second worker that runs calculations on the upper half of the data, then a final bot that runs calculations on all the data.

## How To Install

This application is still in very early phases of development so please don't expext much

But if you have your heart set on it
here is how you can use this program.

### Step 1 - Set Up Python

#### Get Python
if you don't have python then download it here
  https://www.python.org/downloads/release/python-3102/
#### Get the yfinance library
to install the library required for this project
please use the following command

```
py -m pip install yfinance
```

### Step 2 - Download Code

Download the code from the repository

## How To Run The Program

### Step 1 - Run The File
Run the app.py with python in the terminal
using the directory of the file on your local hard drive

### Step 2 - Format

Put the ticker you want in TICKER and the depth you want in DEPTH
Make sure you keep the 'Quotation marks'

```
python run.py 'TICKER' 'DEPTH'
```

