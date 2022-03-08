# Stock Market Forecaster

This is a program that uses data science to predict the stock market from a ticker of your choice!

## How It Works

This program grabs stock data from a givin depth back in time and calcualtes a liniar regreshion for those data values. The data it gets goes back in time in increments of months and ruterns days in those months (This means that the data you get back is in days)
Then, to compensate for big crops or rises in stock price, we have 3 workers, 1 that runs calculations on the bottom half of the data,
a second worker that runs calculations on the upper half of the data, then a final bot that runs calculations on all the data.

## How To Use

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

### Step 3 - Run Code

Run the app.py

You can change the ticker in the ticker variable in the bottom of the app.py
You can change how far the data goes back by changing the depth value, each unit of depth represents one month of time

### Disclaimers

I have not gotten around to adding a ui. So for now, 
enjoy some apple stock :)
