# Danish_Maknojia_MP10

[![CI](https://github.com/nogibjj/Maknojia_Danish_MP10/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Maknojia_Danish_MP10/actions/workflows/cicd.yml)


# Data Processing with PySpark

This project demonstrates basic operations in PySpark, such as loading data, describing data, querying data, and transforming data.

### Prerequisites

#### 1. Installing Spark Locally
To run Spark locally, download and install Spark by following the official [Apache Spark Installation Guide](https://spark.apache.org/downloads.html). 

#### 2. Using GitHub Codespaces
You can use GitHub Codespaces to set up a Spark environment with minimal setup. Codespaces with Linux images often come with Spark pre-installed. You can use Professor Gift's template repository to quickly start with PySpark on GitHub Codespaces: [Gift's Ruff Template](https://github.com/nogibjj/python-ruff-template).

## Operations

The following PySpark operations are demonstrated in this project:

### 1. Loading Data
This operation loads a sample data file into a Spark DataFrame.

**Truncated Output:**

|    |   RK | PLAYER NAME         | TEAM   | OPP     | MATCHUP          | START/SIT   |   PROJ_FPTS |
|---:|-----:|:--------------------|:-------|:--------|:-----------------|:------------|------------:|
|  0 |    1 | CeeDee Lamb         | DAL    | at PIT  | 3 out of 5 stars | A+          |        19.1 |
|  1 |    2 | Nico Collins        | HOU    | vs. BUF | 3 out of 5 stars | A+          |        17.7 |
| ... | ... | ...                 | ...    | ...     | ...              | ...         |         ... |

### 2. Describing Data
This operation describes the data, showing the count, mean, standard deviation, min, and max for numerical columns.

**Truncated Output:**

|    | summary   |       RK | PLAYER NAME   | TEAM   | OPP    | MATCHUP          | START/SIT   |   PROJ_FPTS |
|---:|:----------|---------:|:--------------|:-------|:-------|:-----------------|:------------|------------:|
|  0 | count     | 155      | 155           | 155    | 155    | 155              | 155         |   155       |
|  1 | mean      |  78      |               |        |        |                  |             |     6.06581 |
| ... | ...      | ...      | ...           | ...    | ...    | ...              | ...         |         ... |

### 3. Querying Data
A sample query to calculate the average projected fantasy points per team.

**Query:**
```sql
SELECT TEAM, AVG(PROJ_FPTS) AS avg_proj_points 
FROM WRRankings 
GROUP BY TEAM 
ORDER BY avg_proj_points DESC
```

**Truncated Output:**

|    | TEAM   |   avg_proj_points |
|---:|:-------|------------------:|
|  0 | LV     |           8.63    |
|  1 | IND    |           7.64    |
| ... | ...   | ...               |

### 4. Transforming Data
This operation adds a recommendation column based on the `START/SIT` column values.

**Truncated Output:**

|    |   RK | PLAYER NAME         | TEAM   | OPP     | MATCHUP          | START/SIT   |   PROJ_FPTS | Start_Sit_Recommendation   |
|---:|-----:|:--------------------|:-------|:--------|:-----------------|:------------|------------:|:---------------------------|
|  0 |    1 | CeeDee Lamb         | DAL    | at PIT  | 3 out of 5 stars | A+          |        19.1 | Must Start                 |
|  1 |    2 | Nico Collins        | HOU    | vs. BUF | 3 out of 5 stars | A+          |        17.7 | Must Start                 |
| ... | ... | ...                 | ...    | ...     | ...              | ...         |         ... | ...

## Running the Code

1. Clone this repository.
2. Set up Spark and ensure the environment is configured.
3. Run each operation in a notebook or a script to see the corresponding outputs.
