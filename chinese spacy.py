import spacy
from spacy.lang.zh.examples import sentences
nlp = spacy.load("zh_core_web_sm")
myd = nlp("连女士自己在上海成家立业，因为小孩教育等种种考量，疫情前她与丈夫就已经准备离开上海。 她说，三月以来上海封城打乱计划，但也加深了他们离去的决心。住过国内外很多城市，上海对我来说是最能平衡舒适生活和职业前景的地方。但这次封控政策和种种乱象，令我感到失望和绝望……意识到它是在特殊的事件中依然不能独善其身的一座中国城市，”她说")
print(myd.text)
