# Write your MySQL query statement below
SELECT user_id, COUNT(user_id) AS followers_count
FROM Followers
GROUP BY user_id
order BY user_id