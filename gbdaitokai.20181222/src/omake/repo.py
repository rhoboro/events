import click
import requests

URL = 'https://api.github.com/search/repositories?q={}'


@click.group()
def cli():
    pass


@cli.command(name='list')
@click.option('--query', '-q', required=True, help='search word')
def search(query):
    res = requests.get(URL.format(query))
    full_names = [item['full_name'] for item in res.json()['items']]
    click.echo('\n'.join(full_names))


@cli.command()
@click.option('--num', '-n', default=0, help='item number')
@click.option('--query', '-q', required=True, help='search word')
def show(query, num):
    res = requests.get(URL.format(query))
    item = [item for item in res.json()['items']][num]
    click.echo(item['full_name'])
    if click.confirm('more detail?'):
        click.echo(item)


if __name__ == '__main__':
    cli()
