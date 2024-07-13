import markdown


def convert_markdown_file_to_html(input_file, output_file):
    try:
        # Lese den Inhalt der Markdown-Datei
        with open(input_file, 'r', encoding='utf-8') as file:
            markdown_text = file.read()

        # Konvertiere das Markdown in HTML
        html_body = markdown.markdown(markdown_text)

        # HTML-Vorlage mit erweitertem Styling
        html_template = f"""
        <!DOCTYPE html>
        <html lang="de">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>EURO 2024 // Tagebuch </title>
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
                body {{
                    font-family: 'Roboto', sans-serif;
                    background-color: #f4f4f4;
                    color: #333;
                    margin: 0;
                    padding: 0;
                }}
                .container {{
                    width: 80%;
                    max-width: 800px;
                    margin: 50px auto;
                    background: #fff;
                    padding: 20px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    border-radius: 8px;
                }}
                h1, h2, h3, h4, h5, h6 {{
                    font-weight: 700;
                    color: #444;
                }}
                p {{
                    line-height: 1.8;
                    margin: 10px 0;
                }}
                a {{
                    color: #3498db;
                    text-decoration: none;
                }}
                a:hover {{
                    text-decoration: underline;
                }}
                ul {{
                    padding-left: 20px;
                }}
                blockquote {{
                    border-left: 4px solid #3498db;
                    padding-left: 10px;
                    color: #555;
                    margin: 20px 0;
                    font-style: italic;
                }}
                pre {{
                    background: #f4f4f4;
                    padding: 10px;
                    border-radius: 4px;
                    overflow-x: auto;
                }}
                code {{
                    background: #f4f4f4;
                    padding: 2px 4px;
                    border-radius: 4px;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                {html_body}
            </div>
        </body>
        </html>
        """

        # Schreibe das HTML in die Ausgabedatei
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(html_template)

        print(f"Die Datei {input_file} wurde erfolgreich in {output_file} konvertiert.")

    except FileNotFoundError:
        print(f"Die Datei {input_file} wurde nicht gefunden.")
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")


if __name__ == "__main__":
    input_file = "README.md"
    output_file = "index.html"

    convert_markdown_file_to_html(input_file, output_file)
