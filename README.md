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

**109** channels, **1,190,954.3** hours playtime between **2023-01-17** and **2024-12-21**


### playtime per genre (top 30)

    77958.7h 6.55% Nachrichten
    54114.3h 4.54% Verkaufsshow
    49653.2h 4.17% Krimiserie
    43990.3h 3.69% Werbesendung
    37044.4h 3.11% Dokureihe
    35202.4h 2.96% Dokusoap
    34888.3h 2.93% Regionalmagazin
    31483.0h 2.64% Dokumentation
    28135.8h 2.36% *unknown*
    22332.6h 1.88% Zeichentrickserie
    22062.8h 1.85% Infomercial
    21303.0h 1.79% Animationsserie
    16886.0h 1.42% Comedyserie
    16709.6h 1.40% Morgenmagazin
    15804.6h 1.33% Talkshow
    15701.8h 1.32% Religionsmagazin
    14666.9h 1.23% Magazin
    11783.6h 0.99% E-Sport
    11459.2h 0.96% Sitcom
    10775.5h 0.90% Wetterbericht
    10561.5h 0.89% Quiz
    10522.2h 0.88% Komödie
    10495.9h 0.88% Programmende
    9193.1h  0.77% Realityshow
    9102.5h  0.76% Politikmagazin
    8911.0h  0.75% Wissensmagazin
    8713.4h  0.73% Börsenmagazin
    7953.9h  0.67% Wirtschaftsmagazin
    7910.1h  0.66% Dramaserie
    7906.1h  0.66% Telenovela
