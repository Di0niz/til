Содержание текста utf-8:

```python
#!/usr/bin/python
# -*- coding: utf8 -*-
```


Вывод в консоль в кодировке utf-8:

```python
import codecs
UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)
```
