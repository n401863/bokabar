<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $naam = htmlspecialchars($_POST['naam']);
    $email = htmlspecialchars($_POST['email']);
    $bericht = htmlspecialchars($_POST['bericht']);

    $to = 'n401863@gymnasiumnovum.nl';
    $subject = 'Nieuw Registratieformulier Inzending';
    $message = "Naam: $naam\nE-mail: $email\nBericht: $bericht";
    $headers = "From: $email";

    if (mail($to, $subject, $message, $headers)) {
        // Redirect naar Google na succesvolle verzending
        header("Location: https://www.google.com");
        exit();
    } else {
        echo "Er is een fout opgetreden bij het verzenden van de e-mail.";
    }
} else {
    echo "Ongeldige aanvraagmethode.";
}
?>