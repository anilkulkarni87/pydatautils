"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """PyDataUtils."""


if __name__ == "__main__":
    main(prog_name="pydatautils")  # pragma: no cover
