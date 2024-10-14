<?php
$naam = $_POST['naam'];
$email = $_POST['email'];
$telefoonnummer = $_POST['telefoonnummer'];
$datum = $_POST['datum'];
$tijd = $_POST['tijd'];
$aantal_personen = $_POST['aantal_personen'];

$onderwerp = "Nieuwe reservering";
$bericht = "Er is een nieuwe reservering gemaakt door $naam.\n\n";
$bericht .= "Details:\n";
$bericht .= "Naam: $naam\n";
$bericht .= "E-mail: $email\n";
$bericht .= "Telefoonnummer: $telefoonnummer\n";
$bericht .= "Datum: $datum\n";
$bericht .= "Tijd: $tijd\n";
$bericht .= "Aantal personen: $aantal_personen\n";

mail("n401863@gymnasiumnovum.nl", $onderwerp, $bericht);

echo "Reservering succesvol verstuurd!";
?>