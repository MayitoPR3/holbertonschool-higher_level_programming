USE `mysql`;

-- Check if the table exists; if not, create it
CREATE TABLE IF NOT EXISTS `first_table` (
    `id` INT,
    `name` VARCHAR(256)
);