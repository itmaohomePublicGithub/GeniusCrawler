# GeniusCrawler

##### GeniusCrawler（以下简称为：GC） 是一套基于Python3实现的轻量级异步爬虫请求框架，设计初衷仅为解决日常爬虫采集需求，又不想花更多时间学习Scrapy，故实现此框架用于日常数据抓取之用；

* 得益于核心callback函数的回调，使得该框架易用性高，轻松便能实现异步数据采集需求。
* 项目分工明细，在开发GC项目过程中，每个任务均被划分成两部分实现（用作分布式兼容），分别位于：SpiderUtils/tasks、SpiderUtils/Crawler下实现两个爬虫类，前者为任务类，可理解为任务推送服务；后者则为爬虫实体类，在实际工做中均通过SpiderUtils/SpiderManger 类进行任务的获取与消化。
  
#### Tasks目录说明：
* Tasks位于SpiderUtils/Tasks，主要用于存放推送类业务，不应在此实现爬虫实际逻辑、通常在构建分布式爬虫需求的时候，可在该目录下实现相应的任务类，如生成批量任务后将其推送至Redis，以达到任务分发的目的。

#### Crawler目录说明：
* Crawler位于SpiderUtils/Crawler，主要用于存放爬虫实际逻辑类业务，不应在此实现任务分发、通常在构建分布式或单一爬虫需求时可在该目录下实现相应的实际爬虫取数逻辑，如果说Tasks是任务分发器，那么Crawler就是执行者，在分布式开发中，可在该目录下实现Redis任务获取逻辑，借助WebRequestUtils/AsyncWebRequest类可实现异步高并发取数目的。

#### LoggerUtils目录说明
* LoggerUtils主要为GC项目实现的一套logger方法，支持：info、error、worng等相应等级的日志输出，同时等级不同控制台展示的颜色也不一致，注：在做分布式爬虫开发时不建议单独载入该类，可通过引用SpiderUtils/SpiderManger实现的logger方法，引用后在项目实际运行过程中相应的爬虫会以当前指定的爬虫名称进行重命名，以便于后续更好的做日志分析。

#### DataBaseUtils目录说明
* DataBaseUtils在GC开发项目中肩负着数据存储的光荣使命，目前已实现Redis、SQLite等两钟数据库操作模块，更多数据模型可发挥自己的创意根据已有模板创造出更多种类的数据库支持。
* 在GC项目开发过程中，数据库模型应在SpiderUtils/Module目录下实现，具体可参考Demo文件：SpiderUtils/Module/TaoBaoModule.py的实现
* 数据存储过程可通过实例化后的SpiderUtils/SpiderManger类托管或自行引用均可，如需托管，只需实现SetHandlerData方法（即：将上述实现的SaveData方法传递给SetHandlerData）然后在callback处理完成后会通过yield直接回调SaveData方法完成数据存储。

#### WebRequestUtils目录说明
* 该目录主要实现了同步/异步请求类，请注意：异步类已通过SpiderUtils/SpiderManger内部实现了封装，可通过内置的Forword与Fetch方法完成异步请求。

#### ProxyUtils目录说明
* 该目录主要实现请求代理类，目前只是半成品，后续将逐渐实现。

#### EncyptUtils目录说明
* 该目录实现常见加密方式，诸如md5、rsa、aes、des、hmac等各类常见的加密方式，目前该类尚未实现，未来将逐渐完善！

#### 未来考虑加入的功能
* 鉴于js加密技术的日趋渐长，解密还原便成了爬虫开发过程中遇到的最大瓶颈；后续将会考虑加入基于chromium编译的内核控件作为GC中间件进行js解密还原操作。
* 对于目前移动端的发展趋势，可谓是势在必行，放眼看去，目前大部分较为有用的数据皆转向APP端实现，导致不得不进行APP端的逆向研究，后续将考虑接入APP端驱动服务，让GC变得更加的强大！