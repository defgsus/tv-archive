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

**96** channels, **46,478.2** hours playtime between **2023-01-17** and **2023-02-11**


### playtime per genre (top 30)

    3285.6h 7.07% Nachrichten
    2405.2h 5.18% Verkaufsshow
    1985.5h 4.27% Krimiserie
    1650.6h 3.55% Dokusoap
    1567.3h 3.37% Werbesendung
    1395.7h 3.00% Dokureihe
    1365.3h 2.94% Regionalmagazin
    1174.3h 2.53% *unknown*
    1169.2h 2.52% Dokumentation
    889.9h  1.91% Zeichentrickserie
    864.8h  1.86% Infomercial
    841.2h  1.81% Animationsserie
    786.1h  1.69% Comedyserie
    675.2h  1.45% Morgenmagazin
    610.3h  1.31% Talkshow
    604.5h  1.30% Religionsmagazin
    599.8h  1.29% Programmende
    539.0h  1.16% Magazin
    485.6h  1.04% E-Sport
    438.6h  0.94% Sitcom
    407.5h  0.88% Börsenmagazin
    403.2h  0.87% Wetterbericht
    395.6h  0.85% Wirtschaftsmagazin
    372.2h  0.80% Wissensmagazin
    371.1h  0.80% Quiz
    354.4h  0.76% Dramaserie
    346.8h  0.75% Musikmagazin
    339.8h  0.73% Telenovela
    331.8h  0.71% Gesundheitsmagazin
    309.3h  0.67% Gerichtsshow
