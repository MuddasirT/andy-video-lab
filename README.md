# Andy Video Lab 🎬

A separate, free-first research and production lab for making short animated videos, beginning with **TinyToon Planet**.

The first milestone is a **working storyboard-to-MP4 baseline**, not a claim that AI video generation has been installed. Later milestones introduce benchmarked local video models and agents.

## Quick start on Apple Silicon

Requires Python 3.11+ and FFmpeg.

```bash
git clone https://github.com/MuddasirT/andy-video-lab.git
cd andy-video-lab
brew install ffmpeg
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
andy-video doctor
andy-video storyboard
andy-video render
```

Generated output: `outputs/tinytoon_planet/episode_01.mp4`.

Optional scene images: add `scene_01.png` through `scene_06.png` inside `projects/tinytoon_planet/assets/`. Without images, the renderer creates colored placeholder scenes. The initial video is **silent**, 1080×1920 and 30 seconds. This is a media-pipeline check, not an animated cartoon.

## Roadmap

1. Validate FFmpeg storyboard rendering and test coverage.
2. Benchmark Apple MLX / Wan 2.1 1.3B on a Mac M4 (24 GB memory), including download size, peak memory, runtime, and model license.
3. Add approved character sheets and image-to-video adapters with deterministic asset references.
4. Add local TTS, licensed audio, transitions, captions and QA.
5. Orchestrate specialists with Python and a local FastAPI interface.

See `docs/MODELS.md` for research priorities, licensing and evaluation rules.

Do not commit downloaded models, generated videos, private credentials or third-party copyrighted assets. Review all content designed for children before publication.
