Action1()
{	// 登录事务
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
//	lr_output_message("token%s",lr_eval_string("{token}"));
	if(atoi(lr_eval_string("{dl}"))==1){
	lr_end_transaction("登录事务",LR_PASS);
	}else{
    lr_end_transaction("登录事务",LR_FAIL);
	}
	
	// 基础设施编辑
	lr_start_transaction("基础设施事务");
	
	web_reg_find("Search=Body",
	"SaveCount=bj",
	"Text=OK",
	LAST);

	
	web_add_header("Authorization",
		"{token}");

	
	web_custom_request("基础设施编辑",
		"URL=http://{url}/water_bg/base/updateBaseType",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body={\"i\":1,\"baseId\":8,\"name\":\"lbw广场\",\"longitude\":110,\"latitude\":120,\"useTime\":\"2021-03-09\",\"address\":\"卢本伟顶顶顶顶\",\"describe\":\"用于武昌区的用水\"}",
		LAST);
	
	if(atoi(lr_eval_string("{bj}"))==2){
	 lr_output_message("基础设施编辑事务测试成功");
	}else{
     lr_output_message("基础设施编辑事务测试失败");
	}
	
	// 基础设施详情
	
	web_reg_find("Search=Body",
	"SaveCount=xq",
	"Text=OK",
	LAST);
	
	web_add_header("Authorization",
		"{token}");
	
	web_url("web_url",
		"URL=http://{url}/water_bg/child/getChild?id=1",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		LAST);
	if(atoi(lr_eval_string("{xq}"))==1){
	 lr_output_message("基础设施详情事务测试成功");
	}else{
     lr_output_message("基础设施详情事务测试失败");
	}
	
	// 基础设施修改
	
	web_reg_find("Search=Body",
	"SaveCount=xj",
	"Text=OK",
	LAST);
	
	web_add_header("Authorization",
		"{token}");
	
	web_custom_request("基础设施修改",
		"URL=http://{url}/water_bg/child/updateChild",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body={\"id\":13,\"stockChildId\":1,\"childName\":\"王莹大傻\",\"childStatus\":\"良好\"}",
		LAST);
	
	if(atoi(lr_eval_string("{xj}"))==2){
	 lr_output_message("基础设施修改事务测试成功");
	}else{
     lr_output_message("基础设施修改事务测试失败");
	}
	
	// 基础设施添加
	
	web_reg_find("Search=Body",
	"SaveCount=tj",
	"Text=OK",
	LAST);
	
	web_add_header("Authorization",
		"{token}");
	
	web_custom_request("基础设施添加",
		"URL=http://{url}/water_bg/child/addChild",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body={\"stockChildId\":1,\"childName\":\"666\",\"childStatus\":\"良好\"}",
		LAST);
	
	if(atoi(lr_eval_string("{tj}"))==2){
	 lr_output_message("基础设施添加事务测试成功");
	}else{
     lr_output_message("基础设施添加事务测试失败");
	}
	
	// 基础设施申请
	
	web_reg_find("Search=Body",
	"SaveCount=sq",
	"Text=OK",
	LAST);
	
	web_add_header("Authorization",
		"{token}");
	
	web_url("web_url",
		"URL=http://{url}/water_bg/ask/askStock?id=1&reason=44&askNum=4",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		LAST);
	if(atoi(lr_eval_string("{sq}"))==2){
	lr_end_transaction("基础设施事务",LR_PASS);
	}else{
    lr_end_transaction("基础设施事务",LR_FAIL);
	}
	
	// 设备列表查询
	lr_start_transaction("设备列表事务");
	
	web_reg_find("Search=Body",
	"SaveCount=cx",
	"Text=OK",
	LAST);
	
	web_add_header("Authorization",
		"{token}");
	
	web_custom_request("设备列表查询",
		"URL=http://{url}/water_bg/device/getAll?pageIndex=1&pageSize=6",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body={\"no\":\"55\",\"name\":\"\",\"buyUser\":\"\",\"checkUser\":\"\"}",
		LAST);
	
	if(atoi(lr_eval_string("{cx}"))==1){
	 lr_output_message("设备列表查询事务测试成功");
	}else{
     lr_output_message("设备列表查询事务测试失败");
	}
	
	// 设备列表详情
	web_reg_find("Search=Body",
	"SaveCount=sbxq",
	"Text=OK",
	LAST);
	
	web_add_header("Authorization",
		"{token}");
	
	web_url("设备列表详情",
		"URL=http://{url}/water_bg/basestock/getBaseStock?id=1",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		LAST);
	
	if(atoi(lr_eval_string("{sbxq}"))==1){
	 lr_output_message("设备列表详情测试成功");
	}else{
     lr_output_message("设备列表详情测试失败");
	}
	
	// 设备列表修改
	
	web_reg_find("Search=Body",
	"SaveCount=sbxg",
	"Text=OK",
	LAST);
	
	web_add_header("Authorization",
		"{token}");
	
	web_custom_request("设备列表修改",
		"URL=http://{url}/water_bg/basestock/updatebasestock",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body={\"id\":1,\"no\":\"苹果\",\"name\":\"苹果99 Pro\",\"price\":\"10\",\"buyCount\":\"55\"}",
		LAST);
	
	if(atoi(lr_eval_string("{sbxg}"))==2){
	 lr_output_message("设备列表修改事务测试成功");
	}else{
     lr_output_message("设备列表修改事务测试失败");
	}
	
	// 设备列表分配列表
	web_reg_find("Search=Body",
	"SaveCount=sbfplb",
	"Text=OK",
	LAST);
	
	web_add_header("Authorization",
		"{token}");
	
	web_url("设备列表分配列表",
		"URL=http://{url}/water_bg/base/allBase",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		LAST);
	
	if(atoi(lr_eval_string("{sbfplb}"))==1){
	 lr_output_message("设备列表分配列表测试成功");
	}else{
     lr_output_message("设备列表分配列表测试失败");
	}
	
	// 设备列表分配
	web_reg_find("Search=Body",
	"SaveCount=sbfp",
	"Text=OK",
	LAST);
	
	web_add_header("Authorization",
		"{token}");
	
	web_url("设备列表分配",
		"URL=http://{url}/water_bg/device/disStockToBase?baseId=8&stockId=5&disNum=1",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		LAST);
	
	if(atoi(lr_eval_string("{sbfp}"))==2){
	 lr_output_message("设备列表分配测试成功");
	}else{
     lr_output_message("设备列表分配测试失败");
	}
	
	// 设备列表待批列表
	web_reg_find("Search=Body",
	"SaveCount=sbdplb",
	"Text=OK",
	LAST);
	
	web_add_header("Authorization",
		"{token}");
	
	web_url("设备列表待批列表",
		"URL=http://{url}/water_bg/ask/getAskAll0",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		LAST);
	
	if(atoi(lr_eval_string("{sbdplb}"))==1){
	 lr_output_message("设备列表待批列表测试成功");
	}else{
     lr_output_message("设备列表待批列表测试失败");
	}
	
	// 设备列表已批列表
	web_reg_find("Search=Body",
	"SaveCount=sbyplb",
	"Text=OK",
	LAST);
	
	web_add_header("Authorization",
		"{token}");
	
	web_url("设备列表已批列表",
		"URL=http://{url}/water_bg/ask/getAskAll12",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		LAST);
	
	if(atoi(lr_eval_string("{sbyplb}"))==1){
	 lr_end_transaction("设备列表事务",LR_PASS);
	}else{
    lr_end_transaction("设备列表事务",LR_FAIL);
	}
	
	// 设备属性添加
	
	lr_start_transaction("设备属性事务");
	
	web_reg_find("Search=Body",
	"SaveCount=sbsxtj",
	"Text=添加成功",
	LAST);
	
	web_add_header("Authorization",
		"{token}");
	
	web_custom_request("设备属性添加",
		"URL=http://{url}/water_bg/device/addStatic",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body={\"id\":\"\",\"describe\":\"闫步榕的高玩\",\"unit\":\"个\",\"stockId\":\"1\"}",
		LAST);
	
	if(atoi(lr_eval_string("{sbsxtj}"))==1){
	 lr_output_message("设备属性添加测试成功");
	}else{
     lr_output_message("设备属性添加测试失败");
	}
	
	// 设备属性修改
	

	
	web_reg_find("Search=Body",
	"SaveCount=sbsxxg",
	"Text=修改成功",
	LAST);
	
	web_add_header("Authorization",
		"{token}");
	
	web_custom_request("设备属性修改",
		"URL=http://{url}/water_bg/device/updateStatic",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body={\"id\":1,\"describe\":\"闫步榕\",\"unit\":\"根\",\"stockId\":1}",
		LAST);
	
	if(atoi(lr_eval_string("{sbsxxg}"))==1){
	 lr_end_transaction("设备属性事务",LR_PASS);
	}else{
    lr_end_transaction("设备属性事务",LR_FAIL);
	}
	
	// 爆管监控
	lr_start_transaction("爆管监控事务");
	
	web_reg_find("Search=Body",
	"SaveCount=bgjk",
	"Text=OK",
	LAST);
	
	web_add_header("Authorization",
		"{token}");
	
	web_url("爆管监控",
		"URL=http://{url}/water_bg/boom/getAll",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		LAST);
	
	if(atoi(lr_eval_string("{bgjk}"))==1){
	 lr_end_transaction("爆管监控事务",LR_PASS);
	}else{
    lr_end_transaction("爆管监控事务",LR_FAIL);
	}
	
	return 0;
}
