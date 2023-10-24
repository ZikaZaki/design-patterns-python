"""
Basic video exporting example
"""
from typing import Protocol
from pathlib import Path


class VideoExporter(Protocol):
  """Basic representation of video exporting codec."""

  def prepare_export(self, video_data):
    """Prepares video data for exporting."""

  def do_export(self, folder: Path):
    """Exports the video data to a folder."""


class LosslessVideoExporter:
  """Lossless video exporting codec."""

  def prepare_export(self, video_data):
    print("Preparing video data for lossless export.")

  def do_export(self, folder: Path):
    print(f"Exporting video data in lossless format to {folder}.")


class H264BPVideoExporter:
  """H.264 video exporting codec with Baseline profile."""

  def prepare_export(self, video_data):
    print("Preparing video data for H.264 (Baseline) export.")

  def do_export(self, folder: Path):
    print(f"Exporting video data in H.264 (Baseline) format to {folder}.")


class H264Hi422PVideoExporter:
  """H.264 video exporting codec with Hi422P profile (10-bit, 4:2:2 chroma sampling)."""

  def prepare_export(self, video_data):
    print("Preparing video data for H.264 (Hi422P) export.")

  def do_export(self, folder: Path):
    print(f"Exporting video data in H.264 (Hi422P) format to {folder}.")


class AudioExporter(Protocol):
  """Basic representation of audio exporting codec."""

  def prepare_export(self, audio_data):
    """Prepares audio data for exporting."""

  def do_export(self, folder: Path):
    """Exports the audio data to a folder."""


class AACAudioExporter:
  """AAC audio exporting codec."""

  def prepare_export(self, audio_data):
    print("Preparing audio data for AAC export.")

  def do_export(self, folder: Path):
    print(f"Exporting audio data in AAC format to {folder}.")


class WAVAudioExporter:
  """WAV (lossless) audio exporting codec."""

  def prepare_export(self, audio_data):
    print("Preparing audio data for WAV export.")

  def do_export(self, folder: Path):
    print(f"Exporting audio data in WAV format to {folder}.")


FACTORIES = {
  "low": (H264BPVideoExporter, AACAudioExporter),
  "high": (H264Hi422PVideoExporter, AACAudioExporter),
  "master": (LosslessVideoExporter, WAVAudioExporter),
}

# Helper function
def read_factory() -> tuple[VideoExporter, AudioExporter]:
  """
  Constructs an exporter factory based on the user's preference.
  Returns: An exporter factory.
  """
  # read the desired export quality
  while True:
    export_quality = input(
        f"Enter desired output quality ({', '.join(FACTORIES)}): ")
    try:
        video_class, audio_class = FACTORIES[export_quality]
        return (video_class(), audio_class())
    except KeyError:
        print(f"Unknown output quality option: {export_quality}!")

def do_export(fac: tuple[VideoExporter, AudioExporter]) -> None:
  """Do a test export using a video and audio exporters."""

  # retrieve the exporters
  video_exporter, audio_exporter = fac

  # prepare the export
  video_exporter.prepare_export("placeholder_for_video_data")
  audio_exporter.prepare_export("placeholder_for_audio_data")

  # do the export
  folder = Path("/usr/tmp/video")
  video_exporter.do_export(folder)
  audio_exporter.do_export(folder)

def main() -> None:
  """Main function."""
  
  # create the factory
  factory = read_factory()
  
  # perform the exporting job
  do_export(factory)
  
if __name__ == "__main__":
  main()
