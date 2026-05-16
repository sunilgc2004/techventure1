from flask import Flask, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tech Venture</title>

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: Arial, sans-serif;
        }

        body {
            background: black;
            color: white;
            overflow-x: hidden;
        }

        .background {
            position: fixed;
            width: 100%;
            height: 100%;
            background:
                radial-gradient(circle at top left, rgba(128,0,255,0.3), transparent 30%),
                radial-gradient(circle at bottom right, rgba(0,128,255,0.3), transparent 30%);
            z-index: -1;
            animation: pulse 6s infinite alternate;
        }

        @keyframes pulse {
            from {
                transform: scale(1);
            }
            to {
                transform: scale(1.1);
            }
        }

        nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px 50px;
            backdrop-filter: blur(10px);
            border-bottom: 1px solid rgba(255,255,255,0.1);
            position: sticky;
            top: 0;
        }

        nav h1 {
            color: #b266ff;
            font-size: 30px;
        }

        nav ul {
            display: flex;
            gap: 30px;
            list-style: none;
        }

        nav a {
            text-decoration: none;
            color: white;
            transition: 0.3s;
        }

        nav a:hover {
            color: #b266ff;
        }

        .hero {
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            flex-direction: column;
            padding: 40px;
            animation: fadeIn 1.5s ease;
        }

        .hero h2 {
            font-size: 70px;
            max-width: 1000px;
            background: linear-gradient(to right, white, #b266ff, #4da6ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 20px;
        }

        .hero p {
            font-size: 22px;
            color: #cccccc;
            max-width: 800px;
            line-height: 1.6;
        }

        .buttons {
            margin-top: 40px;
            display: flex;
            gap: 20px;
            flex-wrap: wrap;
            justify-content: center;
        }

        .btn {
            padding: 15px 30px;
            border-radius: 15px;
            border: none;
            cursor: pointer;
            font-size: 18px;
            transition: 0.3s;
        }

        .primary {
            background: #7a00ff;
            color: white;
        }

        .primary:hover {
            background: #5c00c7;
            transform: translateY(-5px);
        }

        .secondary {
            background: transparent;
            border: 1px solid #666;
            color: white;
        }

        .secondary:hover {
            border-color: #b266ff;
            transform: translateY(-5px);
        }

        .section {
            padding: 100px 50px;
            text-align: center;
        }

        .section h3 {
            font-size: 50px;
            margin-bottom: 20px;
            color: #b266ff;
        }

        .cards {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 30px;
            margin-top: 50px;
        }

        .card {
            background: rgba(255,255,255,0.05);
            padding: 30px;
            border-radius: 20px;
            border: 1px solid rgba(255,255,255,0.1);
            transition: 0.4s;
            backdrop-filter: blur(10px);
        }

        .card:hover {
            transform: translateY(-10px) scale(1.03);
            border-color: #b266ff;
            box-shadow: 0 0 25px rgba(178,102,255,0.3);
        }

        .card h4 {
            font-size: 28px;
            margin-bottom: 15px;
            color: #b266ff;
        }

        footer {
            text-align: center;
            padding: 30px;
            border-top: 1px solid rgba(255,255,255,0.1);
            color: #999;
        }

        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
    </style>
</head>
<body>

    <div class="background"></div>

    <nav>
        <h1>Tech Venture</h1>

        <ul>
            <li><a href="#about">About</a></li>
            <li><a href="#services">Services</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </nav>

    <section class="hero">
        <h2>Turning innovative ideas into real-world software products.</h2>

        <p>
            We help students, startups, and businesses build scalable software
            solutions using AI, automation, and modern technologies.
        </p>

        <div class="buttons">
            <button class="btn primary">Start Project</button>
            <button class="btn secondary">View Portfolio</button>
        </div>
    </section>

    <section class="section" id="about">
        <h3>About Us</h3>

        <p>
            Tech Venture is a modern startup focused on delivering innovative
            software solutions for startups, businesses, and students.
        </p>
    </section>

    <section class="section" id="services">
        <h3>Our Services</h3>

        <div class="cards">
            <div class="card">
                <h4>Web Development</h4>
                <p>Modern responsive websites and scalable applications.</p>
            </div>

            <div class="card">
                <h4>AI Solutions</h4>
                <p>Smart AI integrations and automation systems.</p>
            </div>

            <div class="card">
                <h4>Automation Testing</h4>
                <p>Reliable testing and QA automation solutions.</p>
            </div>

            <div class="card">
                <h4>Student Projects</h4>
                <p>Real-time academic and innovative software projects.</p>
            </div>
        </div>
    </section>

    <section class="section" id="contact">
        <h3>Contact</h3>

        <p>Email: hello@techventure.com</p>
        <p>Instagram: @techventure</p>
        <p>LinkedIn: Tech Venture</p>
    </section>

    <footer>
        © 2026 Tech Venture. All rights reserved.
    </footer>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True)
