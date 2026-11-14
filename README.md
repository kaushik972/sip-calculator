# SIP Calculator

A monthly-investment (SIP) calculator: year-by-year balance, amount invested, and how much of the final balance came from growth.

## Why I built this

Friends back in India often ask "what does ₹10,000 a month actually become in 10 years?" — the answer depends entirely on the return you assume, so I wanted a calculator that shows the whole path, year by year, instead of one magic final number.

## What it does

With the defaults (₹10,000/month, 10 years, 12% assumed annual return, compounded monthly) it prints:

- Invested amount, balance, and growth for each year
- The final split between money put in and growth

Change `MONTHLY_AMOUNT`, `YEARS`, or `ANNUAL_RETURN` at the top of `sip_calculator.py` to try other cases.

This is a maths illustration, not investment advice — the return is an assumption you type in, and real returns vary.

## How to run

```bash
cd sip-calculator
python sip_calculator.py
```

## Sample output

```
SIP calculator - 10,000 INR/month, 10 years, 12% assumed annual return
----------------------------------------------------------------
Year        Invested         Balance        Growth
1            120,000         126,825         6,825
2            240,000         269,735        29,735
3            360,000         430,769        70,769
4            480,000         612,226       132,226
5            600,000         816,697       216,697
6            720,000       1,047,099       327,099
7            840,000       1,306,723       466,723
8            960,000       1,599,273       639,273
9          1,080,000       1,928,926       848,926
10         1,200,000       2,300,387     1,100,387
----------------------------------------------------------------
After 10 years: invested 1,200,000 INR, balance 2,300,387 INR, growth 1,100,387 INR
```

## Files

- `sip_calculator.py` — the program (no data file needed)

## Next steps

- Let the user pass the amount, years, and return as command-line arguments
- Compare two returns side by side (for example 8% vs 12%)
- Add a lump-sum comparison for the same total invested amount

*Standard library only for now. Built while learning Python.*
