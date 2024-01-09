-- it lists all records in the table second_table with a score >= 10 in my MySQL server.
-- the records are ordered by descending score
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
