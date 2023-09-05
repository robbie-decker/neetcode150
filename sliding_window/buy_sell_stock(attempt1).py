def buySell(prices):
    myMinIndex = prices.index(min(prices))
    myMax = (max(prices[myMinIndex::]))

    return myMax - prices[myMinIndex]


prices = [7, 6, 3, 9, 1, 6, 2, 4, 5, 7]
buySell(prices)