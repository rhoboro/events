import click

@click.command()
@click.option('--name',
              default='rhoboro',  # デフォルト値を指定
              show_default=True,  # ヘルプでデフォルト値を表示
              help='your name')
def cli(name):
    click.echo(f'Hello {name}!')

if __name__ == '__main__':
    cli()
