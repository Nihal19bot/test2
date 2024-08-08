<?php
include 'db.php';

$email = $_POST['email'];
$password = $_POST['password'];

$sql = "SELECT * FROM users WHERE email='$email' AND password='$password'";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    echo "Login successful!";
    echo "<script>setLoginStatus(true);</script>";
} else {
    echo "Invalid email or password";
}

$conn->close();
?>
