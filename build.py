from jinja2 import Environment, FileSystemLoader
import json
import subprocess

DATA_FILE = "data.json"
TEMPLATE_FILE = "template.tex.j2"
OUTPUT_FILE = "output.tex"


def load_data():
    with open(DATA_FILE) as f:
        data = json.load(f)

    return {"personal": data.get("personal", {})}


def render_template(context):
    env = Environment(loader=FileSystemLoader("."))

    template = env.get_template(TEMPLATE_FILE)
    rendered_content = template.render(context)

    with open(OUTPUT_FILE, "w") as f:
        f.write(rendered_content)


def compile_latex():
    subprocess.run(["pdflatex", OUTPUT_FILE])


if __name__ == "__main__":
    context = load_data()
    render_template(context)
    compile_latex()
