from load_csv import load
import matplotlib.pyplot as plt


def graph(df: []):
    '''Graph function'''

    france_data = df[df['country'] == 'France']

    # plt.plot()
    # plt.title("France Life expectancy Projections")
    # plt.ylabel("Life expectancy")
    # plt.xlabel("Year")
    # plt.grid(True)
    # plt.show()


def main():
    '''Main'''

    graph(load("life_expectancy_years.csv"))


if __name__ == "__main__":
    main()
