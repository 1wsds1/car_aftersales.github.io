<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>ISAD-预约信息查看</title>
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
			<h2>ISAD预约信息查看</h2>
			<p></p>
		</div>
		<div class="navbar">
        	<a href="http://127.0.0.1:8000/Django/System/wxby/templates/order_upload.php">订单提交</a>
            <a href="http://127.0.0.1:8000/Django/System/wxby/templates/status_update.php">订单状态更新</a>
			<a href="#">维修日志填写</a>
            <a href="#">维修日志查看</a>
			<a href="#">质检报告提交</a>
            <a href="#">质检报告查看</a>
			<a href="#" class="right">在线客服</a>
		</div><br>
        <div class="fff" style="height:auto; width:700px"> 
        <?php
                error_reporting(0);  
                $link=mysqli_connect("127.0.0.1","root","123456","ISAD_database");
                if(!$link){
                    die("数据库连接错误：".mysqli_connect_error());
                }

                $sql="SELECT * FROM apply";
                $result = mysqli_query($link, $sql);
                if (mysqli_num_rows($result) >0) {
                // 输出数据
                while($row = mysqli_fetch_assoc($result)) {
                    echo "<br>申请单号: " . $row["apply_id"];
                    echo "<br>用户名: " . $row["user_name"];
                    echo "<br>用户申请类型: " . $row["apply_type"];
                    echo "<br>用户具体需求:<br> " . $row["apply_content"];
                    echo "<br>用户申请时间: " . $row["apply_time"];
                    echo "<br><br>";
                    }
                    } else {
                        echo "<br><br>暂无用户需求";
                    }
                     mysqli_close($link); 
            ?>
        </div><br>
        <div class="footer">
			  <h5>页面内容仅用于作业</h5>
		</div>
    </body>
</html>