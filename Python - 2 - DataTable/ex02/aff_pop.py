from load_csv import load
import matplotlib.pyplot as plt


def truncate(k: str) -> float:
    if k.endswith("M") or k.endswith("k"):
        return float(k[:-1])
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

    if france_data.empty:
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

    max_pop = max(max(france_np), max(belgium_np))
    y_ticks = [i * 1e7 for i in range(int(max_pop / 1e7) + 1)]
    plt.yticks(y_ticks, ["{:,.0f}M".format(k / 1e6) for k in y_ticks])

    # Adjust x-axis ticks and limit axes
    plt.xticks(range(1800, 2051, 40), range(1800, 2051, 40))
    plt.xlim(1800, 2040)

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
