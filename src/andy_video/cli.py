"""CLI for the first working storyboard-to-video baseline."""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WIDTH, HEIGHT, FPS = 1080, 1920, 24


def load_plan(project: str) -> dict:
    path = ROOT / "projects" / project / "episode_01.json"
    if not path.is_file():
        raise SystemExit(f"Storyboard not found: {path}")
    plan = json.loads(path.read_text(encoding="utf-8"))
    if not plan.get("scenes"):
        raise SystemExit("Storyboard has no scenes")
    return plan


def doctor() -> None:
    print("FFmpeg:", shutil.which("ffmpeg") or "MISSING: brew install ffmpeg")
    print("Project root:", ROOT)


def render(project: str) -> Path:
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        raise SystemExit("FFmpeg missing. Install: brew install ffmpeg")
    plan = load_plan(project)
    scenes = plan["scenes"]
    assets = ROOT / "projects" / project / "assets"
    output = ROOT / "outputs" / project / "episode_01.mp4"
    output.parent.mkdir(parents=True, exist_ok=True)
    inputs, filters = [], []
    palette = ["0x80CFFF", "0xF8C4E8", "0xB8E986", "0xF9D77E", "0xB5A4F4", "0xFFB3A7"]
    total = 0
    for index, scene in enumerate(scenes):
        duration = float(scene.get("duration_seconds", 5))
        if not 0 < duration <= 60:
            raise SystemExit(f"Invalid duration for scene {index + 1}")
        total += duration
        image = next((assets / f"scene_{index+1:02d}.{ext}" for ext in ("png", "jpg", "jpeg") if (assets / f"scene_{index+1:02d}.{ext}").is_file()), None)
        if image:
            inputs += ["-loop", "1", "-framerate", str(FPS), "-t", str(duration), "-i", str(image)]
        else:
            inputs += ["-f", "lavfi", "-i", f"color=c={palette[index % len(palette)]}:s={WIDTH}x{HEIGHT}:r={FPS}:d={duration}"]
        filters.append(
            f"[{index}:v]scale={WIDTH}:{HEIGHT}:force_original_aspect_ratio=increase,"
            f"crop={WIDTH}:{HEIGHT},setsar=1,fps={FPS},"
            f"trim=duration={duration},setpts=PTS-STARTPTS,format=yuv420p[v{index}]"
        )
    if abs(total - float(plan.get("duration_seconds", total))) > 0.01:
        raise SystemExit("Episode duration does not match scene durations")
    filters.append(f"{''.join(f'[v{i}]' for i in range(len(scenes)))}concat=n={len(scenes)}:v=1:a=0[out]")
    command = [ffmpeg, "-hide_banner", "-loglevel", "error", "-y", *inputs,
               "-filter_complex", ";".join(filters), "-map", "[out]",
               "-c:v", "libx264", "-preset", "veryfast", "-crf", "23",
               "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(output)]
    subprocess.run(command, check=True)
    print(f"Created {output}: {total:g}s, {WIDTH}x{HEIGHT}, silent")
    return output


def main() -> None:
    parser = argparse.ArgumentParser(prog="andy-video")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("doctor")
    for name in ("storyboard", "render"):
        command = commands.add_parser(name)
        command.add_argument("--project", default="tinytoon_planet")
    args = parser.parse_args()
    if args.command == "doctor":
        doctor()
    elif args.command == "storyboard":
        print(json.dumps(load_plan(args.project), indent=2, ensure_ascii=False))
    else:
        render(args.project)


if __name__ == "__main__":
    main()
