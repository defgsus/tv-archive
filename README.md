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

**97** channels, **554,261.5** hours playtime between **2023-01-17** and **2023-11-21**


### playtime per genre (top 30)

    36466.7h 6.58% Nachrichten
    26495.4h 4.78% Verkaufsshow
    22333.1h 4.03% Krimiserie
    18806.7h 3.39% Werbesendung
    18086.9h 3.26% Dokureihe
    16779.6h 3.03% Dokusoap
    16009.1h 2.89% Regionalmagazin
    14146.7h 2.55% Dokumentation
    13499.0h 2.44% *unknown*
    10274.2h 1.85% Zeichentrickserie
    10101.0h 1.82% Infomercial
    9881.2h  1.78% Animationsserie
    8679.0h  1.57% Comedyserie
    7879.4h  1.42% Morgenmagazin
    7490.1h  1.35% Religionsmagazin
    7415.0h  1.34% Talkshow
    7072.9h  1.28% Magazin
    5582.1h  1.01% Programmende
    5427.9h  0.98% E-Sport
    5324.6h  0.96% Sitcom
    5088.5h  0.92% Wetterbericht
    5020.8h  0.91% Börsenmagazin
    4624.7h  0.83% Quiz
    4324.7h  0.78% Komödie
    4204.3h  0.76% Wissensmagazin
    4158.5h  0.75% Wirtschaftsmagazin
    4083.3h  0.74% Musikmagazin
    3996.8h  0.72% Telenovela
    3877.4h  0.70% Politikmagazin
    3836.9h  0.69% Realityshow
