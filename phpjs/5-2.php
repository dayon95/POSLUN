<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
</head>
<body>
  <?php
    $passwd = $_GET["pawd"];
    if($passwd=="1111"){
      echo "Welcome, Let's PLAY";
    }else{
      echo "Who are you?";
    }
  ?>
</body>
</html>
