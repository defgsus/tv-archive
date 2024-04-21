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

**102** channels, **821,108.2** hours playtime between **2023-01-17** and **2024-04-22**


### playtime per genre (top 30)

    53456.6h 6.51% Nachrichten
    39395.2h 4.80% Verkaufsshow
    33414.2h 4.07% Krimiserie
    28684.4h 3.49% Werbesendung
    26015.0h 3.17% Dokureihe
    24765.7h 3.02% Dokusoap
    23862.6h 2.91% Regionalmagazin
    21232.6h 2.59% Dokumentation
    21048.6h 2.56% *unknown*
    15069.2h 1.84% Zeichentrickserie
    14910.7h 1.82% Infomercial
    14614.9h 1.78% Animationsserie
    12428.5h 1.51% Comedyserie
    11574.3h 1.41% Morgenmagazin
    11478.1h 1.40% Magazin
    11088.2h 1.35% Religionsmagazin
    10941.5h 1.33% Talkshow
    8116.5h  0.99% E-Sport
    7648.5h  0.93% Programmende
    7564.0h  0.92% Sitcom
    7282.8h  0.89% Wetterbericht
    7228.1h  0.88% Börsenmagazin
    7073.4h  0.86% Quiz
    7029.8h  0.86% Komödie
    6088.8h  0.74% Wissensmagazin
    5980.6h  0.73% Politikmagazin
    5919.4h  0.72% Realityshow
    5874.2h  0.72% Wirtschaftsmagazin
    5865.1h  0.71% Telenovela
    5488.2h  0.67% Musikmagazin
