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

**108** channels, **879,896.8** hours playtime between **2023-01-17** and **2024-05-31**


### playtime per genre (top 30)

    57522.2h 6.54% Nachrichten
    41716.4h 4.74% Verkaufsshow
    35797.5h 4.07% Krimiserie
    30880.7h 3.51% Werbesendung
    27704.0h 3.15% Dokureihe
    26604.3h 3.02% Dokusoap
    25565.8h 2.91% Regionalmagazin
    22839.6h 2.60% Dokumentation
    22267.5h 2.53% *unknown*
    16180.9h 1.84% Zeichentrickserie
    15999.9h 1.82% Infomercial
    15678.2h 1.78% Animationsserie
    13207.6h 1.50% Comedyserie
    12517.6h 1.42% Magazin
    12399.4h 1.41% Morgenmagazin
    11896.0h 1.35% Religionsmagazin
    11706.7h 1.33% Talkshow
    8731.5h  0.99% E-Sport
    8151.4h  0.93% Sitcom
    8103.5h  0.92% Programmende
    7834.0h  0.89% Wetterbericht
    7705.7h  0.88% Börsenmagazin
    7616.5h  0.87% Quiz
    7613.9h  0.87% Komödie
    6516.0h  0.74% Realityshow
    6504.6h  0.74% Wissensmagazin
    6502.9h  0.74% Politikmagazin
    6238.9h  0.71% Wirtschaftsmagazin
    6188.3h  0.70% Telenovela
    5816.4h  0.66% Musikmagazin
