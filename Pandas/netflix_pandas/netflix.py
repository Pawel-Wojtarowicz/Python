import pandas as pd
import sys


def load_file():
    try:
        df = pd.read_csv(r'd:\python\git\netflix_pandas\ViewingActivity.csv')
        return df
    except Exception as e:
        print("No such file or directory")
        sys.exit(1)
        

def prepare_file(file):

    df = file.drop(['Attributes', 'Device Type', 'Bookmark', 'Latest Bookmark', 'Supplemental Video Type', 'Country'], axis=1)
    df['Start Time'] = pd.to_datetime(df['Start Time'], utc=True)
    df = df.set_index('Start Time')
    df.index = df.index.tz_convert('Europe/Warsaw')
    df = df.reset_index()
    df['Duration'] = pd.to_timedelta(df['Duration'])
    
    return df

if __name__ == '__main__':

    df = prepare_file(load_file())

    while True:
        name = input("Enter the name of TV-Series: ")
        result = df[df['Title'].str.contains(name, regex=False)]
        #print(df.dtypes)

        if len(result): 
            print(f"\n{result}\nYou have been watched the series through: {result['Duration'].sum()} hours")
        else:
            print(f'There is no such TV-Series named: "{name}", please try again')

