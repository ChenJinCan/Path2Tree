# Path2Tree
Python print path list a to tree structure
Support Python2.x & Python3.x


将路径列表以树形结构的方式输出
支持Python2.x & Python3.x

```
[
    "TEST\\A\\1.txt", 
    "TEST\\A\\2.txt", 
    "TEST\\A\\3.txt", 
    "TEST\\B\\1.txt", 
    "TEST\\B\\2.txt", 
    "TEST\\B\\3.txt", 
    "TEST\\C\\1.txt", 
    "TEST\\C\\2.txt", 
    "TEST\\C\\3.txt", 
    "TEST\\C\\SUB_C\\1.txt", 
    "TEST\\C\\SUB_C\\2.txt", 
    "TEST\\C\\SUB_C\\3.txt", 
    "TEST\\D\\1.txt", 
    "TEST\\D\\2.txt", 
    "TEST\\D\\3.txt"
]

--------->

└─TEST
    ├─ A
    |   ├─ 1.txt
    |   ├─ 2.txt
    |   └─ 3.txt
    ├─ B
    |   ├─ 1.txt
    |   ├─ 2.txt
    |   └─ 3.txt
    ├─ C
    |   ├─ 1.txt
    |   ├─ 2.txt
    |   ├─ 3.txt
    |   └─ SUB_C
    |       ├─ 1.txt
    |       ├─ 2.txt
    |       └─ 3.txt
    └─ D
        ├─ 1.txt
        ├─ 2.txt
        └─ 3.txt
```
