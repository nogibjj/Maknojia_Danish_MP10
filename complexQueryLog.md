```sql

WITH player_stats AS (
    SELECT '2024' AS season, 
        p.PLAYER_NAME AS player, 
        r.TEAM AS team, 
        r.OPP AS opponent, 
        p.PROJ_FPTS AS projected_points
    FROM drm85_mp6.drm85_wr_points p
    JOIN drm85_mp6.drm85_wr_ranking r ON p.PLAYER_NAME = r.PLAYER_NAME
    WHERE p.PROJ_FPTS IS NOT NULL
),
team_player_stats AS (
    SELECT team, 
        player, 
        AVG(projected_points) AS avg_projected_points
    FROM player_stats
    GROUP BY team, player
)

SELECT team, player, avg_projected_points
FROM team_player_stats
ORDER BY avg_projected_points DESC
LIMIT 10;


    
```

```response from databricks
[Row(team='DAL', player='CeeDee Lamb', avg_projected_points=19.100000381469727), Row(team='HOU', player='Nico Collins', avg_projected_points=17.700000762939453), Row(team='CIN', player="Ja'Marr Chase", avg_projected_points=17.399999618530273), Row(team='MIN', player='Justin Jefferson', avg_projected_points=17.200000762939453), Row(team='SEA', player='DK Metcalf', avg_projected_points=16.799999237060547), Row(team='GB', player='Jayden Reed', avg_projected_points=16.100000381469727), Row(team='TB', player='Chris Godwin', avg_projected_points=16.0), Row(team='ARI', player='Marvin Harrison Jr.', avg_projected_points=15.699999809265137), Row(team='SF', player='Deebo Samuel Sr.', avg_projected_points=15.5), Row(team='CAR', player='Diontae Johnson', avg_projected_points=15.5)]
```

```sql

WITH player_stats AS (
    SELECT '2024' AS season, 
        p.PLAYER_NAME AS player, 
        r.TEAM AS team, 
        r.OPP AS opponent, 
        p.PROJ_FPTS AS projected_points
    FROM drm85_mp6.drm85_wr_points p
    JOIN drm85_mp6.drm85_wr_ranking r ON p.PLAYER_NAME = r.PLAYER_NAME
    WHERE p.PROJ_FPTS IS NOT NULL
),
team_player_stats AS (
    SELECT team, 
        player, 
        AVG(projected_points) AS avg_projected_points
    FROM player_stats
    GROUP BY team, player
)

SELECT team, player, avg_projected_points
FROM team_player_stats
ORDER BY avg_projected_points DESC
LIMIT 10;
    
```

```response from databricks
[Row(team='DAL', player='CeeDee Lamb', avg_projected_points=19.100000381469727), Row(team='HOU', player='Nico Collins', avg_projected_points=17.700000762939453), Row(team='CIN', player="Ja'Marr Chase", avg_projected_points=17.399999618530273), Row(team='MIN', player='Justin Jefferson', avg_projected_points=17.200000762939453), Row(team='SEA', player='DK Metcalf', avg_projected_points=16.799999237060547), Row(team='GB', player='Jayden Reed', avg_projected_points=16.100000381469727), Row(team='TB', player='Chris Godwin', avg_projected_points=16.0), Row(team='ARI', player='Marvin Harrison Jr.', avg_projected_points=15.699999809265137), Row(team='CAR', player='Diontae Johnson', avg_projected_points=15.5), Row(team='SF', player='Deebo Samuel Sr.', avg_projected_points=15.5)]
```

```sql

WITH player_stats AS (
    SELECT '2024' AS season, 
        p.PLAYER_NAME AS player, 
        r.TEAM AS team, 
        r.OPP AS opponent, 
        p.PROJ_FPTS AS projected_points
    FROM drm85_mp6.drm85_wr_points p
    JOIN drm85_mp6.drm85_wr_ranking r ON p.PLAYER_NAME = r.PLAYER_NAME
    WHERE p.PROJ_FPTS IS NOT NULL
),
team_player_stats AS (
    SELECT team, 
        player, 
        AVG(projected_points) AS avg_projected_points
    FROM player_stats
    GROUP BY team, player
)

SELECT team, player, avg_projected_points
FROM team_player_stats
ORDER BY avg_projected_points DESC
LIMIT 10;
    
```

```response from databricks
[Row(team='DAL', player='CeeDee Lamb', avg_projected_points=19.100000381469727), Row(team='HOU', player='Nico Collins', avg_projected_points=17.700000762939453), Row(team='CIN', player="Ja'Marr Chase", avg_projected_points=17.399999618530273), Row(team='MIN', player='Justin Jefferson', avg_projected_points=17.200000762939453), Row(team='SEA', player='DK Metcalf', avg_projected_points=16.799999237060547), Row(team='GB', player='Jayden Reed', avg_projected_points=16.100000381469727), Row(team='TB', player='Chris Godwin', avg_projected_points=16.0), Row(team='ARI', player='Marvin Harrison Jr.', avg_projected_points=15.699999809265137), Row(team='SF', player='Deebo Samuel Sr.', avg_projected_points=15.5), Row(team='CAR', player='Diontae Johnson', avg_projected_points=15.5)]
```

```sql

    WITH player_stats AS (
        SELECT '2024' AS season,
            p.PLAYER_NAME AS player,
            r.TEAM AS team,
            r.OPP AS opponent,
            p.PROJ_FPTS AS projected_points
        FROM drm85_mp6.drm85_wr_points p
        JOIN drm85_mp6.drm85_wr_ranking r ON p.PLAYER_NAME = r.PLAYER_NAME
        WHERE p.PROJ_FPTS IS NOT NULL
    ),
    team_player_stats AS (
        SELECT team,
            player,
            AVG(projected_points) AS avg_projected_points
        FROM player_stats
        GROUP BY team, player
    )
    
    SELECT team, player, avg_projected_points
    FROM team_player_stats
    ORDER BY avg_projected_points DESC
    LIMIT 10;
    
```

```response from databricks
[Row(team='DAL', player='CeeDee Lamb', avg_projected_points=19.100000381469727), Row(team='HOU', player='Nico Collins', avg_projected_points=17.700000762939453), Row(team='CIN', player="Ja'Marr Chase", avg_projected_points=17.399999618530273), Row(team='MIN', player='Justin Jefferson', avg_projected_points=17.200000762939453), Row(team='SEA', player='DK Metcalf', avg_projected_points=16.799999237060547), Row(team='GB', player='Jayden Reed', avg_projected_points=16.100000381469727), Row(team='TB', player='Chris Godwin', avg_projected_points=16.0), Row(team='ARI', player='Marvin Harrison Jr.', avg_projected_points=15.699999809265137), Row(team='SF', player='Deebo Samuel Sr.', avg_projected_points=15.5), Row(team='CAR', player='Diontae Johnson', avg_projected_points=15.5)]
```

```sql

    WITH player_stats AS (
        SELECT '2024' AS season,
            p.PLAYER_NAME AS player,
            r.TEAM AS team,
            r.OPP AS opponent,
            p.PROJ_FPTS AS projected_points
        FROM drm85_mp6.drm85_wr_points p
        JOIN drm85_mp6.drm85_wr_ranking r ON p.PLAYER_NAME = r.PLAYER_NAME
        WHERE p.PROJ_FPTS IS NOT NULL
    ),
    team_player_stats AS (
        SELECT team,
            player,
            AVG(projected_points) AS avg_projected_points
        FROM player_stats
        GROUP BY team, player
    )
    
    SELECT team, player, avg_projected_points
    FROM team_player_stats
    ORDER BY avg_projected_points DESC
    LIMIT 10;
    
```

```response from databricks
[Row(team='DAL', player='CeeDee Lamb', avg_projected_points=19.100000381469727), Row(team='HOU', player='Nico Collins', avg_projected_points=17.700000762939453), Row(team='CIN', player="Ja'Marr Chase", avg_projected_points=17.399999618530273), Row(team='MIN', player='Justin Jefferson', avg_projected_points=17.200000762939453), Row(team='SEA', player='DK Metcalf', avg_projected_points=16.799999237060547), Row(team='GB', player='Jayden Reed', avg_projected_points=16.100000381469727), Row(team='TB', player='Chris Godwin', avg_projected_points=16.0), Row(team='ARI', player='Marvin Harrison Jr.', avg_projected_points=15.699999809265137), Row(team='CAR', player='Diontae Johnson', avg_projected_points=15.5), Row(team='SF', player='Deebo Samuel Sr.', avg_projected_points=15.5)]
```

