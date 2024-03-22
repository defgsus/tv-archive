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

**101** channels, **771,143.9** hours playtime between **2023-01-17** and **2024-03-23**


### playtime per genre (top 30)

    50239.2h 6.51% Nachrichten
    37063.8h 4.81% Verkaufsshow
    31461.9h 4.08% Krimiserie
    26782.0h 3.47% Werbesendung
    24504.2h 3.18% Dokureihe
    23288.9h 3.02% Dokusoap
    22443.0h 2.91% Regionalmagazin
    19893.2h 2.58% Dokumentation
    19769.4h 2.56% *unknown*
    14215.8h 1.84% Zeichentrickserie
    14030.4h 1.82% Infomercial
    13675.4h 1.77% Animationsserie
    11714.9h 1.52% Comedyserie
    10968.4h 1.42% Morgenmagazin
    10536.2h 1.37% Magazin
    10416.5h 1.35% Religionsmagazin
    10291.0h 1.33% Talkshow
    7597.5h  0.99% E-Sport
    7259.7h  0.94% Programmende
    7217.2h  0.94% Sitcom
    6858.0h  0.89% Börsenmagazin
    6850.9h  0.89% Wetterbericht
    6592.2h  0.85% Quiz
    6475.9h  0.84% Komödie
    5758.6h  0.75% Wissensmagazin
    5619.6h  0.73% Politikmagazin
    5571.6h  0.72% Wirtschaftsmagazin
    5567.4h  0.72% Realityshow
    5536.2h  0.72% Telenovela
    5237.5h  0.68% Musikmagazin
