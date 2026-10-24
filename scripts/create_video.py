#!/usr/bin/env python3
"""Create a simple 9:16 FOOTNOTE editorial video with text cards and narration."""
import argparse
import os
import re
import subprocess
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 720, 1280
BG = (246, 240, 225)
INK = (35, 29, 28)
MAROON = (112, 32, 48)
MUTED = (104, 91, 83)


def font(size, bold=False):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
    ]
    for path in candidates:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def clean(text):
    return re.sub(r"\s+", " ", text).strip()


def wrap_words(draw, text, fnt, max_width):
    words = text.split()
    lines, line = [], ""
    for word in words:
        test = (line + " " + word).strip()
        if draw.textbbox((0, 0), test, font=fnt)[2] <= max_width or not line:
            line = test
        else:
            lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def make_card(path, kicker, heading, body, index, total):
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    d.rectangle((44, 54, W - 44, 60), fill=MAROON)
    d.text((48, 82), "FOOTNOTE", font=font(25, True), fill=MAROON)
    d.text((W - 180, 88), "ISSUE 001", font=font(16, True), fill=MUTED)
    d.line((48, 130, W - 48, 130), fill=(204, 190, 171), width=2)
    d.text((48, 190), kicker.upper(), font=font(19, True), fill=MAROON)
    hf = font(48, True)
    y = 250
    for line in wrap_words(d, heading, hf, W - 96):
        d.text((48, y), line, font=hf, fill=INK)
        y += 61
    d.line((48, y + 20, 150, y + 20), fill=MAROON, width=5)
    y += 70
    bf = font(28)
    for line in wrap_words(d, body, bf, W - 100):
        d.text((50, y), line, font=bf, fill=INK)
        y += 43
    d.text((48, H - 92), "JAMMU • POONCH • RAJOURI • CHENAB • KASHMIR", font=font(13, True), fill=MUTED)
    d.line((48, H - 58, W - 48, H - 58), fill=(204, 190, 171), width=2)
    d.text((48, H - 44), "FOOTNOTE  /  CULTURE IN CONTEXT", font=font(13, True), fill=MAROON)
    d.text((W - 100, H - 44), f"{index:02d}/{total:02d}", font=font(13, True), fill=INK)
    im.save(path)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--idea", required=True)
    parser.add_argument("--title", default="")
    parser.add_argument("--output", default="output/footnote-video.mp4")
    args = parser.parse_args()

    idea = clean(args.idea)
    if not idea:
        raise SystemExit("Please enter a video idea.")
    title = clean(args.title) or idea
    # Keep the video editorial and transparent: this is a template, not researched reporting.
    short = idea if len(idea) <= 210 else idea[:207].rsplit(" ", 1)[0] + "..."
    scenes = [
        ("A FOOTNOTE SHORT", title, "A story about music, memory and culture from Jammu and Kashmir."),
        ("THE IDEA", short, "Every scene begins with a question worth exploring. This video is a starting point, not a substitute for research."),
        ("THE CONTEXT", "Sound carries history", "Local scenes grow through language, place, community, performance and the people who keep culture moving."),
        ("LOOK CLOSER", "Listen beyond the headline", "Find the original voices. Check dates and sources. Give artists and traditions the context they deserve."),
        ("FOOTNOTE", "Before the beat, there was rhythm.", "Independent stories on hip-hop, music and cultural memory across Jammu, Poonch, Rajouri, Chenab Valley and Kashmir."),
    ]
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    work = out.parent / "video_work"
    work.mkdir(exist_ok=True)
    frame_paths = []
    for i, (kicker, heading, body) in enumerate(scenes, 1):
        p = work / f"scene_{i:02d}.png"
        make_card(p, kicker, heading, body, i, len(scenes))
        frame_paths.append(p)

    narration = " ".join([f"{title}.", f"Our subject is {short}.", scenes[2][2], scenes[3][2], scenes[4][2]])
    wav = work / "narration.wav"
    subprocess.run(["espeak-ng", "-v", "en", "-s", "145", "-w", str(wav), narration], check=True)

    # Build a 9:16 slideshow with gentle fades, then fit narration to the final video.
    inputs = []
    for p in frame_paths:
        inputs += ["-loop", "1", "-t", "4", "-i", str(p)]
    filter_parts = []
    for i in range(len(frame_paths)):
        filter_parts.append(f"[{i}:v]scale={W}:{H},setsar=1,format=yuv420p,fade=t=in:st=0:d=0.35,fade=t=out:st=3.65:d=0.35[v{i}]")
    concat = "".join(f"[v{i}]" for i in range(len(frame_paths))) + f"concat=n={len(frame_paths)}:v=1:a=0[vout]"
    filter_parts.append(concat)
    cmd = ["ffmpeg", "-y", *inputs, "-i", str(wav), "-filter_complex", ";".join(filter_parts),
           "-map", "[vout]", "-map", f"{len(frame_paths)}:a", "-c:v", "libx264", "-preset", "veryfast",
           "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "128k", "-shortest", "-movflags", "+faststart", str(out)]
    subprocess.run(cmd, check=True)
    print(f"Video created: {out}")


if __name__ == "__main__":
    main()
