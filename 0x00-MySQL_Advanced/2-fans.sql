--- selecct grouped data by origin and order by fans
SELECT origin, sum(fans) as nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;