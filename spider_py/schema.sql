CREATE TABLE `focus` (
	`user_name` VARCHAR(50) NOT NULL,
	`user_id` INT(10) NOT NULL,
	`user_img` VARCHAR(255) NOT NULL,
	`avatar` VARCHAR(255) NOT NULL,
	`sign` VARCHAR(255) NOT NULL,
	`title` VARCHAR(50) NOT NULL,
	`title_img` VARCHAR(255) NOT NULL,
	`url` VARCHAR(50) NOT NULL,
	`release_date` VARCHAR(50) NOT NULL,
	`description` VARCHAR(255) NOT NULL,
	`tags` VARCHAR(255) NOT NULL,
	`video_time` SMALLINT(6) NOT NULL
)
	ENGINE=MyISAM
;
