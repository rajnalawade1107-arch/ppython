from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return '''
<!DOCTYPE html>
<html>
<head>
<title>Gym World</title>
<style>
body {
  margin: 0;
  font-family: Arial, sans-serif;
  background: #f4f4f4;
  color: #333;
}
header {
  background: #222;
  color: white;
  text-align: center;
  padding: 25px;
}
nav {
  background: #444;
  padding: 12px;
  text-align: center;
}
nav a {
  color: white;
  text-decoration: none;
  margin: 15px;
}
section {
  padding: 25px;
  margin: 20px;
  background: white;
  border-radius: 10px;
}
h2 {
  color: #e63946;
}
footer {
  background: #222;
  color: white;
  text-align: center;
  padding: 15px;
}
</style>
</head>

<body>

<header>
  <h1>Welcome to Gym World</h1>
  <p>Build Strength, Stay Fit, Live Healthy</p>
</header>

<nav>
  <a href="#about">About</a>
  <a href="#benefits">Benefits</a>
  <a href="#training">Training</a>
  <a href="#exercises">Exercises</a>
</nav>

<section id="about">
  <h2>About Gym</h2>
  <p>
    Gym is a place where people exercise to improve their physical fitness,
    strength, health and overall body performance. Regular workouts help
    maintain a healthy lifestyle.
  </p>
</section>

<section id="benefits">
  <h2>Benefits of Gym</h2>
  <ul>
    <li>Builds muscle strength</li>
    <li>Improves stamina and endurance</li>
    <li>Helps maintain body weight</li>
    <li>Improves heart health</li>
    <li>Boosts confidence and energy</li>
  </ul>
</section>

<section id="training">
  <h2>Types of Training</h2>
  <ul>
    <li>Weight Training – Builds muscles and strength</li>
    <li>Cardio – Improves heart and lung health</li>
    <li>Strength Training – Increases physical power</li>
    <li>Flexibility Training – Improves mobility</li>
  </ul>
</section>

<section id="exercises">
  <h2>Basic Gym Exercises</h2>

  <h3>Push-ups</h3>
  <p>Strengthens the chest, shoulders and triceps.</p>

  <h3>Squats</h3>
  <p>Builds strength in legs and glute muscles.</p>

  <h3>Pull-ups</h3>
  <p>Improves back and arm strength.</p>

  <h3>Bench Press</h3>
  <p>A popular exercise for developing chest muscles.</p>

  <h3>Dumbbell Curls</h3>
  <p>Helps strengthen and develop biceps muscles.</p>
</section>

<footer>
  <p>Gym World | Strong Body, Strong Mind</p>
</footer>

</body>
</html>
'''

@app.route('/health')
def health():
    return jsonify(status="ok")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)