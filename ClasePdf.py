import os
import jinja2
import pdfkit

class Pdf():
    def __init__(self, template_path, css_path):
        self.template_path = template_path
        self.css_path = css_path
        self.template_loader = jinja2.FileSystemLoader(searchpath=os.path.dirname(template_path))
        self.template_env = jinja2.Environment(loader=self.template_loader)

    def render_pdf(self, output_path, contexto):
        template = self.template_env.get_template(os.path.basename(self.template_path))
        html_content = template.render(contexto)
        config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')
        options = {
            'enable-local-file-access': ''
        }
        pdfkit.from_string(html_content, output_path, css=self.css_path, configuration=config, options=options)


