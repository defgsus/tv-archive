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

**101** channels, **758,872.8** hours playtime between **2023-01-17** and **2024-03-16**


### playtime per genre (top 30)

    49425.0h 6.51% Nachrichten
    36462.5h 4.80% Verkaufsshow
    30939.0h 4.08% Krimiserie
    26310.8h 3.47% Werbesendung
    24165.5h 3.18% Dokureihe
    22930.9h 3.02% Dokusoap
    22069.8h 2.91% Regionalmagazin
    19563.9h 2.58% Dokumentation
    19467.3h 2.57% *unknown*
    14012.6h 1.85% Zeichentrickserie
    13802.8h 1.82% Infomercial
    13418.3h 1.77% Animationsserie
    11524.7h 1.52% Comedyserie
    10787.9h 1.42% Morgenmagazin
    10350.5h 1.36% Magazin
    10246.7h 1.35% Religionsmagazin
    10105.5h 1.33% Talkshow
    7472.4h  0.98% E-Sport
    7164.2h  0.94% Programmende
    7120.4h  0.94% Sitcom
    6742.7h  0.89% Wetterbericht
    6741.8h  0.89% Börsenmagazin
    6459.2h  0.85% Quiz
    6401.2h  0.84% Komödie
    5668.1h  0.75% Wissensmagazin
    5506.0h  0.73% Politikmagazin
    5495.9h  0.72% Realityshow
    5491.5h  0.72% Wirtschaftsmagazin
    5438.9h  0.72% Telenovela
    5170.1h  0.68% Musikmagazin
