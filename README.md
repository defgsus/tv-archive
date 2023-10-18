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

**97** channels, **495,020.8** hours playtime between **2023-01-17** and **2023-10-19**


### playtime per genre (top 30)

    32622.7h 6.59% Nachrichten
    23631.2h 4.77% Verkaufsshow
    19905.3h 4.02% Krimiserie
    16727.7h 3.38% Werbesendung
    16309.6h 3.29% Dokureihe
    15118.4h 3.05% Dokusoap
    14280.1h 2.88% Regionalmagazin
    12497.9h 2.52% Dokumentation
    11889.2h 2.40% *unknown*
    9269.0h  1.87% Zeichentrickserie
    9015.7h  1.82% Infomercial
    8826.0h  1.78% Animationsserie
    7895.9h  1.60% Comedyserie
    7006.4h  1.42% Morgenmagazin
    6652.0h  1.34% Religionsmagazin
    6597.2h  1.33% Talkshow
    6208.6h  1.25% Magazin
    5126.3h  1.04% Programmende
    4871.6h  0.98% E-Sport
    4719.7h  0.95% Sitcom
    4605.3h  0.93% Wetterbericht
    4463.3h  0.90% Börsenmagazin
    4161.2h  0.84% Quiz
    3833.2h  0.77% Komödie
    3747.8h  0.76% Musikmagazin
    3736.6h  0.75% Wirtschaftsmagazin
    3734.1h  0.75% Wissensmagazin
    3541.2h  0.72% Telenovela
    3387.6h  0.68% Politikmagazin
    3216.8h  0.65% Realityshow
