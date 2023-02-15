<?php
session_start();
require_once 'compte.php';
require_once 'compteDAO.php';

if (isset($_POST['login']) && isset($_POST['pw'])) {
  $login = $_POST['login'];
  $pw = $_POST['pw'];

  $compte = new Compte($login, $pw);
  $compteDAO = new CompteDAO($compte);

  if ($compteDAO->verifCompte()) {
    $_SESSION['login'] = $login;
    header('Location: accueil.php');
  } else {
    header('Location: index.php');
  }

  // Ajouter un nouveau compte dans la base de données
  $compteDAO->ajouterCompte($login, $pw);
} else {
  header('Location: index.php');
}
?>
