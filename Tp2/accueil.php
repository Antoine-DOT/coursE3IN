<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Page d'accueil</title>
  <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
  <h1>Page d'accueil</h1>
  <div class="list">
    <!-- Affichage de la liste des comptes -->
    <?php
    session_start();

    if (!isset($_SESSION['login'])) {
      header('Location: index.php');
      exit;
    }

    $bdd = new PDO('mysql:host=localhost;dbname=compte;charset=utf8', 'root', '');
    $reponse = $bdd->query('SELECT * FROM db');

    while ($donnees = $reponse->fetch()) {
      echo '<div class="account">';
      echo $donnees['login'];
      echo '</div>';
    }
    ?>
  </div>
  <p style="text-align: center; margin-top: 50px;">Bonjour <?php echo $_SESSION['login']; ?>, vous êtes connecté! Voulez-vous vous deconnecter
  ?  Cliquez sur l'orange.<a href="index.php">
  <br>   
  <div class="fruit">
  <img src="orange.jpg" alt="Fruit" style="width: 250px; height: 200px;">
</div>
<script>
    const fruit = document.querySelector('.fruit');

fruit.addEventListener('mouseover', function() {
  fruit.classList.add('rotate');
});

fruit.addEventListener('mouseout', function() {
  fruit.classList.remove('rotate');
});
  </script>
</body>
</html>