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

**102** channels, **827,930.5** hours playtime between **2023-01-17** and **2024-04-26**


### playtime per genre (top 30)

    53998.5h 6.52% Nachrichten
    39694.2h 4.79% Verkaufsshow
    33745.8h 4.08% Krimiserie
    28937.9h 3.50% Werbesendung
    26167.2h 3.16% Dokureihe
    24970.0h 3.02% Dokusoap
    24106.6h 2.91% Regionalmagazin
    21401.7h 2.58% Dokumentation
    21151.2h 2.55% *unknown*
    15200.0h 1.84% Zeichentrickserie
    15042.4h 1.82% Infomercial
    14747.0h 1.78% Animationsserie
    12548.0h 1.52% Comedyserie
    11696.9h 1.41% Morgenmagazin
    11604.3h 1.40% Magazin
    11173.0h 1.35% Religionsmagazin
    11025.4h 1.33% Talkshow
    8197.5h  0.99% E-Sport
    7704.1h  0.93% Programmende
    7624.9h  0.92% Sitcom
    7349.9h  0.89% Wetterbericht
    7290.3h  0.88% Börsenmagazin
    7158.4h  0.86% Quiz
    7054.9h  0.85% Komödie
    6136.1h  0.74% Wissensmagazin
    6072.6h  0.73% Politikmagazin
    6014.4h  0.73% Realityshow
    5929.0h  0.72% Wirtschaftsmagazin
    5928.8h  0.72% Telenovela
    5522.0h  0.67% Musikmagazin
