# simple-todo-cli

这是一个用Python编写的小型CLI待办事项应用程序。任务存储在本地的`tasks.json`中，无需任何外部依赖。

## 安装

### 准备工作

- Python 3.8+

### 克隆仓库

输入一下命令以克隆仓库：

```bash
git clone https://github.com/yk-kumawat/simple-todo-cli.git
```

## 使用

```bash
# 新建一个待办事项
python todo.py add "Buy groceries"

# 列出所有待办事项
python todo.py list

# 通过list中的编号将待办事项标记为完成
python todo.py done 1

# 通过list中的编号删除待办事项
python todo.py remove 1
```

## 贡献

查看[issues](https://github.com/yk-kumawat/simple-todo-cli/issues)选项卡，找到标记为`good first issue`的未完成任务。
