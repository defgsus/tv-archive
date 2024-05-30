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

**108** channels, **879,872.3** hours playtime between **2023-01-17** and **2024-05-31**


### playtime per genre (top 30)

    57518.6h 6.54% Nachrichten
    41715.5h 4.74% Verkaufsshow
    35797.8h 4.07% Krimiserie
    30879.8h 3.51% Werbesendung
    27704.2h 3.15% Dokureihe
    26604.1h 3.02% Dokusoap
    25564.3h 2.91% Regionalmagazin
    22837.3h 2.60% Dokumentation
    22295.6h 2.53% *unknown*
    16180.3h 1.84% Zeichentrickserie
    15997.6h 1.82% Infomercial
    15678.0h 1.78% Animationsserie
    13207.2h 1.50% Comedyserie
    12513.3h 1.42% Magazin
    12399.4h 1.41% Morgenmagazin
    11895.8h 1.35% Religionsmagazin
    11706.0h 1.33% Talkshow
    8731.5h  0.99% E-Sport
    8148.6h  0.93% Sitcom
    8103.6h  0.92% Programmende
    7834.0h  0.89% Wetterbericht
    7706.1h  0.88% Börsenmagazin
    7616.4h  0.87% Quiz
    7615.6h  0.87% Komödie
    6511.9h  0.74% Realityshow
    6504.6h  0.74% Wissensmagazin
    6503.1h  0.74% Politikmagazin
    6238.9h  0.71% Wirtschaftsmagazin
    6187.6h  0.70% Telenovela
    5816.9h  0.66% Musikmagazin
