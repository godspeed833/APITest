# APITest
## Goal
1. 可以透過使用者認證，管控存取API次數
2. 記錄使用者查詢次數，方便未來計費
3. 整理管理查詢記錄，產生分析
4. 修正upload的問題

## Day 1 task (avon)
* Install postman and flask framework (RESTful, JWT, limiter)
* Try two sample of JWT and RESTful
* Implement a simple framework for ANSer
 - two APIs
 -- get 127.0.0.1:5000/n/<addr>   =>   {"address": <addr>,"username":<user>, "coutn":<count>}
 -- get 127.0.0.1:5000/s/<addr>   =>   {"address": <addr>,"username":<user>, "coutn":<count>}
 - three users (accessable only by registered users, no database, store in list)
 -- admin, anser, user
 - show the API access count based on users
* try flask limiter samples
* implement token based limiter
* logging
 - ip, username, query addr, result
* add upload function
