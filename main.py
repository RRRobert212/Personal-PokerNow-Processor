import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def main():

    data = file_setup("Poker_Logs/23_4_13_poker_now_log_pglbk0n0A4kl6CO8XF0IxloCX.csv")
    bet_amounts(data)

    return


def file_setup(file):

    df = pd.read_csv(file)

    pd.set_option('display.max_rows', None)

    return df


def bet_amounts(df):

    df['at'] = pd.to_datetime(df['at'])

    # Convert the 'at' column to datetime format
    df['at'] = pd.to_datetime(df['at'])

    df['raise_amount'] = df['entry'].str.extract('raises to (\d+\.\d+|\d+)')

    df['bet_amount'] = df['entry'].str.extract('bets (\d+\.\d+|\d+)')

    df['total_amount'] = df['raise_amount'].fillna(df['bet_amount']).astype(float)

    # Drop rows where no bet or raise was recorded
    df.dropna(subset=['total_amount'], inplace=True)

    print(df)

    plt.figure(figsize=(10, 5))
    plt.plot(df['at'], df['total_amount'], marker='o', linestyle='-', color='b')
    plt.title('Bets and Raises Over Time')
    plt.xlabel('Time')
    plt.ylabel('Amount')
    plt.grid(True)
    plt.xticks(rotation=45)  # Rotate date labels for better readability
    plt.tight_layout()  # Adjust layout to make room for label rotation
    plt.show()

    return


def player_list():
    """extracts player names"""
    return

if __name__ == "__main__": main()