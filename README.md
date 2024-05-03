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

**102** channels, **838,176.4** hours playtime between **2023-01-17** and **2024-05-04**


### playtime per genre (top 30)

    54667.8h 6.52% Nachrichten
    40100.3h 4.78% Verkaufsshow
    34106.4h 4.07% Krimiserie
    29306.4h 3.50% Werbesendung
    26471.0h 3.16% Dokureihe
    25308.0h 3.02% Dokusoap
    24377.5h 2.91% Regionalmagazin
    21737.1h 2.59% Dokumentation
    21392.0h 2.55% *unknown*
    15408.0h 1.84% Zeichentrickserie
    15226.2h 1.82% Infomercial
    14922.5h 1.78% Animationsserie
    12680.3h 1.51% Comedyserie
    11821.7h 1.41% Magazin
    11809.4h 1.41% Morgenmagazin
    11319.0h 1.35% Religionsmagazin
    11162.4h 1.33% Talkshow
    8311.7h  0.99% E-Sport
    7786.4h  0.93% Programmende
    7706.9h  0.92% Sitcom
    7443.0h  0.89% Wetterbericht
    7384.6h  0.88% Börsenmagazin
    7241.5h  0.86% Quiz
    7162.4h  0.85% Komödie
    6194.2h  0.74% Wissensmagazin
    6144.0h  0.73% Politikmagazin
    6121.1h  0.73% Realityshow
    5991.7h  0.71% Wirtschaftsmagazin
    5983.0h  0.71% Telenovela
    5578.5h  0.67% Musikmagazin
