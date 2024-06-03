# Http Server, Get JSON, POST JSON


* Mon Jun  3 15:02:45 2024 
* How to run it 

```
  python3 httpjson.py 8000
```

* `curl GET`

```
  curl http://localhost:8000
```

* `curl POST`

```
  curl -X POST http://localhost:8000 -H 'Content-Type: application/json' -d '{"key1" : "From client"}' 
```

* Get JSON and reply JSON

```
  Get json from client 
  {'key1' : 'Get JSON'}

  Reply json to client 
  {'key1' : 'Reply from Server'}
```
