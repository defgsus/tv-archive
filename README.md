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

**109** channels, **1,052,550.1** hours playtime between **2023-01-17** and **2024-09-19**


### playtime per genre (top 30)

    68484.1h 6.51% Nachrichten
    48836.9h 4.64% Verkaufsshow
    43432.1h 4.13% Krimiserie
    38193.0h 3.63% Werbesendung
    33031.0h 3.14% Dokureihe
    31680.6h 3.01% Dokusoap
    30753.2h 2.92% Regionalmagazin
    27534.2h 2.62% Dokumentation
    25336.2h 2.41% *unknown*
    19532.2h 1.86% Zeichentrickserie
    19316.1h 1.84% Infomercial
    18853.0h 1.79% Animationsserie
    15388.4h 1.46% Comedyserie
    14745.6h 1.40% Morgenmagazin
    14322.2h 1.36% Religionsmagazin
    13853.8h 1.32% Talkshow
    13694.8h 1.30% Magazin
    10412.8h 0.99% E-Sport
    10090.2h 0.96% Sitcom
    9529.3h  0.91% Wetterbericht
    9415.4h  0.89% Programmende
    9242.0h  0.88% Komödie
    9135.5h  0.87% Quiz
    8274.0h  0.79% Börsenmagazin
    7897.4h  0.75% Politikmagazin
    7896.3h  0.75% Wissensmagazin
    7861.4h  0.75% Realityshow
    7147.4h  0.68% Wirtschaftsmagazin
    6935.4h  0.66% Telenovela
    6852.9h  0.65% Dramaserie
