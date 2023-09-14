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

**97** channels, **434,223.5** hours playtime between **2023-01-17** and **2023-09-15**


### playtime per genre (top 30)

    28691.1h 6.61% Nachrichten
    20627.2h 4.75% Verkaufsshow
    17580.2h 4.05% Krimiserie
    14639.9h 3.37% Werbesendung
    14312.6h 3.30% Dokureihe
    13211.3h 3.04% Dokusoap
    12529.5h 2.89% Regionalmagazin
    10936.7h 2.52% Dokumentation
    10310.1h 2.37% *unknown*
    8198.4h  1.89% Zeichentrickserie
    7923.1h  1.82% Infomercial
    7694.4h  1.77% Animationsserie
    7051.8h  1.62% Comedyserie
    6152.8h  1.42% Morgenmagazin
    5804.9h  1.34% Religionsmagazin
    5749.2h  1.32% Talkshow
    5431.2h  1.25% Magazin
    4660.9h  1.07% Programmende
    4299.3h  0.99% E-Sport
    4100.4h  0.94% Wetterbericht
    4087.1h  0.94% Sitcom
    3938.2h  0.91% Börsenmagazin
    3590.6h  0.83% Quiz
    3414.5h  0.79% Musikmagazin
    3355.9h  0.77% Komödie
    3296.6h  0.76% Wirtschaftsmagazin
    3252.4h  0.75% Wissensmagazin
    3074.3h  0.71% Telenovela
    2861.1h  0.66% Reportagereihe
    2846.9h  0.66% Politikmagazin
