
SELECT 
ROUND(SUM(CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END) * 100.0 / COUNT(*),2) AS immediate_percentage
FROM (
SELECT customer_id, MIN(order_date) AS order_date,
MIN(customer_pref_delivery_date) AS customer_pref_delivery_date
FROM delivery
GROUP BY customer_id
) AS first_orders;