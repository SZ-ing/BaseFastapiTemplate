# BaseFastapiTemplate

基于 FastAPI 的项目模板，适合按「接口层 → 业务层 → 模型/配置」分层扩展。

## 目录结构

```
BaseFastapiTemplate/
├── app/                          # 应用核心代码
│   ├── api/                      # 接口层：路由、参数校验、调用 Service
│   │   ├── api.py                # 路由汇总
│   │   └── endpoints/            # 各模块接口
│   │       └── base_api.py       # 默认接口（健康检查、配置等）
│   ├── core/                     # 核心配置与生命周期
│   │   ├── life_span.py          # FastAPI lifespan（启动/关闭）
│   │   ├── config_manager.py     # 配置加载（基于项目根目录）
│   │   └── config_schemas.py     # 配置项 Pydantic 模型
│   ├── models/                   # 数据库模型（如 SQLAlchemy/Tortoise）
│   ├── schema/                   # Pydantic 请求/响应模型
│   ├── services/                 # 业务逻辑层
│   └── utils/                    # 通用工具
│       └── utils.py
├── configs/
│   └── configs.yaml              # 主配置（server、path 等）
├── resources/
│   ├── static/                   # 文档静态资源（Swagger UI、ReDoc）
│   └── weights/                  # 权重等资源
├── storage/                      # 持久化目录（由 configs 中 path 引用）
├── tests/                        # 测试
├── main.py                       # 应用入口（项目根目录）
└── README.md
```

## 命名规范

| 类别       | 格式         | 示例              |
| :--------- | :----------- | :---------------- |
| 类         | `AaBbCc`     | `MyClass`         |
| 函数/方法  | `aaBbCc`     | `myFunction()`    |
| 变量       | `aa_bb_cc`   | `my_variable`    |
| 私有变量   | `_aa_bb_cc`  | `self._private_var` |
| 文件名     | `aa_bb_cc`   | `main_logic.py`   |

## 注意事项

1. **多进程模式**：入口文件 `main.py`（项目根目录）中强制使用多进程 `spawn` 模式。
2. **配置路径**：`config_manager` 基于 `__file__` 解析项目根目录，任意工作目录下启动均可正确加载 `configs/configs.yaml`。
3. **文档**：自定义 Swagger UI 与 ReDoc，静态资源挂载在 `resources/static`（`/docs`、`/redoc`）。
