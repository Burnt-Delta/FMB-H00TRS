<!DOCTYPE html>
<html>
<body>
    <?php
        # Parse JSON
        $jsonstring = file_get_contents("../../json/config.json");
        $json = json_decode($jsonstring);

        # Populate auth variables
        $uname = $json->webauth->Username;
        $pword = $json->webauth->Password;

        # Parse POST
        # auth
        if (($_POST['uname'] == $uname) && ($_POST['pword'] == $pword))
            print "Success!";
            # TODO: alter config
        else
            print "Failure.";

    ?>
</body>
</html>