drop database if exists awesome;

create database awesome;

use awesome;

grant select, insert, update, delete on awesome.* to 'www-data'@'*' identified by 'www-data';

create table users (
    `id` varchar(50) not null,
    `email` varchar(50) not null,
    `passwd` varchar(50) not null,
    `admin` bool not null,
    `name` varchar(50) not null,
    `image` varchar(500) not null,
    `created_at` real not null,
    unique key `idx_email` (`email`),
    key `idx_created_at` (`created_at`),
    primary key (`id`)
) engine=innodb default charset=utf8;

create table blogs (
    `id` varchar(50) not null,
    `user_id` varchar(50) not null,
    `user_name` varchar(50) not null,
    `user_image` varchar(500) not null,
    `name` varchar(50) not null,
    `sub_name` varchar(50) not null,
    `summary` varchar(200) not null,
    `content` mediumtext not null,
    `created_at` real not null,
    key `idx_created_at` (`created_at`),
    primary key (`id`)
) engine=innodb default charset=utf8;

create table comments (
    `id` varchar(50) not null,
    `blog_id` varchar(50) not null,
    `user_id` varchar(50) not null,
    `user_name` varchar(50) not null,
    `user_image` varchar(500) not null,
    `content` mediumtext not null,
    `created_at` real not null,
    key `idx_created_at` (`created_at`),
    primary key (`id`)
) engine=innodb default charset=utf8;

CREATE TABLE `acfun_focus` (
    `id` VARCHAR(50) NOT NULL,
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
    `video_time` SMALLINT(6) NOT NULL,
    PRIMARY KEY (`id`)
)ENGINE=innodb DEFAULT CHARSET=utf8;

CREATE TABLE `jinguang` (
	`id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
	`pid` INT(10) UNSIGNED NOT NULL DEFAULT '0',
	`title` VARCHAR(50) NOT NULL DEFAULT 'no title',
	`title_url` VARCHAR(50) NOT NULL DEFAULT 'no url',
	`post_time` VARCHAR(50) NOT NULL DEFAULT 'no specific date',
	`add_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	PRIMARY KEY (`id`)
)
COMMENT='金光布袋戏'
COLLATE='utf8_general_ci'
ENGINE=InnoDB
;

