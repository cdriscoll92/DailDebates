url_front <- "https://www.oireachtas.ie/en/debates/find/?page=1&datePeriod=term&debateType=dail&term=%2Fie%2Foireachtas%2Fhouse%2Fdail%2F"
url_end <- "&resultsPerPage=20"
dail_terms <- c(1:32)
library(xml2)

URLs <- paste(url_front, dail_terms, url_end, sep = "")

for(i in 1:length(URLs)){
  Sys.sleep(3)
  html_page <- readLines(URLs[i])
  closeAllConnections()
  html_doc <- paste(html_page, collapse = "\n")
  
  writeLines(html_doc,
             con = paste("~/Dropbox/Dissertation/data/Ireland/debates/oireachtas html files/",
                         dail_terms[i], ".html", sep = ""))
  
}
