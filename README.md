# cumincadScraper
This repo includes a site-specific ([CumInCAD](http://papers.cumincad.org/)) Python crawler.

[CumInCAD](http://papers.cumincad.org/) is a digital archiving platform supported by several conferences and journals in computer-aided architectural design research society.
Users can scrape all papers in CumInCAD which includes at least one word of keywords (search_words).

the main() function has one argument, total number of papers.
The default value of the argument is 15260, since currently (2020.10.12) the maximum numbers of paper is 15176.

To run the file, users can write those codes

```
$python main()
```

or
with the total number of publications arugment

```
$python main(300)
```



Before users run this file, please check the installed packages.
Users are required to install below:

```
pandas==0.25.3
requests==2.22.0
beautifulsoup4==4.9.3
```

Sometimes, CumInCAD has connection issue. The average time to extract a publication's information is 2-5 sec.
If the time is longer than the average one, please stop the crawler and rerun it.
In this case, users manually change the 'page_number', which is a multiplication of 20. (e.g. 0,20,40,60,80, ...)
```
page_number = 40
```



This repository has been developed by [JinmoRhee](www.jinmorhee.net)
