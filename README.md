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

**97** channels, **498,607.1** hours playtime between **2023-01-17** and **2023-10-21**


### playtime per genre (top 30)

    32883.5h 6.60% Nachrichten
    23815.8h 4.78% Verkaufsshow
    20062.4h 4.02% Krimiserie
    16842.6h 3.38% Werbesendung
    16401.0h 3.29% Dokureihe
    15220.4h 3.05% Dokusoap
    14404.5h 2.89% Regionalmagazin
    12598.9h 2.53% Dokumentation
    11978.5h 2.40% *unknown*
    9326.7h  1.87% Zeichentrickserie
    9079.9h  1.82% Infomercial
    8899.5h  1.78% Animationsserie
    7940.8h  1.59% Comedyserie
    7074.4h  1.42% Morgenmagazin
    6693.7h  1.34% Religionsmagazin
    6641.9h  1.33% Talkshow
    6255.6h  1.25% Magazin
    5153.2h  1.03% Programmende
    4903.8h  0.98% E-Sport
    4757.6h  0.95% Sitcom
    4638.0h  0.93% Wetterbericht
    4503.1h  0.90% Börsenmagazin
    4195.5h  0.84% Quiz
    3850.2h  0.77% Komödie
    3769.6h  0.76% Wirtschaftsmagazin
    3765.6h  0.76% Wissensmagazin
    3765.0h  0.76% Musikmagazin
    3580.8h  0.72% Telenovela
    3422.5h  0.69% Politikmagazin
    3261.4h  0.65% Realityshow
