## Описание выгрузки данных из 1С


Код выгрузки данных:
```bsl

ИмяФайлаОтправки = ПолучитьИмяВременногоФайла();
ФайлРезультата = ПолучитьИмяВременногоФайла();

АдресСервера = "http://localhost:9080";
РесурсНаСервере = "/finance/dashboard_data.json?"+ПутьКФайлу;

Соединение = УстановитьСоединениеССерверомИнтернета(АдресСервера);

ЗаголовокHTTP = Новый Соответствие();
ЗаголовокHTTP.Вставить("Content-Type", "multipart/form-data; boundary=My1cV8bNdr");

Соединение.ОтправитьДляОбработки(ИмяФайлаОтправки, РесурсНаСервере, ФайлРезультата, ЗаголовокHTTP);

```

Код загрузки данных (GAE):

```python

# инициализация
class JSonData(ndb.Model):
  ...
  blob = ndb.BlobProperty()
    
    
def post(self):
  ...
  data = self.request.body
  ...   
  record = JSonData()
  record.blob = blob
  record.put()
  ...


```
