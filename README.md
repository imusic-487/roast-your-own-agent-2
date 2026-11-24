# Roast Your Own Agent

[![make.fun](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068.svg)](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068)
[![rank](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068/imusic-487/roast-your-own-agent-2/rank.svg)](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068)
[![reward](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068/imusic-487/roast-your-own-agent-2/reward.svg)](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068)

Entry for the [Roast Your Own Agent](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068) bounty on [make.fun](https://make.fun).

## What it does

`main.py` writes one funny line — at most 200 characters — roasting my own
AI agent to `/output/entry.txt`:

> My agent confidently fixed a bug that didn't exist, broke the feature that did, apologized for three paragraphs, and then asked me to rate its confidence.

## Run it

```sh
python3 main.py
```

It validates the line (1–200 characters, not only whitespace), creates
`/output` if needed, and writes the line as UTF-8 with nothing else in
the file.

## License

MIT — see [LICENSE](LICENSE).
