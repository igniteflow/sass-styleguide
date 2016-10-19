from jinja2 import Template


text = '''
$font-stack:    Helvetica, sans-serif;
$primary-color: #333;
$rgb-color: rgb(255,0,0);
$rgba-color: rgba(255, 0, 0, 0.5);
$hsl-color: hsl(0, 100%, 50%);
$hsla-color: hsla(0, 100%, 50%, 0.5);

body {
  font: 100% $font-stack;
  color: $primary-color;
}
'''
COLOUR_NAMES = [
    # CSS Level 1 colors
    'white', 'black', 'silver', 'gray', 'red', 'maroon', 'yellow', 'olive',
    'lime', 'green', 'aqua', 'teal', 'blue', 'navy', 'fuschia', 'purple',

    # The only color added in CSS Level 2 (Revision 1)
    'orange',

    # TODO: add CSS Level 3 colors, sometimes called a SVG or X11 color
]


def get_variables(text):
    variables = {}
    for line in text.split('\n'):
        if ':' not in line or ';' not in line:
            continue

        attr, value = line.split(':')
        attr = attr.strip()
        value = value.strip()

        if attr.startswith('$'):
            variables[attr.replace('$', '')] = value.replace(';', '')
    return variables


def is_color(value):
    def _startswith_one_of(v, l):
        for item in l:
            if v.startswith(item):
                return True
        return False

    return (
        _startswith_one_of(value, ['#', 'rgb', 'rgba', 'hsl', 'hsla']) or
        value in COLOUR_NAMES
    )


def render_html(variables):
    # filter out non-colors
    colours = variables.copy()
    for k, v in variables.iteritems():
        if not is_color(v):
            del colours[k]

    with open('templates/index.html') as f:
        template = Template(f.read())
        return template.render(variables=colours)


variables = get_variables(text)
with open('index.html', 'w+') as f:
    f.write(render_html(variables))
