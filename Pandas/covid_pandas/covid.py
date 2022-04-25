import pandas as pd
import sys


def load_file():
    try:
        df = pd.read_csv(
            r'D:\Python\Git\Pandas\covid_pandas\national-history.csv')
        return df
    except Exception as e:
        print("No such file or directory")
        sys.exit(1)


def prepare_file(file):
    df = file.drop(['inIcuCumulative', 'inIcuCurrently',
                    'hospitalizedIncrease', 'hospitalizedCurrently',
                    'hospitalizedCumulative', 'negative', 'negativeIncrease',
                    'onVentilatorCumulative', 'onVentilatorCurrently', 'positive',
                    'positiveIncrease', 'states', 'totalTestResults',
                    'totalTestResultsIncrease'], axis=1)

    return df


def castingToInt(object):
    val = (object.index.values)
    val2 = val.__getitem__(0)
    result = val2.item()
    return result


if __name__ == '__main__':

    df = prepare_file(load_file())

    print("Przykładowe dane: \n\n", df.head(5))
    while True:
        user_input = input("Podaj date 'YYYY-MM-DD', [0] aby zakończyć: ")
        if (user_input == '0'):
            print("Koniec.")
            break
        else:
            result = df[df['date'].str.contains(user_input)]
            # print('\n',result)
            result = castingToInt(result)
            print('\n', df.iloc[result].to_string())

            if len(user_input) > 6 and len(user_input) <= 8:
                print("W całym miesiącu przybyło: ",
                      result['deathIncrease'].sum())
