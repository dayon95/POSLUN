<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
</head>
<body id="target">
	<header>
		<img src="http://cfile23.uf.tistory.com/image/2678EF33578DF4E514B7FA">
		<h1><a href="http://localhost/exindex.html">Javascript</a></h1>
		<link rel="stylesheet" type="text/css" href="http://localhost/style.css">
	</header>
	<nav>
		<ol>
			<?php
				echo file_get_contents("list.txt");
			 ?>
		</ol>
	</nav>
	<div id="control">
		<input type="button" value="white" onclick="document.getElementById('target').className='white'"/>
		<input type="button" value="black" onclick="document.getElementById('target').className='black'"/>
	</div>
	<article>
		<?php
			if(empty($_GET['id'])==false){
				echo file_get_contents($_GET['id'].".txt");
			}

		 ?>
	</article>
</body>
</html>
