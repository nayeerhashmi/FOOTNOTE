# FOOTNOTE Video Studio

A free, GitHub Actions-based starter for turning a FOOTNOTE content idea into a vertical social video.

## Generate a video

1. Open the **Actions** tab in this repository.
2. Select **Create FOOTNOTE video**.
3. Click **Run workflow**.
4. Enter your idea and submit.
5. Open the completed workflow run and download the `footnote-video` artifact.

The first version creates an editorial-style video with animated transitions between text cards and computer-generated narration. It does not create cinematic AI footage, and it does not publish automatically to social media.

## Costs and limits

This uses GitHub-hosted runners and free open-source tools. GitHub Actions usage is subject to the limits and terms of your GitHub plan. The video is created as a downloadable workflow artifact.

## Important

Review every video for factual accuracy, image/music rights, and suitability before posting. This starter does not use copyrighted images or background music. Narration is generated using espeak-ng.

## Local use

Requires Python 3, Pillow, FFmpeg, and espeak-ng. Run:

```bash
python scripts/create_video.py --idea "Your FOOTNOTE video idea" --output output/footnote-video.mp4
```
