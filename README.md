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

**96** channels, **108,305.2** hours playtime between **2023-01-17** and **2023-03-17**


### playtime per genre (top 30)

    7654.2h 7.07% Nachrichten
    5437.7h 5.02% Verkaufsshow
    4549.1h 4.20% Krimiserie
    3667.1h 3.39% Werbesendung
    3488.7h 3.22% Dokusoap
    3273.0h 3.02% Dokureihe
    3209.9h 2.96% Regionalmagazin
    2658.9h 2.46% Dokumentation
    2541.5h 2.35% *unknown*
    2076.9h 1.92% Animationsserie
    1989.0h 1.84% Infomercial
    1951.9h 1.80% Zeichentrickserie
    1777.8h 1.64% Comedyserie
    1555.5h 1.44% Morgenmagazin
    1488.3h 1.37% Programmende
    1437.6h 1.33% Talkshow
    1414.7h 1.31% Religionsmagazin
    1128.3h 1.04% Magazin
    1122.2h 1.04% E-Sport
    1038.6h 0.96% Sitcom
    1011.5h 0.93% Börsenmagazin
    962.5h  0.89% Wetterbericht
    891.4h  0.82% Wirtschaftsmagazin
    850.1h  0.78% Wissensmagazin
    817.8h  0.76% Quiz
    800.9h  0.74% Musikmagazin
    777.0h  0.72% Dramaserie
    764.2h  0.71% Telenovela
    751.5h  0.69% Gesundheitsmagazin
    703.4h  0.65% Sportmagazin
