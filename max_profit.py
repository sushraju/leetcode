#!/usr/bin/env python

def calc_max_profit(prices=[]):

    if prices:
        max_profit = prices[1] - prices[0]
        buying_price = prices[0]
        selling_price = prices[1]
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] - prices[i] > max_profit:
                    max_profit = prices[j] - prices[i]
                    buying_price = prices[i]
                    selling_price = prices[j]
    else:
        max_profit = -1
        buying_price = -1
        selling_price = -1

    return (max_profit,buying_price,selling_price)

def main():

    prices = [26,18,13,14,50,98,39,75,80,78,92,99,93]
    #test case prices = [26, 18, 13, 14]
    print(calc_max_profit(prices))

if __name__ == "__main__":
    main()

