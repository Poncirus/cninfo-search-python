# cninfo-search-python
在巨潮资讯网上搜索公告（多个公司，关键词，屏蔽关键词，公告下载）

## 网站
可以使用 [https://liaohanwen.com/tools/notice-search/](https://liaohanwen.com/tools/notice-search/) 搜索公告

## 使用说明
1. 在 company_list.txt 中写入查询的公司名称（每行一个公司）
2. 在 keyword_list.txt 中写入查询的关键词（每行一个关键词），搜索结果包含有任一关键词的公告
3. 在 banword_list.txt 中写入禁用的关键词（每行一个关键词），含有这些关键词的公告不会被包含在搜索结果中
4. 运行 main.py ，搜索公告并下载
