"""
Author: AlwaysStudent
PythonVersion: 3.7
"""
import markdown2 as md
import codecs


def main():
    with codecs.open("1.md", mode='r', encoding='utf-8') as mdfile:
        md_text = mdfile.read()
    with codecs.open("./katex/Katex.min.css", mode='r', encoding='utf-8') as cssfile:
        css_text = cssfile.read()
    extras = ['code-friendly', 'fenced-code-blocks', 'footnotes']
    html_text = md.markdown(md_text, extras=extras)
    html_name = "1.html"
    with codecs.open(html_name, mode='w', encoding='utf-8') as output_file:
        output_file.write(css_text + html_text)


if __name__ == '__main__':
    main()
