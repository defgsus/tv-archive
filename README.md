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

**109** channels, **1,005,184.5** hours playtime between **2023-01-17** and **2024-08-20**


### playtime per genre (top 30)

    65370.9h 6.50% Nachrichten
    46824.8h 4.66% Verkaufsshow
    41258.8h 4.10% Krimiserie
    36178.7h 3.60% Werbesendung
    31616.3h 3.15% Dokureihe
    30382.8h 3.02% Dokusoap
    29283.9h 2.91% Regionalmagazin
    26223.9h 2.61% Dokumentation
    24559.7h 2.44% *unknown*
    18633.5h 1.85% Zeichentrickserie
    18406.9h 1.83% Infomercial
    18000.0h 1.79% Animationsserie
    14773.2h 1.47% Comedyserie
    14084.2h 1.40% Morgenmagazin
    13668.5h 1.36% Religionsmagazin
    13522.2h 1.35% Magazin
    13181.9h 1.31% Talkshow
    9946.1h  0.99% E-Sport
    9563.5h  0.95% Sitcom
    9064.5h  0.90% Wetterbericht
    9056.0h  0.90% Programmende
    8813.7h  0.88% Komödie
    8656.6h  0.86% Quiz
    8119.5h  0.81% Börsenmagazin
    7511.9h  0.75% Politikmagazin
    7487.4h  0.74% Wissensmagazin
    7439.6h  0.74% Realityshow
    6864.4h  0.68% Wirtschaftsmagazin
    6596.1h  0.66% Telenovela
    6546.1h  0.65% Dramaserie
