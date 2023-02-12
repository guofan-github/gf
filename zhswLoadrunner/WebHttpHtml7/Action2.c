Action2()
{	
	web_reg_find("Search=Body",
	"SaveCount=dl",
	"Text=郭凡",
	LAST);

	lr_start_transaction("登录事务");
	
	web_reg_save_param_json(
	"ParamName=token",
	"QueryString=$.data",
	SEARCH_FILTERS,
	"Scope=BODY",
	LAST);
	web_reg_save_param("ll",
	"LB=",
	"RB=",
	"Search=Body",
	LAST);
	
	
	web_custom_request("登录",
	"URL=http://{url}/water_bg/user/login",
	"Method=POST",
	"TargetFrame=",
	"Resource=0",
	"RecContentType=application/json;charset=UTF-8",
	"Referer=",
	"EncType=application/json;charset=UTF-8",
	"Body={\"userName\":\"admin\",\"password\":\"123\"}",
	LAST);
	
	lr_output_message("数量%s",lr_eval_string("{dl}"));
	
	lr_output_message("token%s",lr_eval_string("{token}"));
	if(atoi(lr_eval_string("{dl}"))==1){
	lr_end_transaction("登录事务",LR_PASS);
	}else{
    lr_end_transaction("登录事务",LR_FAIL);
	}
	
//	
//	// 巡检地点-添加-【添加】
//	
//	lr_start_transaction("巡检地点-添加");
//
//	web_reg_find("SaveCount=tianjia",
//		"Text=添加成功",
//		LAST);
//
//	web_add_header("Authorization",
//		"{token}");
//
//	web_custom_request("web_custom_request",
//		"URL=http://{url}/water_bg/point/addPoint",
//		"Method=POST",
//		"TargetFrame=",
//		"Resource=0",
//		"Referer=",
//		"EncType=application/json",
//		"Body={id: \"\", pointNo: \"www\", pointName: \"亲亲亲\", address: \"吃吃吃\", remark: \"发发发\"}",
//		LAST);
//
//	lr_output_message("数量%s",lr_eval_string("{巡检地点-添加}"));
//	
//	
//	if(atoi(lr_eval_string("{tianjia}"))==1){
//	lr_end_transaction("巡检地点-添加",LR_PASS);
//	}else{
//    lr_end_transaction("巡检地点-添加",LR_FAIL);
//	}
	
	
	// 巡检地点-修改
		lr_start_transaction("巡检地点-修改");
		
		web_reg_find("SaveCount=xiugai",
		"Text=修改成功",
		LAST);
		
		web_add_header("Authorization",
		"{token}");
		
	web_custom_request("web_custom_request",
		"URL=http://{url}/water_bg/point/updatePoint",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body={\"id\":2,\"pointNo\":\"P0002\",\"pointName\":\"测试巡检点2\",\"address\":\"湖畔1\",\"remark\":\"741\"}",
		LAST);

	lr_output_message("数量%s",lr_eval_string("{xiugai}"));	
	
	if(atoi(lr_eval_string("{xiugai}"))==1){
	lr_end_transaction("巡检地点-修改",LR_PASS);
	}else{
    lr_end_transaction("巡检地点-修改",LR_FAIL);
	}
	
	
		//巡检计划-添加
	
		lr_start_transaction("巡检计划-添加");
		
		web_reg_find("SaveCount=xjjhtj",
		"Text=添加成功",
		LAST);
		
		web_add_header("Authorization",
		"{token}");
		
		web_custom_request("web_custom_request",
		"URL=http://{url}/water_bg/patrolpoint/add",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body={\"planNo\":\"吃吃吃\",\"planName\":\"吃草\",\"patType\":1,\"patCycle\":4,\"startDate\":\"2022-06-19T16:00:00.000Z\",\"endDate\":\"2022-06-28T16:00:00.000Z\",\"remark\":\"\",\"pointList\":[{\"id\":3,\"pointNo\":\"P0003\",\"pointName\":\"测试巡检点3\",\"address\":\"湖畔\",\"devNum\":13,\"remark\":\"真凉快\",\"devId\":null}],\"starDate\":\"\"}",
		LAST);

	lr_output_message("数量%s",lr_eval_string("{xjjhtj}"));	
	
	if(atoi(lr_eval_string("{xjjhtj}"))==1){
	lr_end_transaction("巡检计划-添加",LR_PASS);
	}else{
    lr_end_transaction("巡检计划-添加",LR_FAIL);
	}
	
	
	
	// 巡检计划-查看
	lr_start_transaction("巡检计划-查看");
		
	web_reg_find("SaveCount=xjjhck",
	"Text=OK",
	LAST);
	
	web_add_header("Authorization",
	"{token}");
	
	
	web_url("web_url",
		"URL=http://{url}/water_bg/patrolpoint/findById?id=1",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		LAST);


	lr_output_message("数量%s",lr_eval_string("{xjjhck}"));	
	
	if(atoi(lr_eval_string("{xjjhck}"))==1){
	lr_end_transaction("巡检计划-查看",LR_PASS);
	}else{
    lr_end_transaction("巡检计划-查看",LR_FAIL);
	}
	

	// 巡检计划-查看-添加计划
	
		lr_start_transaction("巡检计划-查看-添加计划");
		
		web_reg_find("SaveCount=xjjhcktj",
		"Text=添加成功",
		LAST);
		
		web_add_header("Authorization",
		"{token}");
		
		web_custom_request("web_custom_request",
		"URL=http://{url}/water_bg/patrolTask/addtask",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body={\"executor\":\"wangkuang\",\"taskName\":\"信息\",\"startDate\":\"2022-06-06T16:00:00.000Z\",\"taskType\":\"plan\",\"endDate\":\"2022-06-12T16:00:00.000Z\",\"points\":[{\"id\":5,\"pointNo\":\"P0005\",\"pointName\":\"测试巡检点five\",\"address\":\"湖畔\",\"devNum\":13,\"remark\":\"真凉快\",\"devId\":null}],\"planId\":3}",
		LAST);

	lr_output_message("数量%s",lr_eval_string("{xjjhcktj}"));	
	
	if(atoi(lr_eval_string("{xjjhcktj}"))==1){
	lr_end_transaction("巡检计划-查看-添加计划",LR_PASS);
	}else{
    lr_end_transaction("巡检计划-查看-添加计划",LR_FAIL);
	}
	
	
	
	
	
	// 巡检计划-修改
	
	lr_start_transaction("巡检计划-修改");
		
	web_reg_find("SaveCount=xjjhxg",
	"Text=OK",
	LAST);
	
	web_add_header("Authorization",
	"{token}");
	
	
	web_url("web_url",
		"URL=http://{url}/water_bg/patrolTask/findById?id=1",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		LAST);


	lr_output_message("数量%s",lr_eval_string("{xjjhxg}"));	
	
	if(atoi(lr_eval_string("{xjjhxg}"))==1){
	lr_end_transaction("巡检计划-修改",LR_PASS);
	}else{
    lr_end_transaction("巡检计划-修改",LR_FAIL);
	}
	
	
	
	// 巡检计划-修改-查看
	
	lr_start_transaction("巡检计划-修改-查看");
		
	web_reg_find("SaveCount=xjjhxgck",
	"Text=OK",
	LAST);
	
	web_add_header("Authorization",
	"{token}");
	
	
	web_url("web_url",
		"URL=http://{url}/water_bg/patrolTask/findByTaskId?id=60",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		LAST);


	lr_output_message("数量%s",lr_eval_string("{xjjhxgck}"));	
	
	if(atoi(lr_eval_string("{xjjhxgck}"))==1){
	lr_end_transaction("巡检计划-修改-查看",LR_PASS);
	}else{
    lr_end_transaction("巡检计划-修改-查看",LR_FAIL);
	}
	
	
	// 巡检审核-查看详情
	
	lr_start_transaction("巡检审核-查看详情");
		
	web_reg_find("SaveCount=xjshckxq",
	"Text=OK",
	LAST);
	
	web_add_header("Authorization",
	"{token}");
	
	
	web_url("web_url",
		"URL=http://{url}/water_bg/situation/situationTaskId?id=16",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		LAST);


	lr_output_message("数量%s",lr_eval_string("{xjshckxq}"));	
	
	if(atoi(lr_eval_string("{xjshckxq}"))==1){
	lr_end_transaction("巡检审核-查看详情",LR_PASS);
	}else{
    lr_end_transaction("巡检审核-查看详情",LR_FAIL);
	}
	
	
	// 巡检审核-审核
	
		lr_start_transaction("巡检审核-审核");
		
		web_reg_find("SaveCount=xjshsh",
		"Text=审核成功",
		LAST);
		
		web_add_header("Authorization",
		"{token}");
		
		web_custom_request("web_custom_request",
		"URL=http://{url}/water_bg/check/checkTask",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body={\"executor\":\"wangkuang\",\"taskName\":\"信息\",\"startDate\":\"2022-06-06T16:00:00.000Z\",\"taskType\":\"plan\",\"endDate\":\"2022-06-12T16:00:00.000Z\",\"points\":[{\"id\":5,\"pointNo\":\"P0005\",\"pointName\":\"测试巡检点five\",\"address\":\"湖畔\",\"devNum\":13,\"remark\":\"真凉快\",\"devId\":null}],\"planId\":3}",
		LAST);

	lr_output_message("数量%s",lr_eval_string("{xjshsh}"));	
	
	if(atoi(lr_eval_string("{xjshsh}"))==1){
	lr_end_transaction("巡检审核-审核",LR_PASS);
	}else{
    lr_end_transaction("巡检审核-审核",LR_FAIL);
	}
	
	
	
	//  系统管理-角色管理
	
	lr_start_transaction("系统管理-角色管理");
		
	web_reg_find("SaveCount=jsgl",
	"Text=OK",
	LAST);
	
	web_add_header("Authorization",
	"{token}");
	
	
	web_url("web_url",
		"URL=http://{url}/water_bg/role/list",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		LAST);


	lr_output_message("数量%s",lr_eval_string("{jsgl}"));	
	
	if(atoi(lr_eval_string("{jsgl}"))==1){
	lr_end_transaction("系统管理-角色管理",LR_PASS);
	}else{
    lr_end_transaction("系统管理-角色管理",LR_FAIL);
	}
	
	
	// 角色管理-分配管理
	
	lr_start_transaction("角色管理-分配管理");
		
	web_reg_find("SaveCount=fpgl",
	"Text=OK",
	LAST);
	
	web_add_header("Authorization",
	"{token}");
	
	
	web_url("web_url",
		"URL=http://{url}/water_bg/roleperm/tree?id=1",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		LAST);


	lr_output_message("数量%s",lr_eval_string("{fpgl}"));	
	
	if(atoi(lr_eval_string("{fpgl}"))==1){
	lr_end_transaction("角色管理-分配管理",LR_PASS);
	}else{
    lr_end_transaction("角色管理-分配管理",LR_FAIL);
	}
	
	
	//系统管理-用户管理
	
	lr_start_transaction("系统管理-用户管理");
		
	web_reg_find("SaveCount=yhgl",
	"Text=OK",
	LAST);
	
	web_add_header("Authorization",
	"{token}");
	
	
	web_url("web_url",
		"URL=http://{url}/water_bg/role/list",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		LAST);


	lr_output_message("数量%s",lr_eval_string("{yhgl}"));	
	
	if(atoi(lr_eval_string("{yhgl}"))==1){
	lr_end_transaction("系统管理-用户管理",LR_PASS);
	}else{
    lr_end_transaction("系统管理-用户管理",LR_FAIL);
	}
	
	
	
	// 系统管理-用户管理-修改
	
		lr_start_transaction("系统管理-用户管理-修改");
		
		web_reg_find("SaveCount=yhglxg",
		"Text=OK",
		LAST);
		
		web_add_header("Authorization",
		"{token}");
		
		web_custom_request("web_custom_request",
		"URL=http://{url}/water_bg/user/updateUser",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body={\"executor\":\"wangkuang\",\"taskName\":\"信息\",\"startDate\":\"2022-06-06T16:00:00.000Z\",\"taskType\":\"plan\",\"endDate\":\"2022-06-12T16:00:00.000Z\",\"points\":[{\"id\":5,\"pointNo\":\"P0005\",\"pointName\":\"测试巡检点five\",\"address\":\"湖畔\",\"devNum\":13,\"remark\":\"真凉快\",\"devId\":null}],\"planId\":3}",
		LAST);

	lr_output_message("数量%s",lr_eval_string("{yhglxg}"));	
	
	if(atoi(lr_eval_string("{yhglxg}"))==1){
	lr_end_transaction("系统管理-用户管理-修改",LR_PASS);
	}else{
    lr_end_transaction("系统管理-用户管理-修改",LR_FAIL);
	}
	
	return 0;
}
