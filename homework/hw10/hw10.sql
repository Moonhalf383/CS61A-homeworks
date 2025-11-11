CREATE TABLE parents AS
  SELECT "ace" AS parent, "bella" AS child UNION
  SELECT "ace"          , "charlie"        UNION
  SELECT "daisy"        , "hank"           UNION
  SELECT "finn"         , "ace"            UNION
  SELECT "finn"         , "daisy"          UNION
  SELECT "finn"         , "ginger"         UNION
  SELECT "ellie"        , "finn";

CREATE TABLE dogs AS
  SELECT "ace" AS name, "long" AS fur, 26 AS height UNION
  SELECT "bella"      , "short"      , 52           UNION
  SELECT "charlie"    , "long"       , 47           UNION
  SELECT "daisy"      , "long"       , 46           UNION
  SELECT "ellie"      , "short"      , 35           UNION
  SELECT "finn"       , "curly"      , 32           UNION
  SELECT "ginger"     , "short"      , 28           UNION
  SELECT "hank"       , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT child AS chil 
  FROM dogs,parents
  where parent = name 
  ORDER BY -height; 


-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT name as name,size as size
  FROM dogs,sizes
  where height <= max and height > min;


-- [Optional] Filling out this helper table is recommended
CREATE TABLE siblings AS
  SELECT a.child as sis1,b.child as sis2  
  FROM parents as a,parents as b 
  where a.parent = b.parent and a.child < b.child; 


-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT "The two siblings, "||c.name||" and "||d.name||", have the same size: "||c.size
  FROM siblings,size_of_dogs as c,size_of_dogs as d 
  where sis1 = c.name and sis2 = d.name and c.size = d.size; 



-- Height range for each fur type where all of the heights differ by no more than 30% from the average height

CREATE TABLE low_variance AS
SELECT 
    fur,
    MAX(height) - MIN(height) AS height_range
FROM dogs
GROUP BY fur
HAVING 
    MIN(height) >= 0.7 * AVG(height)
    AND
    MAX(height) <= 1.3 * AVG(height);
