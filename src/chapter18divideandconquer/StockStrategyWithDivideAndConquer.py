''

def StockStrategy(A, start, stop):
    n = stop - start
    
    # edge case 1: start == stop: buy and sell immediately = no profit at all
    if n == 0:
        return 0, start, start

    if n == 1:
        return A[stop] - A[start], start, stop
        
    mid = start + n / 2

    # the "divide" part in Divide & Conquer: try both halfs of the array
    maxProfit1, buy1, sell1 = StockStrategy(A, start, mid - 1)
    maxProfit2, buy2, sell2 = StockStrategy(A, mid, stop)

    maxProfitBuyIndex = start
    maxProfitBuyValue = A[start]
    for k in range(start + 1, mid):
        if A[k] < maxProfitBuyValue:
            maxProfitBuyValue = A[k]
            maxProfitBuyIndex = k
            
    maxProfitSellIndex = mid
    maxProfitSellValue = A[mid]
    for k in range(mid + 1, stop + 1):
        if A[k] > maxProfitSellValue:
            maxProfitSellValue = A[k]
            maxProfitSellIndex = k

    # those two points generate the maximum cross border profit
    maxProfitCrossBorder = maxProfitSellValue - maxProfitBuyValue

    # and now compare our three options and find the best one
    if maxProfit2 > maxProfit1:
        if maxProfitCrossBorder > maxProfit2:
            return maxProfitCrossBorder, maxProfitBuyIndex, maxProfitSellIndex
        else:
            return maxProfit2, buy2, sell2
    else:
        if maxProfitCrossBorder > maxProfit1:
            return maxProfitCrossBorder, maxProfitBuyIndex, maxProfitSellIndex
        else:
            return maxProfit1, buy1, sell1

def StockStrategyWithDivideAndConquer(A):
    return StockStrategy(A, 0, len(A) - 1)
