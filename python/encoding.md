Вывод в консоль в кодировке utf-8.

```python
UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)
```
