import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_dataset(filepath):
    """
    Visualizes a dataset from a CSV file.

    Args:
        filepath: The path to the CSV file.
    """
    try:
        df = pd.read_csv(filepath)
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return
    except pd.errors.EmptyDataError:
        print(f"Error: The file at {filepath} is empty.")
        return
    except pd.errors.ParserError:
        print(f"Error: Could not parse the CSV file at {filepath}. Please check the file format.")
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return

    print("Dataset Overview:")
    print(df.head())
    print("\nDataset Info:")
    print(df.info())
    print("\nDescriptive Statistics:")
    print(df.describe())

    # Basic visualizations
    if not df.empty:
        try:
          #Histograms for numerical columns.
          numerical_cols = df.select_dtypes(include=['number']).columns
          for col in numerical_cols:
              plt.figure()
              sns.histplot(df[col], kde=True)
              plt.title(f'Histogram of {col}')
              plt.show()

          #Countplots for categorical columns.
          categorical_cols = df.select_dtypes(include=['object']).columns
          for col in categorical_cols:
              plt.figure()
              sns.countplot(x=col, data=df)
              plt.title(f'Countplot of {col}')
              plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels
              plt.tight_layout() #Avoid label cutoff
              plt.show()

          #Scatter plots for numerical relationships.
          if len(numerical_cols) >= 2:
            plt.figure()
            sns.pairplot(df[numerical_cols[:5]]) #Limit to 5 for simplicity
            plt.show()

          #Heatmap for correlation.
          if len(numerical_cols) >=2:
            plt.figure()
            correlation_matrix = df[numerical_cols].corr()
            sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
            plt.title('Correlation Heatmap')
            plt.show()

        except Exception as e:
          print(f"Error generating visualizations: {e}")

def main():
    filepath = input("Enter the path to your CSV file: ")
    visualize_dataset(filepath)

if __name__ == "__main__":
    main()