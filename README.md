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

**97** channels, **496,810.2** hours playtime between **2023-01-17** and **2023-10-20**


### playtime per genre (top 30)

    32757.4h 6.59% Nachrichten
    23722.3h 4.77% Verkaufsshow
    19988.9h 4.02% Krimiserie
    16786.5h 3.38% Werbesendung
    16350.3h 3.29% Dokureihe
    15180.2h 3.06% Dokusoap
    14342.4h 2.89% Regionalmagazin
    12558.8h 2.53% Dokumentation
    11930.3h 2.40% *unknown*
    9298.9h  1.87% Zeichentrickserie
    9048.4h  1.82% Infomercial
    8859.6h  1.78% Animationsserie
    7913.9h  1.59% Comedyserie
    7040.2h  1.42% Morgenmagazin
    6671.2h  1.34% Religionsmagazin
    6615.7h  1.33% Talkshow
    6233.5h  1.25% Magazin
    5139.8h  1.03% Programmende
    4885.5h  0.98% E-Sport
    4739.8h  0.95% Sitcom
    4622.2h  0.93% Wetterbericht
    4474.4h  0.90% Börsenmagazin
    4176.6h  0.84% Quiz
    3840.8h  0.77% Komödie
    3757.8h  0.76% Musikmagazin
    3753.6h  0.76% Wirtschaftsmagazin
    3751.7h  0.76% Wissensmagazin
    3561.0h  0.72% Telenovela
    3404.8h  0.69% Politikmagazin
    3241.3h  0.65% Realityshow
