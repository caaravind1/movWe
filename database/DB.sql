/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.7.9 : Database - film_industry_scms
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`film_industry_scms` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `film_industry_scms`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=105 DEFAULT CHARSET=latin1;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add allocate',1,'add_allocate'),
(2,'Can change allocate',1,'change_allocate'),
(3,'Can delete allocate',1,'delete_allocate'),
(4,'Can view allocate',1,'view_allocate'),
(5,'Can add booking',2,'add_booking'),
(6,'Can change booking',2,'change_booking'),
(7,'Can delete booking',2,'delete_booking'),
(8,'Can view booking',2,'view_booking'),
(9,'Can add customer',3,'add_customer'),
(10,'Can change customer',3,'change_customer'),
(11,'Can delete customer',3,'delete_customer'),
(12,'Can view customer',3,'view_customer'),
(13,'Can add login',4,'add_login'),
(14,'Can change login',4,'change_login'),
(15,'Can delete login',4,'delete_login'),
(16,'Can view login',4,'view_login'),
(17,'Can add opportunities',5,'add_opportunities'),
(18,'Can change opportunities',5,'change_opportunities'),
(19,'Can delete opportunities',5,'delete_opportunities'),
(20,'Can view opportunities',5,'view_opportunities'),
(21,'Can add production',6,'add_production'),
(22,'Can change production',6,'change_production'),
(23,'Can delete production',6,'delete_production'),
(24,'Can view production',6,'view_production'),
(25,'Can add request',7,'add_request'),
(26,'Can change request',7,'change_request'),
(27,'Can delete request',7,'delete_request'),
(28,'Can view request',7,'view_request'),
(29,'Can add screen',8,'add_screen'),
(30,'Can change screen',8,'change_screen'),
(31,'Can delete screen',8,'delete_screen'),
(32,'Can view screen',8,'view_screen'),
(33,'Can add seattype',9,'add_seattype'),
(34,'Can change seattype',9,'change_seattype'),
(35,'Can delete seattype',9,'delete_seattype'),
(36,'Can view seattype',9,'view_seattype'),
(37,'Can add timing',10,'add_timing'),
(38,'Can change timing',10,'change_timing'),
(39,'Can delete timing',10,'delete_timing'),
(40,'Can view timing',10,'view_timing'),
(41,'Can add type',11,'add_type'),
(42,'Can change type',11,'change_type'),
(43,'Can delete type',11,'delete_type'),
(44,'Can view type',11,'view_type'),
(45,'Can add theater',12,'add_theater'),
(46,'Can change theater',12,'change_theater'),
(47,'Can delete theater',12,'delete_theater'),
(48,'Can view theater',12,'view_theater'),
(49,'Can add seating',13,'add_seating'),
(50,'Can change seating',13,'change_seating'),
(51,'Can delete seating',13,'delete_seating'),
(52,'Can view seating',13,'view_seating'),
(53,'Can add schedule',14,'add_schedule'),
(54,'Can change schedule',14,'change_schedule'),
(55,'Can delete schedule',14,'delete_schedule'),
(56,'Can view schedule',14,'view_schedule'),
(57,'Can add requestimage',15,'add_requestimage'),
(58,'Can change requestimage',15,'change_requestimage'),
(59,'Can delete requestimage',15,'delete_requestimage'),
(60,'Can view requestimage',15,'view_requestimage'),
(61,'Can add projects',16,'add_projects'),
(62,'Can change projects',16,'change_projects'),
(63,'Can delete projects',16,'delete_projects'),
(64,'Can view projects',16,'view_projects'),
(65,'Can add preference',17,'add_preference'),
(66,'Can change preference',17,'change_preference'),
(67,'Can delete preference',17,'delete_preference'),
(68,'Can view preference',17,'view_preference'),
(69,'Can add payment',18,'add_payment'),
(70,'Can change payment',18,'change_payment'),
(71,'Can delete payment',18,'delete_payment'),
(72,'Can view payment',18,'view_payment'),
(73,'Can add film',19,'add_film'),
(74,'Can change film',19,'change_film'),
(75,'Can delete film',19,'delete_film'),
(76,'Can view film',19,'view_film'),
(77,'Can add bookingchild',20,'add_bookingchild'),
(78,'Can change bookingchild',20,'change_bookingchild'),
(79,'Can delete bookingchild',20,'delete_bookingchild'),
(80,'Can view bookingchild',20,'view_bookingchild'),
(81,'Can add log entry',21,'add_logentry'),
(82,'Can change log entry',21,'change_logentry'),
(83,'Can delete log entry',21,'delete_logentry'),
(84,'Can view log entry',21,'view_logentry'),
(85,'Can add permission',22,'add_permission'),
(86,'Can change permission',22,'change_permission'),
(87,'Can delete permission',22,'delete_permission'),
(88,'Can view permission',22,'view_permission'),
(89,'Can add group',23,'add_group'),
(90,'Can change group',23,'change_group'),
(91,'Can delete group',23,'delete_group'),
(92,'Can view group',23,'view_group'),
(93,'Can add user',24,'add_user'),
(94,'Can change user',24,'change_user'),
(95,'Can delete user',24,'delete_user'),
(96,'Can view user',24,'view_user'),
(97,'Can add content type',25,'add_contenttype'),
(98,'Can change content type',25,'change_contenttype'),
(99,'Can delete content type',25,'delete_contenttype'),
(100,'Can view content type',25,'view_contenttype'),
(101,'Can add session',26,'add_session'),
(102,'Can change session',26,'change_session'),
(103,'Can delete session',26,'delete_session'),
(104,'Can view session',26,'view_session');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'film_app','allocate'),
(2,'film_app','booking'),
(3,'film_app','customer'),
(4,'film_app','login'),
(5,'film_app','opportunities'),
(6,'film_app','production'),
(7,'film_app','request'),
(8,'film_app','screen'),
(9,'film_app','seattype'),
(10,'film_app','timing'),
(11,'film_app','type'),
(12,'film_app','theater'),
(13,'film_app','seating'),
(14,'film_app','schedule'),
(15,'film_app','requestimage'),
(16,'film_app','projects'),
(17,'film_app','preference'),
(18,'film_app','payment'),
(19,'film_app','film'),
(20,'film_app','bookingchild'),
(21,'admin','logentry'),
(22,'auth','permission'),
(23,'auth','group'),
(24,'auth','user'),
(25,'contenttypes','contenttype'),
(26,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2025-01-21 08:41:33.019884'),
(2,'auth','0001_initial','2025-01-21 08:41:33.613914'),
(3,'admin','0001_initial','2025-01-21 08:41:33.773128'),
(4,'admin','0002_logentry_remove_auto_add','2025-01-21 08:41:33.796604'),
(5,'admin','0003_logentry_add_action_flag_choices','2025-01-21 08:41:33.813354'),
(6,'contenttypes','0002_remove_content_type_name','2025-01-21 08:41:33.903743'),
(7,'auth','0002_alter_permission_name_max_length','2025-01-21 08:41:33.942996'),
(8,'auth','0003_alter_user_email_max_length','2025-01-21 08:41:33.985860'),
(9,'auth','0004_alter_user_username_opts','2025-01-21 08:41:34.005999'),
(10,'auth','0005_alter_user_last_login_null','2025-01-21 08:41:34.042525'),
(11,'auth','0006_require_contenttypes_0002','2025-01-21 08:41:34.056469'),
(12,'auth','0007_alter_validators_add_error_messages','2025-01-21 08:41:34.072529'),
(13,'auth','0008_alter_user_username_max_length','2025-01-21 08:41:34.115275'),
(14,'auth','0009_alter_user_last_name_max_length','2025-01-21 08:41:34.155969'),
(15,'auth','0010_alter_group_name_max_length','2025-01-21 08:41:34.195102'),
(16,'auth','0011_update_proxy_permissions','2025-01-21 08:41:34.215720'),
(17,'auth','0012_alter_user_first_name_max_length','2025-01-21 08:41:34.258475'),
(18,'film_app','0001_initial','2025-01-21 08:41:35.658476'),
(19,'sessions','0001_initial','2025-01-21 08:41:35.715002'),
(20,'film_app','0002_remove_projects_videos','2025-01-21 14:38:07.543794');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('1oz34so1sndv6c4a68kouujw8f0a02m6','eyJsaWQiOjUsInBpZCI6MX0:1taR0A:Va74yLCtsOh1I9AB2T3ehv43-i_0E6gGi4tOhdeJNio','2025-02-05 03:01:58.583473'),
('jtqmhlodok0kzzfinu7uenlxsdy549uu','eyJsaWQiOjN9:1tashF:q7y5DZQ22iyMR1Jr7gNXfRSNi-4T6Jwheb1S1m7tNd8','2025-02-06 08:36:17.374128'),
('bter90yhj94k40mrtlx5hm94bxvp46lu','eyJsaWQiOjN9:1tj8Zo:blVdGn3oOSDgPbKE_K_aXF75mSWFfG_mvxxcP1QeqoI','2025-03-01 03:10:44.065671'),
('ydiea68lh75lu1dajiy4okrl96nf5icb','eyJsaWQiOjF9:1tizTh:JC0bWTHbCZUPVmC1gnO1AHNX1GoxF3CXWAuEk4M6-NY','2025-02-28 17:27:49.427479'),
('30w1qlrfe0nqczxfg0b4ur5nbgq9kq8m','eyJsaWQiOjF9:1tjD6s:jA33FyE9E94zyMIdGowWvqyJo8dJPYgnXbHAAJ41E0o','2025-03-01 08:01:10.394569');

/*Table structure for table `film_app_allocate` */

DROP TABLE IF EXISTS `film_app_allocate`;

CREATE TABLE `film_app_allocate` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `played_date` varchar(70) NOT NULL,
  `status` varchar(70) NOT NULL,
  `film_id` bigint(20) NOT NULL,
  `screen_id` bigint(20) NOT NULL,
  `timing_id` bigint(20) NOT NULL,
  `theater_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `film_app_allocate_film_id_614c5cf5` (`film_id`),
  KEY `film_app_allocate_screen_id_1dc79fbe` (`screen_id`),
  KEY `film_app_allocate_timing_id_c4a87e5b` (`timing_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `film_app_allocate` */

insert  into `film_app_allocate`(`id`,`played_date`,`status`,`film_id`,`screen_id`,`timing_id`,`theater_id`) values 
(1,'2025-01-22','allocated',2,2,2,1);

/*Table structure for table `film_app_booking` */

DROP TABLE IF EXISTS `film_app_booking`;

CREATE TABLE `film_app_booking` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `total` varchar(70) NOT NULL,
  `date` varchar(70) NOT NULL,
  `status` varchar(70) NOT NULL,
  `allocate_id` bigint(20) NOT NULL,
  `customer_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `film_app_booking_allocate_id_02975c50` (`allocate_id`),
  KEY `film_app_booking_customer_id_da798c6f` (`customer_id`)
) ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;

/*Data for the table `film_app_booking` */

insert  into `film_app_booking`(`id`,`total`,`date`,`status`,`allocate_id`,`customer_id`) values 
(17,'1200','2025-02-15','Booked',1,1),
(16,'1200','2025-02-15','Booked',1,1),
(14,'1200','2025-02-15','Booked',1,1),
(13,'700','2025-02-15','Booked',1,1),
(12,'1200','2025-02-15','Booked',1,1),
(11,'1200','2025-02-15','Booked',1,1),
(10,'1200','2025-02-15','Booked',1,1);

/*Table structure for table `film_app_bookingchild` */

DROP TABLE IF EXISTS `film_app_bookingchild`;

CREATE TABLE `film_app_bookingchild` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `price` varchar(70) NOT NULL,
  `booking_id` bigint(20) NOT NULL,
  `seating_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `film_app_bookingchild_booking_id_16aacfdb` (`booking_id`),
  KEY `film_app_bookingchild_seating_id_8e7e7f96` (`seating_id`)
) ENGINE=MyISAM AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

/*Data for the table `film_app_bookingchild` */

insert  into `film_app_bookingchild`(`id`,`price`,`booking_id`,`seating_id`) values 
(9,'1200',12,1),
(8,'1200',11,1),
(7,'1200',10,1),
(10,'700',13,4),
(11,'1200',14,1),
(13,'1200',16,1),
(14,'1200',17,1);

/*Table structure for table `film_app_community` */

DROP TABLE IF EXISTS `film_app_community`;

CREATE TABLE `film_app_community` (
  `id` int(12) NOT NULL AUTO_INCREMENT,
  `customer_id` int(12) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `film_app_community` */

insert  into `film_app_community`(`id`,`customer_id`,`name`) values 
(1,1,'film company'),
(2,1,'dejavu');

/*Table structure for table `film_app_customer` */

DROP TABLE IF EXISTS `film_app_customer`;

CREATE TABLE `film_app_customer` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `fname` varchar(60) NOT NULL,
  `lname` varchar(70) NOT NULL,
  `city` varchar(60) NOT NULL,
  `dist` varchar(70) NOT NULL,
  `pin` varchar(70) NOT NULL,
  `phone` varchar(70) NOT NULL,
  `gender` varchar(70) NOT NULL,
  `dob` varchar(70) NOT NULL,
  `resume` varchar(100) NOT NULL,
  `login_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `film_app_customer_login_id_b5f822e7` (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `film_app_customer` */

insert  into `film_app_customer`(`id`,`fname`,`lname`,`city`,`dist`,`pin`,`phone`,`gender`,`dob`,`resume`,`login_id`) values 
(1,'amala','benny','ernakulam','ernakulam','8767667','8765456543','female','10-10-2002','f',6),
(2,'shine','thomax','kochi','ernakulam','676767','8565896325','Male','10/10/1888','',12);

/*Table structure for table `film_app_film` */

DROP TABLE IF EXISTS `film_app_film`;

CREATE TABLE `film_app_film` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `film_name` varchar(60) NOT NULL,
  `film_release` varchar(70) NOT NULL,
  `film_desc` varchar(70) NOT NULL,
  `duration` varchar(70) NOT NULL,
  `type_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `film_app_film_type_id_f4067099` (`type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `film_app_film` */

insert  into `film_app_film`(`id`,`film_name`,`film_release`,`film_desc`,`duration`,`type_id`) values 
(2,'marco','12-1-22','thriller','3:00',2);

/*Table structure for table `film_app_join_community` */

DROP TABLE IF EXISTS `film_app_join_community`;

CREATE TABLE `film_app_join_community` (
  `id` int(12) NOT NULL AUTO_INCREMENT,
  `community_id` int(12) DEFAULT NULL,
  `customer_id` int(12) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `film_app_join_community` */

insert  into `film_app_join_community`(`id`,`community_id`,`customer_id`) values 
(2,1,1),
(3,2,1);

/*Table structure for table `film_app_login` */

DROP TABLE IF EXISTS `film_app_login`;

CREATE TABLE `film_app_login` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(60) NOT NULL,
  `usertype` varchar(70) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

/*Data for the table `film_app_login` */

insert  into `film_app_login`(`id`,`username`,`password`,`usertype`) values 
(1,'admin','admin','admin'),
(3,'athul','athul','theater'),
(5,'ann','ann','producer'),
(6,'qq','qq','cust'),
(7,'rithin','rithin','cust'),
(12,'shine','shine','cust');

/*Table structure for table `film_app_opportunities` */

DROP TABLE IF EXISTS `film_app_opportunities`;

CREATE TABLE `film_app_opportunities` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `title` varchar(60) NOT NULL,
  `details` varchar(60) NOT NULL,
  `project_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `film_app_opportunities_project_id_c8ab4139` (`project_id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `film_app_opportunities` */

insert  into `film_app_opportunities`(`id`,`title`,`details`,`project_id`) values 
(8,'yh','ff',8);

/*Table structure for table `film_app_payment` */

DROP TABLE IF EXISTS `film_app_payment`;

CREATE TABLE `film_app_payment` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `Amount` varchar(70) NOT NULL,
  `booking_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `film_app_payment_booking_id_5482749c` (`booking_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `film_app_payment` */

insert  into `film_app_payment`(`id`,`Amount`,`booking_id`) values 
(1,'570',1);

/*Table structure for table `film_app_preference` */

DROP TABLE IF EXISTS `film_app_preference`;

CREATE TABLE `film_app_preference` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `preference` varchar(60) NOT NULL,
  `Opportunity_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `film_app_preference_Opportunity_id_f19e3eb9` (`Opportunity_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `film_app_preference` */

insert  into `film_app_preference`(`id`,`preference`,`Opportunity_id`) values 
(2,'aa',3),
(4,'okk',4);

/*Table structure for table `film_app_production` */

DROP TABLE IF EXISTS `film_app_production`;

CREATE TABLE `film_app_production` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `team_name` varchar(60) NOT NULL,
  `place` varchar(70) NOT NULL,
  `phone` varchar(70) NOT NULL,
  `email` varchar(70) NOT NULL,
  `login_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `film_app_production_login_id_78fc5e75` (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `film_app_production` */

insert  into `film_app_production`(`id`,`team_name`,`place`,`phone`,`email`,`login_id`) values 
(1,'ann','kochi','8789878987','ann@gmail.com',5);

/*Table structure for table `film_app_projects` */

DROP TABLE IF EXISTS `film_app_projects`;

CREATE TABLE `film_app_projects` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `project_name` varchar(60) NOT NULL,
  `images` varchar(100) NOT NULL,
  `videos` varchar(100) DEFAULT NULL,
  `production_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `film_app_projects_production_id_5692bb31` (`production_id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `film_app_projects` */

insert  into `film_app_projects`(`id`,`project_name`,`images`,`videos`,`production_id`) values 
(8,'uu','abc_14ppgQZ.jpg','pending',1);

/*Table structure for table `film_app_request` */

DROP TABLE IF EXISTS `film_app_request`;

CREATE TABLE `film_app_request` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `date` varchar(60) NOT NULL,
  `status` varchar(60) NOT NULL,
  `Opportunity_id` bigint(20) NOT NULL,
  `customer_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `film_app_request_Opportunity_id_a93066b5` (`Opportunity_id`),
  KEY `film_app_request_customer_id_c40685b9` (`customer_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `film_app_request` */

insert  into `film_app_request`(`id`,`date`,`status`,`Opportunity_id`,`customer_id`) values 
(2,'2025-02-13','Scheduled Meeting',3,1),
(3,'2025-02-13','Pending',3,1),
(4,'2025-02-13','Pending',3,2),
(5,'2025-02-15','Scheduled Meeting',8,1);

/*Table structure for table `film_app_requestimage` */

DROP TABLE IF EXISTS `film_app_requestimage`;

CREATE TABLE `film_app_requestimage` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `image` varchar(100) NOT NULL,
  `type` varchar(60) NOT NULL,
  `request_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `film_app_requestimage_request_id_859e87d5` (`request_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `film_app_requestimage` */

insert  into `film_app_requestimage`(`id`,`image`,`type`,`request_id`) values 
(1,'abc.jpg','image',2);

/*Table structure for table `film_app_schedule` */

DROP TABLE IF EXISTS `film_app_schedule`;

CREATE TABLE `film_app_schedule` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `date` varchar(60) NOT NULL,
  `time` varchar(60) NOT NULL,
  `venue` varchar(60) NOT NULL,
  `request_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `film_app_schedule_request_id_1c37b01a` (`request_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `film_app_schedule` */

insert  into `film_app_schedule`(`id`,`date`,`time`,`venue`,`request_id`) values 
(1,'16-2-25','2:43','lulu mall',2),
(2,'2025-2-20','01:03','kochi darbar hall',2),
(3,'2025-2-28','01:22','crown plaza',2),
(4,'2025-2-28','01:22','crown plaza',2),
(5,'2025-2-28','01:22','crown plaza',2),
(6,'2025-2-20','13:29','kochi',5);

/*Table structure for table `film_app_screen` */

DROP TABLE IF EXISTS `film_app_screen`;

CREATE TABLE `film_app_screen` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `screen_name` varchar(60) NOT NULL,
  `no_seats` varchar(70) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `film_app_screen` */

insert  into `film_app_screen`(`id`,`screen_name`,`no_seats`) values 
(2,'screen 3','30');

/*Table structure for table `film_app_seating` */

DROP TABLE IF EXISTS `film_app_seating`;

CREATE TABLE `film_app_seating` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `row_name` varchar(70) NOT NULL,
  `seat_number` varchar(70) NOT NULL,
  `rate` varchar(70) NOT NULL,
  `screen_id` bigint(20) NOT NULL,
  `seat_type_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `film_app_seating_screen_id_a8cee544` (`screen_id`),
  KEY `film_app_seating_seat_type_id_53ac68fb` (`seat_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `film_app_seating` */

insert  into `film_app_seating`(`id`,`row_name`,`seat_number`,`rate`,`screen_id`,`seat_type_id`) values 
(1,'platinum','5','1200',2,1),
(4,'Gold','4','700',2,1);

/*Table structure for table `film_app_seattype` */

DROP TABLE IF EXISTS `film_app_seattype`;

CREATE TABLE `film_app_seattype` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `seat_type` varchar(60) NOT NULL,
  `desc` varchar(70) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `film_app_seattype` */

insert  into `film_app_seattype`(`id`,`seat_type`,`desc`) values 
(1,'golden','with free drinks');

/*Table structure for table `film_app_theater` */

DROP TABLE IF EXISTS `film_app_theater`;

CREATE TABLE `film_app_theater` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(60) NOT NULL,
  `city` varchar(70) NOT NULL,
  `pin` varchar(60) NOT NULL,
  `phone` varchar(70) NOT NULL,
  `email` varchar(70) NOT NULL,
  `login_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `film_app_theater_login_id_c1a81ec0` (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `film_app_theater` */

insert  into `film_app_theater`(`id`,`name`,`city`,`pin`,`phone`,`email`,`login_id`) values 
(1,'rithin','kochi','878787','98765654','rithin@gmail.com',2),
(2,'athul','kochi','878878','4567898765','athul@gmail.com',3);

/*Table structure for table `film_app_timing` */

DROP TABLE IF EXISTS `film_app_timing`;

CREATE TABLE `film_app_timing` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `timing_name` varchar(60) NOT NULL,
  `time` varchar(70) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `film_app_timing` */

insert  into `film_app_timing`(`id`,`timing_name`,`time`) values 
(2,'morning show','17:10');

/*Table structure for table `film_app_type` */

DROP TABLE IF EXISTS `film_app_type`;

CREATE TABLE `film_app_type` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `type_name` varchar(60) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `film_app_type` */

insert  into `film_app_type`(`id`,`type_name`) values 
(1,'NON AC');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
