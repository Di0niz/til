Описание свойств
----------------

* indexed - данные поля будут проиндексированы;
* repeated - данные, которые будут повторяться

Операции с несколькими записями
-------------------------------

Because each get() or put() operation invokes a separate remote procedure call (RPC), issuing many such calls inside a loop is an inefficient way to process a collection of entities or keys at once. The following methods are faster:

```python
list_of_keys = ndb.put_multi(list_of_entities)
list_of_entities = ndb.get_multi(list_of_keys)
ndb.delete_multi(list_of_keys)
```


## Удаление записей


```
from app.models.db import JSonData

ndb.delete_multi(JSonData.query().fetch(keys_only=True))
```
