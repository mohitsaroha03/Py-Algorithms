# isGFG: , Link: 
# IsDone: 0
def calculateProfitWhenBuyingNow(A, index):
    buyingPrice = A[index]
    maxProfit = 0
    sellAt = index
    for i in range(index + 1, len(A)):
        sellingPrice = A[i]
        profit = sellingPrice - buyingPrice
        if profit > maxProfit:
            maxProfit = profit
            sellAt = i

    return maxProfit, sellAt
    
# check all possible buying times
def StockStrategyBruteForce(A):
    maxProfit = None
    buy = None
    sell = None
    
    for index, item in enumerate(A):
        profit, sellAt = calculateProfitWhenBuyingNow(A, index)
        if (maxProfit is None) or (profit > maxProfit):
            maxProfit = profit
            buy = index
            sell = sellAt
            
    return maxProfit, buy, sell
