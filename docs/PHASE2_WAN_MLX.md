# Phase 2: MLX Wan 2.1 Local Benchmark

Verified against Apple's `mlx-examples/video/wan2.1` source on 2026-11-26. This is a local testing guide; no successful user-machine benchmark is yet recorded.

## Prerequisites

Apple Silicon with 24 GB unified memory (target), Python 3.11+ (current user environment Python 3.13), FFmpeg. From `models/mlx-examples/video/wan2.1`, activate the isolated `.venv-wan`.

```sh
source .venv-wan/bin/activate
python -m pip install -r requirements.txt
python -c "import mlx.core as mx, torch, huggingface_hub; print('MLX', mx.__version__ if hasattr(mx,'__version__') else 'available'); print('torch', torch.__version__)"
ffmpeg -version | head -n 1
python txt2video.py --help
```

The current upstream requirements include `mlx>=0.31.0`, `einops>=0.8.2`, `huggingface_hub`, `numpy`, `Pillow`, `tokenizers`, `torch`, and `tqdm`. Confirm install support with Python 3.13 and arm64 first. If dependency resolution fails, build an isolated Python 3.12 environment, rather than downgrading the main lab.

## First smoke test

Run after installation and checking free disk space. The first run downloads model weights from Hugging Face.

```sh
python txt2video.py \
  "A cute baby panda in a yellow hoodie waves gently in a colorful magical meadow, bright soft 3D cartoon style, child-friendly, no text" \
  --model t2v-1.3B \
  --size 480x272 \
  --frames 17 \
  --steps 8 \
  --guidance 1.0 \
  --seed 42 \
  --no-cache \
  --verbose \
  --output pipo_smoke.mp4
```

This intentionally short/low-resolution test aims to catch compatibility and memory failures before a full 81-frame/50-step run. Visual quality can be poor at 8 steps. Do not confuse a smoke test with production quality. Try 832x480, 81 frames, and more sampling steps after success.

## Notes

- The upstream README reports around 10 GB at 480p/81 frames with `--no-cache`, but the cited single-step timing is on **M4 Max**, not base M4. Expect slower performance and measure actual wall clock.
- T2V-1.3B is text-to-video only. It cannot ensure consistency from a Pipo reference image. Image-to-video support needs a separate suitable model workflow.
- Do not use unquantized 14B variants on a 24 GB machine.
- Record start/end timestamps, output size, memory, errors, model license and inference settings.
- Validate model weight license and downstream monetization terms before publishing.
