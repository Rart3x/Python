from load_csv import load
import matplotlib.pyplot as plt


def graph(df: [], df1: []):
    '''Graph function'''

    if '1900' in df.columns and '1900' in df1.columns:
        gross = df['1900']
        life = df1['1900']
    else:
        print("Error: Any datas for year 1900")
        exit()

    plt.scatter(gross, life)

    plt.xlabel("Gross Domestic product")
    plt.ylabel("Life Expectancy")

    plt.xscale("log")
    plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])

    plt.title("1900")
    plt.show()


def main():
    '''Main'''

    csv = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"

    income_data = load(csv)
    life_expectancy_data = load("life_expectancy_years.csv")

    graph(income_data, life_expectancy_data)


if __name__ == "__main__":
    main()
