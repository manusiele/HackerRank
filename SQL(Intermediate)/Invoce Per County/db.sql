WITH country_stats AS (
    SELECT 
        co.country_name,
        COUNT(i.id) as total_invoices,
        AVG(i.total_price) as avg_amount
    FROM country co
    JOIN city ci ON co.id = ci.country_id
    JOIN customer cu ON ci.id = cu.city_id
    JOIN invoice i ON cu.id = i.customer_id
    GROUP BY co.id, co.country_name
),
overall_avg AS (
    SELECT AVG(i.total_price) as overall_average
    FROM invoice i
)
SELECT 
    cs.country_name,
    cs.total_invoices,
    FORMAT(cs.avg_amount, 6) as avg_amount
FROM country_stats cs
CROSS JOIN overall_avg oa
WHERE cs.avg_amount > oa.overall_average
ORDER BY cs.country_name;