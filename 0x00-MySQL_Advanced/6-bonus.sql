-- script that creates a stored procedure AddBonus that adds a new correction for a student
DROP PROCEDURE IF EXISTS AddBonus
DELIMITER $$
CREATE PROCEDURE AddBonus(user_id, project_name, score)