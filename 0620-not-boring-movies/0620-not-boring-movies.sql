SELECT 
    id, 
    movie, 
    description, 
    rating 
FROM 
    Cinema 
WHERE 
    id % 2 = 1               -- Select odd-numbered IDs
    AND description != 'boring'  -- Exclude boring descriptions
ORDER BY 
    rating DESC;            -- Order the result by rating in descending order
