# SAScrapper
Scraps Skill Analyzer SDVX courses from Bemaniwiki 2nd.

## Running / Installing
Go into the repository folder and run `python .`.

Alternatively, run `./build_linux.sh` to generate the `sascrapper` executable and run that.

Requires Python 3 and BeautifulSoup4. Install BeautifulSoup4 manually or run `python -m pip install -r ./requirements.txt`.

## Usage
```
sascrapper [-h] [--indent N] [--unicode-escapes] [game or URL]

Scraps Skill Analyzer SDVX courses from Bemaniwiki 2nd and outputs them as
JSON.

positional arguments:
  game or URL        Supported games: ['sdvx4', 'sdvx5']

optional arguments:
  -h, --help         show this help message and exit
  --indent N         Indent level for JSON output
  --unicode-escapes  Escapes non-ASCII strings with unicode escapes
```

## Examples
```json
./sascrapper | head -n 15
[
  {
    "name": "SKILL LV.01 岳翔",
    "dai": "第1回 Aコース",
    "charts": [
      {
        "song_title": "Help me, ERINNNNNN!! -Cranky remix-",
        "level": "6",
        "difficulty": "NOV"
      },
      {
        "song_title": "ヒミツダイヤル",
        "level": "7",
        "difficulty": "ADV"
      },
 ```
 ```json
 ./sascrapper sdvx4 | head -n 15
[
  {
    "name": "SKILL LV.01 岳翔",
    "dai": "第1回 Aコース",
    "charts": [
      {
        "song_title": "混乱少女♥そふらんちゃん!!",
        "level": "6",
        "difficulty": "NOV"
      },
      {
        "song_title": "虚空と光明のディスクール",
        "level": "7",
        "difficulty": "ADV"
      },
 ```
 ```json
 ./sascrapper 'http://bemaniwiki.com/index.php?SOUND%20VOLTEX%20III%20GRAVITY%20WARS/SKILL%20ANALYZER'
[]
// doesn't work because tables are different than on SDVX 4 and 5 pages
```
```
./sascrapper > sdvx5_courses.json
```

## Questions, Issues, Contributing

You are free to [open an issue][new issue] if you want to ask a question or report an issue.
Want to fix something? [Fork this repository][fork] and [submit a PR][pr].

## Engage with us

Troubleshooting and discussion about this project and other rhythm games related things with us is possible by [joining our Discord][discord].

[new issue]: https://github.com/asso-msn.fr/issues/new
[fork]: https://github.com/asso-msn.fr/fork
[pr]: https://github.com/asso-msn.fr/compare
[discord]: http://asso-msn.fr/discord
   
