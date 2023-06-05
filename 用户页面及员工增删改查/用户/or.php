<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>预约申请信息</title>
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
			<h2>ISAD维修保养在线预约</h2>
			<p></p>
		</div>
		<div class="navbar">
			<a href="http://127.0.0.1:8000/">售后首页</a>
			<a href="/wxby/history_order">历史订单</a>
			<a href="/wxby/by_plan">保养规划</a>
			<a href="/cdgh/cdgh">充电规划</a>
			<a href="/kf/kf_index" class="right">在线客服</a>
		</div>
        <div class="emphasize" style="height:100px">
			<h3>请您核对预约申请信息</h3>
		</div>
        <div class="fff" style="height:auto; width:700px"> 
            <?php            
                $link=mysqli_connect("127.0.0.1","root","123456","ISAD_database");
                if(!$link){
                    die("数据库连接错误：".mysqli_connect_error());
                }
                // else{
                //     echo"Connection Success<br>";
                // }

                // 生成订单号
                $count_sql = mysqli_query($link, "SELECT COUNT(*) as count from apply");
                $row = mysqli_fetch_assoc($count_sql);
                $count = $row['count'];
                $apply_id = 1000001+ $count;

                // 获取用户填写内容
                $apply_type=htmlspecialchars($_POST['apply_type']);
                $apply_content=htmlspecialchars($_POST['apply_content']);
                
                // 获取用户名称
                $user_name=htmlspecialchars($_POST['user_name']);

                // 获取申请时间
                $apply_time=date('Y-m-d H:i:s');

                echo"申请单号:";
                echo $apply_id;
                echo"<br><br>用户名:";
                echo $user_name;
                echo"<br><br>用户申请类型:";
                echo $apply_type;
                echo("<br><br>用户具体需求:<br>");
                echo $apply_content;
                echo("<br><br>用户申请时间:");
                echo $apply_time;
                
                // echo("<br>INSERT INTO apply(apply_id,user_name,apply_type,apply_content,apply_time) VALUES('$apply_id','$user_name','$apply_type','$apply_content','$apply_time');");

                $sql=mysqli_query($link,"INSERT INTO apply(apply_id,user_name,apply_type,apply_content,apply_time) VALUES('$apply_id','$user_name','$apply_type','$apply_content','$apply_time');");
                if($sql){
                    echo("<br><br><br>我们已收到您的申请, 我们的工作人员会在工作时间通过电话尽快与您确认相关细节, 麻烦您注意接听。");      
                }
                else{
                    echo("<br><br><br>提交申请失败, 请您重新提交一遍预约申请。");
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