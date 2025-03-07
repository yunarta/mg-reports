import os
from jinja2 import Environment, FileSystemLoader

def render_templates(kwargs):
    directory = os.getcwd()
    env = Environment(loader=FileSystemLoader(directory))
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.j2'):
                template_path = os.path.join(root, file)
                template = env.get_template(os.path.relpath(template_path, directory))
                rendered_content = template.render(kwargs)

                output_path = os.path.join(root, file[:-3])
                with open(output_path, 'w') as output_file:
                    output_file.write(rendered_content)
