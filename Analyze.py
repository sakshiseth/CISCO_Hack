from Weather.Citi_Weather_Impact import GetCovidCases
from News_Channel.News_Data import newsDataCapturing

prepareCovidConclusion = GetCovidCases()
prepareCovidConclusion.getCases()

prepareNewsData = newsDataCapturing()
prepareNewsData.getnewsData()


