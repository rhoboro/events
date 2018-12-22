import click


@click.command()
@click.option('--name', '-n',  # -nでも指定できるようにする
              required=True,  # 必須オプションに指定
              help='your name')
def cli(name):
    click.echo(f'Hello {name}!')


if __name__ == '__main__':
    cli()
