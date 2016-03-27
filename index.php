<style type="text/css">

.search-box {
                padding-left: 20%;
                padding-top: 5%;

}
.search-results {
                padding-left: 20%;
                padding-top: 2%;

}
.search-link {
        margin-bottom: 10px;
}

.search-link a:link { color: #FFFFFF; text-decoration: none; font-size: 20px;}
.search-link a:visited { color: #FFFFFF; text-decoration: none; font-size: 20px;}
.search-link a:hover { color: #0000CC; text-decoration: none; font-size: 20px;}
.search-link a:active { color: #FFFFFF; text-decoration: none; font-size: 20px;}

.search {
                padding:8px 15px;
                border:1px solid #dbdbdb;
                width:600px;
                height: 50px;
                font-size: 20px;
}
.button {
                position:relative;
                font-size: 100%;
                top:-1px;
                left:-4px;
                border:2px solid #207cca;       
                background-color:#207cca;
                color:#fafafa;
                width:100px;
                height: 50px;
}

</style>


</style>
<body bgcolor=#1762a1>
<div class="search-box">
<form method="post" action="">
        <input class="search" type="text" name="search-text" placeholder="Search..." required>
        <input class="button" type="submit" name="submit" value="Search">
</form>
</div>

<?php
        if( isset($_POST['submit'])) {

                $text  = $_POST['search-text'];
                
                $links = array("http://google.com","http://facebook.com");
                $arrlen = count($links);

                echo "<div class='search-results'>";

                for ($i=0; $i < $arrlen; $i++) {

                        $link = $links[$i];

                        echo "<div class='search-link'>";
                        echo "<a href=".$link.">".$link."</a><br></div>";
                }

                echo "</div>";
        }
?>


</body>