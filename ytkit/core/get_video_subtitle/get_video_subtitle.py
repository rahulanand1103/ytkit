from youtube_transcript_api import YouTubeTranscriptApi
from typing import List, Union
from pydantic import BaseModel, Field
import os
from ytkit.core.get_video_subtitle.schema import SubtitleInput
from tqdm import tqdm
from ytkit.base import BaseGet


class GetVideoSubtitle:
    """
    A class to fetch YouTube subtitles in the desired language.
    """

    def transcript_info(self, video_id: str) -> List[str]:
        """
        Get available transcript languages for a video.

        :param video_id: str - The YouTube video ID
        :return: List[str] - List of available language codes
        """
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        return [transcript.language_code for transcript in transcript_list]

    def _get_translated_transcript(
        self, video_id: str, language: str
    ) -> Union[List[dict], str]:
        """
        Get transcript for a video in a specified language.

        :param video_id: str - The YouTube video ID
        :param language: str - Language code
        :return: List[dict] or str - Transcript
        """
        transcript = YouTubeTranscriptApi.get_transcript(video_id, [language])
        return " ".join(entry["text"] for entry in transcript)

    def _save_transcript(
        self, content: Union[List[dict], str], save_path: str, video_id: str
    ):
        """
        Save the transcript content to a file.

        :param content: Union[List[dict], str] - Transcript data
        :param save_path: str - Folder path to save the file
        :param video_id: str - The YouTube video ID for naming
        """
        os.makedirs(save_path, exist_ok=True)
        file_path = os.path.join(save_path, f"{video_id}.txt")
        with open(file_path, "w", encoding="utf-8") as file:
            if isinstance(content, list):
                for entry in content:
                    file.write(f"{entry['text']}\n")
            else:
                file.write(content)

    def get(self, **kwargs) -> Union[List[dict], str]:
        """
        Get transcript for video(s) with language handling.

        :param video_ids: List[str] - List of YouTube video IDs
        :param language: str - Desired language code (default: "en")
        :param save_to_disk: str - Folder path to save the transcripts (default: None)
        :return: List[dict] or str - Transcript data
        """
        # Validate inputs using Pydantic model
        validated_input = SubtitleInput(
            video_ids=SubtitleInput.validate_video_ids(kwargs.get("video_ids")),
            language=kwargs.get("language", "en"),
            save_to_disk=kwargs.get("save_to_disk", None),
        )

        results = []
        for video_id in tqdm(validated_input.video_ids):
            try:
                available_languages = self.transcript_info(video_id)
                if validated_input.language in available_languages:
                    transcript = self._get_translated_transcript(
                        video_id, validated_input.language
                    )
                    results.append(transcript)

                    # Save transcript if save_to_disk is provided
                    if validated_input.save_to_disk:
                        self._save_transcript(
                            transcript, validated_input.save_to_disk, video_id
                        )

                else:
                    transcript = YouTubeTranscriptApi.list_transcripts(
                        video_id
                    ).find_transcript([available_languages[0]])
                    translated_transcript = transcript.translate(
                        validated_input.language
                    )
                    fetched_transcript = translated_transcript.fetch()
                    results.append(fetched_transcript)

                    # Save transcript if save_to_disk is provided
                    if validated_input.save_to_disk:
                        self._save_transcript(
                            fetched_transcript, validated_input.save_to_disk, video_id
                        )
            except Exception as e:
                print(e)

        return results if len(results) > 1 else results[0]
