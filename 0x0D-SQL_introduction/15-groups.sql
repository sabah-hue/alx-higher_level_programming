-- script lists number of records with same score
SELECT score, count(score) AS number FROM second_table GROUP BY score ORDER BY number DESC;
