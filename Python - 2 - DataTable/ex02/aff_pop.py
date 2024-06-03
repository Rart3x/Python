from load_csv import load
import matplotlib.pyplot as plt


def truncate(k: str) -> float:
    '''Truncate function'''

    if k.endswith("k"):
        return float(k[:-1]) * 1000
    if k.endswith("M"):
        return float(k[:-1]) * 1000000
    if k.endswith("N"):
        return float(k[:-1]) * 1000000000
    return float(k)


def graph(df: []):
    '''Graph function'''

    # Filter the DataFrame to keep only data for France and Belgium,
    # then remove the first column (country)
    if 'country' in df.columns:
        france_data = df[df['country'] == 'France'].iloc[:, 1:]
    else:
        print("Error: Any datas for country")
        exit()

    if france_data.empty:
        print("Error: Any datas for France")
        exit()

    if 'country' in df.columns:
        belgium_data = df[df['country'] == 'Belgium'].iloc[:, 1:]
    else:
        print("Error: Any datas for country")
        exit()

    if belgium_data.empty:
        print("Error: Any datas for Belgium")
        exit()

    # Convert the filtered DataFrame values to flattened numpy arrays
    france_np = france_data.values.flatten()
    belgium_np = belgium_data.values.flatten()

    years = france_data.columns.astype(int)

    france_np = [truncate(k) for k in france_np]
    belgium_np = [truncate(k) for k in belgium_np]

    plt.plot(years, france_np, label='France')
    plt.plot(years, belgium_np, label='Belgium')

    plt.title("Population Projections")

    # Adjust x-axis ticks and limit axes
    plt.xticks(range(1800, 2051, 40), range(1800, 2051, 40))
    plt.xlim(1800, 2040)

    plt.yticks([20000000, 40000000, 60000000], ["20M", "40M", "60M"])

    plt.ylabel("Population")
    plt.xlabel("Year")

    plt.tight_layout()
    plt.legend()
    plt.show()


def main():
    '''Main'''

    graph(load("population_total.csv"))


if __name__ == "__main__":
    main()
