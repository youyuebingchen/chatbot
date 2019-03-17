# ChatBot 第一课（july online）
## 行业综述
### bot的定义
------
bot：执行大量的自动化告诉挥着机械师繁琐的编辑工作的计算机程序或者脚本以及其所登陆的账户
### chatbot的玩法
-------
- retrieved-based(基于提取): KE(knowledge enger)专家系统（知识库检索）。<br/>
  问题：计算速度是要解决的问题<br/>
  提升：intents 机制（归类） 也就是在框架的前边加一个文本分类器
- generative 例RNN，生成一些人没有想到的。(必读《a neural conversational model》开启了generative model的新纪元)<br/>
  chatterBot库 
- 知识框架<br/>

|             |chatbot conversation framework     |
|------------ |-------------------:|:-------:     |
| open Domain | impossible         |geneal AI(hardest) |
|closed domain| rules-based（easiest| smart machine(hard)|
|             |retrieval-based（人设）|generative-based(数据驱动)|

### chatbot目前的challenge
- 语境 <br/>
  paper1:build end to end dialoge systems using generative hierarchical neural network model<br/> 
  paper2:attion whit intention for a neural network conversation model <br/>
  语言的语境<br/>
  物理的语境
- 统一的语言个性(容易精神分裂)<br/>
  高质量的对话:清洗，花费时间太久<br/>
  paper: a persona-based neural conversation model<br/>
  通过心里学和文本推算出是哪种性格的人
- 模型验证<br/>  BLEU验证
  *我们自己对模型的正误哦按段需要人类的智慧的解读<br/>
  *不存在完美定义的方案<br/>
   paper: how bot to evaluate dialogue system:an empirical study of unsupervised evaluation metrics for dialogue response generation
- 多样性 回答不够多样性比如无论问什么都回答嗯<br/>
  出现原因：数据集<br/>
  paper:a diversity-promoting objective function for neural conversation modeals

-----
### 工业应用综述
- 语音助手（ 主动/被动）
- 餐饮
- 旅游
- 医疗：前台healthtop 很多都是做前台
- 新闻 
- 财经
- 健身

-----
### 工业上的一些坑
- 查找 -> 发现
- 基于知识库 -> 基于检索
- 基于规则 -> 基于数据
- app -> 智能硬件 智能家居

-----
### rule-based 机器人
- grade0：基本的问答事前准备好所有可能的问答情况，然后根据问题做出固定的反应
  不能理解理解问题人在问什么

-----
### 升级！	
- grade1.0：精准对答。通过关键词来判断这句话的意图。<br/>
  先用 word_tokenize分词，然后查看共有词。set(a).isdisjoint(b):查看a和b 集合是否具有共同的元素，如果没有返回True，如果有返回Fasle
- upgrade2.0：先建立知识体系库（构建知识图谱），建一套体系，然后通过搜索的方法来查询答案。<br/>
  也可以使用logic programming  prolog python的prolog:PyKE
- upgrade3.0：利用gTTs把文本转化成音频。相当于为了提升用户体验多加了一个前端。<br/>
  其他场景：微信、slack、Facebook messager等<br/>
  目前工业上根本不可能实现智能对话，还有很长的路要走。


