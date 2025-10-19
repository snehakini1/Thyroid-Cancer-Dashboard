# Thyroid-Cancer-Dashboard
# Thyroid Cancer Risk Data Explorer

A Python-based interactive dashboard for exploring and visualizing thyroid cancer risk data using Sankey diagrams. This application allows users to filter and analyze patient data by diagnosis, country, and minimum case count, with dynamic visualizations.

## Features

- **Interactive Dashboard**: Web-based interface built with Panel
- **Dynamic Filtering**: Filter data by diagnosis type, country, and minimum case count
- **Sankey Visualizations**: Flow diagrams showing relationships between diagnosis, age groups, and case counts
- **Data Exploration**: Tabular view of filtered cases
- **Customizable Plots**: Adjustable width and height for visualizations

## Dataset

The application uses `tcr.csv`, which contains thyroid cancer patient data with the following fields:

- **Patient_ID**: Unique identifier
- **Age**: Patient age
- **Gender**: Male/Female
- **Country**: Patient's country
- **Ethnicity**: Caucasian, Hispanic, Asian, African
- **Family_History**: Yes/No
- **Radiation_Exposure**: Yes/No
- **Iodine_Deficiency**: Yes/No
- **Smoking**: Yes/No
- **Obesity**: Yes/No
- **Diabetes**: Yes/No
- **TSH_Level**: Thyroid-stimulating hormone level
- **T3_Level**: Triiodothyronine level
- **T4_Level**: Thyroxine level
- **Nodule_Size**: Size of thyroid nodule
- **Thyroid_Cancer_Risk**: Low/Medium/High
- **Diagnosis**: Benign/Malignant

## Files

- **`sankey.py`**: Core module for creating Sankey diagrams using Plotly
- **`tcrapi.py`**: API class for loading and filtering thyroid cancer data
- **`tcrapp.py`**: Simple command-line application for generating Sankey diagrams
- **`tcrexplorer.py`**: Interactive Panel dashboard application
- **`tcr.csv`**: Thyroid cancer patient dataset (required)

## Requirements

```
pandas
plotly
panel
```

## Installation

1. Clone or download this repository
2. Install required dependencies:
```bash
pip install pandas plotly panel
```
3. Ensure `tcr.csv` is in the same directory as the Python files

## Usage

### Interactive Dashboard

Run the Panel dashboard for full interactive exploration:

```bash
panel serve tcrexplorer.py
```

Then open your browser to the URL shown in the terminal (typically `http://localhost:5006`).

**Dashboard Features:**
- **Search Panel**: Select diagnosis type, minimum cases threshold, and country
- **Plot Panel**: Adjust visualization dimensions
- **Cases Tab**: View filtered data in a table
- **Network Tab**: View Sankey diagram of diagnosis-age relationships

### Command-Line Application

For quick data exploration without the web interface:

```bash
python tcrapp.py
```

This will generate a Sankey diagram with default parameters (Malignant diagnosis, 4 minimum cases, USA/Canada/Germany).

## How It Works

1. **Data Loading**: The TCRAPI class loads the CSV data
2. **Filtering**: Users select diagnosis, country, and minimum case count
3. **Age Grouping**: Ages are automatically grouped into "Under 50" and "Above 50"
4. **Aggregation**: Cases are counted by diagnosis, age group, and country
5. **Visualization**: Sankey diagrams show flow from diagnosis → age groups, with link thickness representing case counts

## Customization

### Modify Default Parameters

In `tcrapp.py`, change the search parameters:

```python
diagnosis = 'Malignant'  # or 'Benign'
num_cases = 4  # minimum case threshold
countries = ['USA', 'Canada', 'Germany']  # list of countries
```

### Adjust Sankey Appearance

In the `show_sankey()` or `make_sankey()` calls, add optional parameters:

```python
sk.show_sankey(local, 'Diagnosis', 'Age', vals='ncases',
               width=1200, height=800,
               pad=50, thickness=50,
               line_color='black', line_width=1)
```

## Example Output

The Sankey diagram visualizes:
- **Source nodes**: Diagnosis types (e.g., Benign, Malignant)
- **Target nodes**: Age groups (Under 50, Above 50)
- **Link thickness**: Number of cases

This helps identify patterns such as which age groups have higher incidence of malignant diagnoses in specific countries.

## License

This project is provided as-is for educational and research purposes.
