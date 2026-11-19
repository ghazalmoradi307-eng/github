import webbrowser

html_code = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Me</title>
</head>

<body>

    <h1>Contact Me</h1>

    <marquee>
        Let's keep in touch! Send me your messages!
    </marquee>

    <h2>How to Contact</h2>

    <p>
        You can contact me by sending an email to
        <a href="mailto:your-email@example.com">
        your-email@example.com</a>
    </p>

    <p>
        Feel free to reach out anytime.
        I'm always happy to hear from visitors to my site!
    </p>

    <h3>Navigation</h3>

    <ul>
        <li><a href="index.html">Home</a></li>
        <li><a href="contact.html">Contact Me</a></li>
    </ul>

</body>
</html>
"""

with open("contact.html", "w", encoding="utf-8") as file:
    file.write(html_code)

webbrowser.open("contact.html")
