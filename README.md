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

**101** channels, **767,607.9** hours playtime between **2023-01-17** and **2024-03-21**


### playtime per genre (top 30)

    49980.0h 6.51% Nachrichten
    36854.7h 4.80% Verkaufsshow
    31302.7h 4.08% Krimiserie
    26649.7h 3.47% Werbesendung
    24415.1h 3.18% Dokureihe
    23197.5h 3.02% Dokusoap
    22321.3h 2.91% Regionalmagazin
    19811.6h 2.58% Dokumentation
    19696.8h 2.57% *unknown*
    14160.7h 1.84% Zeichentrickserie
    13967.4h 1.82% Infomercial
    13601.0h 1.77% Animationsserie
    11650.5h 1.52% Comedyserie
    10901.6h 1.42% Morgenmagazin
    10487.9h 1.37% Magazin
    10373.5h 1.35% Religionsmagazin
    10238.8h 1.33% Talkshow
    7566.9h  0.99% E-Sport
    7233.0h  0.94% Programmende
    7193.5h  0.94% Sitcom
    6820.5h  0.89% Börsenmagazin
    6820.3h  0.89% Wetterbericht
    6549.6h  0.85% Quiz
    6455.6h  0.84% Komödie
    5734.2h  0.75% Wissensmagazin
    5584.2h  0.73% Politikmagazin
    5548.7h  0.72% Realityshow
    5541.1h  0.72% Wirtschaftsmagazin
    5497.4h  0.72% Telenovela
    5221.2h  0.68% Musikmagazin
