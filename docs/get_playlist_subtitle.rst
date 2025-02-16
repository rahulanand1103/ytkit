GetPlaylistSubtitle
===================

The `GetPlaylistSubtitle` class is designed to retrieve subtitles for all videos in a YouTube playlist. It supports filtering by various criteria, such as language and video count. The subtitles can also be saved to disk for offline usage.

Class Usage
-----------

.. code-block:: python

    from ytkit import GetPlaylistSubtitle

    # Example usage
    get_playlist_subtitle = GetPlaylistSubtitle()
    result = get_playlist_subtitle.get(
        playlist_id="PL8dPuuaLjXtNamNKW5qlS-nKgA0on7Qze",
        limit=2,
        save_to_disk="data",
        language="en"
    )

Method Details
--------------

.. py:method:: get(playlist_id, limit=None, sleep=1, video_ids=None, language="en", save_to_disk=None)
    :param playlist_id: The unique ID of the YouTube playlist.
    :type playlist_id: str
    :param limit: (Optional) Maximum number of videos to fetch.
    :type limit: int
    :param sleep: Time to wait (in seconds) between API calls. Defaults to 1 second and must be non-negative.
    :type sleep: float
    :param language: Desired language code for subtitles. Defaults to ``"en"``.
    :type language: str
    :param save_to_disk: Path to the folder where transcript files will be saved. If ``None``, files are not saved to disk.
    :type save_to_disk: str or None
    :return: The fetched subtitles and metadata for the specified videos.
    :rtype: list[dict] or str

Input Parameters
-----------------

- **playlist_id** *(str)*: The unique ID of the YouTube playlist.
- **limit** *(Optional[int])*: Maximum number of videos to fetch.
- **sleep** *(float)*: Time to wait between API calls. Defaults to 1 second and must be non-negative.
- **language** *(str)*: Desired language code for subtitles. Defaults to ``"en"``.
- **save_to_disk** *(Union[None, str])*: Folder path where transcript files will be saved. If ``None``, files are not saved to disk.

Examples
--------

Fetching subtitles for the first two videos in a playlist:

.. code-block:: python

    get_playlist_subtitle = GetPlaylistSubtitle()
    result = get_playlist_subtitle.get(
        playlist_id="PL8dPuuaLjXtNamNKW5qlS-nKgA0on7Qze",
        limit=2,
        save_to_disk="data",
        language="en"
    )

    print(result)

Notes
-----

- The `playlist_id` is required to identify the playlist.
- If `save_to_disk` is specified, ensure the folder exists or provide a valid path.
- Use the `language` parameter to specify the desired subtitle language.