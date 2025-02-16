GetVideoSubtitle
================

The ``GetVideoSubtitle`` class is designed to retrieve subtitles for specific YouTube videos.  
It supports fetching subtitles in a desired language and saving them to disk for offline usage.

Class Usage
-----------

.. code-block:: python

    from ytkit import GetVideoSubtitle

    # Example usage
    get_video_subtitle = GetVideoSubtitle()
    result = get_video_subtitle.get(
        video_ids=["_uQrJ0TkZlc"],
        language="en",
        save_to_disk="subtitles"
    )

Method Details
--------------

**Input Parameters**

- **video_ids** (*List[str]*):  
  A list of YouTube video IDs for which subtitles should be retrieved.
- **language** (*str*):  
  Desired language code for subtitles. Defaults to ``"en"``.
- **save_to_disk** (*Union[None, str]*):  
  Folder path where transcript files will be saved. If ``None``, files are not saved to disk.

Examples
--------

Fetching subtitles for a specific video:

.. code-block:: python

    from ytkit import GetVideoSubtitle

    get_video_subtitle = GetVideoSubtitle()
    result = get_video_subtitle.get(
        video_ids=["_uQrJ0TkZlc"],
        language="en",
        save_to_disk="subtitles"
    )

    print(result)

Notes
-----

- At least one ``video_id`` must be provided.
- If ``save_to_disk`` is specified, ensure the folder exists or provide a valid path.
- Use the ``language`` parameter to specify the desired subtitle language.
