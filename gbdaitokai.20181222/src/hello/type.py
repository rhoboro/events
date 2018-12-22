import click


@click.command()
@click.option('--count', '-c', type=click.INT, help='repeat')
@click.option('--name', '-n', help='your name')
def cli(name, count):
    for i in range(count):
        click.echo(f'Hello {name}!')


if __name__ == '__main__':
    cli()
