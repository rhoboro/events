import click


@click.group()  # cliという名前のグループを作る
def cli():
    pass


@cli.command()  # cliにコマンドnoonを追加
def noon():
    print('Hello')


@cli.command()  # cliにコマンドmorningを追加
def morning():
    print('Good morning')


if __name__ == '__main__':
    cli()
