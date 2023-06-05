<!DOCTYPE html>

<html>
	<head>
		<meta charset="UTF-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<title>订单状态更新页面</title>
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

            /* 列容器 */
            .row {  
                display: -ms-flexbox; 
                display: flex;
                -ms-flex-wrap: wrap; 
                flex-wrap: wrap;
            }
            /*  */
            /* 创建两个列 */
            /* 边栏 */
            .side {
                -ms-flex: 35%; /* IE10 */
                text-align: center;
                flex: 35%;
                background-color: #f1f1f1;
                padding: 20px;
            }
            
            /* 主要的内容区域 */
            .main {   
                -ms-flex: 65%; /* IE10 */
                flex: 65%;
                text-align: center;
                background-color: white;
                padding: 25px;
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
			<h2>订单状态更新</h2>
			<p></p>
		</div>
		<div class="navbar">
			<a href="#">预约信息查看</a>
        	<a href="http://127.0.0.1:8000/Django/System/wxby/templates/order_upload.php">订单提交</a>
			<a href="#">维修日志填写</a>
            <a href="#">维修日志查看</a>
			<a href="#">质检报告提交</a>
            <a href="#">质检报告查看</a>
			<a href="#" class="right">在线客服</a>
		</div>
        <div class="row">
            <div class="side">
                <?php
                    error_reporting(0);  
                    $link=mysqli_connect("127.0.0.1","root","123456","ISAD_database");
                    if(!$link){
                        die("数据库连接错误：".mysqli_connect_error());
                    }
                    // 获取订单号
                    $order_id=htmlspecialchars($_POST['order_id']);
                    $order_state=htmlspecialchars($_POST['order_state']);

                    if($order_state=="default"){
                        $sql="SELECT order_id, order_type, order_content, order_fee, order_state, order_time FROM i_order WHERE i_order.order_id= '$order_id'";
                        $result = mysqli_query($link, $sql);
                        if (mysqli_num_rows($result) >0) {
                            // 输出数据
                            while($row = mysqli_fetch_assoc($result)) {
                                echo "<br>订单号: " . $row["order_id"];
                                echo "<br>订单类型: " . $row["order_type"];
                                echo "<br>订单详情：<br> " . $row["order_content"];
                                echo "<br>订单费用： " . $row["order_fee"];
                                echo "<br>订单状态： " . $row["order_state"];
                                echo "<br>下单时间： " . $row["order_time"];
                                echo "<br><br>";
                            }
                        } else {
                            echo "<br><br>暂无历史订单, 若您通过搜索内容查找订单, 请检查输入的内容是否正确。";
                        }
                    }else{
                        $sql=mysqli_query($link,"update i_order set order_state = '$order_state' where order_id = '$order_id';");
                        if($sql){
							$sql1="SELECT order_id, order_type, order_content, order_fee, order_state, order_time FROM i_order WHERE i_order.order_id= '$order_id'";
							$result1 = mysqli_query($link, $sql1);
							if (mysqli_num_rows($result1) >0) {
								// 输出数据
								echo("订单状态已修改<br>");
								while($row = mysqli_fetch_assoc($result1)) {
									echo "<br>订单号: " . $row["order_id"];
									echo "<br>订单类型: " . $row["order_type"];
									echo "<br>订单详情：<br> " . $row["order_content"];
									echo "<br>订单费用： " . $row["order_fee"];
									echo "<br>订单状态： " . $row["order_state"];
									echo "<br>下单时间： " . $row["order_time"];
									echo "<br><br>";
								}
							} 
                        }else{
                            echo("<script>alert('订单状态修改失败');</script>");
                        }   
                    }
                    mysqli_close($link); 
                ?>
            </div>
            <div class="main">
                <form action=# method="post">
                    <p>订单号: <input type="text" name="order_id" id="order_id"></p><br>
                    <a href=""><input type="submit" value="查看订单详情" style="font-family: 黑体; width:auto; height:30px;"></a>
                    <br><br>
                    <p>订单状态:
					<select name="order_state" style="font-family: 黑体; width:auto;height:30px; text-align: center;">
                        <option selected value="default">-请选择-</option>
                        <option value="尚未维修/保养">尚未维修/保养</option>
						<option value="正在维修/保养中">正在维修/保养中</option>
						<option value="维修/保养完成, 质检已通过">维修/保养完成, 质检已通过</option>
                        <option value="订单已完成">订单已完成</option>
						<option value="订单中止">订单中止</option>
					</select>
				    </p><br>
				    <a href=""><input type="submit" value="修改状态" style="font-family: 黑体; width:auto; height:30px"></a>
                </form>
            </div>
        </div>
		<div class="footer">
			<h5>页面内容仅用于作业</h5>
	  	</div>
  	</body>
</html>
