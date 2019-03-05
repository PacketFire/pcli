import click

@click.group()
def cli():
    pass


@click.command()
@click.option('--lang', default='none', help='language type')
def paste(lang):
    click.echo(lang)


if __name__ == '__main__':
    cli.add_command(paste)
    cli()