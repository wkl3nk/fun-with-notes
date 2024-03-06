import numpy as np
import pandas as pd

if __name__ == '__main__':
    # Creating a NumPy array
    data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    # Converting NumPy array to a Pandas DataFrame
    df = pd.DataFrame(data, columns=['A', 'B', 'C'])

    # Performing some operations on the DataFrame
    df['D'] = df['A'] + df['B']
    df['E'] = df['C'] * 2

    # Displaying the DataFrame
    print(df)
