Action3()
{	
	web_reg_find("SaveCount=dlxy",
		"Text=范驰",
		LAST);

	web_reg_save_param_json(
		"ParamName=token",
		"QueryString=$.data",
		SEARCH_FILTERS,
		"Scope=BODY",
		LAST);

	
		web_custom_request("登陆测试",
		"URL=http://{url}/water_bg/user/login",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body={\"userName\":\"admin\",\"password\":\"123\"}",
		LAST);

	

	
		
	lr_output_message("数量为%s。", lr_eval_string("{dlxy}"));	
		
	if (atoi(lr_eval_string("{dlxy}")) == 1) {
          lr_output_message("访问首页测试成功！");
      } else {
          lr_output_message("访问首页测试失败!");
      }
	
	
	
	web_reg_find("SaveCount=jrwxxtxy",
		"Text=OK",
		LAST);
	
	
	web_add_header("Authorization",
		"{token}");
	
	
	web_custom_request("进入维修系统首页测试",
		"URL=http://{url}/water_bg/repiar/circular",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body={\"dealWithDate\":\"\",\"endDate\":\"\"}",
		LAST);
	
	if (atoi(lr_eval_string("{jrwxxtxy}")) == 1) {
          lr_output_message("进入维修系统成功！");
      } else {
          lr_output_message("进入维修系统失败!");
      }


//进入未派工单	
	
	web_reg_find("SaveCount=jrwpgdxy",
		"Text=OK",
		LAST);
	
	web_add_header("Authorization",
		"{token}");
	
	web_custom_request("进入未派工单",
		"URL=http://{url}/water_bg/user/repair",
		"Method=GET",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body=",
		LAST);
	
	if (atoi(lr_eval_string("{jrwpgdxy}")) == 1) {
          lr_output_message("进入未派工单成功！");
      } else {
          lr_output_message("进入未派工单失败!");
      }
	
//未派工单查询
	
	web_reg_find("SaveCount=wpgdcxxy",
		"Text=ok",
		LAST);
	
	web_add_header("Authorization",
		"{token}");

	web_custom_request("未派工单查询",
		"URL=http://{url}/water_bg/worker/list",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json;charset=UTF-8",
		"Body={\"state\":1,\"source\":\"撤硕听说\",\"eventId\":\"\",\"reflectPeople\":\"郭凡\",\"phone\":\"\",\"reflectUnit\":\"\",\"reflectArea\":\"\",\"pappenArea\":\"\",\"pageIndex\":4,\"happenDate\":\"\",\"endDate\":\"\"}",
		LAST);
	
	if (atoi(lr_eval_string("{wpgdcxxy}")) == 1) {
          lr_output_message("未派工单查询成功！");
      } else {
          lr_output_message("未派工单查询失败!");
      }
	
//未派工单添加
	web_reg_find("SaveCount=wpgdtjxy",
		"Text=OK",
		LAST);
	
	web_add_header("Authorization",
		"{token}");
	
		
	web_custom_request("添加未派工单",
		"URL=http://{url}/water_bg/repair/add",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json;charset=UTF-8",
		"Body={\"reflectPeople\":\"郭凡\",\"source\":\"刘星跟他说的\",\"phone\":\"13353430762\",\"email\":\"1727254353@qq.com\",\"reflectUnit\":\"郭凡破防时刻\",\"reflectArea\":\"秦岭山下郭凡家\",\"reflectContent\":\"破防了\",\"reflectClass\":\"低\",\"happenDate\":\"2022-06-30 20:12:38\",\"happenArea\":\"6教\",\"eventId\":2,\"endDate\":\"2022-06-30 20:13:06\"}",
		LAST);

	if (atoi(lr_eval_string("{wpgdtjxy}")) == 1) {
          lr_output_message("未派工单添加成功！");
      } else {
          lr_output_message("未派工单添加失败!");
      }
	
//未派工单重置
	web_reg_find("SaveCount=wpgdczxy",
		"Text=ok",
		LAST);
	
	web_add_header("Authorization",
		"{token}");
	
	web_custom_request("未派工单重置",
		"URL=http://{url}/water_bg/worker/list",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json;charset=UTF-8",
		"Body={\"state\":1,\"source\":\"\",\"eventId\":\"\",\"reflectPeople\":\"\",\"phone\":\"\",\"reflectUnit\":\"\",\"reflectArea\":\"\",\"pappenArea\":\"\",\"pageIndex\":1,\"happenDate\":\"\",\"endDate\":\"\"}",
		LAST);

	if (atoi(lr_eval_string("{wpgdczxy}")) == 1) {
          lr_output_message("未派工单重置成功！");
      } else {
          lr_output_message("未派工单重置失败!");
      }
      
//未派工单修改测试
	
	web_reg_find("SaveCount=wpgdxgxy",
		"Text=OK",
		LAST);
	
	web_add_header("Authorization",
		"{token}");
		
	web_custom_request("未派工单修改",
		"URL=http://{url}/water_bg/repair/update",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json;charset=UTF-8",
		"Body={\"id\":59,\"reflectPeople\":\"郭凡\",\"source\":\"刘星跟他说的\",\"phone\":\"13353430762\",\"email\":\"1727254353@qq.com\",\"reflectUnit\":\"郭凡破防时刻\",\"reflectArea\":\"秦岭山下郭凡家\",\"reflectClass\":\"低\",\"happenDate\":\"2022-06-30 20:12:38\",\"happenArea\":\"6教\",\"eventId\":2,\"endDate\":\"2022-06-30 20:13:06\",\"state\":1,\"stateName\":\"未指派\",\"userId\":17}",
		LAST);

	if (atoi(lr_eval_string("{wpgdxgxy}")) == 1) {
          lr_output_message("未派工单修改成功！");
      } else {
          lr_output_message("未派工单修改失败!");
      }
      
//未派工单删除
	web_reg_find("SaveCount=wpgdscxy",
		"Text=OK",
		LAST);
	
	web_add_header("Authorization",
		"{token}");
		
	web_custom_request("未派工单删除",
		"URL=http://{url}/water_bg/repair/delete?id=55",
		"Method=GET",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body=",
		LAST);
		
	if (atoi(lr_eval_string("{wpgdscxy}")) == 1) {
          lr_output_message("未派工单删除成功！");
      } else {
          lr_output_message("未派工单删除失败!");
      }

	
//进入已派工单

	web_reg_find("SaveCount=jrypgdxy",
		"Text=OK",
		LAST);
	
	web_add_header("Authorization",
		"{token}");
	
	web_custom_request("进入已派工单",
		"URL=http://{url}/water_bg/user/repair",
		"Method=GET",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body=",
		LAST);
	
	if (atoi(lr_eval_string("{jrypgdxy}")) == 1) {
          lr_output_message("进入已派工单成功！");
      } else {
          lr_output_message("进入已派工单失败!");
      }
      


	
	
//已派工单重置
	
	web_reg_find("SaveCount=ypgdczxy",
		"Text=ok",
		LAST);
	
	web_add_header("Authorization",
		"{token}");
	
	web_custom_request("已派工单重置",
		"URL=http://{url}/water_bg/worker/list",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body={\"state\":2,\"source\":\"\",\"eventId\":\"\",\"reflectPeople\":\"\",\"phone\":\"\",\"reflectUnit\":\"\",\"reflectArea\":\"\",\"pappenArea\":\"\",\"pageIndex\":0,\"happenDate\":\"\",\"endDate\":\"\"}",
		LAST);

	if (atoi(lr_eval_string("{ypgdczxy}")) == 1) {
          lr_output_message("已派工单重置成功！");
      } else {
          lr_output_message("已派工单重置失败!");
      }
      
      
//已派工单去审核
	web_reg_find("SaveCount=ypgdqshxy",
		"Text=OK",
		LAST);
	
	web_add_header("Authorization",
		"{token}");
	
	web_custom_request("已派工单去审核",
		"URL=http://{url}/water_bg/repair/updateState?id=49&state=3",
		"Method=GET",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body=",
		LAST);
	
	if (atoi(lr_eval_string("{ypgdqshxy}")) == 1) {
          lr_output_message("已派工单去审核成功！");
      } else {
          lr_output_message("已派工单去审核失败!");
      }
	
//已派工单删除
	web_reg_find("SaveCount=ypgdscxy",
		"Text=OK",
		LAST);
	
	web_add_header("Authorization",
		"{token}");
	
	web_custom_request("已派工单删除",
		"URL=http://{url}/water_bg/repair/delete?id=50",
		"Method=GET",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body=",
		LAST);
		
	if (atoi(lr_eval_string("{ypgdscxy}")) == 1) {
          lr_output_message("已派工单删除成功！");
      } else {
          lr_output_message("已派工单删除失败!");
      }

	
	
	
//未审核工单
	
	web_reg_find("SaveCount=jrwshgdxy",
		"Text=OK",
		LAST);
	
	web_add_header("Authorization",
		"{token}");
		
	web_custom_request("进入未审核工单",
		"URL=http://{url}/water_bg/user/repair",
		"Method=GET",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body=",
		LAST);
		
	if (atoi(lr_eval_string("{jrwshgdxy}")) == 1) {
          lr_output_message("进入未审核工单成功！");
      } else {
          lr_output_message("进入未审核工单失败!");
      }
	
	
//未审核工单查询
	web_reg_find("SaveCount=wshgdcxxy",
		"Text=ok",
		LAST);
	
	web_add_header("Authorization",
		"{token}");
	
	web_custom_request("未审核工单查询",
		"URL=http://{url}/water_bg/worker/list",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body={\"state\":3,\"source\":\"\",\"eventId\":\"\",\"reflectPeople\":\"\",\"phone\":\"\",\"reflectUnit\":\"\",\"reflectArea\":\"\",\"pappenArea\":\"\",\"pageIndex\":1,\"happenDate\":\"\",\"endDate\":\"\"}",
		LAST);

	if (atoi(lr_eval_string("{wshgdcxxy}")) == 1) {
          lr_output_message("未审核工单查询成功！");
      } else {
          lr_output_message("未审核工单查询失败!");
      }
      
      
//未审核工单重置
	
	web_reg_find("SaveCount=wshgdczxy",
		"Text=ok",
		LAST);
	
	web_add_header("Authorization",
		"{token}");
		
	web_custom_request("未审核工单重置",
		"URL=http://{url}/water_bg/worker/list",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body={\"state\":3,\"source\":\"\",\"eventId\":\"\",\"reflectPeople\":\"\",\"phone\":\"\",\"reflectUnit\":\"\",\"reflectArea\":\"\",\"pappenArea\":\"\",\"pageIndex\":1,\"happenDate\":\"\",\"endDate\":\"\"}",
		LAST);

	if (atoi(lr_eval_string("{wshgdczxy}")) == 1) {
          lr_output_message("未审核工单查询成功！");
      } else {
          lr_output_message("未审核工单查询失败!");
      }
		
	
	
//未审核工单审核

	web_reg_find("SaveCount=wshgdshxy",
		"Text=OK",
		LAST);
	
	web_add_header("Authorization",
		"{token}");
	
	web_custom_request("未审核工单审核",
		"URL=http://{url}/water_bg/repair/updateState?id=39&state=4",
		"Method=GET",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body=",
		LAST);

	if (atoi(lr_eval_string("{wshgdshxy}")) == 1) {
          lr_output_message("未审核工单审核成功！");
      } else {
          lr_output_message("未审核工单审核失败!");
      }
      
      
//未审核工单删除
	web_reg_find("SaveCount=wshgdscxy",
		"Text=OK",
		LAST);
	
	web_add_header("Authorization",
		"{token}");
	
	web_custom_request("未审核工单删除",
		"URL=http://{url}/water_bg/repair/delete?id=49",
		"Method=GET",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body=",
		LAST);

	if (atoi(lr_eval_string("{wshgdscxy}")) == 1) {
          lr_output_message("未审核工单删除成功！");
      } else {
          lr_output_message("未审核工单删除失败!");
      }
	
//进入已审核工单
	web_reg_find("SaveCount=jryshgdxy",
		"Text=OK",
		LAST);
	
	web_add_header("Authorization",
		"{token}");
	
	web_custom_request("进入已审核工单",
		"URL=http://{url}/water_bg/repair/delete?id=49",
		"Method=GET",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body=",
		LAST);

	if (atoi(lr_eval_string("{jryshgdxy}")) == 1) {
          lr_output_message("未审核工单删除成功！");
      } else {
          lr_output_message("未审核工单删除失败!");
      }
      
//已审核工单查询
	
	web_reg_find("SaveCount=yshgdcxxy",
		"Text=ok",
		LAST);
	
	web_add_header("Authorization",
		"{token}");

	web_custom_request("已审核工单查询",
		"URL=http://{url}/water_bg/worker/list",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body={\"state\":4,\"source\":\"\",\"eventId\":\"\",\"reflectPeople\":\"\",\"phone\":\"\",\"reflectUnit\":\"\",\"reflectArea\":\"\",\"pappenArea\":\"\",\"pageIndex\":1,\"happenDate\":\"\",\"endDate\":\"\"}",
		LAST);
		
	if (atoi(lr_eval_string("{yshgdcxxy}")) == 1) {
          lr_output_message("已审核工单查询成功！");
      } else {
          lr_output_message("已审核工单查询失败!");
      }

//已审核工单重置
	web_reg_find("SaveCount=yshgdczxy",
		"Text=ok",
		LAST);
	
	web_add_header("Authorization",
		"{token}");
	
	web_custom_request("已审核工单重置",
		"URL=http://{url}/water_bg/worker/list",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body={\"state\":4,\"source\":\"\",\"eventId\":\"\",\"reflectPeople\":\"\",\"phone\":\"\",\"reflectUnit\":\"\",\"reflectArea\":\"\",\"pappenArea\":\"\",\"pageIndex\":1,\"happenDate\":\"\",\"endDate\":\"\"}",
		LAST);

	if (atoi(lr_eval_string("{yshgdczxy}")) == 1) {
          lr_output_message("已审核工单重置成功！");
      } else {
          lr_output_message("已审核工单重置失败!");
      }
      
      
//已审核工单删除
	web_reg_find("SaveCount=yshgdscxy",
		"Text=OK",
		LAST);
	
	web_add_header("Authorization",
		"{token}");
	
	web_custom_request("web_custom_request",
		"URL=http://{url}/water_bg/repair/delete?id=10",
		"Method=GET",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body=",
		LAST);
	if (atoi(lr_eval_string("{yshgdscxy}")) == 1) {
          lr_output_message("已审核工单删除成功！");
      } else {
          lr_output_message("已审核工单删除失败!");
      }
	
	
//进入设备维修
	web_reg_find("SaveCount=jrsbwxxy",
		"Text=ok",
		LAST);
	
	web_add_header("Authorization",
		"{token}");
   
	web_custom_request("进入设备维修",
		"URL=http://{url}/water_bg/baseRepair/List",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body={\"createDate\":\"\",\"endDate\":\"\",\"pageIndex\":\"1\",\"pageSize\":\"5\",\"childStatus\":\"\",\"baseName\":\"\"}",
		LAST);
	if (atoi(lr_eval_string("{jrsbwxxy}")) == 1) {
          lr_output_message("进入设备维修成功！");
      } else {
          lr_output_message("进入设备维修失败!");
      }

//设备维修查询
	
	web_reg_find("SaveCount=sbwxcxxy",
		"Text=ok",
		LAST);
	
	web_add_header("Authorization",
		"{token}");
   
   	web_custom_request("设备维修查询",
		"URL=http://{url}/water_bg/baseRepair/List",
		"Method=POST",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body={\"createDate\":\"\",\"endDate\":\"\",\"pageIndex\":\"1\",\"pageSize\":\"5\",\"childStatus\":\"已报修\",\"baseName\":\"\"}",
		LAST);
	if (atoi(lr_eval_string("{sbwxcxxy}")) == 1) {
          lr_output_message("设备维修查询成功！");
      } else {
          lr_output_message("设备维修查询失败!");
      }
	
   
   
//设备维修完成检修
	web_reg_find("SaveCount=sbwxwcjxxy",
		"Text=OK",
		LAST);
	
	web_add_header("Authorization",
		"{token}");
   
   

	web_custom_request("设备维修完成检修",
		"URL=http://{url}/water_bg/baseRepair/updateStatus?deviceId=27",
		"Method=GET",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body=",
		LAST);
	if (atoi(lr_eval_string("{sbwxwcjxxy}")) == 1) {
          lr_output_message("设备维修完成检修成功！");
      } else {
          lr_output_message("设备维修完成检修失败!");
      }
	
	
//设备维修删除

	web_reg_find("SaveCount=sbwxscxy",
		"Text=OK",
		LAST);
	
	web_add_header("Authorization",
		"{token}");
   
   
   

	web_custom_request("设备维修删除",
		"URL=http://{url}/water_bg/baseRepair/delete?id=28",
		"Method=GET",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body=",
		LAST);
		
	if (atoi(lr_eval_string("{sbwxscxy}")) == 1) {
          lr_output_message("设备维修删除成功！");
      } else {
          lr_output_message("设备维修完删除失败!");
      }
	
	return 0;
}
