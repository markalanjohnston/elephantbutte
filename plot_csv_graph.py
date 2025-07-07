import pandas as pd
import matplotlib.pyplot as plt


def main():
    # Read the CSV file located in the repo's main directory
    df = pd.read_csv('Elephant_Butte_merged.csv', parse_dates=['date'])

    # Plot storage over time
    plt.figure(figsize=(10, 6))
    plt.plot(df['date'], df['storage'], label='Storage')
    plt.title('Elephant Butte Storage Over Time')
    plt.xlabel('Date')
    plt.ylabel('Storage (acre-feet)')
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
