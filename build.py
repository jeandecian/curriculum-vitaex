from jinja2 import Environment, FileSystemLoader
import subprocess

TEMPLATE_FILE = "template.tex.j2"
OUTPUT_FILE = "output.tex"


def render_template():
    env = Environment(loader=FileSystemLoader("."))

    template = env.get_template(TEMPLATE_FILE)
    rendered_content = template.render()

    with open(OUTPUT_FILE, "w") as f:
        f.write(rendered_content)


def compile_latex():
    subprocess.run(["pdflatex", OUTPUT_FILE])


if __name__ == "__main__":
    render_template()
    compile_latex()
