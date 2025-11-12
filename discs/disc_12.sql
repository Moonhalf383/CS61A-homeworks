CREATE TABLE pizzas AS
  SELECT "Artichoke" AS name, 12 AS open, 15 AS close UNION
  SELECT "La Val's"         , 11        , 22          UNION
  SELECT "Sliver"           , 11        , 20          UNION
  SELECT "Cheeseboard"      , 16        , 23          UNION
  SELECT "Emilia's"         , 13        , 18;

CREATE TABLE meals AS
  SELECT "breakfast" AS meal, 11 AS time UNION
  SELECT "lunch"            , 13         UNION
  SELECT "dinner"           , 19         UNION
  SELECT "snack"            , 22;


SELECT name as name 
FROM pizzas 
WHERE open < 13
ORDER BY name DESC;

SELECT name as name,MAX(0,(14 - open)) as duration
FROM pizzas 
ORDER BY duration DESC;

-- Pizza places that are open for late-night-snack time and when they close
  SELECT name || " closes at " || close AS status
  FROM pizzas,meals 
  WHERE close >= time and meal = "snack";


-- Two meals at the same place
  SELECT a.meal AS first, b.meal AS second, name
  FROM meals as a, meals as b, pizzas
  WHERE a.time < b.time and a.time > open and b.time < close;





