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

**96** channels, **102,894.4** hours playtime between **2023-01-17** and **2023-03-14**


### playtime per genre (top 30)

    7220.8h 7.02% Nachrichten
    5176.4h 5.03% Verkaufsshow
    4295.7h 4.17% Krimiserie
    3493.4h 3.40% Werbesendung
    3314.8h 3.22% Dokusoap
    3122.4h 3.03% Dokureihe
    3014.6h 2.93% Regionalmagazin
    2528.8h 2.46% Dokumentation
    2449.2h 2.38% *unknown*
    1972.0h 1.92% Animationsserie
    1886.9h 1.83% Infomercial
    1853.7h 1.80% Zeichentrickserie
    1667.8h 1.62% Comedyserie
    1452.8h 1.41% Morgenmagazin
    1404.3h 1.36% Programmende
    1364.1h 1.33% Talkshow
    1349.8h 1.31% Religionsmagazin
    1062.6h 1.03% E-Sport
    1058.2h 1.03% Magazin
    977.6h  0.95% Sitcom
    950.4h  0.92% Börsenmagazin
    911.0h  0.89% Wetterbericht
    834.6h  0.81% Wirtschaftsmagazin
    805.0h  0.78% Wissensmagazin
    772.2h  0.75% Quiz
    758.4h  0.74% Musikmagazin
    745.5h  0.72% Dramaserie
    714.8h  0.69% Telenovela
    712.0h  0.69% Gesundheitsmagazin
    664.6h  0.65% Sportmagazin
