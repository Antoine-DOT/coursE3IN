<?php
require_once 'compte.php';
require_once 'compteDAO.php';

$login = $_POST['login'];
$pw = $_POST['pw'];

$compte = new Compte($login, $pw);
$compteDAO = new CompteDAO($compte);

if ($compteDAO->creerCompte()) {
  echo "Compte créé avec succès.";
} else {
  echo "Impossible de créer le compte. Le nom d'utilisateur est déjà utilisé.";
}
?>
