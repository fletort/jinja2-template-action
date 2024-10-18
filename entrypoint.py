import os
import click
from action.main import Main

@click.command()
#@click.option('--variables', help='Variables', default=None)
@click.option('--keep_template', is_flag=True)
def main(keep_template):
    print(os.environ.get('GITHUB', ''))
    main = Main(keep_template=keep_template)
    variables = os.environ.get('INPUT_VARIABLES', '')
    if variables:
        main.addVariables(variables)
    main.renderAll()

if __name__ == '__main__':
    main()