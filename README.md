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

**109** channels, **1,192,714.5** hours playtime between **2023-01-17** and **2024-12-22**


### playtime per genre (top 30)

    78058.3h 6.54% Nachrichten
    54185.7h 4.54% Verkaufsshow
    49716.1h 4.17% Krimiserie
    44066.5h 3.69% Werbesendung
    37094.0h 3.11% Dokureihe
    35228.2h 2.95% Dokusoap
    34910.5h 2.93% Regionalmagazin
    31539.0h 2.64% Dokumentation
    28183.0h 2.36% *unknown*
    22371.5h 1.88% Zeichentrickserie
    22097.6h 1.85% Infomercial
    21335.2h 1.79% Animationsserie
    16896.5h 1.42% Comedyserie
    16723.1h 1.40% Morgenmagazin
    15832.5h 1.33% Talkshow
    15715.7h 1.32% Religionsmagazin
    14678.8h 1.23% Magazin
    11800.7h 0.99% E-Sport
    11473.5h 0.96% Sitcom
    10791.1h 0.90% Wetterbericht
    10567.0h 0.89% Quiz
    10560.5h 0.89% Komödie
    10510.2h 0.88% Programmende
    9195.1h  0.77% Realityshow
    9104.1h  0.76% Politikmagazin
    8918.7h  0.75% Wissensmagazin
    8713.0h  0.73% Börsenmagazin
    7954.5h  0.67% Wirtschaftsmagazin
    7921.9h  0.66% Arztserie
    7916.4h  0.66% Dramaserie
