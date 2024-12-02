# ChatGPT 聊天机器人

这是一个类似 ChatGPT 的聊天机器人项目，使用了 OpenAI 的 `gpt-4o` 模型。后端采用轻量级的 Python 框架 **FastAPI**，前端使用 **Streamlit**，并具备会话历史记录功能，历史记录显示在左侧边栏中。

## 项目目录

- `/backend`：后端 FastAPI 应用程序
- `/frontend`：前端 Streamlit 应用程序

## 环境要求

- Python 3.10 及以上版本
- 有效的 OpenAI API 密钥

## 安装与运行

### 克隆仓库

```bash
git clone [仓库地址]
cd GPT
```

### 安装依赖

#### 后端

```bash
cd backend
pip install -r requirements.txt
```

#### 前端

```bash
cd frontend
pip install -r requirements.txt
```

### 设置 OpenAI API 密钥

在终端中设置 `OPENAI_API_KEY` 环境变量：

```bash
export OPENAI_API_KEY='your_openai_api_key'
```

### 启动应用程序

#### 启动后端服务器

```bash
cd backend
uvicorn main:app --host 0.0.0.0 --port 8000
```

#### 启动前端应用

在新的终端窗口中：

```bash
cd frontend
streamlit run app.py --server.port=8501
```

### 访问应用

在浏览器中访问：http://localhost:8501

## 功能特性

- **基于 OpenAI 的 `gpt-4o` 模型**：提供类似 ChatGPT 的聊天体验。
- **会话历史记录**：聊天记录显示在左侧边栏，便于查看和管理。
- **简洁的用户界面**：使用 Streamlit 构建，交互友好。
- **高性能后端**：采用 FastAPI，确保快速响应。

## 注意事项

- 确保已获取有效的 OpenAI API 密钥。
- 本项目仅供学习和交流使用，请勿用于商业目的。

## 许可证

MIT License