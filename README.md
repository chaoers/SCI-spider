# SCI-spider

## 项目简介

本项目是用于对[中国科学院文献情报中心期刊分区表](http://www.fenqubiao.com/)的一个基于Selenium的爬虫，爬取信息即为批量搜索中展示的信息

## 运行指南

1. pip通过`requirements.txt`文件安装依赖，同时安装`WebDriver`
2. 在`account.py`中填入账号信息（需要保证ip与账号符合）
3. 将需要爬取的数据放在`list.xlsx`文件下
4. 运行`getData.py`爬取数据，数据会自动存储到`Result.xls`

### 关于断点续搜

本爬虫会记录之前爬取的数据并读取已经爬取到的数据，如果需要重新爬取请删除`history.txt`文件

## Contribution

本项目由[@chaoers](https://github.com/chaoers)完成

## LICENSE

本项目遵循`GPLV3.0`开源协议