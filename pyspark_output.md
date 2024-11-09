The operation is load data

The truncated output is: 

|    |   RK | PLAYER NAME         | TEAM   | OPP     | MATCHUP          | START/SIT   |   PROJ_FPTS |
|---:|-----:|:--------------------|:-------|:--------|:-----------------|:------------|------------:|
|  0 |    1 | CeeDee Lamb         | DAL    | at PIT  | 3 out of 5 stars | A+          |        19.1 |
|  1 |    2 | Nico Collins        | HOU    | vs. BUF | 3 out of 5 stars | A+          |        17.7 |
|  2 |    3 | Ja'Marr Chase       | CIN    | vs. BAL | 3 out of 5 stars | A+          |        17.4 |
|  3 |    4 | Justin Jefferson    | MIN    | vs. NYJ | 3 out of 5 stars | A+          |        17.2 |
|  4 |    5 | DK Metcalf          | SEA    | vs. NYG | 3 out of 5 stars | A+          |        16.8 |
|  5 |    6 | Jayden Reed         | GB     | at LAR  | 3 out of 5 stars | A           |        16.1 |
|  6 |    7 | Chris Godwin        | TB     | at ATL  | 3 out of 5 stars | A           |        16   |
|  7 |    8 | Marvin Harrison Jr. | ARI    | at SF   | 3 out of 5 stars | A           |        15.7 |
|  8 |    9 | Diontae Johnson     | CAR    | at CHI  | 3 out of 5 stars | A           |        15.5 |
|  9 |   10 | Deebo Samuel Sr.    | SF     | vs. ARI | 4 out of 5 stars | A           |        15.5 |

The operation is describe data

The truncated output is: 

|    | summary   |       RK | PLAYER NAME   | TEAM   | OPP    | MATCHUP          | START/SIT   |   PROJ_FPTS |
|---:|:----------|---------:|:--------------|:-------|:-------|:-----------------|:------------|------------:|
|  0 | count     | 155      | 155           | 155    | 155    | 155              | 155         |   155       |
|  1 | mean      |  78      |               |        |        |                  |             |     6.06581 |
|  2 | stddev    |  44.8888 |               |        |        |                  |             |     5.47336 |
|  3 | min       |   1      | A.T. Perry    | ARI    | -      | -                | A           |     0       |
|  4 | max       | 155      | Zay Flowers   | WAS    | vs. TB | 5 out of 5 stars | F           |    19.1     |

The operation is query data

The query is 
        SELECT TEAM, AVG(PROJ_FPTS) AS avg_proj_points 
        FROM WRRankings 
        GROUP BY TEAM 
        ORDER BY avg_proj_points DESC
        

The truncated output is: 

|    | TEAM   |   avg_proj_points |
|---:|:-------|------------------:|
|  0 | LV     |           8.63333 |
|  1 | IND    |           7.64    |
|  2 | DAL    |           7.64    |
|  3 | TB     |           7.6     |
|  4 | GB     |           7.46    |
|  5 | SEA    |           7.23333 |
|  6 | WAS    |           7.2     |
|  7 | ATL    |           7.12    |
|  8 | LAR    |           7.02    |
|  9 | CAR    |           7       |
| 10 | CIN    |           6.71667 |
| 11 | HOU    |           6.62857 |
| 12 | SF     |           6.61667 |
| 13 | BUF    |           6.4     |
| 14 | NO     |           6.4     |
| 15 | MIN    |           6.31667 |
| 16 | JAC    |           6.23333 |
| 17 | CHI    |           5.95    |
| 18 | KC     |           5.86    |
| 19 | ARI    |           5.78333 |
| 20 | NYJ    |           5.75    |
| 21 | CLE    |           5.53333 |
| 22 | PIT    |           5.06    |
| 23 | DEN    |           4.96667 |
| 24 | NYG    |           4.38333 |
| 25 | BAL    |           4.38333 |
| 26 | MIA    |           3.74286 |
| 27 | NE     |           3.44286 |
| 28 | FA     |           0       |

The operation is transform data

The truncated output is: 

|    |   RK | PLAYER NAME         | TEAM   | OPP     | MATCHUP          | START/SIT   |   PROJ_FPTS | Start_Sit_Recommendation   |
|---:|-----:|:--------------------|:-------|:--------|:-----------------|:------------|------------:|:---------------------------|
|  0 |    1 | CeeDee Lamb         | DAL    | at PIT  | 3 out of 5 stars | A+          |        19.1 | Must Start                 |
|  1 |    2 | Nico Collins        | HOU    | vs. BUF | 3 out of 5 stars | A+          |        17.7 | Must Start                 |
|  2 |    3 | Ja'Marr Chase       | CIN    | vs. BAL | 3 out of 5 stars | A+          |        17.4 | Must Start                 |
|  3 |    4 | Justin Jefferson    | MIN    | vs. NYJ | 3 out of 5 stars | A+          |        17.2 | Must Start                 |
|  4 |    5 | DK Metcalf          | SEA    | vs. NYG | 3 out of 5 stars | A+          |        16.8 | Must Start                 |
|  5 |    6 | Jayden Reed         | GB     | at LAR  | 3 out of 5 stars | A           |        16.1 | Consider Starting          |
|  6 |    7 | Chris Godwin        | TB     | at ATL  | 3 out of 5 stars | A           |        16   | Consider Starting          |
|  7 |    8 | Marvin Harrison Jr. | ARI    | at SF   | 3 out of 5 stars | A           |        15.7 | Consider Starting          |
|  8 |    9 | Diontae Johnson     | CAR    | at CHI  | 3 out of 5 stars | A           |        15.5 | Consider Starting          |
|  9 |   10 | Deebo Samuel Sr.    | SF     | vs. ARI | 4 out of 5 stars | A           |        15.5 | Consider Starting          |

The operation is load data

The truncated output is: 

|    |   RK | PLAYER NAME         | TEAM   | OPP     | MATCHUP          | START/SIT   |   PROJ_FPTS |
|---:|-----:|:--------------------|:-------|:--------|:-----------------|:------------|------------:|
|  0 |    1 | CeeDee Lamb         | DAL    | at PIT  | 3 out of 5 stars | A+          |        19.1 |
|  1 |    2 | Nico Collins        | HOU    | vs. BUF | 3 out of 5 stars | A+          |        17.7 |
|  2 |    3 | Ja'Marr Chase       | CIN    | vs. BAL | 3 out of 5 stars | A+          |        17.4 |
|  3 |    4 | Justin Jefferson    | MIN    | vs. NYJ | 3 out of 5 stars | A+          |        17.2 |
|  4 |    5 | DK Metcalf          | SEA    | vs. NYG | 3 out of 5 stars | A+          |        16.8 |
|  5 |    6 | Jayden Reed         | GB     | at LAR  | 3 out of 5 stars | A           |        16.1 |
|  6 |    7 | Chris Godwin        | TB     | at ATL  | 3 out of 5 stars | A           |        16   |
|  7 |    8 | Marvin Harrison Jr. | ARI    | at SF   | 3 out of 5 stars | A           |        15.7 |
|  8 |    9 | Diontae Johnson     | CAR    | at CHI  | 3 out of 5 stars | A           |        15.5 |
|  9 |   10 | Deebo Samuel Sr.    | SF     | vs. ARI | 4 out of 5 stars | A           |        15.5 |

The operation is describe data

The truncated output is: 

|    | summary   |       RK | PLAYER NAME   | TEAM   | OPP    | MATCHUP          | START/SIT   |   PROJ_FPTS |
|---:|:----------|---------:|:--------------|:-------|:-------|:-----------------|:------------|------------:|
|  0 | count     | 155      | 155           | 155    | 155    | 155              | 155         |   155       |
|  1 | mean      |  78      |               |        |        |                  |             |     6.06581 |
|  2 | stddev    |  44.8888 |               |        |        |                  |             |     5.47336 |
|  3 | min       |   1      | A.T. Perry    | ARI    | -      | -                | A           |     0       |
|  4 | max       | 155      | Zay Flowers   | WAS    | vs. TB | 5 out of 5 stars | F           |    19.1     |

The operation is transform data

The truncated output is: 

|    |   RK | PLAYER NAME         | TEAM   | OPP     | MATCHUP          | START/SIT   |   PROJ_FPTS | Start_Sit_Recommendation   |
|---:|-----:|:--------------------|:-------|:--------|:-----------------|:------------|------------:|:---------------------------|
|  0 |    1 | CeeDee Lamb         | DAL    | at PIT  | 3 out of 5 stars | A+          |        19.1 | Must Start                 |
|  1 |    2 | Nico Collins        | HOU    | vs. BUF | 3 out of 5 stars | A+          |        17.7 | Must Start                 |
|  2 |    3 | Ja'Marr Chase       | CIN    | vs. BAL | 3 out of 5 stars | A+          |        17.4 | Must Start                 |
|  3 |    4 | Justin Jefferson    | MIN    | vs. NYJ | 3 out of 5 stars | A+          |        17.2 | Must Start                 |
|  4 |    5 | DK Metcalf          | SEA    | vs. NYG | 3 out of 5 stars | A+          |        16.8 | Must Start                 |
|  5 |    6 | Jayden Reed         | GB     | at LAR  | 3 out of 5 stars | A           |        16.1 | Consider Starting          |
|  6 |    7 | Chris Godwin        | TB     | at ATL  | 3 out of 5 stars | A           |        16   | Consider Starting          |
|  7 |    8 | Marvin Harrison Jr. | ARI    | at SF   | 3 out of 5 stars | A           |        15.7 | Consider Starting          |
|  8 |    9 | Diontae Johnson     | CAR    | at CHI  | 3 out of 5 stars | A           |        15.5 | Consider Starting          |
|  9 |   10 | Deebo Samuel Sr.    | SF     | vs. ARI | 4 out of 5 stars | A           |        15.5 | Consider Starting          |

The operation is load data

The truncated output is: 

|    |   RK | PLAYER NAME         | TEAM   | OPP     | MATCHUP          | START/SIT   |   PROJ_FPTS |
|---:|-----:|:--------------------|:-------|:--------|:-----------------|:------------|------------:|
|  0 |    1 | CeeDee Lamb         | DAL    | at PIT  | 3 out of 5 stars | A+          |        19.1 |
|  1 |    2 | Nico Collins        | HOU    | vs. BUF | 3 out of 5 stars | A+          |        17.7 |
|  2 |    3 | Ja'Marr Chase       | CIN    | vs. BAL | 3 out of 5 stars | A+          |        17.4 |
|  3 |    4 | Justin Jefferson    | MIN    | vs. NYJ | 3 out of 5 stars | A+          |        17.2 |
|  4 |    5 | DK Metcalf          | SEA    | vs. NYG | 3 out of 5 stars | A+          |        16.8 |
|  5 |    6 | Jayden Reed         | GB     | at LAR  | 3 out of 5 stars | A           |        16.1 |
|  6 |    7 | Chris Godwin        | TB     | at ATL  | 3 out of 5 stars | A           |        16   |
|  7 |    8 | Marvin Harrison Jr. | ARI    | at SF   | 3 out of 5 stars | A           |        15.7 |
|  8 |    9 | Diontae Johnson     | CAR    | at CHI  | 3 out of 5 stars | A           |        15.5 |
|  9 |   10 | Deebo Samuel Sr.    | SF     | vs. ARI | 4 out of 5 stars | A           |        15.5 |

The operation is describe data

The truncated output is: 

|    | summary   |       RK | PLAYER NAME   | TEAM   | OPP    | MATCHUP          | START/SIT   |   PROJ_FPTS |
|---:|:----------|---------:|:--------------|:-------|:-------|:-----------------|:------------|------------:|
|  0 | count     | 155      | 155           | 155    | 155    | 155              | 155         |   155       |
|  1 | mean      |  78      |               |        |        |                  |             |     6.06581 |
|  2 | stddev    |  44.8888 |               |        |        |                  |             |     5.47336 |
|  3 | min       |   1      | A.T. Perry    | ARI    | -      | -                | A           |     0       |
|  4 | max       | 155      | Zay Flowers   | WAS    | vs. TB | 5 out of 5 stars | F           |    19.1     |

The operation is query data

The query is 
        SELECT TEAM, AVG(PROJ_FPTS) AS avg_proj_points 
        FROM WRRankings 
        GROUP BY TEAM 
        ORDER BY avg_proj_points DESC
        

The truncated output is: 

|    | TEAM   |   avg_proj_points |
|---:|:-------|------------------:|
|  0 | LV     |           8.63333 |
|  1 | IND    |           7.64    |
|  2 | DAL    |           7.64    |
|  3 | TB     |           7.6     |
|  4 | GB     |           7.46    |
|  5 | SEA    |           7.23333 |
|  6 | WAS    |           7.2     |
|  7 | ATL    |           7.12    |
|  8 | LAR    |           7.02    |
|  9 | CAR    |           7       |
| 10 | CIN    |           6.71667 |
| 11 | HOU    |           6.62857 |
| 12 | SF     |           6.61667 |
| 13 | BUF    |           6.4     |
| 14 | NO     |           6.4     |
| 15 | MIN    |           6.31667 |
| 16 | JAC    |           6.23333 |
| 17 | CHI    |           5.95    |
| 18 | KC     |           5.86    |
| 19 | ARI    |           5.78333 |
| 20 | NYJ    |           5.75    |
| 21 | CLE    |           5.53333 |
| 22 | PIT    |           5.06    |
| 23 | DEN    |           4.96667 |
| 24 | NYG    |           4.38333 |
| 25 | BAL    |           4.38333 |
| 26 | MIA    |           3.74286 |
| 27 | NE     |           3.44286 |
| 28 | FA     |           0       |

The operation is transform data

The truncated output is: 

|    |   RK | PLAYER NAME         | TEAM   | OPP     | MATCHUP          | START/SIT   |   PROJ_FPTS | Start_Sit_Recommendation   |
|---:|-----:|:--------------------|:-------|:--------|:-----------------|:------------|------------:|:---------------------------|
|  0 |    1 | CeeDee Lamb         | DAL    | at PIT  | 3 out of 5 stars | A+          |        19.1 | Must Start                 |
|  1 |    2 | Nico Collins        | HOU    | vs. BUF | 3 out of 5 stars | A+          |        17.7 | Must Start                 |
|  2 |    3 | Ja'Marr Chase       | CIN    | vs. BAL | 3 out of 5 stars | A+          |        17.4 | Must Start                 |
|  3 |    4 | Justin Jefferson    | MIN    | vs. NYJ | 3 out of 5 stars | A+          |        17.2 | Must Start                 |
|  4 |    5 | DK Metcalf          | SEA    | vs. NYG | 3 out of 5 stars | A+          |        16.8 | Must Start                 |
|  5 |    6 | Jayden Reed         | GB     | at LAR  | 3 out of 5 stars | A           |        16.1 | Consider Starting          |
|  6 |    7 | Chris Godwin        | TB     | at ATL  | 3 out of 5 stars | A           |        16   | Consider Starting          |
|  7 |    8 | Marvin Harrison Jr. | ARI    | at SF   | 3 out of 5 stars | A           |        15.7 | Consider Starting          |
|  8 |    9 | Diontae Johnson     | CAR    | at CHI  | 3 out of 5 stars | A           |        15.5 | Consider Starting          |
|  9 |   10 | Deebo Samuel Sr.    | SF     | vs. ARI | 4 out of 5 stars | A           |        15.5 | Consider Starting          |

