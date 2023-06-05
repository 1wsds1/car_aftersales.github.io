<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>ISAD-历史订单查询</title>
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
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
			<h2>ISAD维修保养历史订单</h2>
			<p></p>
		</div>
		<div class="navbar">
            <a href="http://127.0.0.1:8000/">售后首页</a>
			<a href="/wxby/online_reserve">在线预约</a>
			<a href="/wxby/by_plan">保养规划</a>
			<a href="/cdgh/cdgh">充电规划</a>
			<a href="/kf/kf_index" class="right">在线客服</a>
		</div><br>
        <div class="fff" style="height:auto; width:700px"> 
            <?php            
                $link=mysqli_connect("127.0.0.1","root","123456","ISAD_database");
                if(!$link){
                    die("数据库连接错误：".mysqli_connect_error());
                }
				
				// 获取用户名
				$user_name=htmlspecialchars($_POST['user_name']);

				$order_attr=htmlspecialchars($_POST['order_attr']);
				$select_cotent=htmlspecialchars($_POST['select_content']);

				if ($order_attr=="default"){
					$sql = "SELECT order_id, order_type, order_content, order_fee, order_state, order_time FROM i_order WHERE i_order.user_name= '$user_name'";	
				}elseif ($order_attr=="order_content"){
					$sql = "SELECT order_id, order_type, order_content, order_fee, order_state, order_time FROM i_order WHERE i_order.user_name= '$user_name' and order_content like '%$select_cotent%'";
				}elseif ($order_attr=="order_id"){
					$sql = "SELECT order_id, order_type, order_content, order_fee, order_state, order_time FROM i_order WHERE i_order.user_name= '$user_name' and order_id = '$select_cotent'";
				}elseif ($order_attr=="order_type"){
					$sql = "SELECT order_id, order_type, order_content, order_fee, order_state, order_time FROM i_order WHERE i_order.user_name= '$user_name' and order_type = '$select_cotent'";
				}

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
                mysqli_close($link); 
                echo "<br><br>";
            ?>
        </div><br>
        <div class="footer">
			  <h5>页面内容仅用于作业</h5>
		</div>
    </body>
</html>