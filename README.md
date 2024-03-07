# Archive of TV-shows

Scraped directly from a german webpage, started at about mid-January 2023.

TV is not as important anymore but still, archiving the decisions of which programs to run at what time
becomes another puzzle piece in the revelation of mind-control.. 

Data is stored in [docs/data/YEAR/MONTH/YEAR-MONTH-DAY.ndjson](docs/data/) files. 
Each entry looks like this:

```python
{
  "id": "181043890", 
  "url": "https://www.hoerzu.de/tv-programm/south-park-kohle-an-den-chefkoch/bid_181043890/", 
  "channel": "Comedy Central", 
  "title": "South Park", 
  "date": "2023-01-17T05:15:00",    # probably Europe/Berlin timezone 
  "length": 25,                     # minutes 
  "sub_title": "Serie", 
  "genre": "Erwachsenen-Animationsserie", 
  "season": 2, 
  "episode": 14, 
  "year": 1998, 
  "countries": ["USA"],
}
```

## Statistics

**99** channels, **744,789.2** hours playtime between **2023-01-17** and **2024-03-08**


### playtime per genre (top 30)

    48500.2h 6.51% Nachrichten
    35777.6h 4.80% Verkaufsshow
    30325.8h 4.07% Krimiserie
    25782.8h 3.46% Werbesendung
    23782.6h 3.19% Dokureihe
    22507.1h 3.02% Dokusoap
    21632.6h 2.90% Regionalmagazin
    19185.7h 2.58% Dokumentation
    19123.2h 2.57% *unknown*
    13777.4h 1.85% Zeichentrickserie
    13543.8h 1.82% Infomercial
    13133.5h 1.76% Animationsserie
    11306.4h 1.52% Comedyserie
    10579.4h 1.42% Morgenmagazin
    10061.5h 1.35% Religionsmagazin
    10054.8h 1.35% Magazin
    9906.9h  1.33% Talkshow
    7365.4h  0.99% E-Sport
    7055.5h  0.95% Programmende
    7019.9h  0.94% Sitcom
    6645.5h  0.89% Börsenmagazin
    6616.1h  0.89% Wetterbericht
    6314.9h  0.85% Komödie
    6304.1h  0.85% Quiz
    5567.3h  0.75% Wissensmagazin
    5415.4h  0.73% Realityshow
    5398.9h  0.72% Wirtschaftsmagazin
    5382.9h  0.72% Politikmagazin
    5324.4h  0.71% Telenovela
    5095.4h  0.68% Musikmagazin
