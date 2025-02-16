GetChannelSubtitle
===================

The `GetChannelSubtitle` class is designed to retrieve subtitles from all videos in a YouTube channel. This functionality supports filtering videos by various criteria such as content type and popularity. Additionally, you can get subtitles in your desired language and save them to disk for offline usage.

Class Usage
-----------

.. code-block:: python

    from ytkit import GetChannelSubtitle

    # Example usage
    get_channel_subtlte = GetChannelSubtitle()
    result = get_channel_subtlte.get(
        channel_username="TEDx",
        sort_by="popular",
        limit=2,
        save_to_disk="channel_data",
        language="en"
    )

Method Details
--------------

.. py:method:: get(channel_id=None, channel_url=None, channel_username=None, limit=None, sleep=1, sort_by="newest", content_type="videos", video_ids, language="en", save_to_disk=None)
    :param channel_id: (Optional) The unique ID of the YouTube channel.
    :type channel_id: str
    :param channel_url: (Optional) The URL of the YouTube channel.
    :type channel_url: str
    :param channel_username: (Optional) The username of the YouTube channel.
    :type channel_username: str
    :param limit: (Optional) Maximum number of videos to process.
    :type limit: int
    :param sleep: Time to wait (in seconds) between API calls. Defaults to 1 second and must be non-negative.
    :type sleep: float
    :param sort_by: Criterion for sorting videos. Acceptable values are ``"newest"``, ``"oldest"``, or ``"popular"``. Defaults to ``"newest"``.
    :type sort_by: str
    :param content_type: Type of content to include. Acceptable values are ``"videos"``, ``"shorts"``, or ``"streams"``. Defaults to ``"videos"``.
    :type content_type: str
    :param video_ids: List of YouTube video IDs for which subtitles need to be fetched.
    :type video_ids: list[str]
    :param language: Desired language code for subtitles. Defaults to ``"en"``.
    :type language: str
    :param save_to_disk: Path to the folder where transcript files will be saved. If ``None``, files are not saved to disk.
    :type save_to_disk: str or None
    :return: The fetched subtitles and metadata for the specified videos.
    :rtype: dict

Input Parameters
-----------------

- **channel_id** *(Optional[str])*: The unique ID of the YouTube channel.
- **channel_url** *(Optional[str])*: The URL of the YouTube channel.
- **channel_username** *(Optional[str])*: The username of the YouTube channel.
- **limit** *(Optional[int])*: Maximum number of videos to process.
- **sleep** *(float)*: Time to wait between API calls. Defaults to 1 second and must be non-negative.
- **sort_by** *(Literal["newest", "oldest", "popular"])*: Criterion for sorting videos. Defaults to ``"newest"``.
- **content_type** *(Literal["videos", "shorts", "streams"])*: Type of content to include. Defaults to ``"videos"``.
- **language** *(str)*: Desired language code for subtitles. Defaults to ``"en"``.
- **save_to_disk** *(Union[None, str])*: Folder path where transcript files will be saved. If ``None``, files are not saved to disk.

Examples
--------

Fetching subtitles for the most popular videos of the TEDx channel:

.. code-block:: python

    get_channel_subtlte = GetChannelSubtitle()
    result = get_channel_subtlte.get(
        channel_username="TEDx",
        sort_by="popular",
        limit=2,
        save_to_disk="channel_data",
        language="en"
    )

    print(result)

Notes
-----

- Either `channel_id`, `channel_url`, or `channel_username` must be provided.
- If `save_to_disk` is specified, ensure the folder exists or provide a valid path.
- Use the `language` parameter to specify the desired subtitle language.
