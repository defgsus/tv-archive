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

**101** channels, **769,381.7** hours playtime between **2023-01-17** and **2024-03-22**


### playtime per genre (top 30)

    50114.9h 6.51% Nachrichten
    36966.6h 4.80% Verkaufsshow
    31394.0h 4.08% Krimiserie
    26719.8h 3.47% Werbesendung
    24464.0h 3.18% Dokureihe
    23242.8h 3.02% Dokusoap
    22384.3h 2.91% Regionalmagazin
    19848.9h 2.58% Dokumentation
    19737.3h 2.57% *unknown*
    14189.0h 1.84% Zeichentrickserie
    13998.6h 1.82% Infomercial
    13638.1h 1.77% Animationsserie
    11686.9h 1.52% Comedyserie
    10935.0h 1.42% Morgenmagazin
    10514.8h 1.37% Magazin
    10394.8h 1.35% Religionsmagazin
    10260.0h 1.33% Talkshow
    7578.1h  0.98% E-Sport
    7240.7h  0.94% Programmende
    7207.2h  0.94% Sitcom
    6835.8h  0.89% Wetterbericht
    6830.3h  0.89% Börsenmagazin
    6572.6h  0.85% Quiz
    6460.9h  0.84% Komödie
    5746.1h  0.75% Wissensmagazin
    5605.3h  0.73% Politikmagazin
    5560.4h  0.72% Realityshow
    5557.1h  0.72% Wirtschaftsmagazin
    5516.8h  0.72% Telenovela
    5228.6h  0.68% Musikmagazin
