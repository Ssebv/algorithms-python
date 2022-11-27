
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

    candles_count = 4
    candles = [3,2,1,3]
    print(birthday_candles(candles))


main()