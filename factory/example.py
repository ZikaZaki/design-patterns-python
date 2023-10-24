"""
Basic video exporting example
"""
import pathlib
from abc import ABC, abstractmethod


class VideoExporter(ABC):
  """Basic representation of video exporting codec."""

  @abstractmethod
  def prepare_export(self, video_data):
    """Prepares video data for exporting."""

  @abstractmethod
  def do_export(self, folder: pathlib.Path):
    """Exports the video data to a folder."""


class LosslessVideoExporter(VideoExporter):
  """Lossless video exporting codec."""

  def prepare_export(self, video_data):
    print("Preparing video data for lossless export.")

  def do_export(self, folder: pathlib.Path):
    print(f"Exporting video data in lossless format to {folder}.")


class H264BPVideoExporter(VideoExporter):
  """H.264 video exporting codec with Baseline profile."""

  def prepare_export(self, video_data):
    print("Preparing video data for H.264 (Baseline) export.")

  def do_export(self, folder: pathlib.Path):
    print(f"Exporting video data in H.264 (Baseline) format to {folder}.")


class H264Hi422PVideoExporter(VideoExporter):
  """H.264 video exporting codec with Hi422P profile (10-bit, 4:2:2 chroma sampling)."""

  def prepare_export(self, video_data):
    print("Preparing video data for H.264 (Hi422P) export.")

  def do_export(self, folder: pathlib.Path):
    print(f"Exporting video data in H.264 (Hi422P) format to {folder}.")


class AudioExporter(ABC):
  """Basic representation of audio exporting codec."""

  @abstractmethod
  def prepare_export(self, audio_data):
    """Prepares audio data for exporting."""

  @abstractmethod
  def do_export(self, folder: pathlib.Path):
    """Exports the audio data to a folder."""


class AACAudioExporter(AudioExporter):
  """AAC audio exporting codec."""

  def prepare_export(self, audio_data):
    print("Preparing audio data for AAC export.")

  def do_export(self, folder: pathlib.Path):
    print(f"Exporting audio data in AAC format to {folder}.")


class WAVAudioExporter(AudioExporter):
  """WAV (lossless) audio exporting codec."""

  def prepare_export(self, audio_data):
    print("Preparing audio data for WAV export.")

  def do_export(self, folder: pathlib.Path):
    print(f"Exporting audio data in WAV format to {folder}.")


class ExporterFactory(ABC):
  """
  Factory that represents a combination of video and audio codecs.
  The factory doesn't maintain any of the instances it creates.
  """

  @abstractmethod
  def get_video_exporter(self) -> VideoExporter:
    """Returns a new video exporter instance."""
    pass

  @abstractmethod
  def get_audio_exporter(self) -> AudioExporter:
    """Returns a new audio exporter instance."""
    pass


class FastExporter(ExporterFactory):
  """Factory aimed at providing a high speed, lower quality export."""

  def get_video_exporter(self) -> VideoExporter:
    return H264BPVideoExporter()

  def get_audio_exporter(self) -> AudioExporter:
    return AACAudioExporter()


class HighQualityExporter(ExporterFactory):
  """Factory aimed at providing a slower speed, high quality export."""

  def get_video_exporter(self) -> VideoExporter:
    return H264Hi422PVideoExporter()

  def get_audio_exporter(self) -> AudioExporter:
    return AACAudioExporter()


class MasterQualityExporter(ExporterFactory):
  """Factory aimed at providing a high speed, high quality export."""

  def get_video_exporter(self) -> VideoExporter:
    return LosslessVideoExporter()

  def get_audio_exporter(self) -> AudioExporter:
    return WAVAudioExporter()


FACTORIES = {
  "low": FastExporter(),
  "high": HighQualityExporter(),
  "master": MasterQualityExporter(),
}

# Helper function
def read_exporter() -> ExporterFactory:
  """
  Constructs an exporter factory based on the user's preference.
  Returns: An exporter factory.
  """
  # read the desired export quality
  while True:
    export_quality = input(
        f"Enter desired output quality ({', '.join(FACTORIES)}): ")
    try:
        return FACTORIES[export_quality]
    except KeyError:
        print(f"Unknown output quality option: {export_quality}!")

def do_export(fac: ExporterFactory) -> None:
"""Do a test export using a video and audio exporters."""

    # retrieve the exporters
    video_exporter = fac.get_video_exporter()
    audio_exporter = fac.get_audio_exporter()

    # prepare the export
    video_exporter.prepare_export("placeholder_for_video_data")
    audio_exporter.preapre_export("placeholder_for_audio_data")

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
