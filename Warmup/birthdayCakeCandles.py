n = int(input())
candles = list(map(int, input().split()))
maxNum = max(candles)
print(len([candle for candle in candles if candle == maxNum]))