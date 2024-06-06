import logging
import os
import click
import upload, download, new, check_links


@click.group()
def main():
    """
    Wordpress CLI
    """
    logging.basicConfig(
        level=os.getenv("LOG_LEVEL", "INFO"), format="%(levelname)s: %(message)s"
    )


@main.group()
def posts():
    """
    Wordpress posts up- and download
    """


posts.add_command(upload.command)
posts.add_command(download.command)
posts.add_command(new.command)
posts.add_command(new.update_banner_command)
posts.add_command(check_links.command)


if __name__ == "__main__":
    main()
