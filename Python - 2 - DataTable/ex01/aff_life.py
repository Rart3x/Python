from load_csv import load
import matplotlib.pyplot as plt


def graph(df: []):
    '''Graph function'''

    france_data = df[df['country'] == 'France']
    years = france_data.columns[1:]
    life_expectancy = france_data.values[0][1:]

    plt.plot(years, life_expectancy, label='France')
    plt.title("France Life expectancy Projections")

    plt.xticks(years[::40])
    plt.yticks(range(30, 101, 10))

    plt.ylabel("Life expectancy")
    plt.xlabel("Year")

    plt.show()


def main():
    '''Main'''

    graph(load("life_expectancy_years.csv"))


if __name__ == "__main__":
    main()
