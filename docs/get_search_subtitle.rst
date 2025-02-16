GetSearchSubtitle
==================

The `GetSearchSubtitle` class is designed to retrieve subtitles for YouTube videos based on a search query. It supports filtering by various criteria, such as language and video count. The subtitles can also be saved to disk for offline usage.

Class Usage
-----------

.. code-block:: python

    from ytkit import GetSearchSubtitle

    # Example usage
    get_search_subtitle = GetSearchSubtitle()
    result = get_search_subtitle.get(
        query="python tutorial",
        limit=2,
        save_to_disk="test",
        language="en"
    )

Method Details
--------------

.. py:method:: get(query, limit=None, sleep=1, language="en", save_to_disk=None, **kwargs)
    :param query: The search query to find relevant videos on YouTube.
    :type query: str
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

- **query** *(str)*: The search query to find relevant YouTube videos.
- **limit** *(Optional[int])*: Maximum number of videos to fetch.
- **sleep** *(float)*: Time to wait between API calls. Defaults to 1 second and must be non-negative.
- **language** *(str)*: Desired language code for subtitles. Defaults to ``"en"``.
- **save_to_disk** *(Union[None, str])*: Folder path where transcript files will be saved. If ``None``, files are not saved to disk.

Examples
--------

Fetching subtitles for videos related to "python tutorial":

.. code-block:: python

    get_search_subtitle = GetSearchSubtitle()
    result = get_search_subtitle.get(
        query="python tutorial",
        limit=2,
        save_to_disk="test",
        language="en"
    )

    print(result)

Notes
-----

- The `query` parameter is required to specify the search term.
- If `save_to_disk` is specified, ensure the folder exists or provide a valid path.
- Use the `language` parameter to specify the desired subtitle language.