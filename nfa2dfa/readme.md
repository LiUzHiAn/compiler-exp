## How to run
```
$ python run.py
```

## 存储格式说明

- NFA和DFA都是由五元组（状态集合，初始状态，起始状态，字母表，转换规则集）构成。
这里采用字典的放方式保存，字典存储时每个k-v的顺序不关键，以下为DFA和NFA的示例

- DFA示例

```python
{
  "states": [
    "s0",
    "s1",
    "s2",
    "s3",
    "s4"
  ],
  "final_state": "s4",
  "init_state": "s0",
  "transform_rules": {
    "s3": {
      "a": [
        "s1"
      ],
      "b": [
        "s4"
      ]
    },
    "s2": {
      "a": [
        "s1"
      ],
      "b": [
        "s2"
      ]
    },
    "s1": {
      "a": [
        "s1"
      ],
      "b": [
        "s3"
      ]
    },
    "s0": {
      "a": [
        "s1"
      ],
      "b": [
        "s2"
      ]
    },
    "s4": {
      "a": [
        "s1"
      ],
      "b": [
        "s2"
      ]
    }
  },
  "alphabet": [
    "a",
    "b"
  ]
}
```

- DFA示例
 
```python
{
  "states": [
    "s0",
    "s1",
    "s2",
    "s3",
    "s4",
    "s5",
    "s6",
    "s7",
    "s8",
    "s9",
    "s10"
  ],
  "alphabet": [
    "a",
    "b"
  ],
  "init_state": "s0",
  "transform_rules": {
    "s9": {
      "b": [
        "s10"
      ]
    },
    "s8": {
      "b": [
        "s9"
      ]
    },
    "s10": {},
    "s3": {
      "epsilon": [
        "s6"
      ]
    },
    "s2": {
      "a": [
        "s3"
      ]
    },
    "s1": {
      "epsilon": [
        "s2",
        "s4"
      ]
    },
    "s0": {
      "epsilon": [
        "s1",
        "s7"
      ]
    },
    "s7": {
      "a": [
        "s8"
      ]
    },
    "s6": {
      "epsilon": [
        "s1",
        "s7"
      ]
    },
    "s5": {
      "epsilon": [
        "s6"
      ]
    },
    "s4": {
      "b": [
        "s5"
      ]
    }
  },
  "final_state": "s10"
}
```


