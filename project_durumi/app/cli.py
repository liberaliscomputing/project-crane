import click

CONTEXT_SETTINGS = {"help_option_names": ["-h", "--help"]}


@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option()
def cli():
    pass


def common_args_options(func):
    """
    Common click args and options
    """
    func = click.argument("video_id", required=True, type=str)(func)

    return func


@click.command()
@common_args_options
def textify(video_id):
    """
    Ingest a Kids First study(ies) into a FHIR server.
    \b
    Arguments:
        \b
        VIDEO_ID - a YouTube video ID https://www.youtube.com/watch?v=<VIDEO_ID>
    """
    print(video_id)


@click.command()
@common_args_options
def publish(video_id):
    """
    Ingest a Kids First study(ies) into a FHIR server.
    \b
    Arguments:
        \b
        VIDEO_ID - a YouTube video ID https://www.youtube.com/watch?v=<VIDEO_ID>
    """
    print(video_id)


cli.add_command(textify)
cli.add_command(publish)
