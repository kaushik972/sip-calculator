"""
SIP Calculator
--------------
A monthly-investment (SIP) calculator: given a monthly amount, a number
of years, and an assumed annual return, it shows the year-by-year
balance, how much was invested, and how much came from growth.

This is a maths illustration, not investment advice — the return is an
assumption you type in, and real returns vary. No libraries needed.

Built by Shivam Kaushik while learning Python.
Standard library only.
"""

MONTHLY_AMOUNT = 10000   # INR per month
YEARS = 10
ANNUAL_RETURN = 0.12     # 12% assumed, for illustration only


def sip_balance(monthly, years, annual_return):
    """Year-end balances for a monthly SIP, compounded monthly."""
    monthly_rate = annual_return / 12
    balance = 0.0
    invested = 0.0
    rows = []
    for year in range(1, years + 1):
        for _ in range(12):
            balance = balance * (1 + monthly_rate) + monthly
            invested += monthly
        rows.append((year, invested, balance, balance - invested))
    return rows


def main():
    rows = sip_balance(MONTHLY_AMOUNT, YEARS, ANNUAL_RETURN)
    print(f"SIP calculator - {MONTHLY_AMOUNT:,.0f} INR/month, "
          f"{YEARS} years, {ANNUAL_RETURN:.0%} assumed annual return")
    print("-" * 64)
    print(f"{'Year':<6}{'Invested':>14}{'Balance':>16}{'Growth':>14}")
    for year, invested, balance, growth in rows:
        print(f"{year:<6}{invested:>14,.0f}{balance:>16,.0f}{growth:>14,.0f}")
    final = rows[-1]
    print("-" * 64)
    print(f"After {YEARS} years: invested {final[1]:,.0f} INR, "
          f"balance {final[2]:,.0f} INR, growth {final[3]:,.0f} INR")


if __name__ == "__main__":
    main()
