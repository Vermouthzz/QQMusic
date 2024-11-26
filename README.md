# QQMusic
python+pyqt5 QQ音乐客户端



# vscode 配置
```json
{
    // 使用 IntelliSense 了解相关属性。 
    // 悬停以查看现有属性的描述。
    // 欲了解更多信息，请访问: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "run main",
            "type": "debugpy",
            "request": "launch",
            "program": "${workspaceFolder}/app/main.py",
            "console": "integratedTerminal",
            "env": {
                "PYTHONPATH": "${workspaceFolder}"
            }
        }
    ]
}