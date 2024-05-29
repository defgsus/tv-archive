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

**108** channels, **878,040.0** hours playtime between **2023-01-17** and **2024-05-30**


### playtime per genre (top 30)

    57387.2h 6.54% Nachrichten
    41653.2h 4.74% Verkaufsshow
    35728.6h 4.07% Krimiserie
    30812.8h 3.51% Werbesendung
    27663.5h 3.15% Dokureihe
    26546.0h 3.02% Dokusoap
    25532.4h 2.91% Regionalmagazin
    22798.2h 2.60% Dokumentation
    22232.7h 2.53% *unknown*
    16136.4h 1.84% Zeichentrickserie
    15968.0h 1.82% Infomercial
    15646.0h 1.78% Animationsserie
    13176.8h 1.50% Comedyserie
    12487.0h 1.42% Magazin
    12365.4h 1.41% Morgenmagazin
    11876.8h 1.35% Religionsmagazin
    11693.4h 1.33% Talkshow
    8705.4h  0.99% E-Sport
    8130.2h  0.93% Sitcom
    8090.3h  0.92% Programmende
    7814.9h  0.89% Wetterbericht
    7689.1h  0.88% Börsenmagazin
    7603.2h  0.87% Quiz
    7567.9h  0.86% Komödie
    6493.2h  0.74% Wissensmagazin
    6489.5h  0.74% Realityshow
    6477.6h  0.74% Politikmagazin
    6227.3h  0.71% Wirtschaftsmagazin
    6178.3h  0.70% Telenovela
    5806.9h  0.66% Musikmagazin
