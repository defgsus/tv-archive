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

**105** channels, **845,042.6** hours playtime between **2023-01-17** and **2024-05-09**


### playtime per genre (top 30)

    55162.6h 6.53% Nachrichten
    40355.3h 4.78% Verkaufsshow
    34393.8h 4.07% Krimiserie
    29555.5h 3.50% Werbesendung
    26652.7h 3.15% Dokureihe
    25519.7h 3.02% Dokusoap
    24598.4h 2.91% Regionalmagazin
    21895.8h 2.59% Dokumentation
    21531.3h 2.55% *unknown*
    15537.1h 1.84% Zeichentrickserie
    15364.8h 1.82% Infomercial
    15044.7h 1.78% Animationsserie
    12768.9h 1.51% Comedyserie
    11967.3h 1.42% Magazin
    11921.2h 1.41% Morgenmagazin
    11413.3h 1.35% Religionsmagazin
    11253.2h 1.33% Talkshow
    8382.7h  0.99% E-Sport
    7842.0h  0.93% Programmende
    7784.5h  0.92% Sitcom
    7506.1h  0.89% Wetterbericht
    7453.6h  0.88% Börsenmagazin
    7305.2h  0.86% Quiz
    7231.1h  0.86% Komödie
    6250.7h  0.74% Wissensmagazin
    6208.4h  0.73% Politikmagazin
    6208.1h  0.73% Realityshow
    6039.0h  0.71% Wirtschaftsmagazin
    6030.8h  0.71% Telenovela
    5613.1h  0.66% Musikmagazin
