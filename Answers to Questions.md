# Answers to Questions

**1. List at least five specific data quality issues present in this dataset. For each, reference the classification (e.g., missing, noisy, inconsistent) discussed in the slides.**

Based on an initial analysis of the dataset, the following five data quality issues were identified:

*   **Inconsistent Formatting (Location):** The `Location` column contains multiple variations for the same logical place, such as `'n field'`, `'North Field'`, and `'NORTH FIELD'`. This is a data consistency issue that prevents accurate grouping and aggregation.
*   **Noisy Data / Outliers (pH):** The `pH` column has a minimum value of `-2.0`, which is chemically impossible as the pH scale ranges from 0 to 14. This represents noisy data or an outlier that must be corrected.
*   **Noisy Data / Outliers (Temperature):** The `Temperature` column contains extreme outliers, with a maximum value of `796.5`. This is a tad bit questionable for ambient temperature in a farm and indicates a sensor error or data corruption.
*   **Missing Values (Multiple Columns):** The `Temperature`, `SoilMoisture`, `pH`, and `Fertilizer` columns all contain fewer non-null entries than the total number of rows, indicating missing data. These are represented by various formats like "N/A", "None", and blanks.
*   **Inconsistent Formatting (Date):** The `Date` column uses multiple formats interchangeably (e.g., `12-Mar-25`, `4/1/2025`, `15/03/2025`). This data type and format inconsistency prevents chronological sorting and time-series analysis.

**2. Given the variety of dirty values (N/A, None, blank, "missing", etc.), write a Python code snippet to identify all rows where any value is missing, according to the lecture's definitions of missing data.**

To handle the various representations of missing data, we first load the data using pandas, specifying all known missing value formats in the `na_values` parameter. This automatically converts them to `NaN` (Not a Number), pandas' standard missing data marker.

The following code then identifies and displays all rows containing at least one `NaN` value in any column.

```python
import pandas as pd
import numpy as np

# Define all known missing value formats
missing_value_formats = ["n/a", "N/A", "missing", "None", "", " ", "NA", "na"]
# Load the dataset, converting all specified formats to NaN
df = pd.read_csv('smart_farm_raw(in).csv', na_values=missing_value_formats)

# Identify all rows with at least one missing value
missing_rows_df = df[df.isnull().any(axis=1)]

# Display the count and the first 10 examples of such rows
print(f"Found {len(missing_rows_df)} rows with at least one missing value.")
print("\nHere are the first 10 rows with missing data:")
print(missing_rows_df.head(10))
```

**3. Using principles from the discussion, propose a specific method to impute missing values for the "SoilMoisture" attribute. Justify your choice based on the characteristics of this data and the pros/cons of methods from the file.**

The most appropriate method for imputing missing `SoilMoisture` values is **Grouped Median Imputation**.

*   **Method:** For each location (e.g., 'North Field', 'South Field'), we calculate the median `SoilMoisture` for all available readings in that specific location. We then use that location-specific median to fill in the missing values for that group only.

*   **Justification:**
    *   **Superior to Deletion:** Simply deleting the rows with missing moisture would lead to a loss of over 6% of the dataset, discarding valuable information in other columns.
    *   **Superior to Global Statistic:** Using a single global median or mean for the entire dataset is inaccurate because soil conditions can vary significantly between different fields. Grouping by `Location` provides a more contextually relevant and precise imputation.
    *   **Median over Mean:** The `SoilMoisture` column contains extreme outliers (e.g., `9999.0`). The mean is highly sensitive to such outliers and would be skewed, resulting in a poor imputation value. The median is robust to outliers and thus provides a more stable and representative measure of central tendency for this data.

**4. Describe, with pseudocode or code, how you would detect and remove outliers in the "Temperature" column. Be explicit about the criteria you would use, referencing binning or statistical approaches in the slides.**

The most effective approach for the `Temperature` column is to remove outliers based on **Domain Knowledge**, as some values are physically impossible.

*   **Criteria:** A plausible temperature range for a farm environment is between -10°C and 50°C. Any value falling outside these absolute bounds will be treated as a noisy outlier.

*   **Workflow/Pseudocode:**
    1.  Define a minimum threshold `sane_temp_min = -10.0`.
    2.  Define a maximum threshold `sane_temp_max = 50.0`.
    3.  For each row in the DataFrame:
        *   IF `Temperature` < `sane_temp_min` OR `Temperature` > `sane_temp_max`:
            *   Replace the `Temperature` value with `NaN` (to mark it for imputation).
    4.  After removing outliers, impute the newly created `NaN` values using a suitable method, such as the grouped median per location.

*   **Python Code Implementation:**
    ```python
    sane_temp_min = -10.0
    sane_temp_max = 50.0
    df.loc[(df['Temperature'] < sane_temp_min) | (df['Temperature'] > sane_temp_max), 'Temperature'] = np.nan
    ```

**5. Explain a systematic approach (not a code) for correcting location name inconsistencies (e.g., "NORTH FIELD", "n field", "North field") using the slides' recommendations for resolving inconsistencies and field overloading.**

A systematic approach to resolve the inconsistencies in the `Location` column involves the following steps:

1.  **Inspection and Profiling:** First, generate a complete list of all unique values in the `Location` column to understand the full scope of the variations (e.g., 'n field', 'NorthField', 'NORTH FIELD').
2.  **Define Standardization Rules:** Create a definitive mapping (a "dictionary" or "lookup table") that establishes a single, standard format for each location. For example, all variations like "n field", "north field", and "Nrth Field" will be mapped to the standard string `"North Field"`.
3.  **Data Transformation:** Apply this mapping to the entire `Location` column. This process systematically replaces every inconsistent value with its corresponding standardized value, ensuring uniformity across the dataset. This makes the data reliable for grouping and analysis.

**6. Sensors have sometimes uploaded duplicate or near-duplicate rows (same sensor, time, location, but slight variation in other fields). Describe an algorithm or workflow (can include coding or database operations) to detect and remove these duplicates.**

A robust workflow to detect and remove duplicate or near-duplicate records is as follows:

1.  **Define Duplicate Keys:** Identify the columns that define a unique record. Based on the prompt, these are `SensorID`, `Date`, and `Location`.
2.  **Sort Data:** Sort the entire DataFrame based on the key columns (`SensorID`, `Date`, `Location`) and a tie-breaking column (e.g., `Temperature`). Sorting is crucial because it groups all potential duplicates together and ensures that the removal process is deterministic (i.e., it will always keep the "same" row if run multiple times).
3.  **Mark Duplicates:** Use a function like pandas' `df.duplicated()` with the `subset` parameter set to the key columns (`['SensorID', 'Date', 'Location']`). Set the `keep` parameter to `'first'` to mark all subsequent occurrences of a duplicate record as `True`, leaving the first one as `False`.
4.  **Remove Marked Rows:** Filter the DataFrame to keep only the rows that were marked as `False` (i.e., the first unique occurrences), effectively removing all identified duplicates.

**7. The dataset has wildly varying date formats. Describe a robust strategy or Python approach (not just pd.to_datetime) to standardize dates, including how to handle ambiguous or failed parsing, inspired by lecture content on data transformation and ETL.**

A robust strategy for standardizing the mixed-format `Date` column involves a controlled parsing approach that anticipates ambiguity and errors, which is a key principle in ETL (Extract, Transform, Load) pipelines.

1.  **Controlled Parsing with `pd.to_datetime`:** Instead of a blind conversion, we use `pd.to_datetime` with specific parameters to guide the process.
2.  **Handling Ambiguity (`dd/mm/yy` vs. `mm/dd/yy`):** For formats like `4/1/2025`, we can specify `dayfirst=True`. This instructs the parser to treat the first number as the day, a common convention in many parts of the world, resolving the ambiguity.
3.  **Error Handling:** We set the `errors='coerce'` parameter. This is a critical ETL practice. Instead of stopping the entire process when an un-parseable date is found, this setting will gracefully convert it to `NaT` (Not a Time). This allows the program to continue running and enables us to isolate, count, and analyze the failed records separately to determine if a new parsing rule is needed or if the data is truly corrupt.

**8. The "Fertilizer" column has values in both kg and g (some mistakenly entered as "0.003" or "3.2" interchangeably). Propose a practical data cleaning pipeline to standardize this column, referencing transformation and normalization from the discussion slides.**

The pipeline to standardize the `Fertilizer` column involves **transformation based on domain knowledge** to correct for unit inconsistency.

1.  **Analysis and Assumption:** First, analyze the distribution of the `Fertilizer` data using `describe()`. The statistics show most values are small (e.g., 75% are below 3.5), but the maximum is nearly 4000. This strongly suggests that the very large values are gram measurements mistakenly entered in a column intended for kilograms. We establish a rule: **any value above a reasonable threshold (e.g., 100) is assumed to be in grams.**
2.  **Transformation:** We then apply a mathematical transformation to the identified gram-based entries. Specifically, we divide these values by 1000 to convert them to the standard unit of kilograms.
3.  **Verification:** After the transformation, we re-examine the column's statistics (`describe()`) to confirm that the `max`, `mean`, and `std` are now within a plausible range, ensuring all values are standardized to the same unit (kg).

**9. After all cleaning steps, outline two EDA (Exploratory Data Analysis) checks you would perform to confirm your data is clean and ready for mining, and explain why they are important, referencing the principles from the discussion summary.**

Two essential EDA checks to confirm the data is clean and ready for mining are:

1.  **Final Statistical Summary Review:**
    *   **Check:** Run `df.info()` and `df.describe()` on the final, cleaned DataFrame.
    *   **Importance:** This is a fundamental check to programmatically verify data integrity. `df.info()` confirms that there are **no more missing values**. `df.describe()` provides a final sanity check on the numerical data, confirming that the **min, max, mean, and standard deviation** for each column are within a plausible range, which validates our outlier and unit standardization efforts.

2.  **Visual Distribution Analysis (Box Plots and Histograms):**
    *   **Check:** Generate a box plot and a histogram for each of the four numerical columns (`Temperature`, `SoilMoisture`, `pH`, `Fertilizer`).
    *   **Importance:** Visualizations can reveal patterns or anomalies that summary statistics might miss. **Box plots** provide a clear visual confirmation that major outliers have been successfully removed. **Histograms** show the shape of the data's distribution, allowing us to ensure our imputation and cleaning steps haven't introduced strange artifacts (like unnatural spikes) and that the data now follows a more believable distribution, making it suitable for modeling and mining.

