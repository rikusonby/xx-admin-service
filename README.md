# Admin service

## install depend

```
poetry install
```

## run local

```
uvicorn app.main:app --reload
```

## 目录结构

- **`core/`**: 包含应用程序的核心配置和设置，如数据库连接、安全策略和应用配置。此目录是项目基础设施的中心，关键的系统级配置在此进行。

- **`dependencies/`**: 管理API的依赖项注入，包括数据库会话、安全验证等公共依赖功能，以便在不同的路由和服务中重用。

- **`models/`**: 包含所有的ORM数据模型，这些模型定义了数据库的表结构和关系，是数据持久化的基础。

- **`schemas/`**: 存放所有的Pydantic模型，用于请求数据验证和响应数据序列化，确保数据的输入和输出符合预期格式。

- **`services/`**: 业务逻辑层，封装了处理具体业务任务的代码，如用户管理、数据处理等，服务层作为模型和路由之间的中介。

- **`routers/`**: 定义所有的API路由，负责接收请求和返回响应，路由层直接与前端或客户端交互。

- **`internal/`**: 用于存放内部逻辑和工具，这些通常是不希望外部直接访问的功能，如管理任务、后台处理脚本等。

- **`libraries/`**: 集成和封装外部库和服务的代码，如数据库、缓存服务、消息队列等，便于管理和重用。

- **`utils/`**: 存放工具函数和助手代码，这些通常是跨项目多处使用的代码片段，如日期处理、加密函数等。

- **`enums/`**: 定义枚举类型，用于管理固定的数据集，如状态码、角色权限等，提供统一的引用源。
