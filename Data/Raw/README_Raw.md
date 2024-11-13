# Raw Data Folder

This folder contains the original, unprocessed datasets used as input for the data analytics project. Files in this folder are in their original form and should not be modified directly. Instead, load data from this folder into scripts or notebooks where it will undergo cleaning and transformation, with processed versions saved in the `processed` folder.

## Files

### `main_data.csv`

- **Description**: This is the primary dataset for the analysis. It contains all original features as collected from the data source.
- **Source**: [Provide the source of the data, e.g., "Company Internal Database" or "Public Dataset from XYZ"]
- **Contents**:
  - **id**: Unique identifier for each entry.
  - **raw_feature_1**: Feature in its original, unaltered state.
  - **raw_feature_2**: Another raw feature, before any transformations.

### `demographics.csv`

- **Description**: Contains demographic information related to each observation in `main_data.csv`, intended for enrichment and analysis alongside other datasets.
- **Source**: [Provide the source of the data, e.g., "Government Census Data" or "Public Dataset"]
- **Contents**:
  - **region**: Geographical region of each record.
  - **age**: Age of individuals, as recorded in the source.
  - **income**: Reported income level, in original format.

### `sales_data.csv`

- **Description**: Original sales data collected directly from the sales department or system.
- **Source**: [Provide the source of the data, e.g., "Sales Database" or "CRM Export"]
- **Contents**:
  - **sale_id**: Unique identifier for each sale transaction.
  - **product_id**: ID of the product sold.
  - **sale_amount**: Sale amount in its original currency and format.

## Guidelines for Using Raw Data

- **Do not modify** the contents of raw data files directly.
- When working with these files, make copies or load the data into your script or notebook for processing, saving cleaned versions in the `processed` folder.
- Document any transformations applied to the raw data in the `processed` folder README or in the data dictionary.
- Update the data dictionary to include explanations for each raw feature and any derived features after processing.
