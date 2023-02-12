Action4()
{	
	web_reg_find("SaveCount=login_check_point",
		"Text=\"msg\":\"范驰\"",
		LAST);
	
	lr_start_transaction("登录事务");

	web_reg_save_param_json(
		"ParamName=token",
		"QueryString=$.data",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);
	
	web_custom_request("登录",
		"URL=http://{url}/water_bg/user/login",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body={\"userName\":\"admin\",\"password\":\"123\"}",
		LAST);

	lr_output_message(lr_eval_string("{login_check_point}"));
	
	if (atoi(lr_eval_string("{login_check_point}")) == 1){
		lr_end_transaction("登录事务", LR_PASS);
	} else {
		lr_end_transaction("登录事务", LR_FAIL);

	}
	
	
	web_reg_find("SaveCount=getBaseStocks_check_point",
		"Text=\"msg\":\"OK\"",
		LAST);
	
	lr_start_transaction("采购审核事务");
	
	web_add_header("Authorization",
		"{token}");
	
	web_url("添加采购项页面",
		"URL=http://{url}/water_bg/buy/getBaseStocks",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		LAST);
	lr_output_message(lr_eval_string("{getBaseStocks_check_point}"));

	
	if (atoi(lr_eval_string("{getBaseStocks_check_point}")) == 1){
		lr_output_message("访问添加采购项页面测试成功！");
	} else {
		lr_output_message("访问添加采购项页面测试失败！");
	}
	
	
	
	web_reg_find("SaveCount=addCheck_check_point",
		"Text=\"msg\":\"OK\"",
		LAST);
	
	web_add_header("Authorization",
		"{token}");
	
	web_custom_request("添加采购项",
		"URL=http://{url}/water_bg/buy/addCheck",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body={\"buyman\":\"郭凡字仲达\",\"stockId\":6,\"useDate\":\"2022-06-21\",\"buySum\":\"1\",\"buyDate\":\"2022-06-27\",\"description\":\"郭凡字仲达\",\"money\":100,\"price\":100}",
		LAST);

	lr_output_message(lr_eval_string("{addCheck_check_point}"));

	if (atoi(lr_eval_string("{addCheck_check_point}")) == 2){
		lr_output_message("添加采购项测试成功！");
	} else {
		lr_output_message("添加采购项测试失败！");
	}
	
	
	web_reg_find("SaveCount=buycheck_check_point",
		"Text=\"msg\":\"OK\"",
		LAST);
	
	web_add_header("Authorization",
		"{token}");
	
	web_custom_request("采购审核通过操作",
		"URL=http://{url}/water_bg/buy/check",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body={\"id\":12,\"stockId\":6,\"description\":\"郭凡字仲达\",\"useDate\":\"2022-06-20\",\"buySum\":1,\"money\":100,\"buyDate\":\"2022-06-26\",\"checkDate\":null,\"isChecked\":\"未审核\",\"checkman\":null,\"baseStock\":null,\"no\":\"cl21312\",\"name\":\"加氯机\",\"buyman\":\"郭凡字仲达\",\"status\":null,\"pageIndex\":null}",
		LAST);

	lr_output_message(lr_eval_string("{buycheck_check_point}"));

	
	if (atoi(lr_eval_string("{buycheck_check_point}")) == 2){
		lr_output_message("采购审核通过操作测试成功！");
	} else {
		lr_output_message("采购审核通过操作测试失败！");
	}
	
	
	web_reg_find("SaveCount=buycheck_update_point",
		"Text=\"msg\":\"OK\"",
		LAST);
	
	web_add_header("Authorization",
		"{token}");
	
	web_custom_request("采购反馈提交操作",
		"URL=http://{url}/water_bg/buyback/update",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body={\"id\":39,\"buycheckId\":12,\"realprice\":\"100\",\"realbuyCount\":\"1\",\"realcost\":\"100\",\"dec\":\"郭凡字仲达\",\"status\":\"已完成\"}",
		LAST);

	lr_output_message(lr_eval_string("{buycheck_update_point}"));

	
	if (atoi(lr_eval_string("{buycheck_update_point}")) == 2){
		lr_end_transaction("采购审核事务", LR_PASS);
	} else {
		lr_end_transaction("采购审核事务", LR_FAIL);
	}
	
	
	web_reg_find("SaveCount=gmsgetallpump_check_point",
		"Text=\"msg\":\"OK\"",
		LAST);
	
	lr_start_transaction("G-M-S泵站事务");
	
	web_add_header("Authorization",
		"{token}");
	
	web_url("泵站信息页面",
		"URL=http://{url}/water_bg/gms/getallpump",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		LAST);
	lr_output_message(lr_eval_string("{gmsgetallpump_check_point}"));

	
	if (atoi(lr_eval_string("{gmsgetallpump_check_point}")) == 1){
		lr_output_message("访问泵站信息页面测试成功！");
	} else {
		lr_output_message("访问泵站信息页面测试失败！");
	}
	
	
	web_reg_find("SaveCount=gmsaddpump_check_point",
	"Text=\"msg\":\"OK\"",
	LAST);
	
	web_add_header("Authorization",
		"{token}");
	
	web_custom_request("添加站点数据",
		"URL=http://{url}/water_bg/gms/addpump",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body={\"pumpname\":\"ABC\",\"pumptype\":\"1\",\"gas\":\"185.63\",\"intpower\":\"185.63\",\"tp\":\"185.63\",\"outpower\":\"185.63\",\"temperature\":\"185.63\",\"userId\":7,\"pumpsize\":\"大\"}",
		LAST);

	lr_output_message(lr_eval_string("{gmsaddpump_check_point}"));

	
	if (atoi(lr_eval_string("{gmsaddpump_check_point}")) == 2){
		lr_output_message("添加站点数据测试成功！");
	} else {
		lr_output_message("添加站点数据测试失败！");
	}
	
	
	web_reg_find("SaveCount=gmsupdatepump_check_point",
	"Text=\"msg\":\"OK\"",
	LAST);
	
	web_add_header("Authorization",
		"{token}");
	
	web_custom_request("修改站点数据",
		"URL=http://{url}/water_bg/gms/updatepump",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body={\"id\":15,\"pumpname\":\"ABC\",\"pumptype\":\"1\",\"gas\":185.63,\"tp\":185.63,\"intpower\":185.63,\"outpower\":185.63,\"temperature\":185.63,\"userId\":7,\"name\":\"卢文龙\",\"pumpsize\":\"大\"}",
		LAST);

	lr_output_message(lr_eval_string("{gmsupdatepump_check_point}"));

	
	if (atoi(lr_eval_string("{gmsupdatepump_check_point}")) == 2){
		lr_output_message("修改站点数据测试成功！");
	} else {
		lr_output_message("修改站点数据测试失败！");
	}
	
	
	web_reg_find("SaveCount=gmsgetpumpdata_check_point",
	"Text=\"msg\":\"OK\"",
	LAST);
	
	web_add_header("Authorization",
		"{token}");
	
	web_custom_request("泵站数据信息查询",
		"URL=http://{url}/water_bg/gms/getpumpdata",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body={\"pumpId\":1,\"time\":\"2021-03-16\",\"pageIndex\":1}",
		LAST);

	lr_output_message(lr_eval_string("{gmsgetpumpdata_check_point}"));

	
	if (atoi(lr_eval_string("{gmsgetpumpdata_check_point}")) == 1){
		lr_end_transaction("G-M-S泵站事务", LR_PASS);
	} else {
		lr_end_transaction("G-M-S泵站事务", LR_FAIL);
	}
	
	return 0;
}
