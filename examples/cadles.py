# Birthday Cake Candles 
# You are in charge of the cake for your niece's birthday and have decided the cake will have one candle for each year of her total age.
def birthday_candles(candles):
    maximo = max(candles)
    lista = []
    for candle in candles:
        if candle == maximo:
            lista.append(candle)
        else:
            pass

    return lista.count(maximo)

def main ():
    candles = [3,2,1,3]
    print(birthday_candles(candles))

main()