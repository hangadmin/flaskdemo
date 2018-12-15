flask 引入flask_cache 报错， 
`` init_app
    from .jinja2ext import CacheExtension, JINJA_CACHE_ATTR_NAME
  File "D:\Python-test\Projects\FlaskProject\venv\lib\site-packages\flask_cache\jinja2ext.py", line 33, in
 <module>
    from flask.ext.cache import make_template_fragment_key
ModuleNotFoundError: No module named 'flask.ext'
``
请把源码`site-packages\flask_cache\jinja2ext.py`引入方式改为
``from flask_cache import make_template_fragment_key
``