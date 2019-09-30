# Web_Scraping_for_Research

Using web scraping for research purposes is one tool that can be added to the scholarly workflow. This repository contains Python scripts that use BeautifulSoup to scrape a variety of open access journals and subject repositories, including: 

- [ArXiv](https://arxiv.org/)
- [D-Lib Magazine](http://www.dlib.org/) (The Magazine of Digital Library Research)
- [Journal of Open Source Software](https://joss.theoj.org/)
- [Journal of Open Research Software](https://openresearchsoftware.metajnl.com/)
- [Journal of Statistical Software](https://www.jstatsoft.org/index)
- [Code4Lib](https://code4lib.org/)
- [Digital Humanities Quarterly](http://www.digitalhumanities.org/dhq/)
- [Medieval Worlds](https://medieval.vlg.oeaw.ac.at/index.php/medievalworlds)
- [Southern Spaces](https://southernspaces.org/)
- [Sign Systems Studies](http://www.sss.ut.ee/index.php/sss) (semiotics)
- [In the Library with the Lead Pipe](http://www.inthelibrarywiththeleadpipe.org/)
- [Culture Machine](https://culturemachine.co/)

Please note that specific search terms are sometimes used to build a URL for some journals so outputs are specific and limited in quantity and serve as proof of concept. Search terms that are specific to your research question need to be included in building the main URL, which can be derived from using the advance search function and the resulting URL. When possible, JSON outputs of metadata and/or full text are stored in each directory. For journals that host articles as PDFs, the secondary script to download those PDFs locally must be run. In these cases, running the first script results in a JSON output of article metadata (i.e. title, author, url, DOI, date, and abstract [if available]), which may be helpful for analysis of titles and abstracts. The JSON output of the first script is needed for the second script to function, thus must remain in the same directory. 

