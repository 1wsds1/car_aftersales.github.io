<!DOCTYPE html>

<html>
	<head>
		<meta charset="UTF-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<title>订单提交页面</title>
		<style>
			* {
				box-sizing: border-box;
				font-family: "黑体";
			}
			
			/* body 样式 */
			body {
				font-family: Arial;
				margin: 0;
			}
			
			/* 标题 */
			.header {
				padding: 80px;
				text-align: center;
				background: rgb(5, 96, 169);
				color: rgb(255, 255, 255);
			}
			
			/* 标题字体加大 */
			.header h1 {
				font-size: 40px;
			}
			
			/* 导航 */
			.navbar {
				overflow: hidden;
				/* background-color: rgb(214, 213, 213); */
				background: #eee;
			}
			
			/* 导航栏样式 */
			.navbar a {
				float: left;
				display: block;
				color: rgb(0, 0, 0);
				text-align: center;
				padding: 14px 40px;
				text-decoration: none;
			}

			/* 右侧链接*/
			.navbar a.right {
				float: right;
			}
				
			/* 鼠标移动到链接的颜色 */
			.navbar a:hover {
				background-color: #ddd;
				color: black;
			}
			/* 图片 */
			.fff {
				background-color: #eee;
				text-align: center;
				width: 100%;
				padding: 20px;
				margin-left:auto;
				margin-right:auto;
			}

			/* 强调说明 */
			.emphasize {
				background-color: #ffffff;
				text-align: center;
				width:100%;
				padding: 20px;
			}

			/* 底部 */
			.footer {
				padding: 20px;
				text-align: center;
				background: #ddd;
			}
			
			/* 去下划线 */
			a{
				text-decoration: none;
			}
		</style>
	</head>

	<body>
		<div class="header">
			<h2>订单提交</h2>
			<p></p>
        </div>
        <div class="navbar">
			<a href="#">预约信息查看</a>
			<a href="http://127.0.0.1:8000/Django/System/wxby/templates/status_update.php">订单状态更新</a>
			<a href="#">维修日志填写</a>
            <a href="#">维修日志查看</a>
			<a href="#">质检报告提交</a>
            <a href="#">质检报告查看</a>
			<a href="#" class="right">在线客服</a>
		</div><br><br>
		<div class="fff" style="height:auto; width:700px"> 
			<form action=# method="post">
                <p>用户名:<input type="text" name="user_name" id="user_name" /></p><br>
				<p>订单类型:
					<select name="order_type" style="font-family: 黑体; width:80px;height:30px; text-align: center;">
						<option value="维修">维修</option>
						<option value="保养">保养</option>
					</select>
				</p><br>
				<p>订单内容:<br><br>
					<textarea name="order_content" id="order_content" cols="80" rows="15"></textarea><br>
				</p><br>
                <p>订单金额:<input type="text" name="order_fee" /></p>
				<p><br>
                <p>订单状态:
					<select name="order_state" style="font-family: 黑体; width:auto;height:30px; text-align: center;">
						<option selected value="尚未维修/保养">尚未维修/保养</option>
						<option value="正在维修/保养中">正在维修/保养中</option>
						<option value="维修/保养完成, 质检已通过">维修/保养完成, 质检已通过</option>
                        <option value="订单已完成">订单已完成</option>
						<option value="订单中止">订单中止</option>
					</select>
				</p><br>
				<a href=""><input type="submit" style="font-family: 黑体; width:60px; height:30px"></a>
			</form>
		</div><br><br>
		<div class="footer">
			  <h5>页面内容仅用于作业</h5>
		</div>
	</body>
</html>
<?php 
	error_reporting(0);      
    // 连接数据库
    $link=mysqli_connect("127.0.0.1","root","123456","ISAD_database");
    if(!$link){
        die("数据库连接错误：".mysqli_connect_error());
    }

    // 生成订单号
    $count_sql = mysqli_query($link, "SELECT COUNT(*) as count from i_order");
    $row = mysqli_fetch_assoc($count_sql);
    $count = $row['count'];
    $order_id = 2000001+ $count;

    // 获取填写内容
    $order_type=htmlspecialchars($_POST['order_type']);
    $order_content=htmlspecialchars($_POST['order_content']);
    $order_fee=htmlspecialchars($_POST['order_fee']);
    $order_state=htmlspecialchars($_POST['order_state']);
    $user_name=htmlspecialchars($_POST['user_name']);

    // 获取申请时间
    $order_time=date('Y-m-d H:i:s');

    $sql=mysqli_query($link,"INSERT INTO i_order(order_id,user_name,order_type,order_content,order_time,order_fee,order_state) VALUES('$order_id','$user_name','$order_type','$order_content','$order_time','$order_fee','$order_state');");
    if($sql){
        echo("<script>alert('订单创建完成');</script>");      
    }
    else{
        echo("<script>alert('订单创建失败');</script>");
    }
    mysqli_close($link); 
?>