--1.检查更新前的数据
select * from ssdb_infoflow where isValid=1;
--2.以前参数置为无效
UPDATE ssdb_infoflow SET isValid=0 where isValid=1;
--3.插入记录
insert into ssdb_infoflow(id,createDate,crosstime,infoflow,isvalid,orderId,type,weight,infoflow1,infoflow2)
values('201803200001',null,5,'律师做诉保必备，','1','12121212','11','1','一键申请，保函就可到手！','戳>>');
insert into ssdb_infoflow(id,createDate,crosstime,infoflow,isvalid,orderId,type,weight,infoflow1,infoflow2)
values('201803200002',null,5,'申请保函，享','1','12121212','11','1','专人送函','新服务，还可指定送函时间！>>');
insert into ssdb_infoflow(id,createDate,crosstime,infoflow,isvalid,orderId,type,weight,infoflow1,infoflow2)
values('201803200003',null,5,'多问诉保春季特惠，费率低至','1','12121212','11','1','万分5！','速看>>');
insert into ssdb_infoflow(id,createDate,crosstime,infoflow,isvalid,orderId,type,weight,infoflow1,infoflow2)
values('201803200004',null,5,'【惊喜】','1','12121212','11','1','平安保险','上线多问诉保啦，快来申请保函吧！>>');
insert into ssdb_infoflow(id,createDate,crosstime,infoflow,isvalid,orderId,type,weight,infoflow1,infoflow2)
values('201803200005',null,5,'申请保函，享','1','12121212','11','1','专人送函服务','，还可指定送函时间！>>');
insert into ssdb_infoflow(id,createDate,crosstime,infoflow,isvalid,orderId,type,weight,infoflow1,infoflow2)
values('201803200006',null,5,'诉保新服务袭来：','1','12121212','11','1','先出函后付费','，出函更放心！>>');
insert into ssdb_infoflow(id,createDate,crosstime,infoflow,isvalid,orderId,type,weight,infoflow1,infoflow2)
values('201803200007',null,5,'【多问诉保好服务】','1','12121212','11','1','2小时专人审核','，省时更省心！>>');
insert into ssdb_infoflow(id,createDate,crosstime,infoflow,isvalid,orderId,type,weight,infoflow1,infoflow2)
values('201803200008',null,5,'诉保享高返，','1','12121212','11','1','35%','超高返点在等你，猛戳查看>>');