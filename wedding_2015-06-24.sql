# ************************************************************
# Sequel Pro SQL dump
# Version 4096
#
# http://www.sequelpro.com/
# http://code.google.com/p/sequel-pro/
#
# Host: 127.0.0.1 (MySQL 5.5.40)
# Database: wedding
# Generation Time: 2015-06-24 23:19:11 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table albums
# ------------------------------------------------------------

DROP TABLE IF EXISTS `albums`;

CREATE TABLE `albums` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `pa_id` int(11) unsigned NOT NULL,
  `albumname` varchar(255) DEFAULT NULL,
  `information` varchar(255) DEFAULT NULL,
  `cover` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `pa_id` (`pa_id`),
  CONSTRAINT `pa_id` FOREIGN KEY (`pa_id`) REFERENCES `photographers` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `albums` WRITE;
/*!40000 ALTER TABLE `albums` DISABLE KEYS */;

INSERT INTO `albums` (`id`, `pa_id`, `albumname`, `information`, `cover`)
VALUES
	(1,1,'Crazy Love in Han','10/25/2014  Couples: Haiyan & Qinghong','/img/chinese13.jpg'),
	(19,38,'Giving All My Love To You','03/15/2015 Couples: LIUxiang & Xiaomeng','/img/chinese23.jpg'),
	(20,35,'Cherry Blossoms Wedding','04/17/2015 RACHAEL & MATT','/img/british41.jpg'),
	(21,3,'Love In Seoul','12/15/2014  Tom & Lily','/img/korean31.jpg');

/*!40000 ALTER TABLE `albums` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table couple_destination
# ------------------------------------------------------------

DROP TABLE IF EXISTS `couple_destination`;

CREATE TABLE `couple_destination` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `cdc_id` int(11) unsigned NOT NULL,
  `cdd_id` int(11) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cdd_id` (`cdd_id`),
  KEY `cdc_id` (`cdc_id`),
  CONSTRAINT `cdc_id` FOREIGN KEY (`cdc_id`) REFERENCES `couples` (`id`),
  CONSTRAINT `cdd_id` FOREIGN KEY (`cdd_id`) REFERENCES `destinations` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table couple_photographer
# ------------------------------------------------------------

DROP TABLE IF EXISTS `couple_photographer`;

CREATE TABLE `couple_photographer` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `cpp_id` int(11) unsigned NOT NULL,
  `cpc_id` int(11) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cpp_id` (`cpp_id`),
  KEY `cpc_id` (`cpc_id`),
  CONSTRAINT `cpc_id` FOREIGN KEY (`cpc_id`) REFERENCES `couples` (`id`),
  CONSTRAINT `cpp_id` FOREIGN KEY (`cpp_id`) REFERENCES `photographers` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table couples
# ------------------------------------------------------------

DROP TABLE IF EXISTS `couples`;

CREATE TABLE `couples` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `portrait` varchar(255) DEFAULT NULL,
  `couplename` varchar(255) DEFAULT NULL,
  `coupleemail` varchar(255) DEFAULT NULL,
  `couplephone` varchar(255) DEFAULT NULL,
  `coupleinfo` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `couples` WRITE;
/*!40000 ALTER TABLE `couples` DISABLE KEYS */;

INSERT INTO `couples` (`id`, `username`, `password`, `portrait`, `couplename`, `coupleemail`, `couplephone`, `coupleinfo`)
VALUES
	(1,'alice','alice','/img/alice.jpg','Alice Lee','alicelee@gmail.com','+1 719-248-3960',NULL);

/*!40000 ALTER TABLE `couples` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table destinations
# ------------------------------------------------------------

DROP TABLE IF EXISTS `destinations`;

CREATE TABLE `destinations` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `city` varchar(255) DEFAULT NULL,
  `country` varchar(255) DEFAULT NULL,
  `customhabit` varchar(2550) DEFAULT NULL,
  `dphoto1` varchar(255) DEFAULT NULL,
  `dphoto2` varchar(255) DEFAULT NULL,
  `dphoto3` varchar(255) DEFAULT NULL,
  `dphoto4` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `destinations` WRITE;
/*!40000 ALTER TABLE `destinations` DISABLE KEYS */;

INSERT INTO `destinations` (`id`, `city`, `country`, `customhabit`, `dphoto1`, `dphoto2`, `dphoto3`, `dphoto4`)
VALUES
	(1,'Beijing','China','Traditionally, Korean betrothal gifts were brought to the bride\'s home by a band of the groom\'s closest friends. The gifts were placed in a box called a hahm. The group, dressed in costume with blackened faces, would arrive singing at the bride\'s family home. They would stop just outside the house, chanting, \"Hahm for sale, hahm for sale!\" The bride\'s family would rush out and offer money to the group. Through fun negotiation and laughter, the bearers would be bribed until at last the hahm was delivered.\nThe traditional Korean wedding is held at the bride\'s family home. Vows are taken in a ceremony called kunbere: Bride and groom bow to each other and seal their vow by sipping a special wine poured into a gourd grown by the bride\'s mother.\nKorean wedding banquets can be very simple: Noodle soup is the only required dish. In fact, the wedding banquet is called kook soo sang, which means \"noodle banquet.\" Long noodles -- symbolizing a wish for a long and happy life -- are boiled in beef broth and garnished with vegetables. Dok, a sticky rice cake, is served at most Korean events, especially weddings.','/img/chinese11.jpg','/img/chinese21.jpg','/img/chinese31.jpg','/img/chinese41.jpg'),
	(2,'Tokyo','Japan','The Japanese ritual of \"san-san-kudo\", the three by three exchange is rich with meaning. It is performed by the bride and groom and both sets of parents; each person takes 3 sips of sake from each of 3 cups. The first 3 represent three couples, the bride and groom, and their parents. The second 3 represent three human flaws: hatred, passion, and ignorance. \"Ku\", or 9 is a lucky number in Japanese culture. And \"do\" means deliverance from the three flaws.\nThe bride traditionally wears two outfits: the shiro, which is a white kimono worn for the ceremony and the uchikake kimono which is a patterned brocade worn at the reception. The hair is worn in a bun with colorful kanzashi accessories and a white wedding hook called the tsuno kakushi is worn to hide the two front golden tsuno horns to symbolize obedience. The bride also carries a tiny purse (hakoseko), a small encased sword (kaiken), and a fan that is worn in the obi belt that represents happiness and a happy future.','/img/japanese12.png','/img/japanese21.png','/img/japanese31.png','/img/japanese41.pgn'),
	(3,'Seoul','Korea','Traditionally, Korean betrothal gifts were brought to the bride\'s home by a band of the groom\'s closest friends. The group, dressed in costume with blackened faces, would arrive singing at the bride\'s family home. They would stop just outside the house, chanting, \"Hahm for sale, hahm for sale!\" The bride\'s family would rush out and offer money to the group. Through fun negotiation and laughter, the bearers would be bribed until at last the hahm was delivered.\n\nThe traditional Korean wedding is held at the bride\'s family home. Vows are taken in a ceremony called kunbere: Bride and groom bow to each other and seal their vow by sipping a special wine poured into a gourd grown by the bride\'s mother.\n\nKorean wedding banquets can be very simple: Noodle soup is the only required dish. In fact, the wedding banquet is called kook soo sang, which means \"noodle banquet.\" Long noodles -- symbolizing a wish for a long and happy life -- are boiled in beef broth and garnished with vegetables. Dok, a sticky rice cake, is served at most Korean events, especially weddings.','/img/korean11.jpg','/img/korean21.jpg','/img/korean31.jpg','/img/korean41.jpg'),
	(4,'Los Angeles','United States','American',NULL,NULL,NULL,NULL),
	(5,'London','United Kingdom','During the ceremony the bride and groom make their marriage vows. Marriage vows are promises a couple makes to each other during a wedding ceremony. In Western culture, these promises have traditionally included the notions of affection (\"love, comfort, keep\"), faithfulness (\"forsaking all others\"), unconditionality (\"for richer or for poorer\", \"in sickness and in health\"), and permanence (\"as long as we both shall live\", \"until death do us part\").\nMost wedding vows are taken from traditional religious ceremonies, but nowadays in the UK many couples choose touching love poems or lyrics from a love song revised as wedding vows and some couples even choose to write their own vows, rather than relying on standard ones spoken by the celebrant (registrar, priest or vicar).\nAfter the vows have been spoken the couple exchange rings. The wedding ring is placed on the third finger of the left hand, also called the \"ring\" finger. The wedding ring is usually a plain gold ring. I was once told that the third finger was chosen because in the past people believed a vein ran from that finger, straight to the heart - modern anatomy books havel put paid to that theory though.\n','/img/british11.jpg','/img/british21.jpg','/img/british31.jpg','/img/british41.jpg');

/*!40000 ALTER TABLE `destinations` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table orders
# ------------------------------------------------------------

DROP TABLE IF EXISTS `orders`;

CREATE TABLE `orders` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `oc_id` int(11) unsigned NOT NULL,
  `op_id` int(11) unsigned NOT NULL,
  `od_id` int(11) unsigned NOT NULL,
  `orderdate` varchar(255) DEFAULT NULL,
  `orderrequirement` varchar(255) DEFAULT NULL,
  `orderstatus` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `oc_id` (`oc_id`),
  KEY `op_id` (`op_id`),
  KEY `od_id` (`od_id`),
  CONSTRAINT `oc_id` FOREIGN KEY (`oc_id`) REFERENCES `couples` (`id`),
  CONSTRAINT `od_id` FOREIGN KEY (`od_id`) REFERENCES `destinations` (`id`),
  CONSTRAINT `op_id` FOREIGN KEY (`op_id`) REFERENCES `photographers` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table photographers
# ------------------------------------------------------------

DROP TABLE IF EXISTS `photographers`;

CREATE TABLE `photographers` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `dp_id` int(11) unsigned NOT NULL,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `portrait` varchar(255) DEFAULT NULL,
  `photographername` varchar(255) DEFAULT NULL,
  `photographeremail` varchar(255) DEFAULT NULL,
  `photographerphone` varchar(255) DEFAULT NULL,
  `photographerinfo` varchar(2550) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `dp_id` (`dp_id`),
  CONSTRAINT `dp_id` FOREIGN KEY (`dp_id`) REFERENCES `destinations` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `photographers` WRITE;
/*!40000 ALTER TABLE `photographers` DISABLE KEYS */;

INSERT INTO `photographers` (`id`, `dp_id`, `username`, `password`, `portrait`, `photographername`, `photographeremail`, `photographerphone`, `photographerinfo`)
VALUES
	(1,1,'haipingzhu','haipingzhu','/img/haipingzhu.jpg','Haiping Zhu','haipingzhu@163.com','+86 137-2849-2983','I am a senior photographer who take photos with couples'),
	(2,2,'nobi','nobi','/img/nobi.jpg','Nobi Nobita','nobi@gmail.com','+82 837-559-3030',NULL),
	(3,3,'hyunakim','hyunakim','/img/hyuna.png','Hyuna Kim','hyunalove@gmail.com','+77 293-1185-446',NULL),
	(4,1,'raymondli','raymondli','/img/raymondli.png','RayMond Li','rayli@163.com','+86 133-7899-3650',NULL),
	(29,4,'johnsmith','johnsmith','/img/john.png','John Smith','jsmith@gmail.com','+1 719-364-2930','lalallalaal'),
	(35,5,'chrisdodge','chrisdodge','/img/chrisdodge.png','Chris Dodge','chrisd@gmail.com','+44 729-384-2903',NULL),
	(36,2,'wasabikenzo','wasabikenzo','/img/kenzo.png','Wasabi Kenzo','wasabikenzo@gmail.com','+82 928-2834-2047',NULL),
	(37,3,'maiduong','maiduong','/img/mai.jpg','Mai Duong','maid@gmail.com','+77 664-384-9581',NULL),
	(38,1,'fuhao','fuhao','/img/fuhao.jpg','Fu Hao','fuhao@qq.com','+86 139-5743-2837','');

/*!40000 ALTER TABLE `photographers` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table photos
# ------------------------------------------------------------

DROP TABLE IF EXISTS `photos`;

CREATE TABLE `photos` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `ap_id` int(11) unsigned NOT NULL,
  `path` varchar(255) DEFAULT '',
  `photoname` varchar(255) DEFAULT '',
  `photoinformation` varchar(255) DEFAULT '',
  PRIMARY KEY (`id`),
  KEY `ap_id` (`ap_id`),
  CONSTRAINT `ap_id` FOREIGN KEY (`ap_id`) REFERENCES `albums` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `photos` WRITE;
/*!40000 ALTER TABLE `photos` DISABLE KEYS */;

INSERT INTO `photos` (`id`, `ap_id`, `path`, `photoname`, `photoinformation`)
VALUES
	(1,1,'/img/chinese11.jpg','Han Style',''),
	(2,1,'/img/chinese12.jpg','Han Style',''),
	(3,1,'/img/chinese13.jpg','Han Style',''),
	(4,1,'/img/chinese14.jpg','Han Style',''),
	(5,19,'/img/chinese21.jpg','',''),
	(6,19,'/img/chinese22.jpg','',''),
	(7,19,'/img/chinese23.jpg','',''),
	(8,19,'/img/chinese24.jpg','',''),
	(9,20,'/img/british41.jpg','',''),
	(10,20,'/img/british42.jpg','',''),
	(11,20,'/img/british43.jpg','',''),
	(12,20,'/img/british44.jpg','',''),
	(13,21,'/img/korean31.jpg','',''),
	(14,21,'/img/korean32.jpg','',''),
	(15,21,'/img/korean33.jpg','',''),
	(16,21,'/img/korean34.jpg','','');

/*!40000 ALTER TABLE `photos` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
