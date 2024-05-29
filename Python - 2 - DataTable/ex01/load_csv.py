import pandas as pd


def load(path: str) -> pd.DataFrame:
    '''
    Load CSV from a path
    representing CSV file location
    '''

    try:
        data = pd.read_csv(path)
    except FileNotFoundError:
        print(f"Error: file not found: {path}")
        exit()
    except Exception as e:
        print(f"Unknown error: {e}")
        exit()

    print(f"Loading dataset of dimensions {data.shape}")

    return data


def main():
    '''Main'''


if __name__ == "__main__":
    main()
